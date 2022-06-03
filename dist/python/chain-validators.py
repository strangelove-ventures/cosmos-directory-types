# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = cosmoshub_from_dict(json.loads(json_string))
#     result = juno_from_dict(json.loads(json_string))
#     result = osmosis_from_dict(json.loads(json_string))

from enum import Enum
from typing import Any, List, Union, Optional, TypeVar, Type, cast, Callable
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


class Name(Enum):
    COSMOSHUB = "cosmoshub"
    JUNO = "juno"
    OSMOSIS = "osmosis"


class CommissionRates:
    rate: str
    max_rate: str
    max_change_rate: str

    def __init__(self, rate: str, max_rate: str, max_change_rate: str) -> None:
        self.rate = rate
        self.max_rate = max_rate
        self.max_change_rate = max_change_rate

    @staticmethod
    def from_dict(obj: Any) -> 'CommissionRates':
        assert isinstance(obj, dict)
        rate = from_str(obj.get("rate"))
        max_rate = from_str(obj.get("max_rate"))
        max_change_rate = from_str(obj.get("max_change_rate"))
        return CommissionRates(rate, max_rate, max_change_rate)

    def to_dict(self) -> dict:
        result: dict = {}
        result["rate"] = from_str(self.rate)
        result["max_rate"] = from_str(self.max_rate)
        result["max_change_rate"] = from_str(self.max_change_rate)
        return result


class Commission:
    commission_rates: CommissionRates
    update_time: datetime

    def __init__(self, commission_rates: CommissionRates, update_time: datetime) -> None:
        self.commission_rates = commission_rates
        self.update_time = update_time

    @staticmethod
    def from_dict(obj: Any) -> 'Commission':
        assert isinstance(obj, dict)
        commission_rates = CommissionRates.from_dict(obj.get("commission_rates"))
        update_time = from_datetime(obj.get("update_time"))
        return Commission(commission_rates, update_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["commission_rates"] = to_class(CommissionRates, self.commission_rates)
        result["update_time"] = self.update_time.isoformat()
        return result


class TypeEnum(Enum):
    COSMOS_CRYPTO_ED25519_PUB_KEY = "/cosmos.crypto.ed25519.PubKey"


class ConsensusPubkey:
    type: TypeEnum
    key: str

    def __init__(self, type: TypeEnum, key: str) -> None:
        self.type = type
        self.key = key

    @staticmethod
    def from_dict(obj: Any) -> 'ConsensusPubkey':
        assert isinstance(obj, dict)
        type = TypeEnum(obj.get("@type"))
        key = from_str(obj.get("key"))
        return ConsensusPubkey(type, key)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = to_enum(TypeEnum, self.type)
        result["key"] = from_str(self.key)
        return result


class Description:
    moniker: str
    identity: str
    website: str
    security_contact: str
    details: str

    def __init__(self, moniker: str, identity: str, website: str, security_contact: str, details: str) -> None:
        self.moniker = moniker
        self.identity = identity
        self.website = website
        self.security_contact = security_contact
        self.details = details

    @staticmethod
    def from_dict(obj: Any) -> 'Description':
        assert isinstance(obj, dict)
        moniker = from_str(obj.get("moniker"))
        identity = from_str(obj.get("identity"))
        website = from_str(obj.get("website"))
        security_contact = from_str(obj.get("security_contact"))
        details = from_str(obj.get("details"))
        return Description(moniker, identity, website, security_contact, details)

    def to_dict(self) -> dict:
        result: dict = {}
        result["moniker"] = from_str(self.moniker)
        result["identity"] = from_str(self.identity)
        result["website"] = from_str(self.website)
        result["security_contact"] = from_str(self.security_contact)
        result["details"] = from_str(self.details)
        return result


class Restake:
    address: str
    run_time: Union[List[str], str]
    minimum_reward: int

    def __init__(self, address: str, run_time: Union[List[str], str], minimum_reward: int) -> None:
        self.address = address
        self.run_time = run_time
        self.minimum_reward = minimum_reward

    @staticmethod
    def from_dict(obj: Any) -> 'Restake':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        run_time = from_union([lambda x: from_list(from_str, x), from_str], obj.get("run_time"))
        minimum_reward = from_int(obj.get("minimum_reward"))
        return Restake(address, run_time, minimum_reward)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["run_time"] = from_union([lambda x: from_list(from_str, x), from_str], self.run_time)
        result["minimum_reward"] = from_int(self.minimum_reward)
        return result


class Status(Enum):
    BOND_STATUS_BONDED = "BOND_STATUS_BONDED"
    BOND_STATUS_UNBONDED = "BOND_STATUS_UNBONDED"
    BOND_STATUS_UNBONDING = "BOND_STATUS_UNBONDING"


class Validator:
    moniker: str
    identity: Optional[str]
    address: str
    hex_address: str
    uptime: float
    missed_blocks: int
    operator_address: str
    consensus_pubkey: ConsensusPubkey
    jailed: bool
    status: Status
    tokens: str
    delegator_shares: str
    description: Description
    unbonding_height: int
    unbonding_time: datetime
    commission: Commission
    min_self_delegation: str
    rank: int
    mintscan_image: Optional[str]
    keybase_image: Optional[str]
    name: Optional[Name]
    restake: Optional[Restake]

    def __init__(self, moniker: str, identity: Optional[str], address: str, hex_address: str, uptime: float, missed_blocks: int, operator_address: str, consensus_pubkey: ConsensusPubkey, jailed: bool, status: Status, tokens: str, delegator_shares: str, description: Description, unbonding_height: int, unbonding_time: datetime, commission: Commission, min_self_delegation: str, rank: int, mintscan_image: Optional[str], keybase_image: Optional[str], name: Optional[Name], restake: Optional[Restake]) -> None:
        self.moniker = moniker
        self.identity = identity
        self.address = address
        self.hex_address = hex_address
        self.uptime = uptime
        self.missed_blocks = missed_blocks
        self.operator_address = operator_address
        self.consensus_pubkey = consensus_pubkey
        self.jailed = jailed
        self.status = status
        self.tokens = tokens
        self.delegator_shares = delegator_shares
        self.description = description
        self.unbonding_height = unbonding_height
        self.unbonding_time = unbonding_time
        self.commission = commission
        self.min_self_delegation = min_self_delegation
        self.rank = rank
        self.mintscan_image = mintscan_image
        self.keybase_image = keybase_image
        self.name = name
        self.restake = restake

    @staticmethod
    def from_dict(obj: Any) -> 'Validator':
        assert isinstance(obj, dict)
        moniker = from_str(obj.get("moniker"))
        identity = from_union([from_str, from_none], obj.get("identity"))
        address = from_str(obj.get("address"))
        hex_address = from_str(obj.get("hexAddress"))
        uptime = from_float(obj.get("uptime"))
        missed_blocks = from_int(obj.get("missedBlocks"))
        operator_address = from_str(obj.get("operator_address"))
        consensus_pubkey = ConsensusPubkey.from_dict(obj.get("consensus_pubkey"))
        jailed = from_bool(obj.get("jailed"))
        status = Status(obj.get("status"))
        tokens = from_str(obj.get("tokens"))
        delegator_shares = from_str(obj.get("delegator_shares"))
        description = Description.from_dict(obj.get("description"))
        unbonding_height = int(from_str(obj.get("unbonding_height")))
        unbonding_time = from_datetime(obj.get("unbonding_time"))
        commission = Commission.from_dict(obj.get("commission"))
        min_self_delegation = from_str(obj.get("min_self_delegation"))
        rank = from_int(obj.get("rank"))
        mintscan_image = from_union([from_str, from_none], obj.get("mintscan_image"))
        keybase_image = from_union([from_str, from_none], obj.get("keybase_image"))
        name = from_union([Name, from_none], obj.get("name"))
        restake = from_union([Restake.from_dict, from_none], obj.get("restake"))
        return Validator(moniker, identity, address, hex_address, uptime, missed_blocks, operator_address, consensus_pubkey, jailed, status, tokens, delegator_shares, description, unbonding_height, unbonding_time, commission, min_self_delegation, rank, mintscan_image, keybase_image, name, restake)

    def to_dict(self) -> dict:
        result: dict = {}
        result["moniker"] = from_str(self.moniker)
        result["identity"] = from_union([from_str, from_none], self.identity)
        result["address"] = from_str(self.address)
        result["hexAddress"] = from_str(self.hex_address)
        result["uptime"] = to_float(self.uptime)
        result["missedBlocks"] = from_int(self.missed_blocks)
        result["operator_address"] = from_str(self.operator_address)
        result["consensus_pubkey"] = to_class(ConsensusPubkey, self.consensus_pubkey)
        result["jailed"] = from_bool(self.jailed)
        result["status"] = to_enum(Status, self.status)
        result["tokens"] = from_str(self.tokens)
        result["delegator_shares"] = from_str(self.delegator_shares)
        result["description"] = to_class(Description, self.description)
        result["unbonding_height"] = from_str(str(self.unbonding_height))
        result["unbonding_time"] = self.unbonding_time.isoformat()
        result["commission"] = to_class(Commission, self.commission)
        result["min_self_delegation"] = from_str(self.min_self_delegation)
        result["rank"] = from_int(self.rank)
        result["mintscan_image"] = from_union([from_str, from_none], self.mintscan_image)
        result["keybase_image"] = from_union([from_str, from_none], self.keybase_image)
        result["name"] = from_union([lambda x: to_enum(Name, x), from_none], self.name)
        result["restake"] = from_union([lambda x: to_class(Restake, x), from_none], self.restake)
        return result


class Osmosis:
    name: Name
    validators: List[Validator]

    def __init__(self, name: Name, validators: List[Validator]) -> None:
        self.name = name
        self.validators = validators

    @staticmethod
    def from_dict(obj: Any) -> 'Osmosis':
        assert isinstance(obj, dict)
        name = Name(obj.get("name"))
        validators = from_list(Validator.from_dict, obj.get("validators"))
        return Osmosis(name, validators)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = to_enum(Name, self.name)
        result["validators"] = from_list(lambda x: to_class(Validator, x), self.validators)
        return result


def cosmoshub_from_dict(s: Any) -> Osmosis:
    return Osmosis.from_dict(s)


def cosmoshub_to_dict(x: Osmosis) -> Any:
    return to_class(Osmosis, x)


def juno_from_dict(s: Any) -> Osmosis:
    return Osmosis.from_dict(s)


def juno_to_dict(x: Osmosis) -> Any:
    return to_class(Osmosis, x)


def osmosis_from_dict(s: Any) -> Osmosis:
    return Osmosis.from_dict(s)


def osmosis_to_dict(x: Osmosis) -> Any:
    return to_class(Osmosis, x)
