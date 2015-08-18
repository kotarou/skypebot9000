#!/usr/bin/env python

from skype4py.Skype4Py import *
import time
import re
import modules
import settings
import sys
from enums import *

class SkypeBot(object):

    def __init__(self):
        if sys.platform == "linux2":
            self.skype = Skype(Transport='x11')
        else:
            # Windows
            self.skype = Skype()

        self.skype = Skype(Events=self)
        print("Skype added!")
        #self.skype.FriendlyName = "Skype Bot"
        self.skype.Attach()
        print("Skype attached!")
        # Load the modules
        modules.loadModules()
        self.lModules = modules.modules
        print("modules loaded!")
        # print(modules.modules['credits'].module.main([]))
        # print(modules.modules)

    def reloadModules(self):
        modules.loadModules()
        self.lModules = modules.modules

    def AttachmentStatus(self, status):
        if status == apiAttachAvailable:
            self.skype.Attach()

    def MessageStatus(self, msg, status):
        if status == cmsReceived:
            if settings.CHAT_RESTRCT_TYPE == CHAT_RESTRICT_WHITELIST and msg.Chat.Name not in settings.CHAT_WHITELIST:
                return
            if settings.CHAT_RESTRCT_TYPE == CHAT_RESTRICT_BLACKLIST and msg.Chat.Name in settings.CHAT_BLACKLIST:
                return
            print(msg.Chat.Type)
            if msg.Chat.Type in settings.ALLOWED_CHAT_TYPES:
                for module_ in self.lModules.values():
                    for trigger in module_.triggers:
                        match = re.search(trigger, msg.Body, re.IGNORECASE)
                        args = {'msg': msg, 'skype': self.skype, 'main': self}
                        if match:
                            msg.MarkAsSeen()
                            module_.run(args)
                            break
            #     for regexp, target in self.commands.items():
            #         match = re.search(regexp, msg.Body, re.IGNORECASE)
            #         if match:
            #             msg.MarkAsSeen()
            #             reply = target(self, msg, *match.groups())
            #             if reply:
            #                 msg.Chat.SendMessage(reply)
            #             break

    # def cmd_credit(self, msg):
    #     return self.skype.CurrentUserProfile.BalanceToText



    # commands = {
    #     "@userstatus *(.*)": cmd_userstatus,
    #     #"credit": cmd_credit,
    #     "9gag.com": cmd_9gag
    # }

if __name__ == "__main__":
    bot = SkypeBot()

    while True:
        time.sleep(1.0)
