
DICTS=mmcif_pdbx_v5_next mmcif_pdbx_v50

all:
	@for dict in $(DICTS); do \
		echo "Building $$dict"; \
		./scripts/Build.sh $$dict ;\
	 done
