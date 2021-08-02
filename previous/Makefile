DATADIRS = mmcif_pdbx_v31 mmcif_pdbx_v32 mmcif_pdbx_v33 mmcif_pdbx_v40 mmcif_pdbx_v41 mmcif_pdbx_v42


all:	compile 

clean_build: clean

compile:
	@mkdir -p dist
	@for datadir in $(DATADIRS); do \
		echo " "; \
		echo "------------------------------------------------------------"; \
		echo "**** Making $$datadir ****"; \
		echo "------------------------------------------------------------"; \
		(cd dict-$$datadir && make ) || exit 1; \
	done

clean:
	@for datadir in $(DATADIRS); do \
		echo cleaning $$datadir; \
		(cd dict-$$datadir && make clean) || exit 1; \
	done
	@cd dist; rm -f *.dic

