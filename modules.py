# With insirpation fro: https://github.com/opensourcehacker/sevabot
from __future__ import absolute_import, division

import os
import imp
import settings

modules = {}

class Module:

    def __init__(self, skype, name, path):
        # TODO: Scan the file for its regex trigger, which should be defined as "trigger"
        self.skype = skype
        self.path = path
        self.name = name
        self.module = imp.load_source(self.name, self.path)
        self.triggers = self.module.triggers

    @staticmethod
    def isValid(path):
        """
            Simple validity checker.
            TODO: Check if there are any python errors in module before loading it
        """
        return path.endswith(".py")

    def run(self, arg):
        self.module.main(arg)
    # def init(self, skype):
    #     """
    #     (Re)load Python code and get access to exported class instance.
    #     Bound stateful handler to a Skype instance.
    #     """
    #     # http://docs.python.org/2/library/imp.html#imp.load_module
    #     self.module = imp.load_source(self.name, self.path)
    #     #self.handler = module.sevabot_handler
    #     #self.handler.init(skype)


def loadModules():
    """
    Scan all modules folders for executable scripts.
    """

    unloadModules()

    for folder in settings.MODULE_PATHS:
        folder = os.path.abspath(folder)
        for f in os.listdir(folder):
            fpath = os.path.join(folder, f)

            # Remove file extension
            body, ext = os.path.splitext(f)

            module = loadModule(body, fpath)
            if module:
                modules[body] = module

    if not len(modules.keys()):
        raise RuntimeError("No modules found in: %s" % settings.MODULE_PATHS)

    return modules.keys()

def loadModule(name, path):
    # At the moment, only support python programs as modules
    if Module.isValid(path):
        return Module(None, name, path)
    else:
        return None


def unloadModules():
    pass
