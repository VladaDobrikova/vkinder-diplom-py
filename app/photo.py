from config.imports import *


def photos_getAll(owner_id):
    ''' Возвращает все фото в обратном порядке, сортировка и отбор по лайкам
    '''
    dict = {}
    link_profile = 'https://vk.com/id'
    vk = vk_api.VkApi(token=vk_access_token)
    response = vk.method('photos.getAll',
                          {'owner_id': owner_id,
                           'extended': 1,
                           'count': 200})
    for item in response['items']:
        m = 0
        for i in item['sizes']:
            if i['height'] > m:
                m = i['height']
                url = i['url']
        dict[item['id']] = {'url' : url,
                            'likes' : item['likes']['count']}

    df = pd.DataFrame(dict)
    data = df.transpose()
    data = data.sort_values(by='likes', ascending=False)
    data1 = data.head(3)
    dict2 = data1.to_dict('index')
    return dict2


def photos_getMessagesUploadServer():
    ''' Возвращает все фото в обратном порядке, сортировка и отбор по лайкам
    '''
    dict = {}
    link_profile = 'https://vk.com/id'
    vk = vk_api.VkApi(token=access_token_group)
    response = vk.method('photos.getMessagesUploadServer',
                          {'group_id': group_id})
    return response
