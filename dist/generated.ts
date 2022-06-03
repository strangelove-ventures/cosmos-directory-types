// To parse this data:
//
//   import { Convert, AllChainsData, ChainData, AllValidatorsData, ValidatorData, ChainValidatorsData } from "./file";
//
//   const allChainsData = Convert.toAllChainsData(json);
//   const chainData = Convert.toChainData(json);
//   const allValidatorsData = Convert.toAllValidatorsData(json);
//   const validatorData = Convert.toValidatorData(json);
//   const chainValidatorsData = Convert.toChainValidatorsData(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

export interface AllChainsData {
    repository: Repository;
    chains:     AllChainsDataChain[];
}

export interface AllChainsDataChain {
    name:          string;
    path:          string;
    chain_name:    string;
    network_type:  NetworkType;
    pretty_name:   string;
    chain_id:      string;
    status:        PurpleStatus;
    symbol?:       string;
    denom?:        string;
    decimals?:     number;
    image?:        string;
    height:        number | null;
    best_apis:     BestApis;
    params:        PurpleParams;
    coingecko_id?: string;
}

export interface BestApis {
    rest: Grpc[];
    rpc:  Grpc[];
}

export interface Grpc {
    address:   string;
    provider?: string;
}

export enum NetworkType {
    Mainnet = "mainnet",
}

export interface PurpleParams {
    authz?:             boolean;
    bonded_tokens?:     string;
    total_supply?:      string;
    actual_block_time?: number;
    calculated_apr?:    number;
}

export enum PurpleStatus {
    Killed = "killed",
    Live = "live",
}

export interface Repository {
    url:       string;
    branch:    string;
    commit:    string;
    timestamp: number;
}

export interface ChainData {
    repository: Repository;
    chain:      ChainDataChain;
}

export interface ChainDataChain {
    $schema:       string;
    chain_name:    string;
    chain_id:      string;
    pretty_name:   string;
    status:        PurpleStatus;
    network_type:  NetworkType;
    bech32_prefix: string;
    genesis:       Genesis;
    daemon_name:   string;
    node_home:     string;
    key_algos:     string[];
    slip44:        number;
    fees?:         Fees;
    codebase:      Codebase;
    peers:         Peers;
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

export interface Apis {
    rpc:  Grpc[];
    rest: Grpc[];
    grpc: Grpc[];
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
    kind:          string;
    url:           string;
    tx_page:       string;
    account_page?: string;
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

export interface FluffyParams {
    authz:                    boolean;
    actual_block_time:        number;
    actual_blocks_per_year:   number;
    unbonding_time:           number;
    max_validators:           number;
    blocks_per_year?:         number;
    block_time?:              number;
    community_tax?:           number;
    base_inflation:           number;
    total_supply:             string;
    bonded_tokens:            string;
    bonded_ratio:             number;
    estimated_apr?:           number;
    calculated_apr:           number;
    minting_epoch_provision?: number;
    epoch_duration?:          number;
    year_minting_provision?:  number;
}

export interface Peers {
    seeds:            PersistentPeer[];
    persistent_peers: PersistentPeer[];
}

export interface PersistentPeer {
    id:        string;
    address:   string;
    provider?: string;
}

export interface AllValidatorsData {
    repository: Repository;
    validators: AllValidatorsDataValidator[];
}

export interface AllValidatorsDataValidator {
    path:     string;
    name:     string;
    identity: string;
    chains:   ValidatorChain[];
    profile:  Profile;
}

export interface ValidatorChain {
    name:    string;
    address: string;
    restake: boolean | string;
}

export interface Profile {
    name:     string;
    identity: string;
}

export interface ValidatorData {
    repository: Repository;
    validator:  ValidatorDataValidator;
}

export interface ValidatorDataValidator {
    path:     string;
    name:     string;
    identity: string;
    chains:   ChainElement[];
    profile:  Profile;
}

export interface ChainElement {
    name?:               string;
    address:             string;
    restake?:            RestakeClass;
    moniker:             string;
    identity?:           string;
    hexAddress:          string;
    uptime:              number | null;
    missedBlocks:        number;
    operator_address:    string;
    consensus_pubkey:    ConsensusPubkey;
    jailed:              boolean;
    status:              ValidatorStatus;
    tokens:              string;
    delegator_shares:    string;
    description:         Description;
    unbonding_height:    string;
    unbonding_time:      Date;
    commission:          Commission;
    min_self_delegation: string;
    rank:                number;
    mintscan_image?:     string;
    keybase_image?:      string;
}

export interface Commission {
    commission_rates: CommissionRates;
    update_time:      Date;
}

export interface CommissionRates {
    rate:            string;
    max_rate:        string;
    max_change_rate: string;
}

export interface ConsensusPubkey {
    "@type": Type;
    key:     string;
}

export enum Type {
    CosmosCryptoEd25519PubKey = "/cosmos.crypto.ed25519.PubKey",
}

export interface Description {
    moniker:          string;
    identity:         string;
    website:          string;
    security_contact: string;
    details:          string;
}

export interface RestakeClass {
    address:        string;
    run_time:       string[] | string;
    minimum_reward: number;
}

export enum ValidatorStatus {
    BondStatusBonded = "BOND_STATUS_BONDED",
    BondStatusUnbonded = "BOND_STATUS_UNBONDED",
    BondStatusUnbonding = "BOND_STATUS_UNBONDING",
}

export interface ChainValidatorsData {
    name:       string;
    validators: ChainElement[];
}

// Converts JSON strings to/from your types
// and asserts the results of JSON.parse at runtime
export class Convert {
    public static toAllChainsData(json: string): AllChainsData {
        return cast(JSON.parse(json), r("AllChainsData"));
    }

    public static allChainsDataToJson(value: AllChainsData): string {
        return JSON.stringify(uncast(value, r("AllChainsData")), null, 2);
    }

    public static toChainData(json: string): ChainData {
        return cast(JSON.parse(json), r("ChainData"));
    }

    public static chainDataToJson(value: ChainData): string {
        return JSON.stringify(uncast(value, r("ChainData")), null, 2);
    }

    public static toAllValidatorsData(json: string): AllValidatorsData {
        return cast(JSON.parse(json), r("AllValidatorsData"));
    }

    public static allValidatorsDataToJson(value: AllValidatorsData): string {
        return JSON.stringify(uncast(value, r("AllValidatorsData")), null, 2);
    }

    public static toValidatorData(json: string): ValidatorData {
        return cast(JSON.parse(json), r("ValidatorData"));
    }

    public static validatorDataToJson(value: ValidatorData): string {
        return JSON.stringify(uncast(value, r("ValidatorData")), null, 2);
    }

    public static toChainValidatorsData(json: string): ChainValidatorsData {
        return cast(JSON.parse(json), r("ChainValidatorsData"));
    }

    public static chainValidatorsDataToJson(value: ChainValidatorsData): string {
        return JSON.stringify(uncast(value, r("ChainValidatorsData")), null, 2);
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
    "AllChainsData": o([
        { json: "repository", js: "repository", typ: r("Repository") },
        { json: "chains", js: "chains", typ: a(r("AllChainsDataChain")) },
    ], false),
    "AllChainsDataChain": o([
        { json: "name", js: "name", typ: "" },
        { json: "path", js: "path", typ: "" },
        { json: "chain_name", js: "chain_name", typ: "" },
        { json: "network_type", js: "network_type", typ: r("NetworkType") },
        { json: "pretty_name", js: "pretty_name", typ: "" },
        { json: "chain_id", js: "chain_id", typ: "" },
        { json: "status", js: "status", typ: r("PurpleStatus") },
        { json: "symbol", js: "symbol", typ: u(undefined, "") },
        { json: "denom", js: "denom", typ: u(undefined, "") },
        { json: "decimals", js: "decimals", typ: u(undefined, 0) },
        { json: "image", js: "image", typ: u(undefined, "") },
        { json: "height", js: "height", typ: u(0, null) },
        { json: "best_apis", js: "best_apis", typ: r("BestApis") },
        { json: "params", js: "params", typ: r("PurpleParams") },
        { json: "coingecko_id", js: "coingecko_id", typ: u(undefined, "") },
    ], false),
    "BestApis": o([
        { json: "rest", js: "rest", typ: a(r("Grpc")) },
        { json: "rpc", js: "rpc", typ: a(r("Grpc")) },
    ], false),
    "Grpc": o([
        { json: "address", js: "address", typ: "" },
        { json: "provider", js: "provider", typ: u(undefined, "") },
    ], false),
    "PurpleParams": o([
        { json: "authz", js: "authz", typ: u(undefined, true) },
        { json: "bonded_tokens", js: "bonded_tokens", typ: u(undefined, "") },
        { json: "total_supply", js: "total_supply", typ: u(undefined, "") },
        { json: "actual_block_time", js: "actual_block_time", typ: u(undefined, 3.14) },
        { json: "calculated_apr", js: "calculated_apr", typ: u(undefined, 3.14) },
    ], false),
    "Repository": o([
        { json: "url", js: "url", typ: "" },
        { json: "branch", js: "branch", typ: "" },
        { json: "commit", js: "commit", typ: "" },
        { json: "timestamp", js: "timestamp", typ: 0 },
    ], false),
    "ChainData": o([
        { json: "repository", js: "repository", typ: r("Repository") },
        { json: "chain", js: "chain", typ: r("ChainDataChain") },
    ], false),
    "ChainDataChain": o([
        { json: "$schema", js: "$schema", typ: "" },
        { json: "chain_name", js: "chain_name", typ: "" },
        { json: "chain_id", js: "chain_id", typ: "" },
        { json: "pretty_name", js: "pretty_name", typ: "" },
        { json: "status", js: "status", typ: r("PurpleStatus") },
        { json: "network_type", js: "network_type", typ: r("NetworkType") },
        { json: "bech32_prefix", js: "bech32_prefix", typ: "" },
        { json: "genesis", js: "genesis", typ: r("Genesis") },
        { json: "daemon_name", js: "daemon_name", typ: "" },
        { json: "node_home", js: "node_home", typ: "" },
        { json: "key_algos", js: "key_algos", typ: a("") },
        { json: "slip44", js: "slip44", typ: 0 },
        { json: "fees", js: "fees", typ: u(undefined, r("Fees")) },
        { json: "codebase", js: "codebase", typ: r("Codebase") },
        { json: "peers", js: "peers", typ: r("Peers") },
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
    "Apis": o([
        { json: "rpc", js: "rpc", typ: a(r("Grpc")) },
        { json: "rest", js: "rest", typ: a(r("Grpc")) },
        { json: "grpc", js: "grpc", typ: a(r("Grpc")) },
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
        { json: "account_page", js: "account_page", typ: u(undefined, "") },
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
    "FluffyParams": o([
        { json: "authz", js: "authz", typ: true },
        { json: "actual_block_time", js: "actual_block_time", typ: 3.14 },
        { json: "actual_blocks_per_year", js: "actual_blocks_per_year", typ: 3.14 },
        { json: "unbonding_time", js: "unbonding_time", typ: 0 },
        { json: "max_validators", js: "max_validators", typ: 0 },
        { json: "blocks_per_year", js: "blocks_per_year", typ: u(undefined, 0) },
        { json: "block_time", js: "block_time", typ: u(undefined, 3.14) },
        { json: "community_tax", js: "community_tax", typ: u(undefined, 3.14) },
        { json: "base_inflation", js: "base_inflation", typ: 3.14 },
        { json: "total_supply", js: "total_supply", typ: "" },
        { json: "bonded_tokens", js: "bonded_tokens", typ: "" },
        { json: "bonded_ratio", js: "bonded_ratio", typ: 3.14 },
        { json: "estimated_apr", js: "estimated_apr", typ: u(undefined, 3.14) },
        { json: "calculated_apr", js: "calculated_apr", typ: 3.14 },
        { json: "minting_epoch_provision", js: "minting_epoch_provision", typ: u(undefined, 3.14) },
        { json: "epoch_duration", js: "epoch_duration", typ: u(undefined, 0) },
        { json: "year_minting_provision", js: "year_minting_provision", typ: u(undefined, 0) },
    ], false),
    "Peers": o([
        { json: "seeds", js: "seeds", typ: a(r("PersistentPeer")) },
        { json: "persistent_peers", js: "persistent_peers", typ: a(r("PersistentPeer")) },
    ], false),
    "PersistentPeer": o([
        { json: "id", js: "id", typ: "" },
        { json: "address", js: "address", typ: "" },
        { json: "provider", js: "provider", typ: u(undefined, "") },
    ], false),
    "AllValidatorsData": o([
        { json: "repository", js: "repository", typ: r("Repository") },
        { json: "validators", js: "validators", typ: a(r("AllValidatorsDataValidator")) },
    ], false),
    "AllValidatorsDataValidator": o([
        { json: "path", js: "path", typ: "" },
        { json: "name", js: "name", typ: "" },
        { json: "identity", js: "identity", typ: "" },
        { json: "chains", js: "chains", typ: a(r("ValidatorChain")) },
        { json: "profile", js: "profile", typ: r("Profile") },
    ], false),
    "ValidatorChain": o([
        { json: "name", js: "name", typ: "" },
        { json: "address", js: "address", typ: "" },
        { json: "restake", js: "restake", typ: u(true, "") },
    ], false),
    "Profile": o([
        { json: "name", js: "name", typ: "" },
        { json: "identity", js: "identity", typ: "" },
    ], false),
    "ValidatorData": o([
        { json: "repository", js: "repository", typ: r("Repository") },
        { json: "validator", js: "validator", typ: r("ValidatorDataValidator") },
    ], false),
    "ValidatorDataValidator": o([
        { json: "path", js: "path", typ: "" },
        { json: "name", js: "name", typ: "" },
        { json: "identity", js: "identity", typ: "" },
        { json: "chains", js: "chains", typ: a(r("ChainElement")) },
        { json: "profile", js: "profile", typ: r("Profile") },
    ], false),
    "ChainElement": o([
        { json: "name", js: "name", typ: u(undefined, "") },
        { json: "address", js: "address", typ: "" },
        { json: "restake", js: "restake", typ: u(undefined, r("RestakeClass")) },
        { json: "moniker", js: "moniker", typ: "" },
        { json: "identity", js: "identity", typ: u(undefined, "") },
        { json: "hexAddress", js: "hexAddress", typ: "" },
        { json: "uptime", js: "uptime", typ: u(3.14, null) },
        { json: "missedBlocks", js: "missedBlocks", typ: 0 },
        { json: "operator_address", js: "operator_address", typ: "" },
        { json: "consensus_pubkey", js: "consensus_pubkey", typ: r("ConsensusPubkey") },
        { json: "jailed", js: "jailed", typ: true },
        { json: "status", js: "status", typ: r("ValidatorStatus") },
        { json: "tokens", js: "tokens", typ: "" },
        { json: "delegator_shares", js: "delegator_shares", typ: "" },
        { json: "description", js: "description", typ: r("Description") },
        { json: "unbonding_height", js: "unbonding_height", typ: "" },
        { json: "unbonding_time", js: "unbonding_time", typ: Date },
        { json: "commission", js: "commission", typ: r("Commission") },
        { json: "min_self_delegation", js: "min_self_delegation", typ: "" },
        { json: "rank", js: "rank", typ: 0 },
        { json: "mintscan_image", js: "mintscan_image", typ: u(undefined, "") },
        { json: "keybase_image", js: "keybase_image", typ: u(undefined, "") },
    ], false),
    "Commission": o([
        { json: "commission_rates", js: "commission_rates", typ: r("CommissionRates") },
        { json: "update_time", js: "update_time", typ: Date },
    ], false),
    "CommissionRates": o([
        { json: "rate", js: "rate", typ: "" },
        { json: "max_rate", js: "max_rate", typ: "" },
        { json: "max_change_rate", js: "max_change_rate", typ: "" },
    ], false),
    "ConsensusPubkey": o([
        { json: "@type", js: "@type", typ: r("Type") },
        { json: "key", js: "key", typ: "" },
    ], false),
    "Description": o([
        { json: "moniker", js: "moniker", typ: "" },
        { json: "identity", js: "identity", typ: "" },
        { json: "website", js: "website", typ: "" },
        { json: "security_contact", js: "security_contact", typ: "" },
        { json: "details", js: "details", typ: "" },
    ], false),
    "RestakeClass": o([
        { json: "address", js: "address", typ: "" },
        { json: "run_time", js: "run_time", typ: u(a(""), "") },
        { json: "minimum_reward", js: "minimum_reward", typ: 0 },
    ], false),
    "ChainValidatorsData": o([
        { json: "name", js: "name", typ: "" },
        { json: "validators", js: "validators", typ: a(r("ChainElement")) },
    ], false),
    "NetworkType": [
        "mainnet",
    ],
    "PurpleStatus": [
        "killed",
        "live",
    ],
    "Type": [
        "/cosmos.crypto.ed25519.PubKey",
    ],
    "ValidatorStatus": [
        "BOND_STATUS_BONDED",
        "BOND_STATUS_UNBONDED",
        "BOND_STATUS_UNBONDING",
    ],
};

