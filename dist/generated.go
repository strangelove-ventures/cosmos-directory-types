// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    allChainsData, err := UnmarshalAllChainsData(bytes)
//    bytes, err = allChainsData.Marshal()
//
//    chainData, err := UnmarshalChainData(bytes)
//    bytes, err = chainData.Marshal()
//
//    allValidatorsData, err := UnmarshalAllValidatorsData(bytes)
//    bytes, err = allValidatorsData.Marshal()
//
//    validatorData, err := UnmarshalValidatorData(bytes)
//    bytes, err = validatorData.Marshal()
//
//    chainValidatorsData, err := UnmarshalChainValidatorsData(bytes)
//    bytes, err = chainValidatorsData.Marshal()

package main

import "bytes"
import "errors"
import "encoding/json"

func UnmarshalAllChainsData(data []byte) (AllChainsData, error) {
	var r AllChainsData
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *AllChainsData) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalChainData(data []byte) (ChainData, error) {
	var r ChainData
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *ChainData) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalAllValidatorsData(data []byte) (AllValidatorsData, error) {
	var r AllValidatorsData
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *AllValidatorsData) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalValidatorData(data []byte) (ValidatorData, error) {
	var r ValidatorData
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *ValidatorData) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalChainValidatorsData(data []byte) (ChainValidatorsData, error) {
	var r ChainValidatorsData
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *ChainValidatorsData) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

type AllChainsData struct {
	Repository Repository           `json:"repository"`
	Chains     []AllChainsDataChain `json:"chains"`    
}

type AllChainsDataChain struct {
	Name        string       `json:"name"`                  
	Path        string       `json:"path"`                  
	ChainName   string       `json:"chain_name"`            
	NetworkType NetworkType  `json:"network_type"`          
	PrettyName  string       `json:"pretty_name"`           
	ChainID     string       `json:"chain_id"`              
	Status      PurpleStatus `json:"status"`                
	Symbol      *string      `json:"symbol,omitempty"`      
	Denom       *string      `json:"denom,omitempty"`       
	Decimals    *int64       `json:"decimals,omitempty"`    
	Image       *string      `json:"image,omitempty"`       
	Height      *int64       `json:"height"`                
	BestApis    BestApis     `json:"best_apis"`             
	Params      PurpleParams `json:"params"`                
	CoingeckoID *string      `json:"coingecko_id,omitempty"`
}

type BestApis struct {
	REST []Grpc `json:"rest"`
	RPC  []Grpc `json:"rpc"` 
}

type Grpc struct {
	Address  string  `json:"address"`           
	Provider *string `json:"provider,omitempty"`
}

type PurpleParams struct {
	Authz           *bool    `json:"authz,omitempty"`            
	BondedTokens    *string  `json:"bonded_tokens,omitempty"`    
	TotalSupply     *string  `json:"total_supply,omitempty"`     
	ActualBlockTime *float64 `json:"actual_block_time,omitempty"`
	CalculatedAPR   *float64 `json:"calculated_apr,omitempty"`   
}

type Repository struct {
	URL       string `json:"url"`      
	Branch    string `json:"branch"`   
	Commit    string `json:"commit"`   
	Timestamp int64  `json:"timestamp"`
}

type ChainData struct {
	Repository Repository     `json:"repository"`
	Chain      ChainDataChain `json:"chain"`     
}

type ChainDataChain struct {
	Schema       string       `json:"$schema"`       
	ChainName    string       `json:"chain_name"`    
	ChainID      string       `json:"chain_id"`      
	PrettyName   string       `json:"pretty_name"`   
	Status       PurpleStatus `json:"status"`        
	NetworkType  NetworkType  `json:"network_type"`  
	Bech32Prefix string       `json:"bech32_prefix"` 
	Genesis      Genesis      `json:"genesis"`       
	DaemonName   string       `json:"daemon_name"`   
	NodeHome     string       `json:"node_home"`     
	KeyAlgos     []string     `json:"key_algos"`     
	Slip44       int64        `json:"slip44"`        
	Fees         *Fees        `json:"fees,omitempty"`
	Codebase     Codebase     `json:"codebase"`      
	Peers        Peers        `json:"peers"`         
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
	Params       FluffyParams `json:"params"`        
}

type Apis struct {
	RPC  []Grpc `json:"rpc"` 
	REST []Grpc `json:"rest"`
	Grpc []Grpc `json:"grpc"`
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
	Kind        string  `json:"kind"`                  
	URL         string  `json:"url"`                   
	TxPage      string  `json:"tx_page"`               
	AccountPage *string `json:"account_page,omitempty"`
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

type FluffyParams struct {
	Authz                 bool     `json:"authz"`                            
	ActualBlockTime       float64  `json:"actual_block_time"`                
	ActualBlocksPerYear   float64  `json:"actual_blocks_per_year"`           
	UnbondingTime         int64    `json:"unbonding_time"`                   
	MaxValidators         int64    `json:"max_validators"`                   
	BlocksPerYear         *int64   `json:"blocks_per_year,omitempty"`        
	BlockTime             *float64 `json:"block_time,omitempty"`             
	CommunityTax          *float64 `json:"community_tax,omitempty"`          
	BaseInflation         float64  `json:"base_inflation"`                   
	TotalSupply           string   `json:"total_supply"`                     
	BondedTokens          string   `json:"bonded_tokens"`                    
	BondedRatio           float64  `json:"bonded_ratio"`                     
	EstimatedAPR          *float64 `json:"estimated_apr,omitempty"`          
	CalculatedAPR         float64  `json:"calculated_apr"`                   
	MintingEpochProvision *float64 `json:"minting_epoch_provision,omitempty"`
	EpochDuration         *int64   `json:"epoch_duration,omitempty"`         
	YearMintingProvision  *int64   `json:"year_minting_provision,omitempty"` 
}

type Peers struct {
	Seeds           []PersistentPeer `json:"seeds"`           
	PersistentPeers []PersistentPeer `json:"persistent_peers"`
}

type PersistentPeer struct {
	ID       string  `json:"id"`                
	Address  string  `json:"address"`           
	Provider *string `json:"provider,omitempty"`
}

type AllValidatorsData struct {
	Repository Repository                   `json:"repository"`
	Validators []AllValidatorsDataValidator `json:"validators"`
}

type AllValidatorsDataValidator struct {
	Path     string           `json:"path"`    
	Name     string           `json:"name"`    
	Identity string           `json:"identity"`
	Chains   []ValidatorChain `json:"chains"`  
	Profile  Profile          `json:"profile"` 
}

type ValidatorChain struct {
	Name    string        `json:"name"`   
	Address string        `json:"address"`
	Restake *RestakeUnion `json:"restake"`
}

type Profile struct {
	Name     string `json:"name"`    
	Identity string `json:"identity"`
}

type ValidatorData struct {
	Repository Repository             `json:"repository"`
	Validator  ValidatorDataValidator `json:"validator"` 
}

type ValidatorDataValidator struct {
	Path     string         `json:"path"`    
	Name     string         `json:"name"`    
	Identity string         `json:"identity"`
	Chains   []ChainElement `json:"chains"`  
	Profile  Profile        `json:"profile"` 
}

type ChainElement struct {
	Name              *string         `json:"name,omitempty"`          
	Address           string          `json:"address"`                 
	Restake           *RestakeClass   `json:"restake,omitempty"`       
	Moniker           string          `json:"moniker"`                 
	Identity          *string         `json:"identity,omitempty"`      
	HexAddress        string          `json:"hexAddress"`              
	Uptime            *float64        `json:"uptime"`                  
	MissedBlocks      int64           `json:"missedBlocks"`            
	OperatorAddress   string          `json:"operator_address"`        
	ConsensusPubkey   ConsensusPubkey `json:"consensus_pubkey"`        
	Jailed            bool            `json:"jailed"`                  
	Status            ValidatorStatus `json:"status"`                  
	Tokens            string          `json:"tokens"`                  
	DelegatorShares   string          `json:"delegator_shares"`        
	Description       Description     `json:"description"`             
	UnbondingHeight   string          `json:"unbonding_height"`        
	UnbondingTime     string          `json:"unbonding_time"`          
	Commission        Commission      `json:"commission"`              
	MinSelfDelegation string          `json:"min_self_delegation"`     
	Rank              int64           `json:"rank"`                    
	MintscanImage     *string         `json:"mintscan_image,omitempty"`
	KeybaseImage      *string         `json:"keybase_image,omitempty"` 
}

type Commission struct {
	CommissionRates CommissionRates `json:"commission_rates"`
	UpdateTime      string          `json:"update_time"`     
}

type CommissionRates struct {
	Rate          string `json:"rate"`           
	MaxRate       string `json:"max_rate"`       
	MaxChangeRate string `json:"max_change_rate"`
}

type ConsensusPubkey struct {
	Type Type   `json:"@type"`
	Key  string `json:"key"`  
}

type Description struct {
	Moniker         string `json:"moniker"`         
	Identity        string `json:"identity"`        
	Website         string `json:"website"`         
	SecurityContact string `json:"security_contact"`
	Details         string `json:"details"`         
}

type RestakeClass struct {
	Address       string   `json:"address"`       
	RunTime       *RunTime `json:"run_time"`      
	MinimumReward int64    `json:"minimum_reward"`
}

type ChainValidatorsData struct {
	Name       string         `json:"name"`      
	Validators []ChainElement `json:"validators"`
}

type NetworkType string
const (
	Mainnet NetworkType = "mainnet"
)

type PurpleStatus string
const (
	Killed PurpleStatus = "killed"
	Live PurpleStatus = "live"
)

type Type string
const (
	CosmosCryptoEd25519PubKey Type = "/cosmos.crypto.ed25519.PubKey"
)

type ValidatorStatus string
const (
	BondStatusBonded ValidatorStatus = "BOND_STATUS_BONDED"
	BondStatusUnbonded ValidatorStatus = "BOND_STATUS_UNBONDED"
	BondStatusUnbonding ValidatorStatus = "BOND_STATUS_UNBONDING"
)

type RestakeUnion struct {
	Bool   *bool
	String *string
}

func (x *RestakeUnion) UnmarshalJSON(data []byte) error {
	object, err := unmarshalUnion(data, nil, nil, &x.Bool, &x.String, false, nil, false, nil, false, nil, false, nil, false)
	if err != nil {
		return err
	}
	if object {
	}
	return nil
}

func (x *RestakeUnion) MarshalJSON() ([]byte, error) {
	return marshalUnion(nil, nil, x.Bool, x.String, false, nil, false, nil, false, nil, false, nil, false)
}

type RunTime struct {
	String      *string
	StringArray []string
}

func (x *RunTime) UnmarshalJSON(data []byte) error {
	x.StringArray = nil
	object, err := unmarshalUnion(data, nil, nil, nil, &x.String, true, &x.StringArray, false, nil, false, nil, false, nil, false)
	if err != nil {
		return err
	}
	if object {
	}
	return nil
}

func (x *RunTime) MarshalJSON() ([]byte, error) {
	return marshalUnion(nil, nil, nil, x.String, x.StringArray != nil, x.StringArray, false, nil, false, nil, false, nil, false)
}

func unmarshalUnion(data []byte, pi **int64, pf **float64, pb **bool, ps **string, haveArray bool, pa interface{}, haveObject bool, pc interface{}, haveMap bool, pm interface{}, haveEnum bool, pe interface{}, nullable bool) (bool, error) {
	if pi != nil {
		*pi = nil
	}
	if pf != nil {
		*pf = nil
	}
	if pb != nil {
		*pb = nil
	}
	if ps != nil {
		*ps = nil
	}

	dec := json.NewDecoder(bytes.NewReader(data))
	dec.UseNumber()
	tok, err := dec.Token()
	if err != nil {
		return false, err
	}

	switch v := tok.(type) {
	case json.Number:
		if pi != nil {
			i, err := v.Int64()
			if err == nil {
				*pi = &i
				return false, nil
			}
		}
		if pf != nil {
			f, err := v.Float64()
			if err == nil {
				*pf = &f
				return false, nil
			}
			return false, errors.New("Unparsable number")
		}
		return false, errors.New("Union does not contain number")
	case float64:
		return false, errors.New("Decoder should not return float64")
	case bool:
		if pb != nil {
			*pb = &v
			return false, nil
		}
		return false, errors.New("Union does not contain bool")
	case string:
		if haveEnum {
			return false, json.Unmarshal(data, pe)
		}
		if ps != nil {
			*ps = &v
			return false, nil
		}
		return false, errors.New("Union does not contain string")
	case nil:
		if nullable {
			return false, nil
		}
		return false, errors.New("Union does not contain null")
	case json.Delim:
		if v == '{' {
			if haveObject {
				return true, json.Unmarshal(data, pc)
			}
			if haveMap {
				return false, json.Unmarshal(data, pm)
			}
			return false, errors.New("Union does not contain object")
		}
		if v == '[' {
			if haveArray {
				return false, json.Unmarshal(data, pa)
			}
			return false, errors.New("Union does not contain array")
		}
		return false, errors.New("Cannot handle delimiter")
	}
	return false, errors.New("Cannot unmarshal union")

}

func marshalUnion(pi *int64, pf *float64, pb *bool, ps *string, haveArray bool, pa interface{}, haveObject bool, pc interface{}, haveMap bool, pm interface{}, haveEnum bool, pe interface{}, nullable bool) ([]byte, error) {
	if pi != nil {
		return json.Marshal(*pi)
	}
	if pf != nil {
		return json.Marshal(*pf)
	}
	if pb != nil {
		return json.Marshal(*pb)
	}
	if ps != nil {
		return json.Marshal(*ps)
	}
	if haveArray {
		return json.Marshal(pa)
	}
	if haveObject {
		return json.Marshal(pc)
	}
	if haveMap {
		return json.Marshal(pm)
	}
	if haveEnum {
		return json.Marshal(pe)
	}
	if nullable {
		return json.Marshal(nil)
	}
	return nil, errors.New("Union must not be null")
}

