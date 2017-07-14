#
#
#
SHELL=/bin/sh
MAKE=make

all:	compile 
install: compile
build:  compile

checkout:
	curl https://raw.githubusercontent.com/ihmwg/IHM-dictionary/master/ihm-extension.dic -o ihm-extension.dic

compile:
	cp mmcif_ihm_ep.dic ihm-extension.dic
	@cp ihm-extension.dic ../mmcif

clean:
	@rm -rf mmcif_ihm.dic
####
