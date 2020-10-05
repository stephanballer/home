#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ranger='ranger --choosedir=$HOME/.rangerdir; LASTDIR=`cat $HOME/.rangerdir`; cd "$LASTDIR"'
alias ls='ls --color=auto'
alias mkdir='mkdir -pv'
alias wget='wget -c'
#PS1="\e[1m[\u@\h \W]\$ \e[0m"
PS1="[\u@\h \W]€ " 
#PS1="€ "
