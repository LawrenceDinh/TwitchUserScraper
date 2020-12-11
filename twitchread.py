import subprocess
import csv
import requests
import json

 # dict_keys(['mature', 'status', 'broadcaster_language',
# 'broadcaster_software', 'display_name', 'game', 'language', '_id',
# 'name', 'created_at', 'updated_at', 'partner', 'logo', 'video_banner',
# 'profile_banner', 'profile_banner_background_color', 'url', 'views',
# 'followers','broadcaster_type', 'description', 'private_video',
# 'privacy_options_enabled'])


def getchannelinfo(id):
    headers = {
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Client-ID': '5iuiucupzpmifw8n653tlmv5eki82z',
    }

    url = "https://api.twitch.tv/kraken/channels/" + id
    response = requests.get(url,
                            headers=headers)
    #print(id + " " + str(response.status_code))
    if response.status_code == 200:
        data = json.loads(response.text)
        dname = data['display_name']
        game = data['game']
        #print(data.keys())
    else:
        data = None

    return data

