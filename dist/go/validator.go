// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    deuslabs, err := UnmarshalDeuslabs(bytes)
//    bytes, err = deuslabs.Marshal()
//
//    ezstaking, err := UnmarshalEzstaking(bytes)
//    bytes, err = ezstaking.Marshal()
//
//    oni, err := UnmarshalOni(bytes)
//    bytes, err = oni.Marshal()

package main

import "bytes"
import "errors"
import "encoding/json"

func UnmarshalDeuslabs(data []byte) (Deuslabs, error) {
	var r Deuslabs
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Deuslabs) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalEzstaking(data []byte) (Ezstaking, error) {
	var r Ezstaking
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Ezstaking) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

func UnmarshalOni(data []byte) (Oni, error) {
	var r Oni
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Oni) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

type Oni struct {
	Repository Repository        `json:"repository"`
	Validator  DeuslabsValidator `json:"validator"` 
}

type Repository struct {
	URL       string `json:"url"`      
	Branch    string `json:"branch"`   
	Commit    string `json:"commit"`   
	Timestamp int64  `json:"timestamp"`
}

type DeuslabsValidator struct {
	Path     string        `json:"path"`    
	Name     string        `json:"name"`    
	Identity Identity      `json:"identity"`
	Chains   []PurpleChain `json:"chains"`  
	Profile  Profile       `json:"profile"` 
}

type PurpleChain struct {
	Name              string          `json:"name"`                   
	Address           string          `json:"address"`                
	Restake           PurpleRestake   `json:"restake"`                
	Moniker           string          `json:"moniker"`                
	Identity          *Identity       `json:"identity,omitempty"`     
	HexAddress        string          `json:"hexAddress"`             
	Uptime            int64           `json:"uptime"`                 
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
	MintscanImage     string          `json:"mintscan_image"`         
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
	Moniker         string   `json:"moniker"`         
	Identity        Identity `json:"identity"`        
	Website         string   `json:"website"`         
	SecurityContact string   `json:"security_contact"`
	Details         string   `json:"details"`         
}

type PurpleRestake struct {
	Address       string `json:"address"`       
	RunTime       string `json:"run_time"`      
	MinimumReward int64  `json:"minimum_reward"`
}

type Profile struct {
	Name     string   `json:"name"`    
	Identity Identity `json:"identity"`
}

type Ezstaking struct {
	Repository Repository         `json:"repository"`
	Validator  EzstakingValidator `json:"validator"` 
}

type EzstakingValidator struct {
	Path     string        `json:"path"`    
	Name     string        `json:"name"`    
	Identity Identity      `json:"identity"`
	Chains   []FluffyChain `json:"chains"`  
	Profile  Profile       `json:"profile"` 
}

type FluffyChain struct {
	Name              string          `json:"name"`                    
	Address           string          `json:"address"`                 
	Restake           FluffyRestake   `json:"restake"`                 
	Moniker           string          `json:"moniker"`                 
	Identity          Identity        `json:"identity"`                
	HexAddress        string          `json:"hexAddress"`              
	Uptime            *int64          `json:"uptime"`                  
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
	KeybaseImage      string          `json:"keybase_image"`           
}

type FluffyRestake struct {
	Address       string        `json:"address"`       
	RunTime       *RunTimeUnion `json:"run_time"`      
	MinimumReward int64         `json:"minimum_reward"`
}

type Type string
const (
	CosmosCryptoEd25519PubKey Type = "/cosmos.crypto.ed25519.PubKey"
)

type Identity string
const (
	Ed7Ca7124A3F0Ed6 Identity = "ED7CA7124A3F0ED6"
	Empty Identity = ""
	The1534523421A364DB Identity = "1534523421A364DB"
	The5A8Ab49Cf5Caaf3C Identity = "5A8AB49CF5CAAF3C"
)

type Status string
const (
	BondStatusBonded Status = "BOND_STATUS_BONDED"
)

type RunTimeElement string
const (
	The0000 RunTimeElement = "00:00"
	The1200 RunTimeElement = "12:00"
)

type RunTimeUnion struct {
	EnumArray []RunTimeElement
	String    *string
}

func (x *RunTimeUnion) UnmarshalJSON(data []byte) error {
	x.EnumArray = nil
	object, err := unmarshalUnion(data, nil, nil, nil, &x.String, true, &x.EnumArray, false, nil, false, nil, false, nil, false)
	if err != nil {
		return err
	}
	if object {
	}
	return nil
}

func (x *RunTimeUnion) MarshalJSON() ([]byte, error) {
	return marshalUnion(nil, nil, nil, x.String, x.EnumArray != nil, x.EnumArray, false, nil, false, nil, false, nil, false)
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
