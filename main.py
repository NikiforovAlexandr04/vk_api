import time
from urllib.parse import urlencode
import requests as requests


def get_data(method, params, token):
    params.append(("access_token", token))
    params.append(("v", "5.124"))
    url = "https://api.vk.com/method/{}?{}".format(method, urlencode(params))
    response = requests.get(url)
    answer = response.json()
    return answer


def get_albums(user_id, token):
    data = get_data("photos.getAlbums", [("uid", user_id)], token)
    print('Количество альбомов: ' + str(data['response']['count']))
    for i, album in enumerate(data['response']['items']):
        print(i + 1)
        print('ID: ' + str(album['id']) + '\n' + 'Название: ' + str(album['title']) + '\n' + 'Количество фото: ' + str(
            album['size']))


def get_friends(user_id, token):
    data = get_data("getFriends", [("uid", user_id)], token)['response']
    print('Количество друзей: ' + str(data['count']))
    for n, id in enumerate(data['items']):
        wall = get_data("users.get", [("user_ids", id)], token)['response'][0]
        print(str(n+1) + '. ' + str(wall['first_name']) + ' ' + str(wall['last_name']))
        time.sleep(0.5)


def get_wall(user_id, token):
    data = get_data("users.get", [("user_ids", user_id)], token)['response'][0]
    print('Имя: ' + str(data['first_name']))
    print('Фалимиля: ' + str(data['last_name']))
    print('ID: ' + str(data['id']))
    if data['is_closed']:
        print('Аккаунт закрыт')
    else:
        print('Аккаунт открыт')


def main():
    user_id = input('userID: ')
    action = input('Введите albums для просмотра информации об альбомах; wall для просмотра страницы пользователя, '
                   'friends для просмотра друзей: \n')
    acccess_token = input('access_token: ')
    if action == 'albums':
        get_albums(user_id, acccess_token)
    elif action == 'wall':
        get_wall(user_id, acccess_token)
    elif action == 'friends':
        get_friends(user_id, acccess_token)
    else:
        print("Неизвестная команда")


if __name__ == '__main__':
    main()
