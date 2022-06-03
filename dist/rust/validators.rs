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

    #[serde(rename = "validators")]
    validators: Vec<Validator>,
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
pub struct Validator {
    #[serde(rename = "path")]
    path: String,

    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "identity")]
    identity: String,

    #[serde(rename = "chains")]
    chains: Vec<Chain>,

    #[serde(rename = "profile")]
    profile: Profile,
}

#[derive(Serialize, Deserialize)]
pub struct Chain {
    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "restake")]
    restake: Restake,
}

#[derive(Serialize, Deserialize)]
pub struct Profile {
    #[serde(rename = "name")]
    name: String,

    #[serde(rename = "identity")]
    identity: String,
}

#[derive(Serialize, Deserialize)]
#[serde(untagged)]
pub enum Restake {
    Bool(bool),

    String(String),
}
