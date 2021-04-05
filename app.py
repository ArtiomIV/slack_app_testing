import time
import slack
import redis
import json
from threading import Thread
from utils import NewPublicationCheck
from parser_ import main, get_html

red = redis.Redis(
    host = 'redis-18308.c238.us-central1-2.gce.cloud.redislabs.com',
    port = 18308,
    password = 'ljLCe2nxalVGsAtde9nHglLiZJVMFVS7'
)


def startSlackBot():
    workspaces_settings = json.loads(red.get('workspaces'))

    for token in workspaces_settings:
        titels = NewPublicationCheck()
        Thread(target = postMessagge, args = (token, workspaces_settings[token], titels)).start()


def postMessagge(token, tegs, titles):
    while True:
        settings = json.loads(red.get('settings'))
        parser_data = main(get_html(settings['host']))
        client = slack.WebClient(token = token)
        try:
            if int(settings['update_frequency']) == 0:

                titles_to_publish = titles.newPublicationIstant(parser_data, tegs, settings)

                for channel in titles_to_publish:
                        items = titles_to_publish[channel]
                        client.chat_postMessage(channel = channel, text = f"{items[0]} \n{items[1]} \n{items[2]} \n{items[3]}")

            else:

                titles_to_publish = titles.newPublicationTime(parser_data, tegs, settings)

                for channel in titles_to_publish:
                        items = titles_to_publish[channel]
                        client.chat_postMessage(channel = channel, text = f"{items[0]} \n{items[1]} \n{items[2]} \n{items[3]}")
        except Exception as e:
            continue

        time.sleep(2)
 
startSlackBot()