#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

lf () {
    tmp="$(mktemp)"
    /usr/bin/lf -last-dir-path="$tmp" "$@"
    if [ -f "$tmp" ]; then
        dir="$(cat "$tmp")"
        rm -f "$tmp"
        if [ -d "$dir" ]; then
            if [ "$dir" != "$(pwd)" ]; then
                cd "$dir"
            fi
        fi
    fi
}

alias ranger='ranger --choosedir=$HOME/.rangerdir; LASTDIR=`cat $HOME/.rangerdir`; cd "$LASTDIR"'
alias ls='ls --color=auto'
alias mkdir='mkdir -pv'
alias wget='wget -c'
#PS1="\e[1m[\u@\h \W]\$ \e[0m"
#PS1="\033[1m[\u@\h \W]€ \033[0m" 
PS1="[\u@\h \W]€ " 
#PS1="€ "
HISTSIZE=
HISTFILESIZE=
