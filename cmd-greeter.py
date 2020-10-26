#!/usr/bin/env python3

# gobject introspection
import gi

import warnings
import sys
import traceback

# for IPC (used to transmit login and password)
from pydbus import SystemBus  # TODO: replace this. it's abandoned

with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    from gi.repository import LightDM
from gi.repository import GLib

log_file = "/run/lightdm/log.txt"

def lprint(*args, **kwargs):
    original_stdout = sys.stdout # Save a reference to the original standard output
    with open(log_file, 'a') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(*args, **kwargs)
        sys.stdout = original_stdout # Reset the standard output to its original value

class CGreet:
    dbus_connected = False
    lightdm_connected = False
    exit_code = 1
    login = None
    password = None

    def __init__(self):
        with open(log_file, 'w') as f:
            f.write("Log Start\n")

    def setup(self, *args, **kwargs):
        self.g = LightDM.Greeter.new()
        self.g.connect('show-prompt', self.show_prompt)
        self.g.connect('authentication-complete', self.authentication_complete)
        
        try:
            self.g.connect_to_daemon_sync()
            self.lightdm_connected = True
        except Exception:
            print("Exception connecting to daemon:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)
            self.exit_code = 1
        
        try:
            self.system_bus = SystemBus()
            self.dbus_connected = True
        except Exception:
            print("Exception connecting to dbus:")
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)
            self.exit_code = 1

    def show_prompt(self, greeter, text, prompt_type):
        if prompt_type == LightDM.PromptType.QUESTION and (text == "login:"):
            lprint(f'prompt_type  = {prompt_type} :: text = "{text}"')
            greeter.respond(self.login)
        elif prompt_type == LightDM.PromptType.SECRET and (text == "Password: "):
            lprint(f'prompt_type  = {prompt_type} :: text = "{text}"')
            greeter.respond(self.password)
        else:
            lprint(f'prompt_type  = {prompt_type} :: text = "{text}"')

    def authentication_complete(self, greeter):
        session_started = False
        auth_result = greeter.get_is_authenticated()
        lprint(f"authenticated  = {auth_result}")

        if auth_result == True:
            session_started = greeter.start_session_sync(None)  # start the default session
            self.loop.quit()
            lprint(f"session_started  = {session_started}")
            self.loop.quit()

    def run(self):
        self.loop = GLib.MainLoop.new(None, False)

        if (self.dbus_connected == True) and (self.lightdm_connected == True):
            self.g.authenticate()
            self.exit_code = self.loop.run()

        return self.exit_code


if __name__ == "__main__":
    cg = CGreet()
    cg.setup(sys.argv)

    # TODO: next step is to allow the user to input these in a safe way
    cg.login = "archie"
    cg.password = "none"

    exit_code = cg.run()
    sys.exit(exit_code)
