import sys
import settings
from skype4py.Skype4Py.enums import *
import threading

triggers = ["9gag.com", "^honk"]

def changeRole(chat, user, role):
    if role == chatMemberRoleListener:
        chat.SendMessage(user.Handle + " just got muted for 20s for being bad.")
    user.Role = role

def main(args):
    s = args['msg'].Sender
    c = args['msg'].Chat
    mo = c.MemberObjects
    for user_ in mo:
        if user_.Handle == s.Handle:
            if user_.CanSetRoleTo(chatMemberRoleListener):
                oldRole = user_.Role
                changeRole(args['msg'].Chat, user_, chatMemberRoleListener)
                threading.Timer(20, changeRole, [args['msg'].Chat, user_, oldRole]).start()
            else:
                args['msg'].Chat.SendMessage(args['msg'].FromDisplayName + " has too much power to be muted, but is still a shitlord.")
            break

if __name__ == '__main__':
    raise Exception("You cannot run a module from command line")

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
