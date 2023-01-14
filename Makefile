
all: output/abvd_oceanic.nex \
    output/abvd_oceanic.asc.nex \
    output/abvd_oceanic.ascwords.nex \
    output/abvd_oceanic.nocombining.ascwords.nex

output/abvd_oceanic.nex:
	cldfbench abvdoceanic.nexus  --output $@

output/abvd_oceanic.asc.nex:
	cldfbench abvdoceanic.nexus  --output $@ --ascertainment overall

output/abvd_oceanic.ascwords.nex:
	cldfbench abvdoceanic.nexus  --output $@ --ascertainment word

output/abvd_oceanic.nocombining.ascwords.nex:
	cldfbench abvdoceanic.nexus  --output $@ --ascertainment word --removecombined 1

.PHONY: download cldf clean
