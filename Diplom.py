import json
import time
import os
import requests


def get_response(method, params):
    link = 'https://api.vk.com/method/' + method
    response = requests.get(link, params)
    response_dict = response.json()
    if 'error' in response_dict:
        err = response_dict['error']
        if err['error_code'] == 6:
            print("Ждем...")
            time.sleep(1)
            result = get_response(method, params)
        else:
            result = 'error code: {}. error msg: {}.'.format(err['error_code'], err['error_msg'])
    else:
        result = response_dict['response']
    return result


def get_friends(token, id, fields):
    params = {
        'access_token': token,
        'user_id': id,
        'fields': fields,
        'v': '5.73'
    }
    result = get_response('friends.get', params)
    return result


def get_groups(token, id, fields):
    params = {
        'access_token': token,
        'user_id': id,
        'extended': 1,
        'fields': fields,
        'count': 1000,
        'v': '5.73'
    }
    result = get_response('groups.get', params)
    return result


def get_friends_groups(token, friend_id):
    params = {
        'access_token': token,
        'user_id': friend_id,
        'v': '5.73'
    }
    result = get_response('groups.get', params)
    return result


def get_groups_without_friends(token, friends, groups):
    result = groups
    i = 1
    for friend in friends["items"]:
        if "deactivated" in friend:
            continue
        print("{} из {}".format(i, friends['count']))
        i += 1
        friend_groups = get_friends_groups(token, friend['id'])
        if isinstance(friend_groups, str):
            print(friend_groups)
            continue
        result = list(set(result) - set(friend_groups['items']))
        #if i == 10:
        #    break
    return result


def get_data_for_group(group_id, groups):
    for group in groups:
        if group['id'] == group_id:
            return {'name': group['name'], 'id': group['id']}


def get_data_about_groups(groups, groups_without_friends):
    result = []
    for group_id in groups_without_friends:
        data_about_group = get_data_for_group(group_id, groups)
        result.append(data_about_group)
    return result


def get_file():
    token = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'
    id = 5030613
    api = ''
    groups = get_groups(token, id, 'name')
    if isinstance(groups, str):
        print(groups)
        return
    groups_id = []
    for group in groups['items']:
        groups_id.append(group['id'])
    friends = get_friends(token, id, 'deactivated')
    if isinstance(friends, str):
        print(groups)
        return
    groups_without_friends = get_groups_without_friends(token, friends, groups_id)
    data_about_groups = get_data_about_groups(groups['items'], groups_without_friends)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_dir, 'groups.json'), 'w', encoding='utf-8') as file:
        json.dump(data_about_groups, file)

get_file()
