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

import "bytes"
import "errors"
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

type Osmosis struct {
	Name       Name        `json:"name"`      
	Validators []Validator `json:"validators"`
}

type Validator struct {
	Moniker           string          `json:"moniker"`                 
	Identity          *string         `json:"identity,omitempty"`      
	Address           string          `json:"address"`                 
	HexAddress        string          `json:"hexAddress"`              
	Uptime            float64         `json:"uptime"`                  
	MissedBlocks      int64           `json:"missedBlocks"`            
	OperatorAddress   string          `json:"operator_address"`        
	ConsensusPubkey   ConsensusPubkey `json:"consensus_pubkey"`        
	Jailed            bool            `json:"jailed"`                  
	Status            Status          `json:"status"`                  
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
	Name              *Name           `json:"name,omitempty"`          
	Restake           *Restake        `json:"restake,omitempty"`       
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

type Restake struct {
	Address       string   `json:"address"`       
	RunTime       *RunTime `json:"run_time"`      
	MinimumReward int64    `json:"minimum_reward"`
}

type Name string
const (
	NameCosmoshub Name = "cosmoshub"
	NameJuno Name = "juno"
	NameOsmosis Name = "osmosis"
)

type Type string
const (
	CosmosCryptoEd25519PubKey Type = "/cosmos.crypto.ed25519.PubKey"
)

type Status string
const (
	BondStatusBonded Status = "BOND_STATUS_BONDED"
	BondStatusUnbonded Status = "BOND_STATUS_UNBONDED"
	BondStatusUnbonding Status = "BOND_STATUS_UNBONDING"
)

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
