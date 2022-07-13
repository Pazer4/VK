import vk_api

login = 'login'
password = 'mypassword'
token='token'
vk_session = vk_api.VkApi(login, password, token)
vk = vk_session.get_api()
info=vk.wall.getComments(owner_id='-195467613',post_id='2', extended='1')
for i in info.get('items'):
    print(i)


