@ECHO OFF

@docker run --rm -i --net=none -v %CD%:/data blang/latex:ctanfull latexmk -cd -f -interaction=batchmode -pdf %1