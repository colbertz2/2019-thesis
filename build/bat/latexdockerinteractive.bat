@ECHO OFF

@docker run --rm -it --net=none -v %CD%:/data blang/latex:ctanfull bash