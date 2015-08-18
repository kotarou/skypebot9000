#!/usr/bin/env python

from skype4py.Skype4Py import *
import time
import re
import modules
import settings

authNames = ["aronyan1337"]

class SkypeBot(object):

    def __init__(self):
        self.skype = Skype(Events=self)
        #self.skype.FriendlyName = "Skype Bot"
        self.skype.Attach()

        # Load the modules
        modules.loadModules()
        self.lModules = modules.modules
        # print(modules.modules['credits'].module.main([]))
        # print(modules.modules)

    def reloadModules(self):
        modules.loadModules()
        self.lModules = modules.modules

    def AttachmentStatus(self, status):
        if status == apiAttachAvailable:
            self.skype.Attach()

    def MessageStatus(self, msg, status):
        print(status)
        if status == cmsReceived:
            print(msg.Chat.Type)
            if msg.Chat.Type in settings.ALLOWED_CHAT_TYPES:
                for module_ in self.lModules.values():
                    for trigger in module_.triggers:
                        match = re.search(trigger, msg.Body, re.IGNORECASE)
                        args = {'msg': msg, 'skype': skype, 'main': self}
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

    def cmd_userstatus(self, msg, status):
        if msg.Sender.Handle not in authNames:
            return "I'm afraid I can't let you do that, " + msg.FromDisplayName
        if status:
            try:
                self.skype.CurrentUserStatus = status
            except SkypeError, e:
                return str(e)
        return 'Current status: %s' % self.skype.CurrentUserStatus

    # def cmd_credit(self, msg):
    #     return self.skype.CurrentUserProfile.BalanceToText

    # def cmd_9gag(self, msg):
    #     s = msg.Sender
    #     c = msg.Chat
    #     mo = c.MemberObjects
    #     for user_ in mo:
    #         if user_.Handle == s.Handle:
    #             if user_.CanSetRoleTo(chatMemberRoleListener):
    #                 user_.Role = chatMemberRoleListener
    #                 return msg.FromDisplayName + " just got muted for being bad."
    #             else:
    #                 return msg.FromDisplayName + " has too much power to be muted, but is still a shitlord."
    #     return "hi"

    # commands = {
    #     "@userstatus *(.*)": cmd_userstatus,
    #     #"credit": cmd_credit,
    #     "9gag.com": cmd_9gag
    # }

if __name__ == "__main__":
    bot = SkypeBot()

    while True:
        time.sleep(1.0)
