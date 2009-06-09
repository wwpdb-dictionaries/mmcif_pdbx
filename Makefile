EXTERNAL_DATA_DIRS = mmcif_pdbx mmcif_pdbx_internal mmcif_std mmcif_ddl mmcif_pdbx_v31
INTERNAL_DATA_DIRS = mmcif_nmr-star mmcif_em mmcif_emx mmcif_biosync mmcif_ccp4 mmcif_iims mmcif_img mmcif_mdb mmcif_rcsb_nmr mmcif_rcsb_xray mmcif_rcsb_internal mmcif_sym

DATADIRS = $(INTERNAL_DATA_DIRS) $(EXTERNAL_DATA_DIRS)


install: all

all:	compile 

clean_build: clean

compile:
	@for datadir in $(DATADIRS); do \
		echo " "; \
		echo "------------------------------------------------------------"; \
		echo "**** Making $$datadir ****"; \
		echo "------------------------------------------------------------"; \
		(cd dict-$$datadir && make ) || exit 1; \
	done
	@cp mmcif/*.dic ../mmcif

debug:
	@for datadir in $(DATADIRS); do \
		echo " "; \
		echo "------------------------------------------------------------"; \
		echo "**** Making $$datadir ****"; \
		echo "------------------------------------------------------------"; \
		(cd dict-$$datadir && make ) || exit 1; \
	done
	@cp mmcif/*.dic ../mmcif

clean:
	@for datadir in $(DATADIRS); do \
		echo cleaning $$datadir; \
		(cd dict-$$datadir && make clean) || exit 1; \
	done

	@cd mmcif; rm -f *.dic

