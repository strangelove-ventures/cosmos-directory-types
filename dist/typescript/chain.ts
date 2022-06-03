// To parse this data:
//
//   import { Convert, Cosmoshub, Juno, Osmosis } from "./file";
//
//   const cosmoshub = Convert.toCosmoshub(json);
//   const juno = Convert.toJuno(json);
//   const osmosis = Convert.toOsmosis(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

export interface Cosmoshub {
    repository: Repository;
    chain:      CosmoshubChain;
}

export interface CosmoshubChain {
    $schema:       string;
    chain_name:    string;
    chain_id:      string;
    pretty_name:   string;
    status:        string;
    network_type:  string;
    bech32_prefix: string;
    genesis:       Genesis;
    daemon_name:   string;
    node_home:     string;
    key_algos:     string[];
    slip44:        number;
    fees:          Fees;
    codebase:      Codebase;
    peers:         PurplePeers;
    apis:          Apis;
    explorers:     Explorer[];
    name:          string;
    path:          string;
    symbol:        string;
    denom:         string;
    decimals:      number;
    coingecko_id:  string;
    image:         string;
    height:        number;
    best_apis:     BestApis;
    params:        PurpleParams;
}

export interface Apis {
    rpc:  Grpc[];
    rest: Grpc[];
    grpc: Grpc[];
}

export interface Grpc {
    address:  string;
    provider: string;
}

export interface BestApis {
    rest: Grpc[];
    rpc:  Grpc[];
}

export interface Codebase {
    git_repo:            string;
    recommended_version: string;
    compatible_versions: string[];
    binaries?:           Binaries;
}

export interface Binaries {
    "linux/amd64":    string;
    "linux/arm64"?:   string;
    "darwin/amd64"?:  string;
    "windows/amd64"?: string;
}

export interface Explorer {
    kind:    string;
    url:     string;
    tx_page: string;
}

export interface Fees {
    fee_tokens: FeeToken[];
}

export interface FeeToken {
    denom:               string;
    fixed_min_gas_price: number;
}

export interface Genesis {
    genesis_url: string;
}

export interface PurpleParams {
    authz:                  boolean;
    actual_block_time:      number;
    actual_blocks_per_year: number;
    unbonding_time:         number;
    max_validators:         number;
    blocks_per_year:        number;
    block_time:             number;
    community_tax:          number;
    base_inflation:         number;
    bonded_ratio:           number;
    bonded_tokens:          string;
    total_supply:           string;
    estimated_apr:          number;
    calculated_apr:         number;
}

export interface PurplePeers {
    seeds:            Seed[];
    persistent_peers: PersistentPeer[];
}

export interface PersistentPeer {
    id:      string;
    address: string;
}

export interface Seed {
    id:        string;
    address:   string;
    provider?: string;
}

export interface Repository {
    url:       string;
    branch:    string;
    commit:    string;
    timestamp: number;
}

export interface Juno {
    repository: Repository;
    chain:      JunoChain;
}

export interface JunoChain {
    $schema:       string;
    chain_name:    string;
    status:        string;
    network_type:  string;
    pretty_name:   string;
    chain_id:      string;
    bech32_prefix: string;
    slip44:        number;
    genesis:       Genesis;
    codebase:      Codebase;
    daemon_name:   string;
    node_home:     string;
    key_algos:     string[];
    peers:         FluffyPeers;
    apis:          Apis;
    explorers:     Explorer[];
    name:          string;
    path:          string;
    symbol:        string;
    denom:         string;
    decimals:      number;
    coingecko_id:  string;
    image:         string;
    height:        number;
    best_apis:     BestApis;
    params:        PurpleParams;
}

export interface FluffyPeers {
    seeds:            PersistentPeer[];
    persistent_peers: PersistentPeer[];
}

export interface Osmosis {
    repository: Repository;
    chain:      OsmosisChain;
}

export interface OsmosisChain {
    $schema:       string;
    chain_name:    string;
    status:        string;
    network_type:  string;
    pretty_name:   string;
    chain_id:      string;
    bech32_prefix: string;
    daemon_name:   string;
    node_home:     string;
    genesis:       Genesis;
    key_algos:     string[];
    slip44:        number;
    fees:          Fees;
    codebase:      Codebase;
    peers:         TentacledPeers;
    apis:          Apis;
    explorers:     Explorer[];
    name:          string;
    path:          string;
    symbol:        string;
    denom:         string;
    decimals:      number;
    coingecko_id:  string;
    image:         string;
    height:        number;
    best_apis:     BestApis;
    params:        FluffyParams;
}

export interface FluffyParams {
    authz:                   boolean;
    actual_block_time:       number;
    actual_blocks_per_year:  number;
    unbonding_time:          number;
    max_validators:          number;
    bonded_ratio:            number;
    minting_epoch_provision: number;
    epoch_duration:          number;
    year_minting_provision:  number;
    bonded_tokens:           string;
    total_supply:            string;
    base_inflation:          number;
    calculated_apr:          number;
}

export interface TentacledPeers {
    seeds:            Seed[];
    persistent_peers: Seed[];
}

// Converts JSON strings to/from your types
// and asserts the results of JSON.parse at runtime
export class Convert {
    public static toCosmoshub(json: string): Cosmoshub {
        return cast(JSON.parse(json), r("Cosmoshub"));
    }

    public static cosmoshubToJson(value: Cosmoshub): string {
        return JSON.stringify(uncast(value, r("Cosmoshub")), null, 2);
    }

    public static toJuno(json: string): Juno {
        return cast(JSON.parse(json), r("Juno"));
    }

    public static junoToJson(value: Juno): string {
        return JSON.stringify(uncast(value, r("Juno")), null, 2);
    }

    public static toOsmosis(json: string): Osmosis {
        return cast(JSON.parse(json), r("Osmosis"));
    }

    public static osmosisToJson(value: Osmosis): string {
        return JSON.stringify(uncast(value, r("Osmosis")), null, 2);
    }
}

function invalidValue(typ: any, val: any, key: any = ''): never {
    if (key) {
        throw Error(`Invalid value for key "${key}". Expected type ${JSON.stringify(typ)} but got ${JSON.stringify(val)}`);
    }
    throw Error(`Invalid value ${JSON.stringify(val)} for type ${JSON.stringify(typ)}`, );
}

function jsonToJSProps(typ: any): any {
    if (typ.jsonToJS === undefined) {
        const map: any = {};
        typ.props.forEach((p: any) => map[p.json] = { key: p.js, typ: p.typ });
        typ.jsonToJS = map;
    }
    return typ.jsonToJS;
}

function jsToJSONProps(typ: any): any {
    if (typ.jsToJSON === undefined) {
        const map: any = {};
        typ.props.forEach((p: any) => map[p.js] = { key: p.json, typ: p.typ });
        typ.jsToJSON = map;
    }
    return typ.jsToJSON;
}

function transform(val: any, typ: any, getProps: any, key: any = ''): any {
    function transformPrimitive(typ: string, val: any): any {
        if (typeof typ === typeof val) return val;
        return invalidValue(typ, val, key);
    }

    function transformUnion(typs: any[], val: any): any {
        // val must validate against one typ in typs
        const l = typs.length;
        for (let i = 0; i < l; i++) {
            const typ = typs[i];
            try {
                return transform(val, typ, getProps);
            } catch (_) {}
        }
        return invalidValue(typs, val);
    }

    function transformEnum(cases: string[], val: any): any {
        if (cases.indexOf(val) !== -1) return val;
        return invalidValue(cases, val);
    }

    function transformArray(typ: any, val: any): any {
        // val must be an array with no invalid elements
        if (!Array.isArray(val)) return invalidValue("array", val);
        return val.map(el => transform(el, typ, getProps));
    }

    function transformDate(val: any): any {
        if (val === null) {
            return null;
        }
        const d = new Date(val);
        if (isNaN(d.valueOf())) {
            return invalidValue("Date", val);
        }
        return d;
    }

    function transformObject(props: { [k: string]: any }, additional: any, val: any): any {
        if (val === null || typeof val !== "object" || Array.isArray(val)) {
            return invalidValue("object", val);
        }
        const result: any = {};
        Object.getOwnPropertyNames(props).forEach(key => {
            const prop = props[key];
            const v = Object.prototype.hasOwnProperty.call(val, key) ? val[key] : undefined;
            result[prop.key] = transform(v, prop.typ, getProps, prop.key);
        });
        Object.getOwnPropertyNames(val).forEach(key => {
            if (!Object.prototype.hasOwnProperty.call(props, key)) {
                result[key] = transform(val[key], additional, getProps, key);
            }
        });
        return result;
    }

    if (typ === "any") return val;
    if (typ === null) {
        if (val === null) return val;
        return invalidValue(typ, val);
    }
    if (typ === false) return invalidValue(typ, val);
    while (typeof typ === "object" && typ.ref !== undefined) {
        typ = typeMap[typ.ref];
    }
    if (Array.isArray(typ)) return transformEnum(typ, val);
    if (typeof typ === "object") {
        return typ.hasOwnProperty("unionMembers") ? transformUnion(typ.unionMembers, val)
            : typ.hasOwnProperty("arrayItems")    ? transformArray(typ.arrayItems, val)
            : typ.hasOwnProperty("props")         ? transformObject(getProps(typ), typ.additional, val)
            : invalidValue(typ, val);
    }
    // Numbers can be parsed by Date but shouldn't be.
    if (typ === Date && typeof val !== "number") return transformDate(val);
    return transformPrimitive(typ, val);
}

function cast<T>(val: any, typ: any): T {
    return transform(val, typ, jsonToJSProps);
}

function uncast<T>(val: T, typ: any): any {
    return transform(val, typ, jsToJSONProps);
}

function a(typ: any) {
    return { arrayItems: typ };
}

function u(...typs: any[]) {
    return { unionMembers: typs };
}

function o(props: any[], additional: any) {
    return { props, additional };
}

function m(additional: any) {
    return { props: [], additional };
}

function r(name: string) {
    return { ref: name };
}

const typeMap: any = {
    "Cosmoshub": o([
        { json: "repository", js: "repository", typ: r("Repository") },
        { json: "chain", js: "chain", typ: r("CosmoshubChain") },
    ], false),
    "CosmoshubChain": o([
        { json: "$schema", js: "$schema", typ: "" },
        { json: "chain_name", js: "chain_name", typ: "" },
        { json: "chain_id", js: "chain_id", typ: "" },
        { json: "pretty_name", js: "pretty_name", typ: "" },
        { json: "status", js: "status", typ: "" },
        { json: "network_type", js: "network_type", typ: "" },
        { json: "bech32_prefix", js: "bech32_prefix", typ: "" },
        { json: "genesis", js: "genesis", typ: r("Genesis") },
        { json: "daemon_name", js: "daemon_name", typ: "" },
        { json: "node_home", js: "node_home", typ: "" },
        { json: "key_algos", js: "key_algos", typ: a("") },
        { json: "slip44", js: "slip44", typ: 0 },
        { json: "fees", js: "fees", typ: r("Fees") },
        { json: "codebase", js: "codebase", typ: r("Codebase") },
        { json: "peers", js: "peers", typ: r("PurplePeers") },
        { json: "apis", js: "apis", typ: r("Apis") },
        { json: "explorers", js: "explorers", typ: a(r("Explorer")) },
        { json: "name", js: "name", typ: "" },
        { json: "path", js: "path", typ: "" },
        { json: "symbol", js: "symbol", typ: "" },
        { json: "denom", js: "denom", typ: "" },
        { json: "decimals", js: "decimals", typ: 0 },
        { json: "coingecko_id", js: "coingecko_id", typ: "" },
        { json: "image", js: "image", typ: "" },
        { json: "height", js: "height", typ: 0 },
        { json: "best_apis", js: "best_apis", typ: r("BestApis") },
        { json: "params", js: "params", typ: r("PurpleParams") },
    ], false),
    "Apis": o([
        { json: "rpc", js: "rpc", typ: a(r("Grpc")) },
        { json: "rest", js: "rest", typ: a(r("Grpc")) },
        { json: "grpc", js: "grpc", typ: a(r("Grpc")) },
    ], false),
    "Grpc": o([
        { json: "address", js: "address", typ: "" },
        { json: "provider", js: "provider", typ: "" },
    ], false),
    "BestApis": o([
        { json: "rest", js: "rest", typ: a(r("Grpc")) },
        { json: "rpc", js: "rpc", typ: a(r("Grpc")) },
    ], false),
    "Codebase": o([
        { json: "git_repo", js: "git_repo", typ: "" },
        { json: "recommended_version", js: "recommended_version", typ: "" },
        { json: "compatible_versions", js: "compatible_versions", typ: a("") },
        { json: "binaries", js: "binaries", typ: u(undefined, r("Binaries")) },
    ], false),
    "Binaries": o([
        { json: "linux/amd64", js: "linux/amd64", typ: "" },
        { json: "linux/arm64", js: "linux/arm64", typ: u(undefined, "") },
        { json: "darwin/amd64", js: "darwin/amd64", typ: u(undefined, "") },
        { json: "windows/amd64", js: "windows/amd64", typ: u(undefined, "") },
    ], false),
    "Explorer": o([
        { json: "kind", js: "kind", typ: "" },
        { json: "url", js: "url", typ: "" },
        { json: "tx_page", js: "tx_page", typ: "" },
    ], false),
    "Fees": o([
        { json: "fee_tokens", js: "fee_tokens", typ: a(r("FeeToken")) },
    ], false),
    "FeeToken": o([
        { json: "denom", js: "denom", typ: "" },
        { json: "fixed_min_gas_price", js: "fixed_min_gas_price", typ: 0 },
    ], false),
    "Genesis": o([
        { json: "genesis_url", js: "genesis_url", typ: "" },
    ], false),
    "PurpleParams": o([
        { json: "authz", js: "authz", typ: true },
        { json: "actual_block_time", js: "actual_block_time", typ: 3.14 },
        { json: "actual_blocks_per_year", js: "actual_blocks_per_year", typ: 3.14 },
        { json: "unbonding_time", js: "unbonding_time", typ: 0 },
        { json: "max_validators", js: "max_validators", typ: 0 },
        { json: "blocks_per_year", js: "blocks_per_year", typ: 0 },
        { json: "block_time", js: "block_time", typ: 3.14 },
        { json: "community_tax", js: "community_tax", typ: 3.14 },
        { json: "base_inflation", js: "base_inflation", typ: 3.14 },
        { json: "bonded_ratio", js: "bonded_ratio", typ: 3.14 },
        { json: "bonded_tokens", js: "bonded_tokens", typ: "" },
        { json: "total_supply", js: "total_supply", typ: "" },
        { json: "estimated_apr", js: "estimated_apr", typ: 3.14 },
        { json: "calculated_apr", js: "calculated_apr", typ: 3.14 },
    ], false),
    "PurplePeers": o([
        { json: "seeds", js: "seeds", typ: a(r("Seed")) },
        { json: "persistent_peers", js: "persistent_peers", typ: a(r("PersistentPeer")) },
    ], false),
    "PersistentPeer": o([
        { json: "id", js: "id", typ: "" },
        { json: "address", js: "address", typ: "" },
    ], false),
    "Seed": o([
        { json: "id", js: "id", typ: "" },
        { json: "address", js: "address", typ: "" },
        { json: "provider", js: "provider", typ: u(undefined, "") },
    ], false),
    "Repository": o([
        { json: "url", js: "url", typ: "" },
        { json: "branch", js: "branch", typ: "" },
        { json: "commit", js: "commit", typ: "" },
        { json: "timestamp", js: "timestamp", typ: 0 },
    ], false),
    "Juno": o([
        { json: "repository", js: "repository", typ: r("Repository") },
        { json: "chain", js: "chain", typ: r("JunoChain") },
    ], false),
    "JunoChain": o([
        { json: "$schema", js: "$schema", typ: "" },
        { json: "chain_name", js: "chain_name", typ: "" },
        { json: "status", js: "status", typ: "" },
        { json: "network_type", js: "network_type", typ: "" },
        { json: "pretty_name", js: "pretty_name", typ: "" },
        { json: "chain_id", js: "chain_id", typ: "" },
        { json: "bech32_prefix", js: "bech32_prefix", typ: "" },
        { json: "slip44", js: "slip44", typ: 0 },
        { json: "genesis", js: "genesis", typ: r("Genesis") },
        { json: "codebase", js: "codebase", typ: r("Codebase") },
        { json: "daemon_name", js: "daemon_name", typ: "" },
        { json: "node_home", js: "node_home", typ: "" },
        { json: "key_algos", js: "key_algos", typ: a("") },
        { json: "peers", js: "peers", typ: r("FluffyPeers") },
        { json: "apis", js: "apis", typ: r("Apis") },
        { json: "explorers", js: "explorers", typ: a(r("Explorer")) },
        { json: "name", js: "name", typ: "" },
        { json: "path", js: "path", typ: "" },
        { json: "symbol", js: "symbol", typ: "" },
        { json: "denom", js: "denom", typ: "" },
        { json: "decimals", js: "decimals", typ: 0 },
        { json: "coingecko_id", js: "coingecko_id", typ: "" },
        { json: "image", js: "image", typ: "" },
        { json: "height", js: "height", typ: 0 },
        { json: "best_apis", js: "best_apis", typ: r("BestApis") },
        { json: "params", js: "params", typ: r("PurpleParams") },
    ], false),
    "FluffyPeers": o([
        { json: "seeds", js: "seeds", typ: a(r("PersistentPeer")) },
        { json: "persistent_peers", js: "persistent_peers", typ: a(r("PersistentPeer")) },
    ], false),
    "Osmosis": o([
        { json: "repository", js: "repository", typ: r("Repository") },
        { json: "chain", js: "chain", typ: r("OsmosisChain") },
    ], false),
    "OsmosisChain": o([
        { json: "$schema", js: "$schema", typ: "" },
        { json: "chain_name", js: "chain_name", typ: "" },
        { json: "status", js: "status", typ: "" },
        { json: "network_type", js: "network_type", typ: "" },
        { json: "pretty_name", js: "pretty_name", typ: "" },
        { json: "chain_id", js: "chain_id", typ: "" },
        { json: "bech32_prefix", js: "bech32_prefix", typ: "" },
        { json: "daemon_name", js: "daemon_name", typ: "" },
        { json: "node_home", js: "node_home", typ: "" },
        { json: "genesis", js: "genesis", typ: r("Genesis") },
        { json: "key_algos", js: "key_algos", typ: a("") },
        { json: "slip44", js: "slip44", typ: 0 },
        { json: "fees", js: "fees", typ: r("Fees") },
        { json: "codebase", js: "codebase", typ: r("Codebase") },
        { json: "peers", js: "peers", typ: r("TentacledPeers") },
        { json: "apis", js: "apis", typ: r("Apis") },
        { json: "explorers", js: "explorers", typ: a(r("Explorer")) },
        { json: "name", js: "name", typ: "" },
        { json: "path", js: "path", typ: "" },
        { json: "symbol", js: "symbol", typ: "" },
        { json: "denom", js: "denom", typ: "" },
        { json: "decimals", js: "decimals", typ: 0 },
        { json: "coingecko_id", js: "coingecko_id", typ: "" },
        { json: "image", js: "image", typ: "" },
        { json: "height", js: "height", typ: 0 },
        { json: "best_apis", js: "best_apis", typ: r("BestApis") },
        { json: "params", js: "params", typ: r("FluffyParams") },
    ], false),
    "FluffyParams": o([
        { json: "authz", js: "authz", typ: true },
        { json: "actual_block_time", js: "actual_block_time", typ: 3.14 },
        { json: "actual_blocks_per_year", js: "actual_blocks_per_year", typ: 3.14 },
        { json: "unbonding_time", js: "unbonding_time", typ: 0 },
        { json: "max_validators", js: "max_validators", typ: 0 },
        { json: "bonded_ratio", js: "bonded_ratio", typ: 3.14 },
        { json: "minting_epoch_provision", js: "minting_epoch_provision", typ: 3.14 },
        { json: "epoch_duration", js: "epoch_duration", typ: 0 },
        { json: "year_minting_provision", js: "year_minting_provision", typ: 0 },
        { json: "bonded_tokens", js: "bonded_tokens", typ: "" },
        { json: "total_supply", js: "total_supply", typ: "" },
        { json: "base_inflation", js: "base_inflation", typ: 3.14 },
        { json: "calculated_apr", js: "calculated_apr", typ: 3.14 },
    ], false),
    "TentacledPeers": o([
        { json: "seeds", js: "seeds", typ: a(r("Seed")) },
        { json: "persistent_peers", js: "persistent_peers", typ: a(r("Seed")) },
    ], false),
};
