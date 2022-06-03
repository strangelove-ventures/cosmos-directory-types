// To parse this data:
//
//   import { Convert, Index } from "./file";
//
//   const index = Convert.toIndex(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

export interface Index {
    repository: Repository;
    chains:     Chain[];
}

export interface Chain {
    name:          string;
    path:          string;
    chain_name:    string;
    network_type:  NetworkType;
    pretty_name:   string;
    chain_id:      string;
    status:        Status;
    symbol?:       string;
    denom?:        string;
    decimals?:     number;
    image?:        string;
    height:        number | null;
    best_apis:     BestApis;
    params:        Params;
    coingecko_id?: string;
}

export interface BestApis {
    rest: REST[];
    rpc:  REST[];
}

export interface REST {
    address:   string;
    provider?: string;
}

export enum NetworkType {
    Mainnet = "mainnet",
}

export interface Params {
    authz?:             boolean;
    bonded_tokens?:     string;
    total_supply?:      string;
    actual_block_time?: number;
    calculated_apr?:    number;
}

export enum Status {
    Killed = "killed",
    Live = "live",
}

export interface Repository {
    url:       string;
    branch:    string;
    commit:    string;
    timestamp: number;
}

// Converts JSON strings to/from your types
// and asserts the results of JSON.parse at runtime
export class Convert {
    public static toIndex(json: string): Index {
        return cast(JSON.parse(json), r("Index"));
    }

    public static indexToJson(value: Index): string {
        return JSON.stringify(uncast(value, r("Index")), null, 2);
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
    "Index": o([
        { json: "repository", js: "repository", typ: r("Repository") },
        { json: "chains", js: "chains", typ: a(r("Chain")) },
    ], false),
    "Chain": o([
        { json: "name", js: "name", typ: "" },
        { json: "path", js: "path", typ: "" },
        { json: "chain_name", js: "chain_name", typ: "" },
        { json: "network_type", js: "network_type", typ: r("NetworkType") },
        { json: "pretty_name", js: "pretty_name", typ: "" },
        { json: "chain_id", js: "chain_id", typ: "" },
        { json: "status", js: "status", typ: r("Status") },
        { json: "symbol", js: "symbol", typ: u(undefined, "") },
        { json: "denom", js: "denom", typ: u(undefined, "") },
        { json: "decimals", js: "decimals", typ: u(undefined, 0) },
        { json: "image", js: "image", typ: u(undefined, "") },
        { json: "height", js: "height", typ: u(0, null) },
        { json: "best_apis", js: "best_apis", typ: r("BestApis") },
        { json: "params", js: "params", typ: r("Params") },
        { json: "coingecko_id", js: "coingecko_id", typ: u(undefined, "") },
    ], false),
    "BestApis": o([
        { json: "rest", js: "rest", typ: a(r("REST")) },
        { json: "rpc", js: "rpc", typ: a(r("REST")) },
    ], false),
    "REST": o([
        { json: "address", js: "address", typ: "" },
        { json: "provider", js: "provider", typ: u(undefined, "") },
    ], false),
    "Params": o([
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
    "NetworkType": [
        "mainnet",
    ],
    "Status": [
        "killed",
        "live",
    ],
};
