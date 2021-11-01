"" General
set number	" Show line numbers
set linebreak	" Break lines at word (requires Wrap lines)
set showbreak=+++	" Wrap-broken line prefix
set textwidth=100	" Line wrap (number of cols)
set showmatch	" Highlight matching brace
"set visualbell	" Use visual bell (no beeping)
set clipboard=unnamedplus

"use this to not consider deleted characters in clipboard
noremap <Leader>p "0p
noremap <Leader>P "0P
vnoremap <Leader>p "0p

set hlsearch	" Highlight all search results
set smartcase	" Enable smart-case search
set ignorecase	" Always case-insensitive
set incsearch	" Searches for strings incrementally
 
set autoindent	" Auto-indent new lines
set shiftwidth=2	" Number of auto-indent spaces
set smartindent	" Enable smart-indent
set smarttab	" Enable smart-tabs
set softtabstop=2	" Number of spaces per Tab
 
"# Advanced
set ruler	" Show row and column ruler information
 
set undolevels=1000	" Number of undo levels
set backspace=indent,eol,start	" Backspace behaviour


augroup highlightcursorline
    autocmd!
    autocmd VimEnter,WinEnter * set cursorline cursorcolumn
    autocmd WinLeave * set nocursorline nocursorcolumn
augroup END

" remap split navigations to ctrl + hjkl
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>












" --------------------------------- PLUGIN AREA-------------------------------

" adding fzf plugin
set rtp+=~/.fzf

nmap <A-f> :FZF<ENTER>


" To add plugins with vim plug, follow instructions from
" https://github.com/junegunn/vim-plug
" https://github.com/junegunn/vim-plug/wiki/tutorial

" Plugins will be downloaded under the specified directory.
call plug#begin()
"call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.vim/plugged')

" Declare the list of plugins.
"Plug 'tpope/vim-sensible'
"Plug 'junegunn/seoul256.vim'
Plug 'morhetz/gruvbox'
Plug 'neoclide/coc.nvim', {'branch': 'release'}

" Managing navigation between vim and tmux
" allows to use the same keys (CTRL+hjkl) for smothly navigating between tmux
" and vim panels... its like magic :-)
Plug 'christoomey/vim-tmux-navigator'


" Ultisnips plugin
" Track the engine.
Plug 'SirVer/ultisnips'

" Snippets are separated from the engine. Add this if you want them:
Plug 'honza/vim-snippets'

" Trigger configuration. You need to change this to something other than <tab> if you use one of the following:
" - https://github.com/Valloric/YouCompleteMe
" - https://github.com/nvim-lua/completion-nvim
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<c-b>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"

" If you want :UltiSnipsEdit to split your window.
let g:UltiSnipsEditSplit="vertical"




" List ends here. Plugins become visible to Vim after this call.
call plug#end()
