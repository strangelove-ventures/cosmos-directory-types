# cosmos-directory-types

Generated types from [eco-stake/cosmos-directory](https://github.com/eco-stake/cosmos-directory) endpoints using [quicktype](https://github.com/quicktype/quicktype) 🧑‍🚀

## Quickstart

Prerequisites: Make, Node.js 14 or above, Yarn

```sh
make        # bootstrap project dependencies
make build  # generate types artifacts to dist/
```

## Workflow

**Build process**

Refer to project [Makefile](./Makefile) or diagram below.

```plain
                                              ┌──────────────────────┐
                                          ┌──▶│ /                    │───┐
                                          │   └──────────────────────┘   │
                                          │                              │
┌─────────────────────────────────────┐   │        AllChainsData         │
│   https://chains.cosmos.directory   │───┤                              │
└─────────────────────────────────────┘   │                              │
                                          │   ┌──────────────────────┐   │
                                          │   │ /cosmoshub           │   │
                                          └──▶│ /juno                │───┤
                                              │ /osmosis             │   │
                                              └──────────────────────┘   │
                                                                         │
                                                     ChainData           │
                                                                         │
                                                                         │    ┌────────────────┐
                                              ┌──────────────────────┐   │    │       go       │
                                          ┌──▶│ /                    │───┤    ├────────────────┤
                                          │   └──────────────────────┘   │    │     python     │
                                          │                              ├───▶├────────────────┤
                                          │      AllValidatorsData       │    │      rust      │
                                          │                              │    ├────────────────┤
                                          │                              │    │   typescript   │
                                          │   ┌──────────────────────┐   │    └────────────────┘
┌─────────────────────────────────────┐   │   │ /deuslabs            │   │
│ https://validators.cosmos.directory │───┼──▶│ /ezstaking           │───┤
└─────────────────────────────────────┘   │   │ /oni                 │   │
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

**Scheduled GitHub workflow**

Generated types will be rebuilt every 12 hours [(view workflow)](./.github/workflows/schedule.yml).

## License

[MIT License, Copyright (c) 2022 Strangelove Ventures](./LICENSE)
