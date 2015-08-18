import sys
import settings

triggers = ["^!reload"]

def main(args):
    if args['msg'].Sender.Handle not in settings.ADMINS:
        args['msg'].Chat.SendMessage(args['msg'].Sender.Handle + "Does not have access to that command")
    else:
        args['main'].reloadModules()
        args['msg'].Chat.SendMessage("Modules reloaded")
        args['msg'].Chat.SendMessage("Availble modules are: " + str(args['main'].lModules.keys()))

if __name__ == '__main__':
    raise Exception("You cannot run a module from command line")
