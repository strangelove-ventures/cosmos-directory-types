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
#     result = deuslabs_from_dict(json.loads(json_string))
#     result = ezstaking_from_dict(json.loads(json_string))
#     result = oni_from_dict(json.loads(json_string))

from typing import Any, Optional, List, Union, TypeVar, Type, cast, Callable
from datetime import datetime
from enum import Enum
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class Repository:
    url: str
    branch: str
    commit: str
    timestamp: int

    def __init__(self, url: str, branch: str, commit: str, timestamp: int) -> None:
        self.url = url
        self.branch = branch
        self.commit = commit
        self.timestamp = timestamp

    @staticmethod
    def from_dict(obj: Any) -> 'Repository':
        assert isinstance(obj, dict)
        url = from_str(obj.get("url"))
        branch = from_str(obj.get("branch"))
        commit = from_str(obj.get("commit"))
        timestamp = from_int(obj.get("timestamp"))
        return Repository(url, branch, commit, timestamp)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_str(self.url)
        result["branch"] = from_str(self.branch)
        result["commit"] = from_str(self.commit)
        result["timestamp"] = from_int(self.timestamp)
        return result


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


class Identity(Enum):
    ED7_CA7124_A3_F0_ED6 = "ED7CA7124A3F0ED6"
    EMPTY = ""
    THE_1534523421_A364_DB = "1534523421A364DB"
    THE_5_A8_AB49_CF5_CAAF3_C = "5A8AB49CF5CAAF3C"


class Description:
    moniker: str
    identity: Identity
    website: str
    security_contact: str
    details: str

    def __init__(self, moniker: str, identity: Identity, website: str, security_contact: str, details: str) -> None:
        self.moniker = moniker
        self.identity = identity
        self.website = website
        self.security_contact = security_contact
        self.details = details

    @staticmethod
    def from_dict(obj: Any) -> 'Description':
        assert isinstance(obj, dict)
        moniker = from_str(obj.get("moniker"))
        identity = Identity(obj.get("identity"))
        website = from_str(obj.get("website"))
        security_contact = from_str(obj.get("security_contact"))
        details = from_str(obj.get("details"))
        return Description(moniker, identity, website, security_contact, details)

    def to_dict(self) -> dict:
        result: dict = {}
        result["moniker"] = from_str(self.moniker)
        result["identity"] = to_enum(Identity, self.identity)
        result["website"] = from_str(self.website)
        result["security_contact"] = from_str(self.security_contact)
        result["details"] = from_str(self.details)
        return result


class PurpleRestake:
    address: str
    run_time: str
    minimum_reward: int

    def __init__(self, address: str, run_time: str, minimum_reward: int) -> None:
        self.address = address
        self.run_time = run_time
        self.minimum_reward = minimum_reward

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleRestake':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        run_time = from_str(obj.get("run_time"))
        minimum_reward = from_int(obj.get("minimum_reward"))
        return PurpleRestake(address, run_time, minimum_reward)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["run_time"] = from_str(self.run_time)
        result["minimum_reward"] = from_int(self.minimum_reward)
        return result


class Status(Enum):
    BOND_STATUS_BONDED = "BOND_STATUS_BONDED"


class PurpleChain:
    name: str
    address: str
    restake: PurpleRestake
    moniker: str
    identity: Optional[Identity]
    hex_address: str
    uptime: int
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
    min_self_delegation: int
    rank: int
    mintscan_image: str
    keybase_image: Optional[str]

    def __init__(self, name: str, address: str, restake: PurpleRestake, moniker: str, identity: Optional[Identity], hex_address: str, uptime: int, missed_blocks: int, operator_address: str, consensus_pubkey: ConsensusPubkey, jailed: bool, status: Status, tokens: str, delegator_shares: str, description: Description, unbonding_height: int, unbonding_time: datetime, commission: Commission, min_self_delegation: int, rank: int, mintscan_image: str, keybase_image: Optional[str]) -> None:
        self.name = name
        self.address = address
        self.restake = restake
        self.moniker = moniker
        self.identity = identity
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

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleChain':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        address = from_str(obj.get("address"))
        restake = PurpleRestake.from_dict(obj.get("restake"))
        moniker = from_str(obj.get("moniker"))
        identity = from_union([Identity, from_none], obj.get("identity"))
        hex_address = from_str(obj.get("hexAddress"))
        uptime = from_int(obj.get("uptime"))
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
        min_self_delegation = int(from_str(obj.get("min_self_delegation")))
        rank = from_int(obj.get("rank"))
        mintscan_image = from_str(obj.get("mintscan_image"))
        keybase_image = from_union([from_str, from_none], obj.get("keybase_image"))
        return PurpleChain(name, address, restake, moniker, identity, hex_address, uptime, missed_blocks, operator_address, consensus_pubkey, jailed, status, tokens, delegator_shares, description, unbonding_height, unbonding_time, commission, min_self_delegation, rank, mintscan_image, keybase_image)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["address"] = from_str(self.address)
        result["restake"] = to_class(PurpleRestake, self.restake)
        result["moniker"] = from_str(self.moniker)
        result["identity"] = from_union([lambda x: to_enum(Identity, x), from_none], self.identity)
        result["hexAddress"] = from_str(self.hex_address)
        result["uptime"] = from_int(self.uptime)
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
        result["min_self_delegation"] = from_str(str(self.min_self_delegation))
        result["rank"] = from_int(self.rank)
        result["mintscan_image"] = from_str(self.mintscan_image)
        result["keybase_image"] = from_union([from_str, from_none], self.keybase_image)
        return result


class Profile:
    name: str
    identity: Identity

    def __init__(self, name: str, identity: Identity) -> None:
        self.name = name
        self.identity = identity

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        identity = Identity(obj.get("identity"))
        return Profile(name, identity)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["identity"] = to_enum(Identity, self.identity)
        return result


class DeuslabsValidator:
    path: str
    name: str
    identity: Identity
    chains: List[PurpleChain]
    profile: Profile

    def __init__(self, path: str, name: str, identity: Identity, chains: List[PurpleChain], profile: Profile) -> None:
        self.path = path
        self.name = name
        self.identity = identity
        self.chains = chains
        self.profile = profile

    @staticmethod
    def from_dict(obj: Any) -> 'DeuslabsValidator':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        name = from_str(obj.get("name"))
        identity = Identity(obj.get("identity"))
        chains = from_list(PurpleChain.from_dict, obj.get("chains"))
        profile = Profile.from_dict(obj.get("profile"))
        return DeuslabsValidator(path, name, identity, chains, profile)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        result["name"] = from_str(self.name)
        result["identity"] = to_enum(Identity, self.identity)
        result["chains"] = from_list(lambda x: to_class(PurpleChain, x), self.chains)
        result["profile"] = to_class(Profile, self.profile)
        return result


class Oni:
    repository: Repository
    validator: DeuslabsValidator

    def __init__(self, repository: Repository, validator: DeuslabsValidator) -> None:
        self.repository = repository
        self.validator = validator

    @staticmethod
    def from_dict(obj: Any) -> 'Oni':
        assert isinstance(obj, dict)
        repository = Repository.from_dict(obj.get("repository"))
        validator = DeuslabsValidator.from_dict(obj.get("validator"))
        return Oni(repository, validator)

    def to_dict(self) -> dict:
        result: dict = {}
        result["repository"] = to_class(Repository, self.repository)
        result["validator"] = to_class(DeuslabsValidator, self.validator)
        return result


class RunTimeElement(Enum):
    THE_0000 = "00:00"
    THE_1200 = "12:00"


class FluffyRestake:
    address: str
    run_time: Union[List[RunTimeElement], str]
    minimum_reward: int

    def __init__(self, address: str, run_time: Union[List[RunTimeElement], str], minimum_reward: int) -> None:
        self.address = address
        self.run_time = run_time
        self.minimum_reward = minimum_reward

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyRestake':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        run_time = from_union([lambda x: from_list(RunTimeElement, x), from_str], obj.get("run_time"))
        minimum_reward = from_int(obj.get("minimum_reward"))
        return FluffyRestake(address, run_time, minimum_reward)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["run_time"] = from_union([lambda x: from_list(lambda x: to_enum(RunTimeElement, x), x), from_str], self.run_time)
        result["minimum_reward"] = from_int(self.minimum_reward)
        return result


class FluffyChain:
    name: str
    address: str
    restake: FluffyRestake
    moniker: str
    identity: Identity
    hex_address: str
    uptime: Optional[int]
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
    min_self_delegation: int
    rank: int
    mintscan_image: Optional[str]
    keybase_image: str

    def __init__(self, name: str, address: str, restake: FluffyRestake, moniker: str, identity: Identity, hex_address: str, uptime: Optional[int], missed_blocks: int, operator_address: str, consensus_pubkey: ConsensusPubkey, jailed: bool, status: Status, tokens: str, delegator_shares: str, description: Description, unbonding_height: int, unbonding_time: datetime, commission: Commission, min_self_delegation: int, rank: int, mintscan_image: Optional[str], keybase_image: str) -> None:
        self.name = name
        self.address = address
        self.restake = restake
        self.moniker = moniker
        self.identity = identity
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

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyChain':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        address = from_str(obj.get("address"))
        restake = FluffyRestake.from_dict(obj.get("restake"))
        moniker = from_str(obj.get("moniker"))
        identity = Identity(obj.get("identity"))
        hex_address = from_str(obj.get("hexAddress"))
        uptime = from_union([from_int, from_none], obj.get("uptime"))
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
        min_self_delegation = int(from_str(obj.get("min_self_delegation")))
        rank = from_int(obj.get("rank"))
        mintscan_image = from_union([from_str, from_none], obj.get("mintscan_image"))
        keybase_image = from_str(obj.get("keybase_image"))
        return FluffyChain(name, address, restake, moniker, identity, hex_address, uptime, missed_blocks, operator_address, consensus_pubkey, jailed, status, tokens, delegator_shares, description, unbonding_height, unbonding_time, commission, min_self_delegation, rank, mintscan_image, keybase_image)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["address"] = from_str(self.address)
        result["restake"] = to_class(FluffyRestake, self.restake)
        result["moniker"] = from_str(self.moniker)
        result["identity"] = to_enum(Identity, self.identity)
        result["hexAddress"] = from_str(self.hex_address)
        result["uptime"] = from_union([from_int, from_none], self.uptime)
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
        result["min_self_delegation"] = from_str(str(self.min_self_delegation))
        result["rank"] = from_int(self.rank)
        result["mintscan_image"] = from_union([from_str, from_none], self.mintscan_image)
        result["keybase_image"] = from_str(self.keybase_image)
        return result


class EzstakingValidator:
    path: str
    name: str
    identity: Identity
    chains: List[FluffyChain]
    profile: Profile

    def __init__(self, path: str, name: str, identity: Identity, chains: List[FluffyChain], profile: Profile) -> None:
        self.path = path
        self.name = name
        self.identity = identity
        self.chains = chains
        self.profile = profile

    @staticmethod
    def from_dict(obj: Any) -> 'EzstakingValidator':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        name = from_str(obj.get("name"))
        identity = Identity(obj.get("identity"))
        chains = from_list(FluffyChain.from_dict, obj.get("chains"))
        profile = Profile.from_dict(obj.get("profile"))
        return EzstakingValidator(path, name, identity, chains, profile)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        result["name"] = from_str(self.name)
        result["identity"] = to_enum(Identity, self.identity)
        result["chains"] = from_list(lambda x: to_class(FluffyChain, x), self.chains)
        result["profile"] = to_class(Profile, self.profile)
        return result


class Ezstaking:
    repository: Repository
    validator: EzstakingValidator

    def __init__(self, repository: Repository, validator: EzstakingValidator) -> None:
        self.repository = repository
        self.validator = validator

    @staticmethod
    def from_dict(obj: Any) -> 'Ezstaking':
        assert isinstance(obj, dict)
        repository = Repository.from_dict(obj.get("repository"))
        validator = EzstakingValidator.from_dict(obj.get("validator"))
        return Ezstaking(repository, validator)

    def to_dict(self) -> dict:
        result: dict = {}
        result["repository"] = to_class(Repository, self.repository)
        result["validator"] = to_class(EzstakingValidator, self.validator)
        return result


def deuslabs_from_dict(s: Any) -> Oni:
    return Oni.from_dict(s)


def deuslabs_to_dict(x: Oni) -> Any:
    return to_class(Oni, x)


def ezstaking_from_dict(s: Any) -> Ezstaking:
    return Ezstaking.from_dict(s)


def ezstaking_to_dict(x: Ezstaking) -> Any:
    return to_class(Ezstaking, x)


def oni_from_dict(s: Any) -> Oni:
    return Oni.from_dict(s)


def oni_to_dict(x: Oni) -> Any:
    return to_class(Oni, x)
