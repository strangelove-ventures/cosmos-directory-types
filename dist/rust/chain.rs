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
pub struct Cosmoshub {
    #[serde(rename = "repository")]
    repository: Repository,

    #[serde(rename = "chain")]
    chain: CosmoshubChain,
}

#[derive(Serialize, Deserialize)]
pub struct CosmoshubChain {
    #[serde(rename = "$schema")]
    schema: String,

    #[serde(rename = "chain_name")]
    chain_name: String,

    #[serde(rename = "chain_id")]
    chain_id: String,

    #[serde(rename = "pretty_name")]
    pretty_name: String,

    #[serde(rename = "status")]
    status: String,

    #[serde(rename = "network_type")]
    network_type: String,

    #[serde(rename = "bech32_prefix")]
    bech32_prefix: String,

    #[serde(rename = "genesis")]
    genesis: Genesis,

    #[serde(rename = "daemon_name")]
    daemon_name: String,

    #[serde(rename = "node_home")]
    node_home: String,

    #[serde(rename = "key_algos")]
    key_algos: Vec<String>,

    #[serde(rename = "slip44")]
    slip44: i64,

    #[serde(rename = "fees")]
    fees: Fees,

    #[serde(rename = "codebase")]
    codebase: Codebase,

    #[serde(rename = "peers")]
    peers: PurplePeers,

    #[serde(rename = "apis")]
    apis: Apis,

    #[serde(rename = "explorers")]
    explorers: Vec<Explorer>,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "path")]
    path: String,

    #[serde(rename = "symbol")]
    symbol: String,

    #[serde(rename = "denom")]
    denom: String,

    #[serde(rename = "decimals")]
    decimals: i64,

    #[serde(rename = "coingecko_id")]
    coingecko_id: String,

    #[serde(rename = "image")]
    image: String,

    #[serde(rename = "height")]
    height: i64,

    #[serde(rename = "best_apis")]
    best_apis: BestApis,

    #[serde(rename = "params")]
    params: PurpleParams,
}

#[derive(Serialize, Deserialize)]
pub struct Apis {
    #[serde(rename = "rpc")]
    rpc: Vec<Grpc>,

    #[serde(rename = "rest")]
    rest: Vec<Grpc>,

    #[serde(rename = "grpc")]
    grpc: Vec<Grpc>,
}

#[derive(Serialize, Deserialize)]
pub struct Grpc {
    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "provider")]
    provider: String,
}

#[derive(Serialize, Deserialize)]
pub struct BestApis {
    #[serde(rename = "rest")]
    rest: Vec<Grpc>,

    #[serde(rename = "rpc")]
    rpc: Vec<Grpc>,
}

#[derive(Serialize, Deserialize)]
pub struct Codebase {
    #[serde(rename = "git_repo")]
    git_repo: String,

    #[serde(rename = "recommended_version")]
    recommended_version: String,

    #[serde(rename = "compatible_versions")]
    compatible_versions: Vec<String>,

    #[serde(rename = "binaries")]
    binaries: Option<Binaries>,
}

#[derive(Serialize, Deserialize)]
pub struct Binaries {
    #[serde(rename = "linux/amd64")]
    linux_amd64: String,

    #[serde(rename = "linux/arm64")]
    linux_arm64: Option<String>,

    #[serde(rename = "darwin/amd64")]
    darwin_amd64: Option<String>,

    #[serde(rename = "windows/amd64")]
    windows_amd64: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Explorer {
    #[serde(rename = "kind")]
    kind: String,

    #[serde(rename = "url")]
    url: String,

    #[serde(rename = "tx_page")]
    tx_page: String,
}

#[derive(Serialize, Deserialize)]
pub struct Fees {
    #[serde(rename = "fee_tokens")]
    fee_tokens: Vec<FeeToken>,
}

#[derive(Serialize, Deserialize)]
pub struct FeeToken {
    #[serde(rename = "denom")]
    denom: String,

    #[serde(rename = "fixed_min_gas_price")]
    fixed_min_gas_price: i64,
}

#[derive(Serialize, Deserialize)]
pub struct Genesis {
    #[serde(rename = "genesis_url")]
    genesis_url: String,
}

#[derive(Serialize, Deserialize)]
pub struct PurpleParams {
    #[serde(rename = "authz")]
    authz: bool,

    #[serde(rename = "actual_block_time")]
    actual_block_time: f64,

    #[serde(rename = "actual_blocks_per_year")]
    actual_blocks_per_year: f64,

    #[serde(rename = "unbonding_time")]
    unbonding_time: i64,

    #[serde(rename = "max_validators")]
    max_validators: i64,

    #[serde(rename = "blocks_per_year")]
    blocks_per_year: i64,

    #[serde(rename = "block_time")]
    block_time: f64,

    #[serde(rename = "community_tax")]
    community_tax: f64,

    #[serde(rename = "base_inflation")]
    base_inflation: f64,

    #[serde(rename = "bonded_ratio")]
    bonded_ratio: f64,

    #[serde(rename = "bonded_tokens")]
    bonded_tokens: String,

    #[serde(rename = "total_supply")]
    total_supply: String,

    #[serde(rename = "estimated_apr")]
    estimated_apr: f64,

    #[serde(rename = "calculated_apr")]
    calculated_apr: f64,
}

#[derive(Serialize, Deserialize)]
pub struct PurplePeers {
    #[serde(rename = "seeds")]
    seeds: Vec<Seed>,

    #[serde(rename = "persistent_peers")]
    persistent_peers: Vec<PersistentPeer>,
}

#[derive(Serialize, Deserialize)]
pub struct PersistentPeer {
    #[serde(rename = "id")]
    id: String,

    #[serde(rename = "address")]
    address: String,
}

#[derive(Serialize, Deserialize)]
pub struct Seed {
    #[serde(rename = "id")]
    id: String,

    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "provider")]
    provider: Option<String>,
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
pub struct Juno {
    #[serde(rename = "repository")]
    repository: Repository,

    #[serde(rename = "chain")]
    chain: JunoChain,
}

#[derive(Serialize, Deserialize)]
pub struct JunoChain {
    #[serde(rename = "$schema")]
    schema: String,

    #[serde(rename = "chain_name")]
    chain_name: String,

    #[serde(rename = "status")]
    status: String,

    #[serde(rename = "network_type")]
    network_type: String,

    #[serde(rename = "pretty_name")]
    pretty_name: String,

    #[serde(rename = "chain_id")]
    chain_id: String,

    #[serde(rename = "bech32_prefix")]
    bech32_prefix: String,

    #[serde(rename = "slip44")]
    slip44: i64,

    #[serde(rename = "genesis")]
    genesis: Genesis,

    #[serde(rename = "codebase")]
    codebase: Codebase,

    #[serde(rename = "daemon_name")]
    daemon_name: String,

    #[serde(rename = "node_home")]
    node_home: String,

    #[serde(rename = "key_algos")]
    key_algos: Vec<String>,

    #[serde(rename = "peers")]
    peers: FluffyPeers,

    #[serde(rename = "apis")]
    apis: Apis,

    #[serde(rename = "explorers")]
    explorers: Vec<Explorer>,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "path")]
    path: String,

    #[serde(rename = "symbol")]
    symbol: String,

    #[serde(rename = "denom")]
    denom: String,

    #[serde(rename = "decimals")]
    decimals: i64,

    #[serde(rename = "coingecko_id")]
    coingecko_id: String,

    #[serde(rename = "image")]
    image: String,

    #[serde(rename = "height")]
    height: i64,

    #[serde(rename = "best_apis")]
    best_apis: BestApis,

    #[serde(rename = "params")]
    params: PurpleParams,
}

#[derive(Serialize, Deserialize)]
pub struct FluffyPeers {
    #[serde(rename = "seeds")]
    seeds: Vec<PersistentPeer>,

    #[serde(rename = "persistent_peers")]
    persistent_peers: Vec<PersistentPeer>,
}

#[derive(Serialize, Deserialize)]
pub struct Osmosis {
    #[serde(rename = "repository")]
    repository: Repository,

    #[serde(rename = "chain")]
    chain: OsmosisChain,
}

#[derive(Serialize, Deserialize)]
pub struct OsmosisChain {
    #[serde(rename = "$schema")]
    schema: String,

    #[serde(rename = "chain_name")]
    chain_name: String,

    #[serde(rename = "status")]
    status: String,

    #[serde(rename = "network_type")]
    network_type: String,

    #[serde(rename = "pretty_name")]
    pretty_name: String,

    #[serde(rename = "chain_id")]
    chain_id: String,

    #[serde(rename = "bech32_prefix")]
    bech32_prefix: String,

    #[serde(rename = "daemon_name")]
    daemon_name: String,

    #[serde(rename = "node_home")]
    node_home: String,

    #[serde(rename = "genesis")]
    genesis: Genesis,

    #[serde(rename = "key_algos")]
    key_algos: Vec<String>,

    #[serde(rename = "slip44")]
    slip44: i64,

    #[serde(rename = "fees")]
    fees: Fees,

    #[serde(rename = "codebase")]
    codebase: Codebase,

    #[serde(rename = "peers")]
    peers: TentacledPeers,

    #[serde(rename = "apis")]
    apis: Apis,

    #[serde(rename = "explorers")]
    explorers: Vec<Explorer>,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "path")]
    path: String,

    #[serde(rename = "symbol")]
    symbol: String,

    #[serde(rename = "denom")]
    denom: String,

    #[serde(rename = "decimals")]
    decimals: i64,

    #[serde(rename = "coingecko_id")]
    coingecko_id: String,

    #[serde(rename = "image")]
    image: String,

    #[serde(rename = "height")]
    height: i64,

    #[serde(rename = "best_apis")]
    best_apis: BestApis,

    #[serde(rename = "params")]
    params: FluffyParams,
}

#[derive(Serialize, Deserialize)]
pub struct FluffyParams {
    #[serde(rename = "authz")]
    authz: bool,

    #[serde(rename = "actual_block_time")]
    actual_block_time: f64,

    #[serde(rename = "actual_blocks_per_year")]
    actual_blocks_per_year: f64,

    #[serde(rename = "unbonding_time")]
    unbonding_time: i64,

    #[serde(rename = "max_validators")]
    max_validators: i64,

    #[serde(rename = "bonded_ratio")]
    bonded_ratio: f64,

    #[serde(rename = "minting_epoch_provision")]
    minting_epoch_provision: f64,

    #[serde(rename = "epoch_duration")]
    epoch_duration: i64,

    #[serde(rename = "year_minting_provision")]
    year_minting_provision: i64,

    #[serde(rename = "bonded_tokens")]
    bonded_tokens: String,

    #[serde(rename = "total_supply")]
    total_supply: String,

    #[serde(rename = "base_inflation")]
    base_inflation: f64,

    #[serde(rename = "calculated_apr")]
    calculated_apr: f64,
}

#[derive(Serialize, Deserialize)]
pub struct TentacledPeers {
    #[serde(rename = "seeds")]
    seeds: Vec<Seed>,

    #[serde(rename = "persistent_peers")]
    persistent_peers: Vec<Seed>,
}
