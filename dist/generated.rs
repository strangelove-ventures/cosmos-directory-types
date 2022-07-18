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
pub struct AllChainsData {
    #[serde(rename = "chains")]
    chains: Vec<AllChainsDataChain>,

    #[serde(rename = "repository")]
    repository: Repository,
}

#[derive(Serialize, Deserialize)]
pub struct AllChainsDataChain {
    #[serde(rename = "best_apis")]
    best_apis: BestApis,

    #[serde(rename = "chain_id")]
    chain_id: String,

    #[serde(rename = "chain_name")]
    chain_name: String,

    #[serde(rename = "coingecko_id")]
    coingecko_id: Option<String>,

    #[serde(rename = "decimals")]
    decimals: Option<i64>,

    #[serde(rename = "denom")]
    denom: Option<String>,

    #[serde(rename = "height")]
    height: Option<i64>,

    #[serde(rename = "image")]
    image: Option<String>,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "network_type")]
    network_type: NetworkType,

    #[serde(rename = "params")]
    params: PurpleParams,

    #[serde(rename = "path")]
    path: String,

    #[serde(rename = "pretty_name")]
    pretty_name: String,

    #[serde(rename = "status")]
    status: PurpleStatus,

    #[serde(rename = "symbol")]
    symbol: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct BestApis {
    #[serde(rename = "rest")]
    rest: Vec<Grpc>,

    #[serde(rename = "rpc")]
    rpc: Vec<Grpc>,
}

#[derive(Serialize, Deserialize)]
pub struct Grpc {
    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "provider")]
    provider: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct PurpleParams {
    #[serde(rename = "actual_block_time")]
    actual_block_time: Option<f64>,

    #[serde(rename = "authz")]
    authz: Option<bool>,

    #[serde(rename = "bonded_tokens")]
    bonded_tokens: Option<String>,

    #[serde(rename = "calculated_apr")]
    calculated_apr: Option<f64>,

    #[serde(rename = "total_supply")]
    total_supply: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Repository {
    #[serde(rename = "branch")]
    branch: String,

    #[serde(rename = "commit")]
    commit: String,

    #[serde(rename = "timestamp")]
    timestamp: i64,

    #[serde(rename = "url")]
    url: String,
}

#[derive(Serialize, Deserialize)]
pub struct ChainData {
    #[serde(rename = "chain")]
    chain: ChainDataChain,

    #[serde(rename = "repository")]
    repository: Repository,
}

#[derive(Serialize, Deserialize)]
pub struct ChainDataChain {
    #[serde(rename = "apis")]
    apis: Apis,

    #[serde(rename = "bech32_prefix")]
    bech32_prefix: String,

    #[serde(rename = "best_apis")]
    best_apis: BestApis,

    #[serde(rename = "chain_id")]
    chain_id: String,

    #[serde(rename = "chain_name")]
    chain_name: String,

    #[serde(rename = "codebase")]
    codebase: Codebase,

    #[serde(rename = "coingecko_id")]
    coingecko_id: String,

    #[serde(rename = "daemon_name")]
    daemon_name: String,

    #[serde(rename = "decimals")]
    decimals: i64,

    #[serde(rename = "denom")]
    denom: String,

    #[serde(rename = "explorers")]
    explorers: Vec<Explorer>,

    #[serde(rename = "fees")]
    fees: Option<Fees>,

    #[serde(rename = "genesis")]
    genesis: Genesis,

    #[serde(rename = "height")]
    height: i64,

    #[serde(rename = "image")]
    image: String,

    #[serde(rename = "key_algos")]
    key_algos: Vec<String>,

    #[serde(rename = "logo_URIs")]
    logo_ur_is: Option<LogoUrIs>,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "network_type")]
    network_type: NetworkType,

    #[serde(rename = "node_home")]
    node_home: String,

    #[serde(rename = "params")]
    params: FluffyParams,

    #[serde(rename = "path")]
    path: String,

    #[serde(rename = "peers")]
    peers: Peers,

    #[serde(rename = "pretty_name")]
    pretty_name: String,

    #[serde(rename = "$schema")]
    schema: String,

    #[serde(rename = "slip44")]
    slip44: i64,

    #[serde(rename = "status")]
    status: PurpleStatus,

    #[serde(rename = "symbol")]
    symbol: String,

    #[serde(rename = "updatelink")]
    updatelink: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Apis {
    #[serde(rename = "grpc")]
    grpc: Vec<Grpc>,

    #[serde(rename = "rest")]
    rest: Vec<Grpc>,

    #[serde(rename = "rpc")]
    rpc: Vec<Grpc>,
}

#[derive(Serialize, Deserialize)]
pub struct Codebase {
    #[serde(rename = "binaries")]
    binaries: Option<Binaries>,

    #[serde(rename = "compatible_versions")]
    compatible_versions: Vec<String>,

    #[serde(rename = "git_repo")]
    git_repo: String,

    #[serde(rename = "recommended_version")]
    recommended_version: String,
}

#[derive(Serialize, Deserialize)]
pub struct Binaries {
    #[serde(rename = "darwin/amd64")]
    darwin_amd64: Option<String>,

    #[serde(rename = "linux/amd64")]
    linux_amd64: String,

    #[serde(rename = "linux/arm64")]
    linux_arm64: String,

    #[serde(rename = "windows/amd64")]
    windows_amd64: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Explorer {
    #[serde(rename = "account_page")]
    account_page: Option<String>,

    #[serde(rename = "kind")]
    kind: String,

    #[serde(rename = "tx_page")]
    tx_page: String,

    #[serde(rename = "url")]
    url: String,
}

#[derive(Serialize, Deserialize)]
pub struct Fees {
    #[serde(rename = "fee_tokens")]
    fee_tokens: Vec<FeeToken>,
}

#[derive(Serialize, Deserialize)]
pub struct FeeToken {
    #[serde(rename = "average_gas_price")]
    average_gas_price: Option<f64>,

    #[serde(rename = "denom")]
    denom: String,

    #[serde(rename = "fixed_min_gas_price")]
    fixed_min_gas_price: i64,

    #[serde(rename = "high_gas_price")]
    high_gas_price: Option<f64>,

    #[serde(rename = "low_gas_price")]
    low_gas_price: Option<i64>,
}

#[derive(Serialize, Deserialize)]
pub struct Genesis {
    #[serde(rename = "genesis_url")]
    genesis_url: String,
}

#[derive(Serialize, Deserialize)]
pub struct LogoUrIs {
    #[serde(rename = "png")]
    png: String,
}

#[derive(Serialize, Deserialize)]
pub struct FluffyParams {
    #[serde(rename = "actual_block_time")]
    actual_block_time: f64,

    #[serde(rename = "actual_blocks_per_year")]
    actual_blocks_per_year: f64,

    #[serde(rename = "annual_provision")]
    annual_provision: String,

    #[serde(rename = "authz")]
    authz: bool,

    #[serde(rename = "base_inflation")]
    base_inflation: f64,

    #[serde(rename = "block_time")]
    block_time: Option<f64>,

    #[serde(rename = "blocks_per_year")]
    blocks_per_year: Option<i64>,

    #[serde(rename = "bonded_ratio")]
    bonded_ratio: f64,

    #[serde(rename = "bonded_tokens")]
    bonded_tokens: String,

    #[serde(rename = "calculated_apr")]
    calculated_apr: f64,

    #[serde(rename = "community_tax")]
    community_tax: f64,

    #[serde(rename = "epoch_duration")]
    epoch_duration: Option<i64>,

    #[serde(rename = "estimated_apr")]
    estimated_apr: f64,

    #[serde(rename = "max_validators")]
    max_validators: i64,

    #[serde(rename = "minting_epoch_provision")]
    minting_epoch_provision: Option<f64>,

    #[serde(rename = "total_supply")]
    total_supply: String,

    #[serde(rename = "unbonding_time")]
    unbonding_time: i64,

    #[serde(rename = "year_minting_provision")]
    year_minting_provision: Option<i64>,
}

#[derive(Serialize, Deserialize)]
pub struct Peers {
    #[serde(rename = "persistent_peers")]
    persistent_peers: Vec<PersistentPeer>,

    #[serde(rename = "seeds")]
    seeds: Vec<PersistentPeer>,
}

#[derive(Serialize, Deserialize)]
pub struct PersistentPeer {
    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "id")]
    id: String,

    #[serde(rename = "provider")]
    provider: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct AllValidatorsData {
    #[serde(rename = "repository")]
    repository: Repository,

    #[serde(rename = "validators")]
    validators: Vec<AllValidatorsDataValidator>,
}

#[derive(Serialize, Deserialize)]
pub struct AllValidatorsDataValidator {
    #[serde(rename = "chains")]
    chains: Vec<ValidatorChain>,

    #[serde(rename = "identity")]
    identity: String,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "path")]
    path: String,

    #[serde(rename = "profile")]
    profile: ChainProfile,
}

#[derive(Serialize, Deserialize)]
pub struct ValidatorChain {
    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "restake")]
    restake: RestakeUnion,
}

#[derive(Serialize, Deserialize)]
pub struct ChainProfile {
    #[serde(rename = "apps")]
    apps: Option<Vec<String>>,

    #[serde(rename = "identity")]
    identity: String,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "$schema")]
    schema: Option<Schema>,

    #[serde(rename = "twitter")]
    twitter: Option<String>,

    #[serde(rename = "website")]
    website: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct ValidatorData {
    #[serde(rename = "repository")]
    repository: Repository,

    #[serde(rename = "validator")]
    validator: ValidatorDataValidator,
}

#[derive(Serialize, Deserialize)]
pub struct ValidatorDataValidator {
    #[serde(rename = "chains")]
    chains: Vec<ChainElement>,

    #[serde(rename = "identity")]
    identity: String,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "path")]
    path: String,

    #[serde(rename = "profile")]
    profile: PurpleProfile,
}

#[derive(Serialize, Deserialize)]
pub struct ChainElement {
    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "commission")]
    commission: Option<Commission>,

    #[serde(rename = "consensus_pubkey")]
    consensus_pubkey: Option<ConsensusPubkey>,

    #[serde(rename = "delegator_shares")]
    delegator_shares: Option<String>,

    #[serde(rename = "description")]
    description: Option<Description>,

    #[serde(rename = "hexAddress")]
    hex_address: Option<String>,

    #[serde(rename = "identity")]
    identity: Option<String>,

    #[serde(rename = "jailed")]
    jailed: Option<bool>,

    #[serde(rename = "keybase_image")]
    keybase_image: Option<String>,

    #[serde(rename = "min_self_delegation")]
    min_self_delegation: Option<String>,

    #[serde(rename = "mintscan_image")]
    mintscan_image: Option<String>,

    #[serde(rename = "missedBlocks")]
    missed_blocks: Option<i64>,

    #[serde(rename = "moniker")]
    moniker: Option<String>,

    #[serde(rename = "name")]
    name: Option<String>,

    #[serde(rename = "operator_address")]
    operator_address: Option<String>,

    #[serde(rename = "path")]
    path: Option<String>,

    #[serde(rename = "profile")]
    profile: Option<ChainProfile>,

    #[serde(rename = "rank")]
    rank: Option<i64>,

    #[serde(rename = "restake")]
    restake: Option<RestakeClass>,

    #[serde(rename = "status")]
    status: Option<ValidatorStatus>,

    #[serde(rename = "tokens")]
    tokens: Option<String>,

    #[serde(rename = "unbonding_height")]
    unbonding_height: Option<String>,

    #[serde(rename = "unbonding_time")]
    unbonding_time: Option<String>,

    #[serde(rename = "uptime")]
    uptime: Option<f64>,
}

#[derive(Serialize, Deserialize)]
pub struct Commission {
    #[serde(rename = "commission_rates")]
    commission_rates: CommissionRates,

    #[serde(rename = "update_time")]
    update_time: String,
}

#[derive(Serialize, Deserialize)]
pub struct CommissionRates {
    #[serde(rename = "max_change_rate")]
    max_change_rate: String,

    #[serde(rename = "max_rate")]
    max_rate: String,

    #[serde(rename = "rate")]
    rate: String,
}

#[derive(Serialize, Deserialize)]
pub struct ConsensusPubkey {
    #[serde(rename = "@type")]
    consensus_pubkey_type: Type,

    #[serde(rename = "key")]
    key: String,
}

#[derive(Serialize, Deserialize)]
pub struct Description {
    #[serde(rename = "details")]
    details: String,

    #[serde(rename = "identity")]
    identity: String,

    #[serde(rename = "moniker")]
    moniker: String,

    #[serde(rename = "security_contact")]
    security_contact: String,

    #[serde(rename = "website")]
    website: String,
}

#[derive(Serialize, Deserialize)]
pub struct RestakeClass {
    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "minimum_reward")]
    minimum_reward: f64,

    #[serde(rename = "run_time")]
    run_time: RunTime,
}

#[derive(Serialize, Deserialize)]
pub struct PurpleProfile {
    #[serde(rename = "identity")]
    identity: String,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "$schema")]
    schema: Schema,
}

#[derive(Serialize, Deserialize)]
pub struct ChainValidatorsData {
    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "validators")]
    validators: Vec<ChainElement>,
}

#[derive(Serialize, Deserialize)]
#[serde(untagged)]
pub enum RestakeUnion {
    Bool(bool),

    String(String),
}

#[derive(Serialize, Deserialize)]
#[serde(untagged)]
pub enum RunTime {
    String(String),

    StringArray(Vec<String>),
}

#[derive(Serialize, Deserialize)]
pub enum NetworkType {
    #[serde(rename = "mainnet")]
    Mainnet,
}

#[derive(Serialize, Deserialize)]
pub enum PurpleStatus {
    #[serde(rename = "live")]
    Live,
}

#[derive(Serialize, Deserialize)]
pub enum Schema {
    #[serde(rename = "../profile.schema.json")]
    ProfileSchemaJson,
}

#[derive(Serialize, Deserialize)]
pub enum Type {
    #[serde(rename = "/cosmos.crypto.ed25519.PubKey")]
    CosmosCryptoEd25519PubKey,
}

#[derive(Serialize, Deserialize)]
pub enum ValidatorStatus {
    #[serde(rename = "BOND_STATUS_BONDED")]
    BondStatusBonded,

    #[serde(rename = "BOND_STATUS_UNBONDED")]
    BondStatusUnbonded,

    #[serde(rename = "BOND_STATUS_UNBONDING")]
    BondStatusUnbonding,
}

