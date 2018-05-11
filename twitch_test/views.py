from django.shortcuts import render

from twitch import TwitchClient


def home(request):
    client = TwitchClient('jcpe0okes3rzyqvoaopi65mptv8vh1')

    fcc_users = [
        'ESL_SC2',
        'OgamingSC2',
        'cretetion',
        'freecodecamp',
        'storbeck',
        'habathcx',
        'RobotCaleb',
        'noobs2ninjas',
        'Ninja',
        'omgcorey1'
    ]

    user_list = client.users.translate_usernames_to_ids(fcc_users)
    users = []

    for user in user_list:
        user_dict = {}
        stream = client.streams.get_live_streams(user.id)
        user_dict['name'] = user.name
        user_dict['logo'] = str(user['logo'])
        user_dict['profile'] = 'https://twitch.tv/' + user.name

        if not stream:
            user_status = user_dict['name'] + ' is offline'
            user_dict['status'] = user_status
        else:
            user_status = user_dict['name'] + ' is now playing: ' + stream[0]['game']
            user_dict['status'] = user_status
        users.append(user_dict)

    context = {
        'users': users,
    }

    return render(request, 'home.html', context)
