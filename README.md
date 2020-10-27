# cmd-greeter
a command line lightdm greeter

## Arch Linux usage instructions
* Install the lightdm package
* Make sure lightdm is your only enabled display manager service
* Clone this repo
* Edit /etc/lightdm/lightdm.conf so that `greeter-session=lightdm-cmd-greeter` is under the `[Seat:*]` section
* Put lightdm-cmd-greeter.desktop into /usr/share/xgreeters/
* Put com.greyltc.cgreet.conf into /etc/dbus-1/system.d/ (& create that folder if it does not exist)
* Reload the dbus service
* Put lightdm-cmd-greeter into /usr/bin/
* Restart the lightdm service
    - this should end your desktop session and present you with your new greeter (a black screen since this is not a graphical greeter)
* Somehow open a terminal on the computer (via ssh or ctrl-alt-f2 or something)
* Execute lightdm-cmd-greeter-login
    - You'll be prompted for a user name and password
    - If you enter them correctly, that user's default destop session should launch
