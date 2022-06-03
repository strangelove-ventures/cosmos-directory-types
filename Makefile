CHAINS_ENDPOINT := https://chains.cosmos.directory
VALIDATORS_ENDPOINT := https://validators.cosmos.directory

prepare:
	yarn install
	mkdir -p dist/{go,python,rust,typescript}
	mkdir -p samples/{chains,chain,validators,validator,chain-validators}/
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

build: build_go build_python build_rust build_typescript
	date > dist/.timestamp

build_go:
	node_modules/.bin/quicktype --lang go samples/chains --out dist/go/chains.go
	node_modules/.bin/quicktype --lang go samples/chain --out dist/go/chain.go
	node_modules/.bin/quicktype --lang go samples/validators --out dist/go/validators.go
	node_modules/.bin/quicktype --lang go samples/validator --out dist/go/validator.go
	node_modules/.bin/quicktype --lang go samples/chain-validators --out dist/go/chain-validators.go

build_python:
	node_modules/.bin/quicktype --lang python samples/chains --out dist/python/chains.py
	node_modules/.bin/quicktype --lang python samples/chain --out dist/python/chain.py
	node_modules/.bin/quicktype --lang python samples/validators --out dist/python/validators.py
	node_modules/.bin/quicktype --lang python samples/validator --out dist/python/validator.py
	node_modules/.bin/quicktype --lang python samples/chain-validators --out dist/python/chain-validators.py

build_rust:
	node_modules/.bin/quicktype --lang rust samples/chains --out dist/rust/chains.rs
	node_modules/.bin/quicktype --lang rust samples/chain --out dist/rust/chain.rs
	node_modules/.bin/quicktype --lang rust samples/validators --out dist/rust/validators.rs
	node_modules/.bin/quicktype --lang rust samples/validator --out dist/rust/validator.rs
	node_modules/.bin/quicktype --lang rust samples/chain-validators --out dist/rust/chain-validators.rs

build_typescript:
	node_modules/.bin/quicktype --lang typescript samples/chains --out dist/typescript/chains.ts
	node_modules/.bin/quicktype --lang typescript samples/chain --out dist/typescript/chain.ts
	node_modules/.bin/quicktype --lang typescript samples/validators --out dist/typescript/validators.ts
	node_modules/.bin/quicktype --lang typescript samples/validator --out dist/typescript/validator.ts
	node_modules/.bin/quicktype --lang typescript samples/chain-validators --out dist/typescript/chain-validators.ts

clean:
	rm -rf dist/**/*
	rm -rf samples/**/*
