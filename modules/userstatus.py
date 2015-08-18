import sys
import settings

triggers = ["^!stuff"]

def main(args):
    args['msg'].Chat.SendMessage("This is a test")

if __name__ == '__main__':
    raise Exception("You cannot run a module from command line")
