" REQUIRED. This makes vim invoke Latex-Suite when you open a tex file.
filetype plugin on
filetype indent on

"set autoindent
set nu
if !isdirectory($HOME."/.vim")
    call mkdir($HOME."/.vim", "", 0770)
endif
if !isdirectory($HOME."/.vim/undo-dir")
    call mkdir($HOME."/.vim/undo-dir", "", 0700)
endif
set undodir=~/.vim/undo-dir
set undofile

" vmap <C-x> "+d
" vmap <C-v> "+p
" imap <C-c> <ESC>"+yya
map <C-j> :winc j<CR>
map <C-k> :winc k<CR>
map <C-h> :winc h<CR>
map <C-l> :winc l<CR>

let g:vimtex_view_general_viewer = 'zathura'
let g:vimtex_quickfix_blgparser = 'enable'

call plug#begin('~/.vim/plugged')

Plug 'ervandew/supertab'
Plug 'lervag/vimtex'

call plug#end()
