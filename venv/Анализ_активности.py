import vk_api

login = 'mylogin'
password = 'mypassword'
token='token'

vk_session = vk_api.VkApi(login, password, token)
vk = vk_session.get_api()

group_id='-183283083'
how_many_post=input('Как много постов:')
how_many_liks=input('Как много лайков им надо иметь:')
how_many_comments=input('Как много комментов им надо иметь:')
print('Теперь жди')
otchot={}
post_id=[]

info=vk.wall.get(owner_id=group_id,count=how_many_post)
for i in info['items']:
    post_id+=[i['id']]


for i in post_id:

    info_repost = vk.wall.getReposts(owner_id=group_id, post_id=f'{i}', count='9')
    info_comment = vk.wall.getComments(owner_id=group_id, post_id=f'{i}', extended='1')
    info_like = vk.likes.getList(type='post', owner_id=group_id, item_id=f'{i}', extended='1')


    for j in info_repost.get('profiles'):
        id=j.get('id')
        first_name=j.get('first_name')
        last_name=j.get('last_name')

        if id in otchot.keys():
            otchot[id][1]+=1
        else:
            otchot[id]=[first_name+' '+last_name,1,0,0]

    for j in info_like.get('items'):
        id=j.get('id')
        first_name=j.get('first_name')
        last_name=j.get('last_name')

        if id in otchot.keys():
            otchot[id][2]+=1
        else:
            otchot[id]=[first_name+' '+last_name,0,1,0]

    for j in info_comment.get('items'):
        id=j.get('from_id')


        if id in otchot.keys():
            otchot[id][3]+=1
        else:
            otchot[id]=['No name',0,0,1]

print('    id        Name            repost  like  comment')
for i in otchot.keys():
    if (otchot[i][2] >= int(how_many_liks)) or (otchot[i][3] >= int(how_many_comments)):
        print(f'{i}  {" "*(9-len(str(i)))}{otchot[i][0]}  {" "*(20-len(str(otchot[i][0])))}{otchot[i][1]}  {" "*(5-len(str(otchot[i][1])))}{otchot[i][2]}  {" "*(5-len(str(otchot[i][2])))}{otchot[i][3]}')