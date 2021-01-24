#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [[ ! $DISPLAY && -t 0 && $(tty) == /dev/tty1 ]]; then
	    exec startx -- vt1 &> /dev/null
fi
