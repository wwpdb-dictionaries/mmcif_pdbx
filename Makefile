include ../etc/Makefile.platform

EXTERNAL_DATA_DIRS = mmcif_ddl mmcif_std mmcif_em mmcif_pdbx_v40 
INTERNAL_DATA_DIRS = mmcif_pdbx_v41 mmcif_nmr-star mmcif_sas mmcif_biosync mmcif_ccp4 mmcif_img mmcif_mdb mmcif_rcsb_nmr mmcif_rcsb_xray mmcif_sym  mmcif_pdbx_v5_next  mmcif_pdbx_v31 mmcif_pdbx_v32

DATADIRS = $(INTERNAL_DATA_DIRS) $(EXTERNAL_DATA_DIRS)


install: all

all:	compile 

clean_build: clean

compile:
	@mkdir -p ../mmcif
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

export:
	mkdir -p $(EXPORT_DIR)
	@sed 's/^DATADIRS = $$(INTERNAL_DATA_DIRS) $$(EXTERNAL_DATA_DIRS)/DATADIRS = $$(EXTERNAL_DATA_DIRS)/g' Makefile > $(EXPORT_DIR)/Makefile
	mkdir -p $(EXPORT_DIR)/mmcif
	@cp -r dict-mmcif_ddl $(EXPORT_DIR)
	@rm -rf $(EXPORT_DIR)/dict-mmcif_ddl/.svn
	@cp -r dict-mmcif_std $(EXPORT_DIR)
	@rm -rf $(EXPORT_DIR)/dict-mmcif_std/.svn
	@cp -r dict-mmcif_em $(EXPORT_DIR)
	@rm -rf $(EXPORT_DIR)/dict-mmcif_iims/.svn
	@cp -r dict-mmcif_pdbx_v40 $(EXPORT_DIR)
	@rm -rf $(EXPORT_DIR)/dict-mmcif_pdbx_v40/.svn

