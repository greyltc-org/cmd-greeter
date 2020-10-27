# cmd-greeter
a command line lightdm greeter

## Install
Install the lightdm-cmd-greeter package [from the AUR](https://aur.archlinux.org/packages/lightdm-cmd-greeter/)

or manually (tested only in Arch Linux):  

* Install the lightdm, python and python-pydbus packages
* Clone this repo
* Put lightdm-cmd-greeter.desktop into /usr/share/xgreeters/
* Put com.greyltc.cgreet.conf into /etc/dbus-1/system.d/ (& create that folder if it does not exist)
* Put lightdm-cmd-greeter into /usr/bin/
* Reload the dbus service
## Setup
* Make sure lightdm is your only enabled display manager service
* Edit /etc/lightdm/lightdm.conf so that `greeter-session=lightdm-cmd-greeter` is under the `[Seat:*]` section
## Usage
* Restart the lightdm service
    - this should end your desktop session and present you with your new greeter (a black screen since this is not a graphical greeter)
* Somehow open a terminal on the computer (via ssh or ctrl-alt-f2 or something)
* Execute lightdm-cmd-greeter-login
    - You'll be prompted for a user name and password
    - If you enter them correctly, that user's default destop session should launch
