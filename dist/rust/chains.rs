// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::[object Object];
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: [object Object] = serde_json::from_str(&json).unwrap();
// }

extern crate serde_derive;

#[derive(Serialize, Deserialize)]
pub struct Index {
    #[serde(rename = "repository")]
    repository: Repository,

    #[serde(rename = "chains")]
    chains: Vec<Chain>,
}

#[derive(Serialize, Deserialize)]
pub struct Chain {
    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "path")]
    path: String,

    #[serde(rename = "chain_name")]
    chain_name: String,

    #[serde(rename = "network_type")]
    network_type: NetworkType,

    #[serde(rename = "pretty_name")]
    pretty_name: String,

    #[serde(rename = "chain_id")]
    chain_id: String,

    #[serde(rename = "status")]
    status: Status,

    #[serde(rename = "symbol")]
    symbol: Option<String>,

    #[serde(rename = "denom")]
    denom: Option<String>,

    #[serde(rename = "decimals")]
    decimals: Option<i64>,

    #[serde(rename = "image")]
    image: Option<String>,

    #[serde(rename = "height")]
    height: Option<i64>,

    #[serde(rename = "best_apis")]
    best_apis: BestApis,

    #[serde(rename = "params")]
    params: Params,

    #[serde(rename = "coingecko_id")]
    coingecko_id: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct BestApis {
    #[serde(rename = "rest")]
    rest: Vec<Rest>,

    #[serde(rename = "rpc")]
    rpc: Vec<Rest>,
}

#[derive(Serialize, Deserialize)]
pub struct Rest {
    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "provider")]
    provider: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Params {
    #[serde(rename = "authz")]
    authz: Option<bool>,

    #[serde(rename = "bonded_tokens")]
    bonded_tokens: Option<String>,

    #[serde(rename = "total_supply")]
    total_supply: Option<String>,

    #[serde(rename = "actual_block_time")]
    actual_block_time: Option<f64>,

    #[serde(rename = "calculated_apr")]
    calculated_apr: Option<f64>,
}

#[derive(Serialize, Deserialize)]
pub struct Repository {
    #[serde(rename = "url")]
    url: String,

    #[serde(rename = "branch")]
    branch: String,

    #[serde(rename = "commit")]
    commit: String,

    #[serde(rename = "timestamp")]
    timestamp: i64,
}

#[derive(Serialize, Deserialize)]
pub enum NetworkType {
    #[serde(rename = "mainnet")]
    Mainnet,
}

#[derive(Serialize, Deserialize)]
pub enum Status {
    #[serde(rename = "killed")]
    Killed,

    #[serde(rename = "live")]
    Live,
}
