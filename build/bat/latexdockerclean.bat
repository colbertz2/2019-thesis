@ECHO OFF

@docker run --rm -i --net=none -v %CD%:/data blang/latex:ctanfull latexmk -cd -c %1