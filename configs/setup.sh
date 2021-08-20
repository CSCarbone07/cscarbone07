config_names=(
$PWD"/.bash_aliases"
$PWD"/.tmux.conf" 
$PWD"/.vimrc"
$PWD"/init.vim" 
)
config_paths=(
$HOME"/.bash_aliases"
$HOME"/.tmux.conf" 
$HOME"/.vimrc" 
$HOME"/.config/nvim/init.vim" 
)
#config_names[1]=.vimrc 
declare -i it=0
for var in ${config_paths[@]}
do
    echo $var
    echo ${config_names[$it]} 

    
    if sudo ln -s ${config_names[$it]} $var
    then
	echo $var succesfully linked
    else
	echo $var file was already set up, readding link
	rm $var 
	sudo ln -s ${config_names[$it]} $var
    fi

    it+=1

done



sudo apt install xclip
