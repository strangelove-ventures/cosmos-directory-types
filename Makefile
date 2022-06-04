CHAINS_ENDPOINT := https://chains.cosmos.directory
VALIDATORS_ENDPOINT := https://validators.cosmos.directory

SAMPLE_DIRNAMES := chains chain validators validator chain-validators

prepare:
	yarn install
	mkdir -p $(foreach dirname,$(SAMPLE_DIRNAMES),samples/$(dirname))
	curl -s "$(CHAINS_ENDPOINT)" > samples/chains/index.json
	curl -s "$(CHAINS_ENDPOINT)/cosmoshub" > samples/chain/cosmoshub.json
	curl -s "$(CHAINS_ENDPOINT)/juno" > samples/chain/juno.json
	curl -s "$(CHAINS_ENDPOINT)/osmosis" > samples/chain/osmosis.json
	curl -s "$(VALIDATORS_ENDPOINT)" > samples/validators/index.json
	curl -s "$(VALIDATORS_ENDPOINT)/deuslabs" > samples/validator/deuslabs.json
	curl -s "$(VALIDATORS_ENDPOINT)/ezstaking" > samples/validator/ezstaking.json
	curl -s "$(VALIDATORS_ENDPOINT)/oni" > samples/validator/oni.json
	curl -s "$(VALIDATORS_ENDPOINT)/chains/cosmoshub" > samples/chain-validators/cosmoshub.json
	curl -s "$(VALIDATORS_ENDPOINT)/chains/juno" > samples/chain-validators/juno.json
	curl -s "$(VALIDATORS_ENDPOINT)/chains/osmosis" > samples/chain-validators/osmosis.json

build:
	CHAINS_ENDPOINT=$(CHAINS_ENDPOINT) VALIDATORS_ENDPOINT=$(VALIDATORS_ENDPOINT) ./build.js

clean:
	rm -rf dist/**/*
	rm -rf samples/**/*
