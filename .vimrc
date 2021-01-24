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
set spell
set tabstop=8 softtabstop=0 expandtab shiftwidth=4 smarttab

" vmap <C-x> "+d
" vmap <C-v> "+p
" imap <C-c> <ESC>"+yya
map <C-j> :winc j<CR>
map <C-k> :winc k<CR>
map <C-h> :winc h<CR>
map <C-l> :winc l<CR>
map <leader>f :Lf

augroup SpellUnderline
  autocmd!
  autocmd ColorScheme *
    \ highlight SpellBad
    \   cterm=Underline
    \   ctermfg=NONE
    \   ctermbg=NONE
    \   term=Reverse
    \   gui=Undercurl
    \   guisp=Red
  autocmd ColorScheme *
    \ highlight SpellCap
    \   cterm=Underline
    \   ctermfg=NONE
    \   ctermbg=NONE
    \   term=Reverse
    \   gui=Undercurl
    \   guisp=Red
  autocmd ColorScheme *
    \ highlight SpellLocal
    \   cterm=Underline
    \   ctermfg=NONE
    \   ctermbg=NONE
    \   term=Reverse
    \   gui=Undercurl
    \   guisp=Red
  autocmd ColorScheme *
    \ highlight SpellRare
    \   cterm=Underline
    \   ctermfg=NONE
    \   ctermbg=NONE
    \   term=Reverse
    \   gui=Undercurl
    \   guisp=Red
  augroup END

colorscheme default

if has("autocmd")
  au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$")
    \| exe "normal! g'\"" | endif
endif

let g:vimtex_view_general_viewer = 'zathura'
let g:vimtex_quickfix_blgparser = 'enable'
let g:Tex_flavor='latex'
let g:Tex_BibtexFlavor = 'biber'
let g:Tex_MultipleCompileFormats='pdf,dvi'
let g:Tex_DefaultTargetFormat="pdf"
let g:Tex_CompileRule_pdf = 'pdflatex --synctex=-1 -src-specials -interaction=nonstopmode -file-line-error-style $*'

call plug#begin('~/.vim/plugged')

Plug 'ervandew/supertab'
Plug 'lervag/vimtex'
Plug 'ptzz/lf.vim'

call plug#end()


