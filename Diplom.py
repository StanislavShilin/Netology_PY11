import json
import time
import os
import types

import vk


def get_api():
    token = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'
    session = vk.Session(access_token=token)
    result = vk.API(session, v='5.73')
    return result


def get_friends(api, id, fields):
    try:
        result = api.friends.get(user_id=id, fields=fields)
    except Exception as err:
        if err.code == 6:
            print("Ждем...")
            time.sleep(1)
            result = get_friends(api,id, fields)
        else:
            result = err
    return result


def get_groups(api, id, fields):
    try:
        result = api.groups.get(user_id=id, extended=1, fields=fields, count=1000)
    except Exception as err:
        if err.code == 6:
            print("Ждем...")
            time.sleep(1)
            result = get_groups(api, id, fields)
        else:
            result = err
    return result


def get_friends_groups(api, friend_id):
    try:
        result = api.groups.get(user_id=friend_id)
    except Exception as err:
        if err.code == 6:
            print("Ждем...")
            time.sleep(1)
            result = get_friends_groups(api, friend_id)
        else:
            result = err
    return result


def get_groups_without_friends(friends, api, groups):
    result = groups
    i = 1
    for friend in friends["items"]:
        if "deactivated" in friend:
            continue
        print("{} из {}".format(i, friends['count']))
        i += 1
        friend_groups = get_friends_groups(api, friend['id'])
        if isinstance(friend_groups, vk.exceptions.VkAPIError):
            print(friend_groups)
            continue
        result = list(set(result) - set(friend_groups['items']))
        #if i == 10:
            #break
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
    id = 5030613
    api = get_api()
    groups = get_groups(api, id, 'name')
    if isinstance(groups, vk.exceptions.VkAPIError):
        print(groups)
        return
    groups_id = []
    for group in groups['items']:
        groups_id.append(group['id'])
    friends = get_friends(api, id, 'deactivated')
    if isinstance(friends, vk.exceptions.VkAPIError):
        print(groups)
        return
    groups_without_friends = get_groups_without_friends(friends, api, groups_id)
    data_about_groups = get_data_about_groups(groups['items'], groups_without_friends)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_dir, 'groups.json'), 'w', encoding='utf-8') as file:
        json.dump(data_about_groups, file)

get_file()