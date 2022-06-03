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
pub struct Osmosis {
    #[serde(rename = "name")]
    name: Name,

    #[serde(rename = "validators")]
    validators: Vec<Validator>,
}

#[derive(Serialize, Deserialize)]
pub struct Validator {
    #[serde(rename = "moniker")]
    moniker: String,

    #[serde(rename = "identity")]
    identity: Option<String>,

    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "hexAddress")]
    hex_address: String,

    #[serde(rename = "uptime")]
    uptime: f64,

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
    keybase_image: Option<String>,

    #[serde(rename = "name")]
    name: Option<Name>,

    #[serde(rename = "restake")]
    restake: Option<Restake>,
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
pub struct Restake {
    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "run_time")]
    run_time: RunTime,

    #[serde(rename = "minimum_reward")]
    minimum_reward: i64,
}

#[derive(Serialize, Deserialize)]
#[serde(untagged)]
pub enum RunTime {
    String(String),

    StringArray(Vec<String>),
}

#[derive(Serialize, Deserialize)]
pub enum Name {
    #[serde(rename = "cosmoshub")]
    Cosmoshub,

    #[serde(rename = "juno")]
    Juno,

    #[serde(rename = "osmosis")]
    Osmosis,
}

#[derive(Serialize, Deserialize)]
pub enum Type {
    #[serde(rename = "/cosmos.crypto.ed25519.PubKey")]
    CosmosCryptoEd25519PubKey,
}

#[derive(Serialize, Deserialize)]
pub enum Status {
    #[serde(rename = "BOND_STATUS_BONDED")]
    BondStatusBonded,

    #[serde(rename = "BOND_STATUS_UNBONDED")]
    BondStatusUnbonded,

    #[serde(rename = "BOND_STATUS_UNBONDING")]
    BondStatusUnbonding,
}
