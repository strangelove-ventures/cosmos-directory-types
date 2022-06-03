# cosmos-directory-types

Generated types from [cosmos.directory](https://github.com/eco-stake/cosmos-directory) endpoints using [quicktype](https://github.com/quicktype/quicktype) 🧑‍🚀

## Quickstart

Prerequisites: Make, Node.js 14 or above, Yarn

```sh
make        # prepare sample files to generate types
make build  # generate types artifacts to dist/
```

## Workflow

- Get sample endpoint results for each paths, save as JSON files
- Generate types artifacts, output as `.go`, `.py`, `.rs`, and `.ts`

```plain
                                              ┌──────────────────────┐
                                          ┌──▶│ /                    │───┐
                                          │   └──────────────────────┘   │
                                          │                              │
                                          │        AllChainsData         │
                                          │                              │
                                          │                              │
                                          │   ┌──────────────────────┐   │
                                          │   │ /cosmoshub           │   │
                                          ├──▶│ /juno                │───┤
                                          │   │ /osmosis             │   │
                                          │   └──────────────────────┘   │
                                          │                              │
                                          │          ChainData           │
                                          │                              │
                                          │                              │    ┌────────────────┐
                                          │   ┌──────────────────────┐   │    │       go       │
┌─────────────────────────────────────┐   ├──▶│ /                    │───┤    ├────────────────┤
│   https://chains.cosmos.directory   │   │   └──────────────────────┘   │    │     python     │
└─────────────────────────────────────┘   │                              ├───▶├────────────────┤
┌─────────────────────────────────────┐───┤      AllValidatorsData       │    │      rust      │
│ https://validators.cosmos.directory │   │                              │    ├────────────────┤
└─────────────────────────────────────┘   │                              │    │   typescript   │
                                          │   ┌──────────────────────┐   │    └────────────────┘
                                          │   │ /deuslabs            │   │
                                          ├──▶│ /ezstaking           │───┤
                                          │   │ /oni                 │   │
                                          │   └──────────────────────┘   │
                                          │                              │
                                          │        ValidatorData         │
                                          │                              │
                                          │                              │
                                          │   ┌──────────────────────┐   │
                                          │   │ /chains/cosmoshub    │   │
                                          └──▶│ /chains/juno         │───┘
                                              │ /chains/osmosis      │
                                              └──────────────────────┘

                                                ChainValidatorsData



               endpoints                           endpoint paths               generated types

```

## License

[MIT License, Copyright (c) 2022 Strangelove Ventures](./LICENSE)
