from Include.core.helpers.requestApi import get_users

profile_info_text = 'Информация о вашем профиле'
profile_security = '👮‍♀ Здесь отображена информация которая видна другим пользователям'
profile_view = 'Профиль пользователя'

def get_info_user(tgid):
    users = get_users()
    data = []
    for id in range(0, len(users)):
        telegramid = users[id]['telegram_id']
        if telegramid == tgid:
            data.append('🙍 ‍Фамиля Имя: {}'.format(users[id]['full_name']))
            if users[id]['university']:
                data.append('🏫 Информация об образовании: {}'.format(users[id]['university']))
            if users[id]['email']:
                data.append('✉ Email: {}'.format(users[id]['email']))
            if users[id]['vk']:
                data.append('👨‍👨‍👦 Вконтакте: {}'.format(users[id]['vk']))
            if users[id]['about_me']:
                data.append('📝 Ваше описание: {}'.format(users[id]['about_me']))

    fin_text = ''
    for i in data:
        fin_text += i+"\n"

    return fin_text
