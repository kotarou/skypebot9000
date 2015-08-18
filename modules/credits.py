import sys
import settings

triggers = ["^!credits"]

def main(args):
    args['msg'].Chat.SendMessage("Skypebot written by kotarou")


if __name__ == '__main__':
    raise Exception("You cannot run a module from command line")
