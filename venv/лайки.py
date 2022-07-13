import vk_api

login = 'login'
password = 'mypassword'
token='token'
vk_session = vk_api.VkApi(login, password, token)
vk = vk_session.get_api()
info=vk.likes.getList(type='post',owner_id='-183283083',item_id='1387',extended='1')
for i in info.get('items'):
    print(i.get('id'),':',i.get('first_name')+' '+i.get('last_name'))

