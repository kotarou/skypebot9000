import sys
import settings

triggers = ["^!userstatus"]

def main(args):
    if args['msg'].Sender.Handle not in settings.ADMINS:
        args['msg'].Chat.SendMessage("I'm afraid I can't let you do that, " + args['msg'].FromDisplayName)
    else:
        words = args['msg'].Body.split(" ")
        if len(words) > 1:
            newStatus = words[1]
        else:
            args['msg'].Chat.SendMessage("Current status: " + args['skype'].CurrentUserStatus)
            return
        try:
            args['skype'].CurrentUserStatus = newStatus
        except Exception, e:
            print(e)
            args['msg'].Chat.SendMessage("Error setting userstatus to " + newStatus)
        #return 'Current status: %s' % self.skype.CurrentUserStatus


if __name__ == '__main__':
    raise Exception("You cannot run a module from command line")
