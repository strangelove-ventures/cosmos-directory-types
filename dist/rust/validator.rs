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
pub struct Oni {
    #[serde(rename = "repository")]
    repository: Repository,

    #[serde(rename = "validator")]
    validator: DeuslabsValidator,
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
pub struct DeuslabsValidator {
    #[serde(rename = "path")]
    path: String,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "identity")]
    identity: Identity,

    #[serde(rename = "chains")]
    chains: Vec<PurpleChain>,

    #[serde(rename = "profile")]
    profile: Profile,
}

#[derive(Serialize, Deserialize)]
pub struct PurpleChain {
    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "restake")]
    restake: PurpleRestake,

    #[serde(rename = "moniker")]
    moniker: String,

    #[serde(rename = "identity")]
    identity: Option<Identity>,

    #[serde(rename = "hexAddress")]
    hex_address: String,

    #[serde(rename = "uptime")]
    uptime: i64,

    #[serde(rename = "missedBlocks")]
    missed_blocks: i64,

    #[serde(rename = "operator_address")]
    operator_address: String,

    #[serde(rename = "consensus_pubkey")]
    consensus_pubkey: ConsensusPubkey,

    #[serde(rename = "jailed")]
    jailed: bool,

    #[serde(rename = "status")]
    status: Status,

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
    mintscan_image: String,

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
    identity: Identity,

    #[serde(rename = "website")]
    website: String,

    #[serde(rename = "security_contact")]
    security_contact: String,

    #[serde(rename = "details")]
    details: String,
}

#[derive(Serialize, Deserialize)]
pub struct PurpleRestake {
    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "run_time")]
    run_time: String,

    #[serde(rename = "minimum_reward")]
    minimum_reward: i64,
}

#[derive(Serialize, Deserialize)]
pub struct Profile {
    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "identity")]
    identity: Identity,
}

#[derive(Serialize, Deserialize)]
pub struct Ezstaking {
    #[serde(rename = "repository")]
    repository: Repository,

    #[serde(rename = "validator")]
    validator: EzstakingValidator,
}

#[derive(Serialize, Deserialize)]
pub struct EzstakingValidator {
    #[serde(rename = "path")]
    path: String,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "identity")]
    identity: Identity,

    #[serde(rename = "chains")]
    chains: Vec<FluffyChain>,

    #[serde(rename = "profile")]
    profile: Profile,
}

#[derive(Serialize, Deserialize)]
pub struct FluffyChain {
    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "restake")]
    restake: FluffyRestake,

    #[serde(rename = "moniker")]
    moniker: String,

    #[serde(rename = "identity")]
    identity: Identity,

    #[serde(rename = "hexAddress")]
    hex_address: String,

    #[serde(rename = "uptime")]
    uptime: Option<i64>,

    #[serde(rename = "missedBlocks")]
    missed_blocks: i64,

    #[serde(rename = "operator_address")]
    operator_address: String,

    #[serde(rename = "consensus_pubkey")]
    consensus_pubkey: ConsensusPubkey,

    #[serde(rename = "jailed")]
    jailed: bool,

    #[serde(rename = "status")]
    status: Status,

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
    keybase_image: String,
}

#[derive(Serialize, Deserialize)]
pub struct FluffyRestake {
    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "run_time")]
    run_time: RunTimeUnion,

    #[serde(rename = "minimum_reward")]
    minimum_reward: i64,
}

#[derive(Serialize, Deserialize)]
#[serde(untagged)]
pub enum RunTimeUnion {
    EnumArray(Vec<RunTimeElement>),

    String(String),
}

#[derive(Serialize, Deserialize)]
pub enum Type {
    #[serde(rename = "/cosmos.crypto.ed25519.PubKey")]
    CosmosCryptoEd25519PubKey,
}

#[derive(Serialize, Deserialize)]
pub enum Identity {
    #[serde(rename = "ED7CA7124A3F0ED6")]
    Ed7Ca7124A3F0Ed6,

    #[serde(rename = "")]
    Empty,

    #[serde(rename = "1534523421A364DB")]
    The1534523421A364Db,

    #[serde(rename = "5A8AB49CF5CAAF3C")]
    The5A8Ab49Cf5Caaf3C,
}

#[derive(Serialize, Deserialize)]
pub enum Status {
    #[serde(rename = "BOND_STATUS_BONDED")]
    BondStatusBonded,
}

#[derive(Serialize, Deserialize)]
pub enum RunTimeElement {
    #[serde(rename = "00:00")]
    The0000,

    #[serde(rename = "12:00")]
    The1200,
}
