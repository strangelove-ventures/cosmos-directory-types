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

export interface Osmosis {
    name:       Name;
    validators: Validator[];
}

export enum Name {
    Cosmoshub = "cosmoshub",
    Juno = "juno",
    Osmosis = "osmosis",
}

export interface Validator {
    moniker:             string;
    identity?:           string;
    address:             string;
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
    mintscan_image?:     string;
    keybase_image?:      string;
    name?:               Name;
    restake?:            Restake;
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

export interface Restake {
    address:        string;
    run_time:       string[] | string;
    minimum_reward: number;
}

export enum Status {
    BondStatusBonded = "BOND_STATUS_BONDED",
    BondStatusUnbonded = "BOND_STATUS_UNBONDED",
    BondStatusUnbonding = "BOND_STATUS_UNBONDING",
}

// Converts JSON strings to/from your types
// and asserts the results of JSON.parse at runtime
export class Convert {
    public static toCosmoshub(json: string): Osmosis {
        return cast(JSON.parse(json), r("Osmosis"));
    }

    public static cosmoshubToJson(value: Osmosis): string {
        return JSON.stringify(uncast(value, r("Osmosis")), null, 2);
    }

    public static toJuno(json: string): Osmosis {
        return cast(JSON.parse(json), r("Osmosis"));
    }

    public static junoToJson(value: Osmosis): string {
        return JSON.stringify(uncast(value, r("Osmosis")), null, 2);
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
    "Osmosis": o([
        { json: "name", js: "name", typ: r("Name") },
        { json: "validators", js: "validators", typ: a(r("Validator")) },
    ], false),
    "Validator": o([
        { json: "moniker", js: "moniker", typ: "" },
        { json: "identity", js: "identity", typ: u(undefined, "") },
        { json: "address", js: "address", typ: "" },
        { json: "hexAddress", js: "hexAddress", typ: "" },
        { json: "uptime", js: "uptime", typ: 3.14 },
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
        { json: "keybase_image", js: "keybase_image", typ: u(undefined, "") },
        { json: "name", js: "name", typ: u(undefined, r("Name")) },
        { json: "restake", js: "restake", typ: u(undefined, r("Restake")) },
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
    "Restake": o([
        { json: "address", js: "address", typ: "" },
        { json: "run_time", js: "run_time", typ: u(a(""), "") },
        { json: "minimum_reward", js: "minimum_reward", typ: 0 },
    ], false),
    "Name": [
        "cosmoshub",
        "juno",
        "osmosis",
    ],
    "Type": [
        "/cosmos.crypto.ed25519.PubKey",
    ],
    "Status": [
        "BOND_STATUS_BONDED",
        "BOND_STATUS_UNBONDED",
        "BOND_STATUS_UNBONDING",
    ],
};
