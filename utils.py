import pytz
from datetime import datetime, timedelta

class NewPublicationCheck:
    def __init__(self):
        self.first_scan = False
        self.buffer_dict = {}
        self.delta = 0

    def newPublicationIstant(self, info, tegs_list, settings):
        last_article = info[1]['url']
        title_to_publish = {}

        if info[1]['url'] == last_article:
            for channel in tegs_list:
    
                for teg in info[1]["tegs"]:

                    if teg in tegs_list[channel]:
                        title_to_publish[channel] = [settings['text'], last_article, info[1]['text'], info[1]['time']]

        if self.first_scan == False:
    
            for channel in tegs_list:
        
                for teg in info[1]["tegs"]:

                    if teg in tegs_list[channel]:
                        title_to_publish[channel] = [settings['text'], last_article, info[1]['text'], info[1]['time']]
                        self.first_scan = True

        return title_to_publish

    def newPublicationTime(self, info, tegs_list, settings):
        titles_to_publish = {}
        last_article = info[1]['url']
        now = datetime.now(pytz.timezone('Europe/Moscow'))
        now_format = datetime(int(now.strftime("%Y")), int(now.strftime("%m")), int(now.strftime("%d")), int(now.strftime("%H")), int(now.strftime("%M")))

        if info[1]['url'] == last_article:
            for channel in tegs_list:
    
                for teg in info[1]["tegs"]:

                    if teg in tegs_list[channel]:
                        self.buffer_dict[channel] = [settings['text'], last_article, info[1]['text'], info[1]['time']]
                    
                        if now_format == self.delta:
                            titles_to_publish = self.buffer_dict
                            self.buffer_dict = {}
                            self.delta = now_format + timedelta(days = 0) #int(settings['update_frequency'])


        if self.first_scan == False:
            for channel in tegs_list:

                for teg in info[1]["tegs"]:

                    if teg in tegs_list[channel]:
                        titles_to_publish[channel] = [settings['text'], last_article, info[1]['text'], info[1]['time']]
                        self.delta = now_format + timedelta(days = 0)
                        self.first_scan = True

        return titles_to_publish





