import json
import time
import os
import vk


def get_api():
    token = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'
    session = vk.Session(access_token=token)
    result = vk.API(session, v='5.73')
    return result


def get_groups_without_friends(friends, api, groups):
    result = groups
    i = 1
    for friend in friends["items"]:
        if "deactivated" in friend:
            continue
        print("{} из {}".format(i, friends['count']))
        i += 1
        try:
            friend_groups = api.groups.get(user_id=friend['id'])
        except:
            print('Не удалось получить группы друга: {} {}'.format(friend['first_name'], friend['last_name']))
            continue
        time.sleep(2)
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


id = 5030613
api = get_api()
groups = api.groups.get(user_id=id, extended=1, fields='name', count=1000)
time.sleep(2)
groups_id = []
for group in groups['items']:
    groups_id.append(group['id'])
friends = api.friends.get(user_id=id, fields='deactivated')
groups_without_friends = get_groups_without_friends(friends, api, groups_id)
data_about_groups = get_data_about_groups(groups['items'], groups_without_friends)
current_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_dir, 'groups.json'), 'w', encoding='utf-8') as file:
    json.dump(data_about_groups, file)
