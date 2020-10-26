# cmd-greeter
a command line lightdm greeter

## Arch Linux usage instructions
* Install the lightdm package
* Make sure lightm is your only enabled display manager service
* Clone this repo into /var/tmp/
* Edit /etc/lightdm/lightdm.conf so that 'greeter-session=lightdm-cmd-greeter' is under the '[Seat:*]' section
* Put lightdm-cmd-greeter.desktop into /usr/share/xgreeters/
* Restart the lightdm service

This is a work in progress. Today it can only log in a user named "archie" with the password "none"
