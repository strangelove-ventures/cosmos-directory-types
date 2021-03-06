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
	Chains     []AllChainsDataChain `json:"chains"`    
	Repository Repository           `json:"repository"`
}

type AllChainsDataChain struct {
	BestApis    BestApis     `json:"best_apis"`             
	ChainID     string       `json:"chain_id"`              
	ChainName   string       `json:"chain_name"`            
	CoingeckoID *string      `json:"coingecko_id,omitempty"`
	Decimals    *int64       `json:"decimals,omitempty"`    
	Denom       *string      `json:"denom,omitempty"`       
	Height      *int64       `json:"height"`                
	Image       *string      `json:"image,omitempty"`       
	Name        string       `json:"name"`                  
	NetworkType NetworkType  `json:"network_type"`          
	Params      PurpleParams `json:"params"`                
	Path        string       `json:"path"`                  
	PrettyName  string       `json:"pretty_name"`           
	Status      PurpleStatus `json:"status"`                
	Symbol      *string      `json:"symbol,omitempty"`      
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
	ActualBlockTime *float64 `json:"actual_block_time,omitempty"`
	Authz           *bool    `json:"authz,omitempty"`            
	BondedTokens    *string  `json:"bonded_tokens,omitempty"`    
	CalculatedAPR   *float64 `json:"calculated_apr"`             
	TotalSupply     *string  `json:"total_supply,omitempty"`     
}

type Repository struct {
	Branch    string `json:"branch"`   
	Commit    string `json:"commit"`   
	Timestamp int64  `json:"timestamp"`
	URL       string `json:"url"`      
}

type ChainData struct {
	Chain      ChainDataChain `json:"chain"`     
	Repository Repository     `json:"repository"`
}

type ChainDataChain struct {
	Apis         Apis         `json:"apis"`                
	Bech32Prefix string       `json:"bech32_prefix"`       
	BestApis     BestApis     `json:"best_apis"`           
	ChainID      string       `json:"chain_id"`            
	ChainName    string       `json:"chain_name"`          
	Codebase     Codebase     `json:"codebase"`            
	CoingeckoID  string       `json:"coingecko_id"`        
	DaemonName   string       `json:"daemon_name"`         
	Decimals     int64        `json:"decimals"`            
	Denom        string       `json:"denom"`               
	Explorers    []Explorer   `json:"explorers"`           
	Fees         *Fees        `json:"fees,omitempty"`      
	Genesis      Genesis      `json:"genesis"`             
	Height       int64        `json:"height"`              
	Image        string       `json:"image"`               
	KeyAlgos     []string     `json:"key_algos"`           
	LogoURIs     *LogoURIs    `json:"logo_URIs,omitempty"` 
	Name         string       `json:"name"`                
	NetworkType  NetworkType  `json:"network_type"`        
	NodeHome     string       `json:"node_home"`           
	Params       FluffyParams `json:"params"`              
	Path         string       `json:"path"`                
	Peers        Peers        `json:"peers"`               
	PrettyName   string       `json:"pretty_name"`         
	Schema       string       `json:"$schema"`             
	Slip44       int64        `json:"slip44"`              
	Status       PurpleStatus `json:"status"`              
	Symbol       string       `json:"symbol"`              
	Updatelink   *string      `json:"updatelink,omitempty"`
}

type Apis struct {
	Grpc []Grpc `json:"grpc"`
	REST []Grpc `json:"rest"`
	RPC  []Grpc `json:"rpc"` 
}

type Codebase struct {
	Binaries           *Binaries `json:"binaries,omitempty"`          
	CompatibleVersions []string  `json:"compatible_versions"`         
	CosmosSDKVersion   *string   `json:"cosmos_sdk_version,omitempty"`
	CosmwasmEnabled    *bool     `json:"cosmwasm_enabled,omitempty"`  
	CosmwasmVersion    *string   `json:"cosmwasm_version,omitempty"`  
	GitRepo            string    `json:"git_repo"`                    
	RecommendedVersion string    `json:"recommended_version"`         
	TendermintVersion  *string   `json:"tendermint_version,omitempty"`
}

type Binaries struct {
	DarwinAmd64  *string `json:"darwin/amd64,omitempty"` 
	LinuxAmd64   string  `json:"linux/amd64"`            
	LinuxArm64   string  `json:"linux/arm64"`            
	WindowsAmd64 *string `json:"windows/amd64,omitempty"`
}

type Explorer struct {
	AccountPage *string `json:"account_page,omitempty"`
	Kind        string  `json:"kind"`                  
	TxPage      string  `json:"tx_page"`               
	URL         string  `json:"url"`                   
}

type Fees struct {
	FeeTokens []FeeToken `json:"fee_tokens"`
}

type FeeToken struct {
	AverageGasPrice  *float64 `json:"average_gas_price,omitempty"`
	Denom            string   `json:"denom"`                      
	FixedMinGasPrice int64    `json:"fixed_min_gas_price"`        
	HighGasPrice     *float64 `json:"high_gas_price,omitempty"`   
	LowGasPrice      *int64   `json:"low_gas_price,omitempty"`    
}

type Genesis struct {
	GenesisURL string `json:"genesis_url"`
}

type LogoURIs struct {
	PNG string `json:"png"`
}

type FluffyParams struct {
	ActualBlockTime       float64      `json:"actual_block_time"`                
	ActualBlocksPerYear   float64      `json:"actual_blocks_per_year"`           
	AnnualProvision       string       `json:"annual_provision"`                 
	Authz                 bool         `json:"authz"`                            
	BaseInflation         float64      `json:"base_inflation"`                   
	BlockTime             *float64     `json:"block_time,omitempty"`             
	BlocksPerYear         *int64       `json:"blocks_per_year,omitempty"`        
	BondedRatio           float64      `json:"bonded_ratio"`                     
	BondedTokens          string       `json:"bonded_tokens"`                    
	CalculatedAPR         float64      `json:"calculated_apr"`                   
	CommunityTax          float64      `json:"community_tax"`                    
	Distribution          Distribution `json:"distribution"`                     
	EpochDuration         *int64       `json:"epoch_duration,omitempty"`         
	EstimatedAPR          float64      `json:"estimated_apr"`                    
	MaxValidators         int64        `json:"max_validators"`                   
	Mint                  Mint         `json:"mint"`                             
	MintingEpochProvision *float64     `json:"minting_epoch_provision,omitempty"`
	Slashing              Slashing     `json:"slashing"`                         
	Staking               Staking      `json:"staking"`                          
	TotalSupply           string       `json:"total_supply"`                     
	UnbondingTime         int64        `json:"unbonding_time"`                   
	YearMintingProvision  *int64       `json:"year_minting_provision,omitempty"` 
}

type Distribution struct {
	BaseProposerReward  string `json:"base_proposer_reward"` 
	BonusProposerReward string `json:"bonus_proposer_reward"`
	CommunityTax        string `json:"community_tax"`        
	WithdrawAddrEnabled bool   `json:"withdraw_addr_enabled"`
}

type Mint struct {
	BlocksPerYear                        *string                            `json:"blocks_per_year,omitempty"`                         
	DistributionProportions              *DistributionProportions           `json:"distribution_proportions,omitempty"`                
	EpochIdentifier                      *string                            `json:"epoch_identifier,omitempty"`                        
	GenesisEpochProvisions               *string                            `json:"genesis_epoch_provisions,omitempty"`                
	GoalBonded                           *string                            `json:"goal_bonded,omitempty"`                             
	InflationMax                         *string                            `json:"inflation_max,omitempty"`                           
	InflationMin                         *string                            `json:"inflation_min,omitempty"`                           
	InflationRateChange                  *string                            `json:"inflation_rate_change,omitempty"`                   
	MintDenom                            string                             `json:"mint_denom"`                                        
	MintingRewardsDistributionStartEpoch *string                            `json:"minting_rewards_distribution_start_epoch,omitempty"`
	ReductionFactor                      *string                            `json:"reduction_factor,omitempty"`                        
	ReductionPeriodInEpochs              *string                            `json:"reduction_period_in_epochs,omitempty"`              
	WeightedDeveloperRewardsReceivers    []WeightedDeveloperRewardsReceiver `json:"weighted_developer_rewards_receivers,omitempty"`    
}

type DistributionProportions struct {
	CommunityPool    string `json:"community_pool"`   
	DeveloperRewards string `json:"developer_rewards"`
	PoolIncentives   string `json:"pool_incentives"`  
	Staking          string `json:"staking"`          
}

type WeightedDeveloperRewardsReceiver struct {
	Address string `json:"address"`
	Weight  string `json:"weight"` 
}

type Slashing struct {
	DowntimeJailDuration    string `json:"downtime_jail_duration"`    
	MinSignedPerWindow      string `json:"min_signed_per_window"`     
	SignedBlocksWindow      string `json:"signed_blocks_window"`      
	SlashFractionDoubleSign string `json:"slash_fraction_double_sign"`
	SlashFractionDowntime   string `json:"slash_fraction_downtime"`   
}

type Staking struct {
	BondDenom         string  `json:"bond_denom"`                   
	HistoricalEntries int64   `json:"historical_entries"`           
	MaxEntries        int64   `json:"max_entries"`                  
	MaxValidators     int64   `json:"max_validators"`               
	MinCommissionRate *string `json:"min_commission_rate,omitempty"`
	UnbondingTime     string  `json:"unbonding_time"`               
}

type Peers struct {
	PersistentPeers []PersistentPeer `json:"persistent_peers"`
	Seeds           []PersistentPeer `json:"seeds"`           
}

type PersistentPeer struct {
	Address  string  `json:"address"`           
	ID       string  `json:"id"`                
	Provider *string `json:"provider,omitempty"`
}

type AllValidatorsData struct {
	Repository Repository                   `json:"repository"`
	Validators []AllValidatorsDataValidator `json:"validators"`
}

type AllValidatorsDataValidator struct {
	Chains   []ValidatorChain `json:"chains"`  
	Identity string           `json:"identity"`
	Name     string           `json:"name"`    
	Path     string           `json:"path"`    
	Profile  ChainProfile     `json:"profile"` 
}

type ValidatorChain struct {
	Address string        `json:"address"`
	Name    string        `json:"name"`   
	Restake *RestakeUnion `json:"restake"`
}

type ChainProfile struct {
	Apps     []string `json:"apps,omitempty"`   
	Identity string   `json:"identity"`         
	Name     string   `json:"name"`             
	Schema   *Schema  `json:"$schema,omitempty"`
	Twitter  *string  `json:"twitter,omitempty"`
	Website  *string  `json:"website,omitempty"`
}

type ValidatorData struct {
	Repository Repository             `json:"repository"`
	Validator  ValidatorDataValidator `json:"validator"` 
}

type ValidatorDataValidator struct {
	Chains   []ChainElement `json:"chains"`  
	Identity string         `json:"identity"`
	Name     string         `json:"name"`    
	Path     string         `json:"path"`    
	Profile  PurpleProfile  `json:"profile"` 
}

type ChainElement struct {
	Address             string               `json:"address"`                        
	Commission          *Commission          `json:"commission,omitempty"`           
	ConsensusPubkey     *ConsensusPubkey     `json:"consensus_pubkey,omitempty"`     
	DelegatorShares     *string              `json:"delegator_shares,omitempty"`     
	Description         *Description         `json:"description,omitempty"`          
	HexAddress          *string              `json:"hex_address,omitempty"`          
	Identity            *string              `json:"identity,omitempty"`             
	Jailed              *bool                `json:"jailed,omitempty"`               
	KeybaseImage        *string              `json:"keybase_image,omitempty"`        
	MinSelfDelegation   *string              `json:"min_self_delegation,omitempty"`  
	MintscanImage       *string              `json:"mintscan_image,omitempty"`       
	MissedBlocks        *int64               `json:"missed_blocks,omitempty"`        
	MissedBlocksPeriods []MissedBlocksPeriod `json:"missed_blocks_periods,omitempty"`
	Moniker             *string              `json:"moniker,omitempty"`              
	Name                *string              `json:"name,omitempty"`                 
	OperatorAddress     *string              `json:"operator_address,omitempty"`     
	Path                *string              `json:"path,omitempty"`                 
	Profile             *ChainProfile        `json:"profile,omitempty"`              
	Rank                *int64               `json:"rank,omitempty"`                 
	Restake             *RestakeClass        `json:"restake,omitempty"`              
	Services            *Services            `json:"services,omitempty"`             
	SigningInfo         *SigningInfo         `json:"signing_info,omitempty"`         
	Slashes             []Slash              `json:"slashes,omitempty"`              
	Status              *ValidatorStatus     `json:"status,omitempty"`               
	Tokens              *string              `json:"tokens,omitempty"`               
	UnbondingHeight     *string              `json:"unbonding_height,omitempty"`     
	UnbondingTime       *string              `json:"unbonding_time,omitempty"`       
	Uptime              *float64             `json:"uptime,omitempty"`               
	UptimePeriods       []UptimePeriod       `json:"uptime_periods,omitempty"`       
}

type Commission struct {
	CommissionRates CommissionRates `json:"commission_rates"`
	UpdateTime      string          `json:"update_time"`     
}

type CommissionRates struct {
	MaxChangeRate string `json:"max_change_rate"`
	MaxRate       string `json:"max_rate"`       
	Rate          string `json:"rate"`           
}

type ConsensusPubkey struct {
	Key  string `json:"key"`  
	Type Type   `json:"@type"`
}

type Description struct {
	Details         string `json:"details"`         
	Identity        string `json:"identity"`        
	Moniker         string `json:"moniker"`         
	SecurityContact string `json:"security_contact"`
	Website         string `json:"website"`         
}

type MissedBlocksPeriod struct {
	Blocks int64 `json:"blocks"`
	Missed int64 `json:"missed"`
}

type RestakeClass struct {
	Address       string   `json:"address"`       
	MinimumReward float64  `json:"minimum_reward"`
	RunTime       *RunTime `json:"run_time"`      
}

type Services struct {
	StakingRewards StakingRewards `json:"staking_rewards"`
}

type StakingRewards struct {
	Name     string `json:"name"`    
	Slug     string `json:"slug"`    
	Verified bool   `json:"verified"`
}

type SigningInfo struct {
	Address             string `json:"address"`              
	IndexOffset         string `json:"index_offset"`         
	JailedUntil         string `json:"jailed_until"`         
	MissedBlocksCounter string `json:"missed_blocks_counter"`
	StartHeight         string `json:"start_height"`         
	Tombstoned          bool   `json:"tombstoned"`           
}

type Slash struct {
	Fraction        string `json:"fraction"`        
	ValidatorPeriod string `json:"validator_period"`
}

type UptimePeriod struct {
	Blocks int64   `json:"blocks"`
	Uptime float64 `json:"uptime"`
}

type PurpleProfile struct {
	Identity string `json:"identity"`
	Name     string `json:"name"`    
	Schema   Schema `json:"$schema"` 
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
	Live PurpleStatus = "live"
)

type Schema string
const (
	ProfileSchemaJSON Schema = "../profile.schema.json"
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

