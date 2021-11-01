# source this file in the actual .bashrc file
# source /home/cscarbone/git/cscarbone07/configs/.bashrc


tmux source-file ~/.tmux.conf
#tmux

wC=/mnt/c/Users/CSCarbone
wH=/mnt/d/M/C
#cd $wC 

if [ ! "$TMUX" ]; then
  tmux
fi

export LAST_KEYBOARD_LAYOUT="us"
