import vk_api

login = 'login'
password = 'mypassword'
token='token'
vk_session = vk_api.VkApi(login, password, token)
vk = vk_session.get_api()
info=vk.wall.getReposts(owner_id='-183283083',post_id='1387',count='9')
for i in info.get('profiles'):
    print(i)


