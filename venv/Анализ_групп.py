import vk_api
from vk_api.execute import VkFunction
import matplotlib.pyplot as plt
import numpy as np



#получения тoкена
# http://oauth.vk.com/authorize?client_id=7472462&scope=photos,audio,video,docs,notes,pages,status,offers,questions,wall,groups,email,notifications,stats,ads,offline,docs,pages,stats,notifications&response_type=token
login = 'login'
password = 'password'
token='token'
vk_session = vk_api.VkApi(login,password,token)
vk = vk_session.get_api()


group="youareking"
limit=9000 #колличество подписчиков группы
offset=-26000
bdate = {2021: 0, 2020: 0}  # 2021-полностью скрытые,2020-полускрытые
sex = {'man': 0, 'woman': 0, 'secret': 0}
while limit > offset:
    offset += 26000
    group_members = VkFunction(code=f'var group = "{group}";var our_offset = {offset};var limit = {limit};' +
                                    """var members = API.groups.getMembers({"group_id": group,"fields": "sex,bdate","count": "1000","offset": our_offset}).items;
                                  var offset = 1000; 
                                  while (offset < 25000 && (our_offset + offset) < limit) 
                                  {
                                    members = members + "," + API.groups.getMembers({"group_id": group, "fields": "sex,bdate", "count": "1000", "offset": offset + our_offset}).items;
                                    offset = offset + 1000;
                                  };
                                  return members;""")
    request = group_members(vk)
    try:
        request = request.split(',')
    except:
        continue

    for i in range(4,len(request),1):
        temp_sex=''
        temp_bdate=''
        if request[i] == 'banned' or request[i] == 'deleted':
            sex['secret']+=1
            continue
        if request[i].isalpha():
            if request[i+2].isalpha():
                if request[i-1].isdigit():
                    temp_sex = request[i-1]
                    bdate[2021]+=1
                else:
                    temp_sex = request[i-2]
                    if len(request[i-1]) > 6:
                        temp_bdate = int(request[i-1][-4:])
                    else:
                        bdate[2020]+=1

        if temp_sex:
            if temp_sex == '1':
                sex['woman'] += 1
            elif temp_sex == '2':
                sex['man'] += 1
            else:
                bad4 = request[i + 2]
                bad3 = request[i + 1]
                bad2 = request[i - 2]
                bad1 = request[i - 1]
                bad = request[i]
                sex['secret'] += 1

        if temp_bdate:
            if temp_bdate in bdate.keys():
                bdate[temp_bdate] += 1
            else:
                bdate[temp_bdate] = 1

print("Пол:")
for i in sex.items():
    print(i)

sort_bdate=list(bdate.keys())
sort_bdate.sort()
sort_bdate2=[]
sort_bdate3=[]
print("Возраст:")
for i in sort_bdate:
    if i < 2020:
        sort_bdate3+=[2020-i]
        sort_bdate2+=[bdate[i]]
    print(f'({i}){2020-i}:{bdate[i]}')

plt.figure(1)
plt.bar(sort_bdate3,sort_bdate2)


plt.figure(2)
plt.bar(list(sex.keys()),list(sex.values()))
plt.show()

