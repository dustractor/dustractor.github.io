test:
	sass scss/screen.scss style/screen.css
	./gents > index.html
	firefox index.html

code:
	vim -c 'so proj.vim'
