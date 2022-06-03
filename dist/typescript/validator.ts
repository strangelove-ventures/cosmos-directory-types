// To parse this data:
//
//   import { Convert, Deuslabs, Ezstaking, Oni } from "./file";
//
//   const deuslabs = Convert.toDeuslabs(json);
//   const ezstaking = Convert.toEzstaking(json);
//   const oni = Convert.toOni(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

export interface Oni {
    repository: Repository;
    validator:  DeuslabsValidator;
}

export interface Repository {
    url:       string;
    branch:    string;
    commit:    string;
    timestamp: number;
}

export interface DeuslabsValidator {
    path:     string;
    name:     string;
    identity: Identity;
    chains:   PurpleChain[];
    profile:  Profile;
}

export interface PurpleChain {
    name:                string;
    address:             string;
    restake:             PurpleRestake;
    moniker:             string;
    identity?:           Identity;
    hexAddress:          string;
    uptime:              number;
    missedBlocks:        number;
    operator_address:    string;
    consensus_pubkey:    ConsensusPubkey;
    jailed:              boolean;
    status:              Status;
    tokens:              string;
    delegator_shares:    string;
    description:         Description;
    unbonding_height:    string;
    unbonding_time:      Date;
    commission:          Commission;
    min_self_delegation: string;
    rank:                number;
    mintscan_image:      string;
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
    identity:         Identity;
    website:          string;
    security_contact: string;
    details:          string;
}

export enum Identity {
    Ed7Ca7124A3F0Ed6 = "ED7CA7124A3F0ED6",
    Empty = "",
    The1534523421A364DB = "1534523421A364DB",
    The5A8Ab49Cf5Caaf3C = "5A8AB49CF5CAAF3C",
}

export interface PurpleRestake {
    address:        string;
    run_time:       string;
    minimum_reward: number;
}

export enum Status {
    BondStatusBonded = "BOND_STATUS_BONDED",
}

export interface Profile {
    name:     string;
    identity: Identity;
}

export interface Ezstaking {
    repository: Repository;
    validator:  EzstakingValidator;
}

export interface EzstakingValidator {
    path:     string;
    name:     string;
    identity: Identity;
    chains:   FluffyChain[];
    profile:  Profile;
}

export interface FluffyChain {
    name:                string;
    address:             string;
    restake:             FluffyRestake;
    moniker:             string;
    identity:            Identity;
    hexAddress:          string;
    uptime:              number | null;
    missedBlocks:        number;
    operator_address:    string;
    consensus_pubkey:    ConsensusPubkey;
    jailed:              boolean;
    status:              Status;
    tokens:              string;
    delegator_shares:    string;
    description:         Description;
    unbonding_height:    string;
    unbonding_time:      Date;
    commission:          Commission;
    min_self_delegation: string;
    rank:                number;
    mintscan_image?:     string;
    keybase_image:       string;
}

export interface FluffyRestake {
    address:        string;
    run_time:       RunTimeElement[] | string;
    minimum_reward: number;
}

export enum RunTimeElement {
    The0000 = "00:00",
    The1200 = "12:00",
}

// Converts JSON strings to/from your types
// and asserts the results of JSON.parse at runtime
export class Convert {
    public static toDeuslabs(json: string): Oni {
        return cast(JSON.parse(json), r("Oni"));
    }

    public static deuslabsToJson(value: Oni): string {
        return JSON.stringify(uncast(value, r("Oni")), null, 2);
    }

    public static toEzstaking(json: string): Ezstaking {
        return cast(JSON.parse(json), r("Ezstaking"));
    }

    public static ezstakingToJson(value: Ezstaking): string {
        return JSON.stringify(uncast(value, r("Ezstaking")), null, 2);
    }

    public static toOni(json: string): Oni {
        return cast(JSON.parse(json), r("Oni"));
    }

    public static oniToJson(value: Oni): string {
        return JSON.stringify(uncast(value, r("Oni")), null, 2);
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
    "Oni": o([
        { json: "repository", js: "repository", typ: r("Repository") },
        { json: "validator", js: "validator", typ: r("DeuslabsValidator") },
    ], false),
    "Repository": o([
        { json: "url", js: "url", typ: "" },
        { json: "branch", js: "branch", typ: "" },
        { json: "commit", js: "commit", typ: "" },
        { json: "timestamp", js: "timestamp", typ: 0 },
    ], false),
    "DeuslabsValidator": o([
        { json: "path", js: "path", typ: "" },
        { json: "name", js: "name", typ: "" },
        { json: "identity", js: "identity", typ: r("Identity") },
        { json: "chains", js: "chains", typ: a(r("PurpleChain")) },
        { json: "profile", js: "profile", typ: r("Profile") },
    ], false),
    "PurpleChain": o([
        { json: "name", js: "name", typ: "" },
        { json: "address", js: "address", typ: "" },
        { json: "restake", js: "restake", typ: r("PurpleRestake") },
        { json: "moniker", js: "moniker", typ: "" },
        { json: "identity", js: "identity", typ: u(undefined, r("Identity")) },
        { json: "hexAddress", js: "hexAddress", typ: "" },
        { json: "uptime", js: "uptime", typ: 0 },
        { json: "missedBlocks", js: "missedBlocks", typ: 0 },
        { json: "operator_address", js: "operator_address", typ: "" },
        { json: "consensus_pubkey", js: "consensus_pubkey", typ: r("ConsensusPubkey") },
        { json: "jailed", js: "jailed", typ: true },
        { json: "status", js: "status", typ: r("Status") },
        { json: "tokens", js: "tokens", typ: "" },
        { json: "delegator_shares", js: "delegator_shares", typ: "" },
        { json: "description", js: "description", typ: r("Description") },
        { json: "unbonding_height", js: "unbonding_height", typ: "" },
        { json: "unbonding_time", js: "unbonding_time", typ: Date },
        { json: "commission", js: "commission", typ: r("Commission") },
        { json: "min_self_delegation", js: "min_self_delegation", typ: "" },
        { json: "rank", js: "rank", typ: 0 },
        { json: "mintscan_image", js: "mintscan_image", typ: "" },
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
        { json: "identity", js: "identity", typ: r("Identity") },
        { json: "website", js: "website", typ: "" },
        { json: "security_contact", js: "security_contact", typ: "" },
        { json: "details", js: "details", typ: "" },
    ], false),
    "PurpleRestake": o([
        { json: "address", js: "address", typ: "" },
        { json: "run_time", js: "run_time", typ: "" },
        { json: "minimum_reward", js: "minimum_reward", typ: 0 },
    ], false),
    "Profile": o([
        { json: "name", js: "name", typ: "" },
        { json: "identity", js: "identity", typ: r("Identity") },
    ], false),
    "Ezstaking": o([
        { json: "repository", js: "repository", typ: r("Repository") },
        { json: "validator", js: "validator", typ: r("EzstakingValidator") },
    ], false),
    "EzstakingValidator": o([
        { json: "path", js: "path", typ: "" },
        { json: "name", js: "name", typ: "" },
        { json: "identity", js: "identity", typ: r("Identity") },
        { json: "chains", js: "chains", typ: a(r("FluffyChain")) },
        { json: "profile", js: "profile", typ: r("Profile") },
    ], false),
    "FluffyChain": o([
        { json: "name", js: "name", typ: "" },
        { json: "address", js: "address", typ: "" },
        { json: "restake", js: "restake", typ: r("FluffyRestake") },
        { json: "moniker", js: "moniker", typ: "" },
        { json: "identity", js: "identity", typ: r("Identity") },
        { json: "hexAddress", js: "hexAddress", typ: "" },
        { json: "uptime", js: "uptime", typ: u(0, null) },
        { json: "missedBlocks", js: "missedBlocks", typ: 0 },
        { json: "operator_address", js: "operator_address", typ: "" },
        { json: "consensus_pubkey", js: "consensus_pubkey", typ: r("ConsensusPubkey") },
        { json: "jailed", js: "jailed", typ: true },
        { json: "status", js: "status", typ: r("Status") },
        { json: "tokens", js: "tokens", typ: "" },
        { json: "delegator_shares", js: "delegator_shares", typ: "" },
        { json: "description", js: "description", typ: r("Description") },
        { json: "unbonding_height", js: "unbonding_height", typ: "" },
        { json: "unbonding_time", js: "unbonding_time", typ: Date },
        { json: "commission", js: "commission", typ: r("Commission") },
        { json: "min_self_delegation", js: "min_self_delegation", typ: "" },
        { json: "rank", js: "rank", typ: 0 },
        { json: "mintscan_image", js: "mintscan_image", typ: u(undefined, "") },
        { json: "keybase_image", js: "keybase_image", typ: "" },
    ], false),
    "FluffyRestake": o([
        { json: "address", js: "address", typ: "" },
        { json: "run_time", js: "run_time", typ: u(a(r("RunTimeElement")), "") },
        { json: "minimum_reward", js: "minimum_reward", typ: 0 },
    ], false),
    "Type": [
        "/cosmos.crypto.ed25519.PubKey",
    ],
    "Identity": [
        "ED7CA7124A3F0ED6",
        "",
        "1534523421A364DB",
        "5A8AB49CF5CAAF3C",
    ],
    "Status": [
        "BOND_STATUS_BONDED",
    ],
    "RunTimeElement": [
        "00:00",
        "12:00",
    ],
};
