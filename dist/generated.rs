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
    #[serde(rename = "repository")]
    repository: Repository,

    #[serde(rename = "chains")]
    chains: Vec<AllChainsDataChain>,
}

#[derive(Serialize, Deserialize)]
pub struct AllChainsDataChain {
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
    status: PurpleStatus,

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
    params: PurpleParams,

    #[serde(rename = "coingecko_id")]
    coingecko_id: Option<String>,
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
pub struct ChainData {
    #[serde(rename = "repository")]
    repository: Repository,

    #[serde(rename = "chain")]
    chain: ChainDataChain,
}

#[derive(Serialize, Deserialize)]
pub struct ChainDataChain {
    #[serde(rename = "$schema")]
    schema: String,

    #[serde(rename = "chain_name")]
    chain_name: String,

    #[serde(rename = "chain_id")]
    chain_id: String,

    #[serde(rename = "pretty_name")]
    pretty_name: String,

    #[serde(rename = "status")]
    status: PurpleStatus,

    #[serde(rename = "network_type")]
    network_type: NetworkType,

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
    fees: Option<Fees>,

    #[serde(rename = "codebase")]
    codebase: Codebase,

    #[serde(rename = "peers")]
    peers: Peers,

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
pub struct Apis {
    #[serde(rename = "rpc")]
    rpc: Vec<Grpc>,

    #[serde(rename = "rest")]
    rest: Vec<Grpc>,

    #[serde(rename = "grpc")]
    grpc: Vec<Grpc>,
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

    #[serde(rename = "account_page")]
    account_page: Option<String>,
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

    #[serde(rename = "blocks_per_year")]
    blocks_per_year: Option<i64>,

    #[serde(rename = "block_time")]
    block_time: Option<f64>,

    #[serde(rename = "community_tax")]
    community_tax: Option<f64>,

    #[serde(rename = "base_inflation")]
    base_inflation: f64,

    #[serde(rename = "total_supply")]
    total_supply: String,

    #[serde(rename = "bonded_tokens")]
    bonded_tokens: String,

    #[serde(rename = "bonded_ratio")]
    bonded_ratio: f64,

    #[serde(rename = "estimated_apr")]
    estimated_apr: Option<f64>,

    #[serde(rename = "calculated_apr")]
    calculated_apr: f64,

    #[serde(rename = "minting_epoch_provision")]
    minting_epoch_provision: Option<f64>,

    #[serde(rename = "epoch_duration")]
    epoch_duration: Option<i64>,

    #[serde(rename = "year_minting_provision")]
    year_minting_provision: Option<i64>,
}

#[derive(Serialize, Deserialize)]
pub struct Peers {
    #[serde(rename = "seeds")]
    seeds: Vec<PersistentPeer>,

    #[serde(rename = "persistent_peers")]
    persistent_peers: Vec<PersistentPeer>,
}

#[derive(Serialize, Deserialize)]
pub struct PersistentPeer {
    #[serde(rename = "id")]
    id: String,

    #[serde(rename = "address")]
    address: String,

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
    #[serde(rename = "path")]
    path: String,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "identity")]
    identity: String,

    #[serde(rename = "chains")]
    chains: Vec<ValidatorChain>,

    #[serde(rename = "profile")]
    profile: Profile,
}

#[derive(Serialize, Deserialize)]
pub struct ValidatorChain {
    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "restake")]
    restake: RestakeUnion,
}

#[derive(Serialize, Deserialize)]
pub struct Profile {
    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "identity")]
    identity: String,
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
    #[serde(rename = "path")]
    path: String,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "identity")]
    identity: String,

    #[serde(rename = "chains")]
    chains: Vec<ChainElement>,

    #[serde(rename = "profile")]
    profile: Profile,
}

#[derive(Serialize, Deserialize)]
pub struct ChainElement {
    #[serde(rename = "name")]
    name: Option<String>,

    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "restake")]
    restake: Option<RestakeClass>,

    #[serde(rename = "moniker")]
    moniker: String,

    #[serde(rename = "identity")]
    identity: Option<String>,

    #[serde(rename = "hexAddress")]
    hex_address: String,

    #[serde(rename = "uptime")]
    uptime: Option<f64>,

    #[serde(rename = "missedBlocks")]
    missed_blocks: i64,

    #[serde(rename = "operator_address")]
    operator_address: String,

    #[serde(rename = "consensus_pubkey")]
    consensus_pubkey: ConsensusPubkey,

    #[serde(rename = "jailed")]
    jailed: bool,

    #[serde(rename = "status")]
    status: ValidatorStatus,

    #[serde(rename = "tokens")]
    tokens: String,

    #[serde(rename = "delegator_shares")]
    delegator_shares: String,

    #[serde(rename = "description")]
    description: Description,

    #[serde(rename = "unbonding_height")]
    unbonding_height: String,

    #[serde(rename = "unbonding_time")]
    unbonding_time: String,

    #[serde(rename = "commission")]
    commission: Commission,

    #[serde(rename = "min_self_delegation")]
    min_self_delegation: String,

    #[serde(rename = "rank")]
    rank: i64,

    #[serde(rename = "mintscan_image")]
    mintscan_image: Option<String>,

    #[serde(rename = "keybase_image")]
    keybase_image: Option<String>,
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
    #[serde(rename = "rate")]
    rate: String,

    #[serde(rename = "max_rate")]
    max_rate: String,

    #[serde(rename = "max_change_rate")]
    max_change_rate: String,
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
    #[serde(rename = "moniker")]
    moniker: String,

    #[serde(rename = "identity")]
    identity: String,

    #[serde(rename = "website")]
    website: String,

    #[serde(rename = "security_contact")]
    security_contact: String,

    #[serde(rename = "details")]
    details: String,
}

#[derive(Serialize, Deserialize)]
pub struct RestakeClass {
    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "run_time")]
    run_time: RunTime,

    #[serde(rename = "minimum_reward")]
    minimum_reward: i64,
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
    #[serde(rename = "killed")]
    Killed,

    #[serde(rename = "live")]
    Live,
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
