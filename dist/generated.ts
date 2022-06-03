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
    chains:     AllChainsDataChain[];
    repository: Repository;
}

export interface AllChainsDataChain {
    best_apis:     BestApis;
    chain_id:      string;
    chain_name:    string;
    coingecko_id?: string;
    decimals?:     number;
    denom?:        string;
    height:        number | null;
    image?:        string;
    name:          string;
    network_type:  NetworkType;
    params:        PurpleParams;
    path:          string;
    pretty_name:   string;
    status:        PurpleStatus;
    symbol?:       string;
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
    actual_block_time?: number;
    authz?:             boolean;
    bonded_tokens?:     string;
    calculated_apr?:    number;
    total_supply?:      string;
}

export enum PurpleStatus {
    Killed = "killed",
    Live = "live",
}

export interface Repository {
    branch:    string;
    commit:    string;
    timestamp: number;
    url:       string;
}

export interface ChainData {
    chain:      ChainDataChain;
    repository: Repository;
}

export interface ChainDataChain {
    $schema:       string;
    apis:          Apis;
    bech32_prefix: string;
    best_apis:     BestApis;
    chain_id:      string;
    chain_name:    string;
    codebase:      Codebase;
    coingecko_id:  string;
    daemon_name:   string;
    decimals:      number;
    denom:         string;
    explorers:     Explorer[];
    fees?:         Fees;
    genesis:       Genesis;
    height:        number;
    image:         string;
    key_algos:     string[];
    name:          string;
    network_type:  NetworkType;
    node_home:     string;
    params:        FluffyParams;
    path:          string;
    peers:         Peers;
    pretty_name:   string;
    slip44:        number;
    status:        PurpleStatus;
    symbol:        string;
}

export interface Apis {
    grpc: Grpc[];
    rest: Grpc[];
    rpc:  Grpc[];
}

export interface Codebase {
    binaries?:           Binaries;
    compatible_versions: string[];
    git_repo:            string;
    recommended_version: string;
}

export interface Binaries {
    "darwin/amd64"?:  string;
    "linux/amd64":    string;
    "linux/arm64"?:   string;
    "windows/amd64"?: string;
}

export interface Explorer {
    account_page?: string;
    kind:          string;
    tx_page:       string;
    url:           string;
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
    actual_block_time:        number;
    actual_blocks_per_year:   number;
    authz:                    boolean;
    base_inflation:           number;
    block_time?:              number;
    blocks_per_year?:         number;
    bonded_ratio:             number;
    bonded_tokens:            string;
    calculated_apr:           number;
    community_tax?:           number;
    epoch_duration?:          number;
    estimated_apr?:           number;
    max_validators:           number;
    minting_epoch_provision?: number;
    total_supply:             string;
    unbonding_time:           number;
    year_minting_provision?:  number;
}

export interface Peers {
    persistent_peers: PersistentPeer[];
    seeds:            PersistentPeer[];
}

export interface PersistentPeer {
    address:   string;
    id:        string;
    provider?: string;
}

export interface AllValidatorsData {
    repository: Repository;
    validators: AllValidatorsDataValidator[];
}

export interface AllValidatorsDataValidator {
    chains:   ValidatorChain[];
    identity: string;
    name:     string;
    path:     string;
    profile:  Profile;
}

export interface ValidatorChain {
    address: string;
    name:    string;
    restake: boolean | string;
}

export interface Profile {
    identity: string;
    name:     string;
}

export interface ValidatorData {
    repository: Repository;
    validator:  ValidatorDataValidator;
}

export interface ValidatorDataValidator {
    chains:   ChainElement[];
    identity: string;
    name:     string;
    path:     string;
    profile:  Profile;
}

export interface ChainElement {
    address:             string;
    commission:          Commission;
    consensus_pubkey:    ConsensusPubkey;
    delegator_shares:    string;
    description:         Description;
    hexAddress:          string;
    identity?:           string;
    jailed:              boolean;
    keybase_image?:      string;
    min_self_delegation: string;
    mintscan_image?:     string;
    missedBlocks:        number;
    moniker:             string;
    name?:               string;
    operator_address:    string;
    rank:                number;
    restake?:            RestakeClass;
    status:              ValidatorStatus;
    tokens:              string;
    unbonding_height:    string;
    unbonding_time:      Date;
    uptime:              number | null;
}

export interface Commission {
    commission_rates: CommissionRates;
    update_time:      Date;
}

export interface CommissionRates {
    max_change_rate: string;
    max_rate:        string;
    rate:            string;
}

export interface ConsensusPubkey {
    "@type": Type;
    key:     string;
}

export enum Type {
    CosmosCryptoEd25519PubKey = "/cosmos.crypto.ed25519.PubKey",
}

export interface Description {
    details:          string;
    identity:         string;
    moniker:          string;
    security_contact: string;
    website:          string;
}

export interface RestakeClass {
    address:        string;
    minimum_reward: number;
    run_time:       string[] | string;
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
        { json: "chains", js: "chains", typ: a(r("AllChainsDataChain")) },
        { json: "repository", js: "repository", typ: r("Repository") },
    ], false),
    "AllChainsDataChain": o([
        { json: "best_apis", js: "best_apis", typ: r("BestApis") },
        { json: "chain_id", js: "chain_id", typ: "" },
        { json: "chain_name", js: "chain_name", typ: "" },
        { json: "coingecko_id", js: "coingecko_id", typ: u(undefined, "") },
        { json: "decimals", js: "decimals", typ: u(undefined, 0) },
        { json: "denom", js: "denom", typ: u(undefined, "") },
        { json: "height", js: "height", typ: u(0, null) },
        { json: "image", js: "image", typ: u(undefined, "") },
        { json: "name", js: "name", typ: "" },
        { json: "network_type", js: "network_type", typ: r("NetworkType") },
        { json: "params", js: "params", typ: r("PurpleParams") },
        { json: "path", js: "path", typ: "" },
        { json: "pretty_name", js: "pretty_name", typ: "" },
        { json: "status", js: "status", typ: r("PurpleStatus") },
        { json: "symbol", js: "symbol", typ: u(undefined, "") },
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
        { json: "actual_block_time", js: "actual_block_time", typ: u(undefined, 3.14) },
        { json: "authz", js: "authz", typ: u(undefined, true) },
        { json: "bonded_tokens", js: "bonded_tokens", typ: u(undefined, "") },
        { json: "calculated_apr", js: "calculated_apr", typ: u(undefined, 3.14) },
        { json: "total_supply", js: "total_supply", typ: u(undefined, "") },
    ], false),
    "Repository": o([
        { json: "branch", js: "branch", typ: "" },
        { json: "commit", js: "commit", typ: "" },
        { json: "timestamp", js: "timestamp", typ: 0 },
        { json: "url", js: "url", typ: "" },
    ], false),
    "ChainData": o([
        { json: "chain", js: "chain", typ: r("ChainDataChain") },
        { json: "repository", js: "repository", typ: r("Repository") },
    ], false),
    "ChainDataChain": o([
        { json: "$schema", js: "$schema", typ: "" },
        { json: "apis", js: "apis", typ: r("Apis") },
        { json: "bech32_prefix", js: "bech32_prefix", typ: "" },
        { json: "best_apis", js: "best_apis", typ: r("BestApis") },
        { json: "chain_id", js: "chain_id", typ: "" },
        { json: "chain_name", js: "chain_name", typ: "" },
        { json: "codebase", js: "codebase", typ: r("Codebase") },
        { json: "coingecko_id", js: "coingecko_id", typ: "" },
        { json: "daemon_name", js: "daemon_name", typ: "" },
        { json: "decimals", js: "decimals", typ: 0 },
        { json: "denom", js: "denom", typ: "" },
        { json: "explorers", js: "explorers", typ: a(r("Explorer")) },
        { json: "fees", js: "fees", typ: u(undefined, r("Fees")) },
        { json: "genesis", js: "genesis", typ: r("Genesis") },
        { json: "height", js: "height", typ: 0 },
        { json: "image", js: "image", typ: "" },
        { json: "key_algos", js: "key_algos", typ: a("") },
        { json: "name", js: "name", typ: "" },
        { json: "network_type", js: "network_type", typ: r("NetworkType") },
        { json: "node_home", js: "node_home", typ: "" },
        { json: "params", js: "params", typ: r("FluffyParams") },
        { json: "path", js: "path", typ: "" },
        { json: "peers", js: "peers", typ: r("Peers") },
        { json: "pretty_name", js: "pretty_name", typ: "" },
        { json: "slip44", js: "slip44", typ: 0 },
        { json: "status", js: "status", typ: r("PurpleStatus") },
        { json: "symbol", js: "symbol", typ: "" },
    ], false),
    "Apis": o([
        { json: "grpc", js: "grpc", typ: a(r("Grpc")) },
        { json: "rest", js: "rest", typ: a(r("Grpc")) },
        { json: "rpc", js: "rpc", typ: a(r("Grpc")) },
    ], false),
    "Codebase": o([
        { json: "binaries", js: "binaries", typ: u(undefined, r("Binaries")) },
        { json: "compatible_versions", js: "compatible_versions", typ: a("") },
        { json: "git_repo", js: "git_repo", typ: "" },
        { json: "recommended_version", js: "recommended_version", typ: "" },
    ], false),
    "Binaries": o([
        { json: "darwin/amd64", js: "darwin/amd64", typ: u(undefined, "") },
        { json: "linux/amd64", js: "linux/amd64", typ: "" },
        { json: "linux/arm64", js: "linux/arm64", typ: u(undefined, "") },
        { json: "windows/amd64", js: "windows/amd64", typ: u(undefined, "") },
    ], false),
    "Explorer": o([
        { json: "account_page", js: "account_page", typ: u(undefined, "") },
        { json: "kind", js: "kind", typ: "" },
        { json: "tx_page", js: "tx_page", typ: "" },
        { json: "url", js: "url", typ: "" },
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
        { json: "actual_block_time", js: "actual_block_time", typ: 3.14 },
        { json: "actual_blocks_per_year", js: "actual_blocks_per_year", typ: 3.14 },
        { json: "authz", js: "authz", typ: true },
        { json: "base_inflation", js: "base_inflation", typ: 3.14 },
        { json: "block_time", js: "block_time", typ: u(undefined, 3.14) },
        { json: "blocks_per_year", js: "blocks_per_year", typ: u(undefined, 0) },
        { json: "bonded_ratio", js: "bonded_ratio", typ: 3.14 },
        { json: "bonded_tokens", js: "bonded_tokens", typ: "" },
        { json: "calculated_apr", js: "calculated_apr", typ: 3.14 },
        { json: "community_tax", js: "community_tax", typ: u(undefined, 3.14) },
        { json: "epoch_duration", js: "epoch_duration", typ: u(undefined, 0) },
        { json: "estimated_apr", js: "estimated_apr", typ: u(undefined, 3.14) },
        { json: "max_validators", js: "max_validators", typ: 0 },
        { json: "minting_epoch_provision", js: "minting_epoch_provision", typ: u(undefined, 3.14) },
        { json: "total_supply", js: "total_supply", typ: "" },
        { json: "unbonding_time", js: "unbonding_time", typ: 0 },
        { json: "year_minting_provision", js: "year_minting_provision", typ: u(undefined, 0) },
    ], false),
    "Peers": o([
        { json: "persistent_peers", js: "persistent_peers", typ: a(r("PersistentPeer")) },
        { json: "seeds", js: "seeds", typ: a(r("PersistentPeer")) },
    ], false),
    "PersistentPeer": o([
        { json: "address", js: "address", typ: "" },
        { json: "id", js: "id", typ: "" },
        { json: "provider", js: "provider", typ: u(undefined, "") },
    ], false),
    "AllValidatorsData": o([
        { json: "repository", js: "repository", typ: r("Repository") },
        { json: "validators", js: "validators", typ: a(r("AllValidatorsDataValidator")) },
    ], false),
    "AllValidatorsDataValidator": o([
        { json: "chains", js: "chains", typ: a(r("ValidatorChain")) },
        { json: "identity", js: "identity", typ: "" },
        { json: "name", js: "name", typ: "" },
        { json: "path", js: "path", typ: "" },
        { json: "profile", js: "profile", typ: r("Profile") },
    ], false),
    "ValidatorChain": o([
        { json: "address", js: "address", typ: "" },
        { json: "name", js: "name", typ: "" },
        { json: "restake", js: "restake", typ: u(true, "") },
    ], false),
    "Profile": o([
        { json: "identity", js: "identity", typ: "" },
        { json: "name", js: "name", typ: "" },
    ], false),
    "ValidatorData": o([
        { json: "repository", js: "repository", typ: r("Repository") },
        { json: "validator", js: "validator", typ: r("ValidatorDataValidator") },
    ], false),
    "ValidatorDataValidator": o([
        { json: "chains", js: "chains", typ: a(r("ChainElement")) },
        { json: "identity", js: "identity", typ: "" },
        { json: "name", js: "name", typ: "" },
        { json: "path", js: "path", typ: "" },
        { json: "profile", js: "profile", typ: r("Profile") },
    ], false),
    "ChainElement": o([
        { json: "address", js: "address", typ: "" },
        { json: "commission", js: "commission", typ: r("Commission") },
        { json: "consensus_pubkey", js: "consensus_pubkey", typ: r("ConsensusPubkey") },
        { json: "delegator_shares", js: "delegator_shares", typ: "" },
        { json: "description", js: "description", typ: r("Description") },
        { json: "hexAddress", js: "hexAddress", typ: "" },
        { json: "identity", js: "identity", typ: u(undefined, "") },
        { json: "jailed", js: "jailed", typ: true },
        { json: "keybase_image", js: "keybase_image", typ: u(undefined, "") },
        { json: "min_self_delegation", js: "min_self_delegation", typ: "" },
        { json: "mintscan_image", js: "mintscan_image", typ: u(undefined, "") },
        { json: "missedBlocks", js: "missedBlocks", typ: 0 },
        { json: "moniker", js: "moniker", typ: "" },
        { json: "name", js: "name", typ: u(undefined, "") },
        { json: "operator_address", js: "operator_address", typ: "" },
        { json: "rank", js: "rank", typ: 0 },
        { json: "restake", js: "restake", typ: u(undefined, r("RestakeClass")) },
        { json: "status", js: "status", typ: r("ValidatorStatus") },
        { json: "tokens", js: "tokens", typ: "" },
        { json: "unbonding_height", js: "unbonding_height", typ: "" },
        { json: "unbonding_time", js: "unbonding_time", typ: Date },
        { json: "uptime", js: "uptime", typ: u(3.14, null) },
    ], false),
    "Commission": o([
        { json: "commission_rates", js: "commission_rates", typ: r("CommissionRates") },
        { json: "update_time", js: "update_time", typ: Date },
    ], false),
    "CommissionRates": o([
        { json: "max_change_rate", js: "max_change_rate", typ: "" },
        { json: "max_rate", js: "max_rate", typ: "" },
        { json: "rate", js: "rate", typ: "" },
    ], false),
    "ConsensusPubkey": o([
        { json: "@type", js: "@type", typ: r("Type") },
        { json: "key", js: "key", typ: "" },
    ], false),
    "Description": o([
        { json: "details", js: "details", typ: "" },
        { json: "identity", js: "identity", typ: "" },
        { json: "moniker", js: "moniker", typ: "" },
        { json: "security_contact", js: "security_contact", typ: "" },
        { json: "website", js: "website", typ: "" },
    ], false),
    "RestakeClass": o([
        { json: "address", js: "address", typ: "" },
        { json: "minimum_reward", js: "minimum_reward", typ: 0 },
        { json: "run_time", js: "run_time", typ: u(a(""), "") },
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

