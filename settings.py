from skype4py.Skype4Py.enums import *
from enums import *

# The relative or absolute paths of module folders for loading
MODULE_PATHS = ["modules"]

# Admins are the only ones allowed to issue sensitive commands to the bot
ADMINS = ["aronyan1337", "offenderninethousand"]

# Use a blacklist or a whitelist? This is global
# Note that if you use a whitelist, you will need to manually add your PM channel with the bot to make it react to you
CHAT_RESTRCT_TYPE = CHAT_RESTRICT_WHITELIST
# Chats that we will not react to
CHAT_BLACKLIST = []
# Chats that we will react to
CHAT_WHITELIST = ["name=#offenderninethousand/$729f69da8783440d", "#live:freeyorp101/$e8a84be0086d982b", "#offenderninethousand/$aronyan1337;5dde4b02b1eec1d5", "name=#sam.burns.wellington/$182ccd28efea1693", "#aronyan1337/$offenderninethousand;3977caa726dce30e"]

# Don't change under here unless you really know what you are doing
# this doesn't work on *nix
ALLOWED_CHAT_TYPES = [chatTypeDialog, chatTypeLegacyDialog, chatTypeMultiChat]
