// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    index, err := UnmarshalIndex(bytes)
//    bytes, err = index.Marshal()

package main

import "encoding/json"

func UnmarshalIndex(data []byte) (Index, error) {
	var r Index
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Index) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

type Index struct {
	Repository Repository `json:"repository"`
	Chains     []Chain    `json:"chains"`    
}

type Chain struct {
	Name        string      `json:"name"`                  
	Path        string      `json:"path"`                  
	ChainName   string      `json:"chain_name"`            
	NetworkType NetworkType `json:"network_type"`          
	PrettyName  string      `json:"pretty_name"`           
	ChainID     string      `json:"chain_id"`              
	Status      Status      `json:"status"`                
	Symbol      *string     `json:"symbol,omitempty"`      
	Denom       *string     `json:"denom,omitempty"`       
	Decimals    *int64      `json:"decimals,omitempty"`    
	Image       *string     `json:"image,omitempty"`       
	Height      *int64      `json:"height"`                
	BestApis    BestApis    `json:"best_apis"`             
	Params      Params      `json:"params"`                
	CoingeckoID *string     `json:"coingecko_id,omitempty"`
}

type BestApis struct {
	REST []REST `json:"rest"`
	RPC  []REST `json:"rpc"` 
}

type REST struct {
	Address  string  `json:"address"`           
	Provider *string `json:"provider,omitempty"`
}

type Params struct {
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

type NetworkType string
const (
	Mainnet NetworkType = "mainnet"
)

type Status string
const (
	Killed Status = "killed"
	Live Status = "live"
)
