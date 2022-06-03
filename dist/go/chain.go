// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    cosmoshub, err := UnmarshalCosmoshub(bytes)
//    bytes, err = cosmoshub.Marshal()
//
//    juno, err := UnmarshalJuno(bytes)
//    bytes, err = juno.Marshal()
//
//    osmosis, err := UnmarshalOsmosis(bytes)
//    bytes, err = osmosis.Marshal()

package main

import "encoding/json"

func UnmarshalCosmoshub(data []byte) (Cosmoshub, error) {
	var r Cosmoshub
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Cosmoshub) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalJuno(data []byte) (Juno, error) {
	var r Juno
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Juno) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalOsmosis(data []byte) (Osmosis, error) {
	var r Osmosis
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Osmosis) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

type Cosmoshub struct {
	Repository Repository     `json:"repository"`
	Chain      CosmoshubChain `json:"chain"`     
}

type CosmoshubChain struct {
	Schema       string       `json:"$schema"`      
	ChainName    string       `json:"chain_name"`   
	ChainID      string       `json:"chain_id"`     
	PrettyName   string       `json:"pretty_name"`  
	Status       string       `json:"status"`       
	NetworkType  string       `json:"network_type"` 
	Bech32Prefix string       `json:"bech32_prefix"`
	Genesis      Genesis      `json:"genesis"`      
	DaemonName   string       `json:"daemon_name"`  
	NodeHome     string       `json:"node_home"`    
	KeyAlgos     []string     `json:"key_algos"`    
	Slip44       int64        `json:"slip44"`       
	Fees         Fees         `json:"fees"`         
	Codebase     Codebase     `json:"codebase"`     
	Peers        PurplePeers  `json:"peers"`        
	Apis         Apis         `json:"apis"`         
	Explorers    []Explorer   `json:"explorers"`    
	Name         string       `json:"name"`         
	Path         string       `json:"path"`         
	Symbol       string       `json:"symbol"`       
	Denom        string       `json:"denom"`        
	Decimals     int64        `json:"decimals"`     
	CoingeckoID  string       `json:"coingecko_id"` 
	Image        string       `json:"image"`        
	Height       int64        `json:"height"`       
	BestApis     BestApis     `json:"best_apis"`    
	Params       PurpleParams `json:"params"`       
}

type Apis struct {
	RPC  []Grpc `json:"rpc"` 
	REST []Grpc `json:"rest"`
	Grpc []Grpc `json:"grpc"`
}

type Grpc struct {
	Address  string `json:"address"` 
	Provider string `json:"provider"`
}

type BestApis struct {
	REST []Grpc `json:"rest"`
	RPC  []Grpc `json:"rpc"` 
}

type Codebase struct {
	GitRepo            string    `json:"git_repo"`           
	RecommendedVersion string    `json:"recommended_version"`
	CompatibleVersions []string  `json:"compatible_versions"`
	Binaries           *Binaries `json:"binaries,omitempty"` 
}

type Binaries struct {
	LinuxAmd64   string  `json:"linux/amd64"`            
	LinuxArm64   *string `json:"linux/arm64,omitempty"`  
	DarwinAmd64  *string `json:"darwin/amd64,omitempty"` 
	WindowsAmd64 *string `json:"windows/amd64,omitempty"`
}

type Explorer struct {
	Kind   string `json:"kind"`   
	URL    string `json:"url"`    
	TxPage string `json:"tx_page"`
}

type Fees struct {
	FeeTokens []FeeToken `json:"fee_tokens"`
}

type FeeToken struct {
	Denom            string `json:"denom"`              
	FixedMinGasPrice int64  `json:"fixed_min_gas_price"`
}

type Genesis struct {
	GenesisURL string `json:"genesis_url"`
}

type PurpleParams struct {
	Authz               bool    `json:"authz"`                 
	ActualBlockTime     float64 `json:"actual_block_time"`     
	ActualBlocksPerYear float64 `json:"actual_blocks_per_year"`
	UnbondingTime       int64   `json:"unbonding_time"`        
	MaxValidators       int64   `json:"max_validators"`        
	BlocksPerYear       int64   `json:"blocks_per_year"`       
	BlockTime           float64 `json:"block_time"`            
	CommunityTax        float64 `json:"community_tax"`         
	BaseInflation       float64 `json:"base_inflation"`        
	BondedRatio         float64 `json:"bonded_ratio"`          
	BondedTokens        string  `json:"bonded_tokens"`         
	TotalSupply         string  `json:"total_supply"`          
	EstimatedAPR        float64 `json:"estimated_apr"`         
	CalculatedAPR       float64 `json:"calculated_apr"`        
}

type PurplePeers struct {
	Seeds           []Seed           `json:"seeds"`           
	PersistentPeers []PersistentPeer `json:"persistent_peers"`
}

type PersistentPeer struct {
	ID      string `json:"id"`     
	Address string `json:"address"`
}

type Seed struct {
	ID       string  `json:"id"`                
	Address  string  `json:"address"`           
	Provider *string `json:"provider,omitempty"`
}

type Repository struct {
	URL       string `json:"url"`      
	Branch    string `json:"branch"`   
	Commit    string `json:"commit"`   
	Timestamp int64  `json:"timestamp"`
}

type Juno struct {
	Repository Repository `json:"repository"`
	Chain      JunoChain  `json:"chain"`     
}

type JunoChain struct {
	Schema       string       `json:"$schema"`      
	ChainName    string       `json:"chain_name"`   
	Status       string       `json:"status"`       
	NetworkType  string       `json:"network_type"` 
	PrettyName   string       `json:"pretty_name"`  
	ChainID      string       `json:"chain_id"`     
	Bech32Prefix string       `json:"bech32_prefix"`
	Slip44       int64        `json:"slip44"`       
	Genesis      Genesis      `json:"genesis"`      
	Codebase     Codebase     `json:"codebase"`     
	DaemonName   string       `json:"daemon_name"`  
	NodeHome     string       `json:"node_home"`    
	KeyAlgos     []string     `json:"key_algos"`    
	Peers        FluffyPeers  `json:"peers"`        
	Apis         Apis         `json:"apis"`         
	Explorers    []Explorer   `json:"explorers"`    
	Name         string       `json:"name"`         
	Path         string       `json:"path"`         
	Symbol       string       `json:"symbol"`       
	Denom        string       `json:"denom"`        
	Decimals     int64        `json:"decimals"`     
	CoingeckoID  string       `json:"coingecko_id"` 
	Image        string       `json:"image"`        
	Height       int64        `json:"height"`       
	BestApis     BestApis     `json:"best_apis"`    
	Params       PurpleParams `json:"params"`       
}

type FluffyPeers struct {
	Seeds           []PersistentPeer `json:"seeds"`           
	PersistentPeers []PersistentPeer `json:"persistent_peers"`
}

type Osmosis struct {
	Repository Repository   `json:"repository"`
	Chain      OsmosisChain `json:"chain"`     
}

type OsmosisChain struct {
	Schema       string         `json:"$schema"`      
	ChainName    string         `json:"chain_name"`   
	Status       string         `json:"status"`       
	NetworkType  string         `json:"network_type"` 
	PrettyName   string         `json:"pretty_name"`  
	ChainID      string         `json:"chain_id"`     
	Bech32Prefix string         `json:"bech32_prefix"`
	DaemonName   string         `json:"daemon_name"`  
	NodeHome     string         `json:"node_home"`    
	Genesis      Genesis        `json:"genesis"`      
	KeyAlgos     []string       `json:"key_algos"`    
	Slip44       int64          `json:"slip44"`       
	Fees         Fees           `json:"fees"`         
	Codebase     Codebase       `json:"codebase"`     
	Peers        TentacledPeers `json:"peers"`        
	Apis         Apis           `json:"apis"`         
	Explorers    []Explorer     `json:"explorers"`    
	Name         string         `json:"name"`         
	Path         string         `json:"path"`         
	Symbol       string         `json:"symbol"`       
	Denom        string         `json:"denom"`        
	Decimals     int64          `json:"decimals"`     
	CoingeckoID  string         `json:"coingecko_id"` 
	Image        string         `json:"image"`        
	Height       int64          `json:"height"`       
	BestApis     BestApis       `json:"best_apis"`    
	Params       FluffyParams   `json:"params"`       
}

type FluffyParams struct {
	Authz                 bool    `json:"authz"`                  
	ActualBlockTime       float64 `json:"actual_block_time"`      
	ActualBlocksPerYear   float64 `json:"actual_blocks_per_year"` 
	UnbondingTime         int64   `json:"unbonding_time"`         
	MaxValidators         int64   `json:"max_validators"`         
	BondedRatio           float64 `json:"bonded_ratio"`           
	MintingEpochProvision float64 `json:"minting_epoch_provision"`
	EpochDuration         int64   `json:"epoch_duration"`         
	YearMintingProvision  int64   `json:"year_minting_provision"` 
	BondedTokens          string  `json:"bonded_tokens"`          
	TotalSupply           string  `json:"total_supply"`           
	BaseInflation         float64 `json:"base_inflation"`         
	CalculatedAPR         float64 `json:"calculated_apr"`         
}

type TentacledPeers struct {
	Seeds           []Seed `json:"seeds"`           
	PersistentPeers []Seed `json:"persistent_peers"`
}
