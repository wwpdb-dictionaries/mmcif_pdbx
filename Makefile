
DICTS=mmcif_pdbx_v50 mmcif_pdbx_v5_next
#DICTS=mmcif_pdbx_v5_next
TARGET=local

all:
	@for dict in $(DICTS); do \
		echo "Building $$dict"; \
		./scripts/Build.sh $$dict $(TARGET) ;\
	 done
