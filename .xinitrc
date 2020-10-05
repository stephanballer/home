#!/bin/sh

#eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh)
#export SSH_AUTH_SOCK 

export EDITOR='/bin/vim' VISUAL='/bin/vim'

exec dbus-launch --exit-with-session i3
