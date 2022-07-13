import vk_api
from datetime import datetime



#получения тoкена
# http://oauth.vk.com/authorize?client_id=7472462&scope=photos,audio,video,docs,notes,pages,status,offers,questions,wall,groups,email,notifications,stats,ads,offline,docs,pages,stats,notifications&response_type=token
login = 'login'
password = 'password'
token='token'
vk_session = vk_api.VkApi(login,password,token)
vk = vk_session.get_api()

members_request = vk.groups.getMembers(group_id='locelotkal',fields="last_seen",count='1000',offset='0')
members_dict = members_request.get('items')

#сбор словаря с последним посещением участников
members_new_dict = {} #словарь с id:время последнего захода
members_error_array = [] #массив с участниками, у кого нет графы last_seen
for member in members_dict:
    try:
        member_last_seen = member['last_seen']['time']
    except:
        members_error_array += [member['id']]
    members_new_dict[member['id']] = member_last_seen

#сортировка
members_sorted_dict = {}
sorted_keys = sorted(members_new_dict, key=members_new_dict.get, reverse=True)
for i in sorted_keys:
    members_sorted_dict[i] = members_new_dict[i]

#вывод отсортированных значений
print('    id     Время последнего посещения')
for member in members_sorted_dict.keys():
    time = datetime.utcfromtimestamp(members_sorted_dict[member]).strftime('%Y-%m-%d')
    print(f'{member}      {time}')

print()
#вывод странных людей
print('Люди без графы lust_seen')
for member in members_error_array:
    print(member)



