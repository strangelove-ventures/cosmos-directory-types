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
#     result = all_chains_data_from_dict(json.loads(json_string))
#     result = chain_data_from_dict(json.loads(json_string))
#     result = all_validators_data_from_dict(json.loads(json_string))
#     result = validator_data_from_dict(json.loads(json_string))
#     result = chain_validators_data_from_dict(json.loads(json_string))

from typing import Optional, Any, List, Union, TypeVar, Callable, Type, cast
from enum import Enum
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


class Grpc:
    address: str
    provider: Optional[str]

    def __init__(self, address: str, provider: Optional[str]) -> None:
        self.address = address
        self.provider = provider

    @staticmethod
    def from_dict(obj: Any) -> 'Grpc':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        provider = from_union([from_none, from_str], obj.get("provider"))
        return Grpc(address, provider)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["provider"] = from_union([from_none, from_str], self.provider)
        return result


class BestApis:
    rest: List[Grpc]
    rpc: List[Grpc]

    def __init__(self, rest: List[Grpc], rpc: List[Grpc]) -> None:
        self.rest = rest
        self.rpc = rpc

    @staticmethod
    def from_dict(obj: Any) -> 'BestApis':
        assert isinstance(obj, dict)
        rest = from_list(Grpc.from_dict, obj.get("rest"))
        rpc = from_list(Grpc.from_dict, obj.get("rpc"))
        return BestApis(rest, rpc)

    def to_dict(self) -> dict:
        result: dict = {}
        result["rest"] = from_list(lambda x: to_class(Grpc, x), self.rest)
        result["rpc"] = from_list(lambda x: to_class(Grpc, x), self.rpc)
        return result


class NetworkType(Enum):
    MAINNET = "mainnet"


class PurpleParams:
    actual_block_time: Optional[float]
    authz: Optional[bool]
    bonded_tokens: Optional[str]
    calculated_apr: Optional[float]
    total_supply: Optional[str]

    def __init__(self, actual_block_time: Optional[float], authz: Optional[bool], bonded_tokens: Optional[str], calculated_apr: Optional[float], total_supply: Optional[str]) -> None:
        self.actual_block_time = actual_block_time
        self.authz = authz
        self.bonded_tokens = bonded_tokens
        self.calculated_apr = calculated_apr
        self.total_supply = total_supply

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleParams':
        assert isinstance(obj, dict)
        actual_block_time = from_union([from_float, from_none], obj.get("actual_block_time"))
        authz = from_union([from_bool, from_none], obj.get("authz"))
        bonded_tokens = from_union([from_none, from_str], obj.get("bonded_tokens"))
        calculated_apr = from_union([from_float, from_none], obj.get("calculated_apr"))
        total_supply = from_union([from_none, from_str], obj.get("total_supply"))
        return PurpleParams(actual_block_time, authz, bonded_tokens, calculated_apr, total_supply)

    def to_dict(self) -> dict:
        result: dict = {}
        result["actual_block_time"] = from_union([to_float, from_none], self.actual_block_time)
        result["authz"] = from_union([from_bool, from_none], self.authz)
        result["bonded_tokens"] = from_union([from_none, from_str], self.bonded_tokens)
        result["calculated_apr"] = from_union([to_float, from_none], self.calculated_apr)
        result["total_supply"] = from_union([from_none, from_str], self.total_supply)
        return result


class PurpleStatus(Enum):
    LIVE = "live"


class AllChainsDataChain:
    best_apis: BestApis
    chain_id: str
    chain_name: str
    coingecko_id: Optional[str]
    decimals: Optional[int]
    denom: Optional[str]
    height: Optional[int]
    image: Optional[str]
    name: str
    network_type: NetworkType
    params: PurpleParams
    path: str
    pretty_name: str
    status: PurpleStatus
    symbol: Optional[str]

    def __init__(self, best_apis: BestApis, chain_id: str, chain_name: str, coingecko_id: Optional[str], decimals: Optional[int], denom: Optional[str], height: Optional[int], image: Optional[str], name: str, network_type: NetworkType, params: PurpleParams, path: str, pretty_name: str, status: PurpleStatus, symbol: Optional[str]) -> None:
        self.best_apis = best_apis
        self.chain_id = chain_id
        self.chain_name = chain_name
        self.coingecko_id = coingecko_id
        self.decimals = decimals
        self.denom = denom
        self.height = height
        self.image = image
        self.name = name
        self.network_type = network_type
        self.params = params
        self.path = path
        self.pretty_name = pretty_name
        self.status = status
        self.symbol = symbol

    @staticmethod
    def from_dict(obj: Any) -> 'AllChainsDataChain':
        assert isinstance(obj, dict)
        best_apis = BestApis.from_dict(obj.get("best_apis"))
        chain_id = from_str(obj.get("chain_id"))
        chain_name = from_str(obj.get("chain_name"))
        coingecko_id = from_union([from_none, from_str], obj.get("coingecko_id"))
        decimals = from_union([from_int, from_none], obj.get("decimals"))
        denom = from_union([from_none, from_str], obj.get("denom"))
        height = from_union([from_int, from_none], obj.get("height"))
        image = from_union([from_none, from_str], obj.get("image"))
        name = from_str(obj.get("name"))
        network_type = NetworkType(obj.get("network_type"))
        params = PurpleParams.from_dict(obj.get("params"))
        path = from_str(obj.get("path"))
        pretty_name = from_str(obj.get("pretty_name"))
        status = PurpleStatus(obj.get("status"))
        symbol = from_union([from_none, from_str], obj.get("symbol"))
        return AllChainsDataChain(best_apis, chain_id, chain_name, coingecko_id, decimals, denom, height, image, name, network_type, params, path, pretty_name, status, symbol)

    def to_dict(self) -> dict:
        result: dict = {}
        result["best_apis"] = to_class(BestApis, self.best_apis)
        result["chain_id"] = from_str(self.chain_id)
        result["chain_name"] = from_str(self.chain_name)
        result["coingecko_id"] = from_union([from_none, from_str], self.coingecko_id)
        result["decimals"] = from_union([from_int, from_none], self.decimals)
        result["denom"] = from_union([from_none, from_str], self.denom)
        result["height"] = from_union([from_int, from_none], self.height)
        result["image"] = from_union([from_none, from_str], self.image)
        result["name"] = from_str(self.name)
        result["network_type"] = to_enum(NetworkType, self.network_type)
        result["params"] = to_class(PurpleParams, self.params)
        result["path"] = from_str(self.path)
        result["pretty_name"] = from_str(self.pretty_name)
        result["status"] = to_enum(PurpleStatus, self.status)
        result["symbol"] = from_union([from_none, from_str], self.symbol)
        return result


class Repository:
    branch: str
    commit: str
    timestamp: int
    url: str

    def __init__(self, branch: str, commit: str, timestamp: int, url: str) -> None:
        self.branch = branch
        self.commit = commit
        self.timestamp = timestamp
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'Repository':
        assert isinstance(obj, dict)
        branch = from_str(obj.get("branch"))
        commit = from_str(obj.get("commit"))
        timestamp = from_int(obj.get("timestamp"))
        url = from_str(obj.get("url"))
        return Repository(branch, commit, timestamp, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["branch"] = from_str(self.branch)
        result["commit"] = from_str(self.commit)
        result["timestamp"] = from_int(self.timestamp)
        result["url"] = from_str(self.url)
        return result


class AllChainsData:
    chains: List[AllChainsDataChain]
    repository: Repository

    def __init__(self, chains: List[AllChainsDataChain], repository: Repository) -> None:
        self.chains = chains
        self.repository = repository

    @staticmethod
    def from_dict(obj: Any) -> 'AllChainsData':
        assert isinstance(obj, dict)
        chains = from_list(AllChainsDataChain.from_dict, obj.get("chains"))
        repository = Repository.from_dict(obj.get("repository"))
        return AllChainsData(chains, repository)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chains"] = from_list(lambda x: to_class(AllChainsDataChain, x), self.chains)
        result["repository"] = to_class(Repository, self.repository)
        return result


class Apis:
    grpc: List[Grpc]
    rest: List[Grpc]
    rpc: List[Grpc]

    def __init__(self, grpc: List[Grpc], rest: List[Grpc], rpc: List[Grpc]) -> None:
        self.grpc = grpc
        self.rest = rest
        self.rpc = rpc

    @staticmethod
    def from_dict(obj: Any) -> 'Apis':
        assert isinstance(obj, dict)
        grpc = from_list(Grpc.from_dict, obj.get("grpc"))
        rest = from_list(Grpc.from_dict, obj.get("rest"))
        rpc = from_list(Grpc.from_dict, obj.get("rpc"))
        return Apis(grpc, rest, rpc)

    def to_dict(self) -> dict:
        result: dict = {}
        result["grpc"] = from_list(lambda x: to_class(Grpc, x), self.grpc)
        result["rest"] = from_list(lambda x: to_class(Grpc, x), self.rest)
        result["rpc"] = from_list(lambda x: to_class(Grpc, x), self.rpc)
        return result


class Binaries:
    darwin_amd64: Optional[str]
    linux_amd64: str
    linux_arm64: str
    windows_amd64: Optional[str]

    def __init__(self, darwin_amd64: Optional[str], linux_amd64: str, linux_arm64: str, windows_amd64: Optional[str]) -> None:
        self.darwin_amd64 = darwin_amd64
        self.linux_amd64 = linux_amd64
        self.linux_arm64 = linux_arm64
        self.windows_amd64 = windows_amd64

    @staticmethod
    def from_dict(obj: Any) -> 'Binaries':
        assert isinstance(obj, dict)
        darwin_amd64 = from_union([from_none, from_str], obj.get("darwin/amd64"))
        linux_amd64 = from_str(obj.get("linux/amd64"))
        linux_arm64 = from_str(obj.get("linux/arm64"))
        windows_amd64 = from_union([from_none, from_str], obj.get("windows/amd64"))
        return Binaries(darwin_amd64, linux_amd64, linux_arm64, windows_amd64)

    def to_dict(self) -> dict:
        result: dict = {}
        result["darwin/amd64"] = from_union([from_none, from_str], self.darwin_amd64)
        result["linux/amd64"] = from_str(self.linux_amd64)
        result["linux/arm64"] = from_str(self.linux_arm64)
        result["windows/amd64"] = from_union([from_none, from_str], self.windows_amd64)
        return result


class Codebase:
    binaries: Optional[Binaries]
    compatible_versions: List[str]
    cosmos_sdk_version: Optional[str]
    git_repo: str
    recommended_version: str
    tendermint_version: Optional[str]

    def __init__(self, binaries: Optional[Binaries], compatible_versions: List[str], cosmos_sdk_version: Optional[str], git_repo: str, recommended_version: str, tendermint_version: Optional[str]) -> None:
        self.binaries = binaries
        self.compatible_versions = compatible_versions
        self.cosmos_sdk_version = cosmos_sdk_version
        self.git_repo = git_repo
        self.recommended_version = recommended_version
        self.tendermint_version = tendermint_version

    @staticmethod
    def from_dict(obj: Any) -> 'Codebase':
        assert isinstance(obj, dict)
        binaries = from_union([Binaries.from_dict, from_none], obj.get("binaries"))
        compatible_versions = from_list(from_str, obj.get("compatible_versions"))
        cosmos_sdk_version = from_union([from_none, from_str], obj.get("cosmos_sdk_version"))
        git_repo = from_str(obj.get("git_repo"))
        recommended_version = from_str(obj.get("recommended_version"))
        tendermint_version = from_union([from_none, from_str], obj.get("tendermint_version"))
        return Codebase(binaries, compatible_versions, cosmos_sdk_version, git_repo, recommended_version, tendermint_version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["binaries"] = from_union([lambda x: to_class(Binaries, x), from_none], self.binaries)
        result["compatible_versions"] = from_list(from_str, self.compatible_versions)
        result["cosmos_sdk_version"] = from_union([from_none, from_str], self.cosmos_sdk_version)
        result["git_repo"] = from_str(self.git_repo)
        result["recommended_version"] = from_str(self.recommended_version)
        result["tendermint_version"] = from_union([from_none, from_str], self.tendermint_version)
        return result


class Explorer:
    account_page: Optional[str]
    kind: str
    tx_page: str
    url: str

    def __init__(self, account_page: Optional[str], kind: str, tx_page: str, url: str) -> None:
        self.account_page = account_page
        self.kind = kind
        self.tx_page = tx_page
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'Explorer':
        assert isinstance(obj, dict)
        account_page = from_union([from_none, from_str], obj.get("account_page"))
        kind = from_str(obj.get("kind"))
        tx_page = from_str(obj.get("tx_page"))
        url = from_str(obj.get("url"))
        return Explorer(account_page, kind, tx_page, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["account_page"] = from_union([from_none, from_str], self.account_page)
        result["kind"] = from_str(self.kind)
        result["tx_page"] = from_str(self.tx_page)
        result["url"] = from_str(self.url)
        return result


class FeeToken:
    average_gas_price: Optional[float]
    denom: str
    fixed_min_gas_price: int
    high_gas_price: Optional[float]
    low_gas_price: Optional[int]

    def __init__(self, average_gas_price: Optional[float], denom: str, fixed_min_gas_price: int, high_gas_price: Optional[float], low_gas_price: Optional[int]) -> None:
        self.average_gas_price = average_gas_price
        self.denom = denom
        self.fixed_min_gas_price = fixed_min_gas_price
        self.high_gas_price = high_gas_price
        self.low_gas_price = low_gas_price

    @staticmethod
    def from_dict(obj: Any) -> 'FeeToken':
        assert isinstance(obj, dict)
        average_gas_price = from_union([from_float, from_none], obj.get("average_gas_price"))
        denom = from_str(obj.get("denom"))
        fixed_min_gas_price = from_int(obj.get("fixed_min_gas_price"))
        high_gas_price = from_union([from_float, from_none], obj.get("high_gas_price"))
        low_gas_price = from_union([from_int, from_none], obj.get("low_gas_price"))
        return FeeToken(average_gas_price, denom, fixed_min_gas_price, high_gas_price, low_gas_price)

    def to_dict(self) -> dict:
        result: dict = {}
        result["average_gas_price"] = from_union([to_float, from_none], self.average_gas_price)
        result["denom"] = from_str(self.denom)
        result["fixed_min_gas_price"] = from_int(self.fixed_min_gas_price)
        result["high_gas_price"] = from_union([to_float, from_none], self.high_gas_price)
        result["low_gas_price"] = from_union([from_int, from_none], self.low_gas_price)
        return result


class Fees:
    fee_tokens: List[FeeToken]

    def __init__(self, fee_tokens: List[FeeToken]) -> None:
        self.fee_tokens = fee_tokens

    @staticmethod
    def from_dict(obj: Any) -> 'Fees':
        assert isinstance(obj, dict)
        fee_tokens = from_list(FeeToken.from_dict, obj.get("fee_tokens"))
        return Fees(fee_tokens)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fee_tokens"] = from_list(lambda x: to_class(FeeToken, x), self.fee_tokens)
        return result


class Genesis:
    genesis_url: str

    def __init__(self, genesis_url: str) -> None:
        self.genesis_url = genesis_url

    @staticmethod
    def from_dict(obj: Any) -> 'Genesis':
        assert isinstance(obj, dict)
        genesis_url = from_str(obj.get("genesis_url"))
        return Genesis(genesis_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["genesis_url"] = from_str(self.genesis_url)
        return result


class LogoURIs:
    png: str

    def __init__(self, png: str) -> None:
        self.png = png

    @staticmethod
    def from_dict(obj: Any) -> 'LogoURIs':
        assert isinstance(obj, dict)
        png = from_str(obj.get("png"))
        return LogoURIs(png)

    def to_dict(self) -> dict:
        result: dict = {}
        result["png"] = from_str(self.png)
        return result


class FluffyParams:
    actual_block_time: float
    actual_blocks_per_year: float
    annual_provision: str
    authz: bool
    base_inflation: float
    block_time: Optional[float]
    blocks_per_year: Optional[int]
    bonded_ratio: float
    bonded_tokens: str
    calculated_apr: float
    community_tax: float
    epoch_duration: Optional[int]
    estimated_apr: float
    max_validators: int
    minting_epoch_provision: Optional[float]
    total_supply: str
    unbonding_time: int
    year_minting_provision: Optional[int]

    def __init__(self, actual_block_time: float, actual_blocks_per_year: float, annual_provision: str, authz: bool, base_inflation: float, block_time: Optional[float], blocks_per_year: Optional[int], bonded_ratio: float, bonded_tokens: str, calculated_apr: float, community_tax: float, epoch_duration: Optional[int], estimated_apr: float, max_validators: int, minting_epoch_provision: Optional[float], total_supply: str, unbonding_time: int, year_minting_provision: Optional[int]) -> None:
        self.actual_block_time = actual_block_time
        self.actual_blocks_per_year = actual_blocks_per_year
        self.annual_provision = annual_provision
        self.authz = authz
        self.base_inflation = base_inflation
        self.block_time = block_time
        self.blocks_per_year = blocks_per_year
        self.bonded_ratio = bonded_ratio
        self.bonded_tokens = bonded_tokens
        self.calculated_apr = calculated_apr
        self.community_tax = community_tax
        self.epoch_duration = epoch_duration
        self.estimated_apr = estimated_apr
        self.max_validators = max_validators
        self.minting_epoch_provision = minting_epoch_provision
        self.total_supply = total_supply
        self.unbonding_time = unbonding_time
        self.year_minting_provision = year_minting_provision

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyParams':
        assert isinstance(obj, dict)
        actual_block_time = from_float(obj.get("actual_block_time"))
        actual_blocks_per_year = from_float(obj.get("actual_blocks_per_year"))
        annual_provision = from_str(obj.get("annual_provision"))
        authz = from_bool(obj.get("authz"))
        base_inflation = from_float(obj.get("base_inflation"))
        block_time = from_union([from_float, from_none], obj.get("block_time"))
        blocks_per_year = from_union([from_int, from_none], obj.get("blocks_per_year"))
        bonded_ratio = from_float(obj.get("bonded_ratio"))
        bonded_tokens = from_str(obj.get("bonded_tokens"))
        calculated_apr = from_float(obj.get("calculated_apr"))
        community_tax = from_float(obj.get("community_tax"))
        epoch_duration = from_union([from_int, from_none], obj.get("epoch_duration"))
        estimated_apr = from_float(obj.get("estimated_apr"))
        max_validators = from_int(obj.get("max_validators"))
        minting_epoch_provision = from_union([from_float, from_none], obj.get("minting_epoch_provision"))
        total_supply = from_str(obj.get("total_supply"))
        unbonding_time = from_int(obj.get("unbonding_time"))
        year_minting_provision = from_union([from_int, from_none], obj.get("year_minting_provision"))
        return FluffyParams(actual_block_time, actual_blocks_per_year, annual_provision, authz, base_inflation, block_time, blocks_per_year, bonded_ratio, bonded_tokens, calculated_apr, community_tax, epoch_duration, estimated_apr, max_validators, minting_epoch_provision, total_supply, unbonding_time, year_minting_provision)

    def to_dict(self) -> dict:
        result: dict = {}
        result["actual_block_time"] = to_float(self.actual_block_time)
        result["actual_blocks_per_year"] = to_float(self.actual_blocks_per_year)
        result["annual_provision"] = from_str(self.annual_provision)
        result["authz"] = from_bool(self.authz)
        result["base_inflation"] = to_float(self.base_inflation)
        result["block_time"] = from_union([to_float, from_none], self.block_time)
        result["blocks_per_year"] = from_union([from_int, from_none], self.blocks_per_year)
        result["bonded_ratio"] = to_float(self.bonded_ratio)
        result["bonded_tokens"] = from_str(self.bonded_tokens)
        result["calculated_apr"] = to_float(self.calculated_apr)
        result["community_tax"] = to_float(self.community_tax)
        result["epoch_duration"] = from_union([from_int, from_none], self.epoch_duration)
        result["estimated_apr"] = to_float(self.estimated_apr)
        result["max_validators"] = from_int(self.max_validators)
        result["minting_epoch_provision"] = from_union([to_float, from_none], self.minting_epoch_provision)
        result["total_supply"] = from_str(self.total_supply)
        result["unbonding_time"] = from_int(self.unbonding_time)
        result["year_minting_provision"] = from_union([from_int, from_none], self.year_minting_provision)
        return result


class PersistentPeer:
    address: str
    id: str
    provider: Optional[str]

    def __init__(self, address: str, id: str, provider: Optional[str]) -> None:
        self.address = address
        self.id = id
        self.provider = provider

    @staticmethod
    def from_dict(obj: Any) -> 'PersistentPeer':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        id = from_str(obj.get("id"))
        provider = from_union([from_none, from_str], obj.get("provider"))
        return PersistentPeer(address, id, provider)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["id"] = from_str(self.id)
        result["provider"] = from_union([from_none, from_str], self.provider)
        return result


class Peers:
    persistent_peers: List[PersistentPeer]
    seeds: List[PersistentPeer]

    def __init__(self, persistent_peers: List[PersistentPeer], seeds: List[PersistentPeer]) -> None:
        self.persistent_peers = persistent_peers
        self.seeds = seeds

    @staticmethod
    def from_dict(obj: Any) -> 'Peers':
        assert isinstance(obj, dict)
        persistent_peers = from_list(PersistentPeer.from_dict, obj.get("persistent_peers"))
        seeds = from_list(PersistentPeer.from_dict, obj.get("seeds"))
        return Peers(persistent_peers, seeds)

    def to_dict(self) -> dict:
        result: dict = {}
        result["persistent_peers"] = from_list(lambda x: to_class(PersistentPeer, x), self.persistent_peers)
        result["seeds"] = from_list(lambda x: to_class(PersistentPeer, x), self.seeds)
        return result


class ChainDataChain:
    apis: Apis
    bech32_prefix: str
    best_apis: BestApis
    chain_id: str
    chain_name: str
    codebase: Codebase
    coingecko_id: str
    daemon_name: str
    decimals: int
    denom: str
    explorers: List[Explorer]
    fees: Optional[Fees]
    genesis: Genesis
    height: int
    image: str
    key_algos: List[str]
    logo_ur_is: Optional[LogoURIs]
    name: str
    network_type: NetworkType
    node_home: str
    params: FluffyParams
    path: str
    peers: Peers
    pretty_name: str
    schema: str
    slip44: int
    status: PurpleStatus
    symbol: str
    updatelink: Optional[str]

    def __init__(self, apis: Apis, bech32_prefix: str, best_apis: BestApis, chain_id: str, chain_name: str, codebase: Codebase, coingecko_id: str, daemon_name: str, decimals: int, denom: str, explorers: List[Explorer], fees: Optional[Fees], genesis: Genesis, height: int, image: str, key_algos: List[str], logo_ur_is: Optional[LogoURIs], name: str, network_type: NetworkType, node_home: str, params: FluffyParams, path: str, peers: Peers, pretty_name: str, schema: str, slip44: int, status: PurpleStatus, symbol: str, updatelink: Optional[str]) -> None:
        self.apis = apis
        self.bech32_prefix = bech32_prefix
        self.best_apis = best_apis
        self.chain_id = chain_id
        self.chain_name = chain_name
        self.codebase = codebase
        self.coingecko_id = coingecko_id
        self.daemon_name = daemon_name
        self.decimals = decimals
        self.denom = denom
        self.explorers = explorers
        self.fees = fees
        self.genesis = genesis
        self.height = height
        self.image = image
        self.key_algos = key_algos
        self.logo_ur_is = logo_ur_is
        self.name = name
        self.network_type = network_type
        self.node_home = node_home
        self.params = params
        self.path = path
        self.peers = peers
        self.pretty_name = pretty_name
        self.schema = schema
        self.slip44 = slip44
        self.status = status
        self.symbol = symbol
        self.updatelink = updatelink

    @staticmethod
    def from_dict(obj: Any) -> 'ChainDataChain':
        assert isinstance(obj, dict)
        apis = Apis.from_dict(obj.get("apis"))
        bech32_prefix = from_str(obj.get("bech32_prefix"))
        best_apis = BestApis.from_dict(obj.get("best_apis"))
        chain_id = from_str(obj.get("chain_id"))
        chain_name = from_str(obj.get("chain_name"))
        codebase = Codebase.from_dict(obj.get("codebase"))
        coingecko_id = from_str(obj.get("coingecko_id"))
        daemon_name = from_str(obj.get("daemon_name"))
        decimals = from_int(obj.get("decimals"))
        denom = from_str(obj.get("denom"))
        explorers = from_list(Explorer.from_dict, obj.get("explorers"))
        fees = from_union([Fees.from_dict, from_none], obj.get("fees"))
        genesis = Genesis.from_dict(obj.get("genesis"))
        height = from_int(obj.get("height"))
        image = from_str(obj.get("image"))
        key_algos = from_list(from_str, obj.get("key_algos"))
        logo_ur_is = from_union([LogoURIs.from_dict, from_none], obj.get("logo_URIs"))
        name = from_str(obj.get("name"))
        network_type = NetworkType(obj.get("network_type"))
        node_home = from_str(obj.get("node_home"))
        params = FluffyParams.from_dict(obj.get("params"))
        path = from_str(obj.get("path"))
        peers = Peers.from_dict(obj.get("peers"))
        pretty_name = from_str(obj.get("pretty_name"))
        schema = from_str(obj.get("$schema"))
        slip44 = from_int(obj.get("slip44"))
        status = PurpleStatus(obj.get("status"))
        symbol = from_str(obj.get("symbol"))
        updatelink = from_union([from_none, from_str], obj.get("updatelink"))
        return ChainDataChain(apis, bech32_prefix, best_apis, chain_id, chain_name, codebase, coingecko_id, daemon_name, decimals, denom, explorers, fees, genesis, height, image, key_algos, logo_ur_is, name, network_type, node_home, params, path, peers, pretty_name, schema, slip44, status, symbol, updatelink)

    def to_dict(self) -> dict:
        result: dict = {}
        result["apis"] = to_class(Apis, self.apis)
        result["bech32_prefix"] = from_str(self.bech32_prefix)
        result["best_apis"] = to_class(BestApis, self.best_apis)
        result["chain_id"] = from_str(self.chain_id)
        result["chain_name"] = from_str(self.chain_name)
        result["codebase"] = to_class(Codebase, self.codebase)
        result["coingecko_id"] = from_str(self.coingecko_id)
        result["daemon_name"] = from_str(self.daemon_name)
        result["decimals"] = from_int(self.decimals)
        result["denom"] = from_str(self.denom)
        result["explorers"] = from_list(lambda x: to_class(Explorer, x), self.explorers)
        result["fees"] = from_union([lambda x: to_class(Fees, x), from_none], self.fees)
        result["genesis"] = to_class(Genesis, self.genesis)
        result["height"] = from_int(self.height)
        result["image"] = from_str(self.image)
        result["key_algos"] = from_list(from_str, self.key_algos)
        result["logo_URIs"] = from_union([lambda x: to_class(LogoURIs, x), from_none], self.logo_ur_is)
        result["name"] = from_str(self.name)
        result["network_type"] = to_enum(NetworkType, self.network_type)
        result["node_home"] = from_str(self.node_home)
        result["params"] = to_class(FluffyParams, self.params)
        result["path"] = from_str(self.path)
        result["peers"] = to_class(Peers, self.peers)
        result["pretty_name"] = from_str(self.pretty_name)
        result["$schema"] = from_str(self.schema)
        result["slip44"] = from_int(self.slip44)
        result["status"] = to_enum(PurpleStatus, self.status)
        result["symbol"] = from_str(self.symbol)
        result["updatelink"] = from_union([from_none, from_str], self.updatelink)
        return result


class ChainData:
    chain: ChainDataChain
    repository: Repository

    def __init__(self, chain: ChainDataChain, repository: Repository) -> None:
        self.chain = chain
        self.repository = repository

    @staticmethod
    def from_dict(obj: Any) -> 'ChainData':
        assert isinstance(obj, dict)
        chain = ChainDataChain.from_dict(obj.get("chain"))
        repository = Repository.from_dict(obj.get("repository"))
        return ChainData(chain, repository)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chain"] = to_class(ChainDataChain, self.chain)
        result["repository"] = to_class(Repository, self.repository)
        return result


class ValidatorChain:
    address: str
    name: str
    restake: Union[bool, str]

    def __init__(self, address: str, name: str, restake: Union[bool, str]) -> None:
        self.address = address
        self.name = name
        self.restake = restake

    @staticmethod
    def from_dict(obj: Any) -> 'ValidatorChain':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        name = from_str(obj.get("name"))
        restake = from_union([from_bool, from_str], obj.get("restake"))
        return ValidatorChain(address, name, restake)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["name"] = from_str(self.name)
        result["restake"] = from_union([from_bool, from_str], self.restake)
        return result


class Schema(Enum):
    PROFILE_SCHEMA_JSON = "../profile.schema.json"


class ChainProfile:
    apps: Optional[List[str]]
    identity: str
    name: str
    schema: Optional[Schema]
    twitter: Optional[str]
    website: Optional[str]

    def __init__(self, apps: Optional[List[str]], identity: str, name: str, schema: Optional[Schema], twitter: Optional[str], website: Optional[str]) -> None:
        self.apps = apps
        self.identity = identity
        self.name = name
        self.schema = schema
        self.twitter = twitter
        self.website = website

    @staticmethod
    def from_dict(obj: Any) -> 'ChainProfile':
        assert isinstance(obj, dict)
        apps = from_union([lambda x: from_list(from_str, x), from_none], obj.get("apps"))
        identity = from_str(obj.get("identity"))
        name = from_str(obj.get("name"))
        schema = from_union([Schema, from_none], obj.get("$schema"))
        twitter = from_union([from_none, from_str], obj.get("twitter"))
        website = from_union([from_none, from_str], obj.get("website"))
        return ChainProfile(apps, identity, name, schema, twitter, website)

    def to_dict(self) -> dict:
        result: dict = {}
        result["apps"] = from_union([lambda x: from_list(from_str, x), from_none], self.apps)
        result["identity"] = from_str(self.identity)
        result["name"] = from_str(self.name)
        result["$schema"] = from_union([lambda x: to_enum(Schema, x), from_none], self.schema)
        result["twitter"] = from_union([from_none, from_str], self.twitter)
        result["website"] = from_union([from_none, from_str], self.website)
        return result


class AllValidatorsDataValidator:
    chains: List[ValidatorChain]
    identity: str
    name: str
    path: str
    profile: ChainProfile

    def __init__(self, chains: List[ValidatorChain], identity: str, name: str, path: str, profile: ChainProfile) -> None:
        self.chains = chains
        self.identity = identity
        self.name = name
        self.path = path
        self.profile = profile

    @staticmethod
    def from_dict(obj: Any) -> 'AllValidatorsDataValidator':
        assert isinstance(obj, dict)
        chains = from_list(ValidatorChain.from_dict, obj.get("chains"))
        identity = from_str(obj.get("identity"))
        name = from_str(obj.get("name"))
        path = from_str(obj.get("path"))
        profile = ChainProfile.from_dict(obj.get("profile"))
        return AllValidatorsDataValidator(chains, identity, name, path, profile)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chains"] = from_list(lambda x: to_class(ValidatorChain, x), self.chains)
        result["identity"] = from_str(self.identity)
        result["name"] = from_str(self.name)
        result["path"] = from_str(self.path)
        result["profile"] = to_class(ChainProfile, self.profile)
        return result


class AllValidatorsData:
    repository: Repository
    validators: List[AllValidatorsDataValidator]

    def __init__(self, repository: Repository, validators: List[AllValidatorsDataValidator]) -> None:
        self.repository = repository
        self.validators = validators

    @staticmethod
    def from_dict(obj: Any) -> 'AllValidatorsData':
        assert isinstance(obj, dict)
        repository = Repository.from_dict(obj.get("repository"))
        validators = from_list(AllValidatorsDataValidator.from_dict, obj.get("validators"))
        return AllValidatorsData(repository, validators)

    def to_dict(self) -> dict:
        result: dict = {}
        result["repository"] = to_class(Repository, self.repository)
        result["validators"] = from_list(lambda x: to_class(AllValidatorsDataValidator, x), self.validators)
        return result


class CommissionRates:
    max_change_rate: str
    max_rate: str
    rate: str

    def __init__(self, max_change_rate: str, max_rate: str, rate: str) -> None:
        self.max_change_rate = max_change_rate
        self.max_rate = max_rate
        self.rate = rate

    @staticmethod
    def from_dict(obj: Any) -> 'CommissionRates':
        assert isinstance(obj, dict)
        max_change_rate = from_str(obj.get("max_change_rate"))
        max_rate = from_str(obj.get("max_rate"))
        rate = from_str(obj.get("rate"))
        return CommissionRates(max_change_rate, max_rate, rate)

    def to_dict(self) -> dict:
        result: dict = {}
        result["max_change_rate"] = from_str(self.max_change_rate)
        result["max_rate"] = from_str(self.max_rate)
        result["rate"] = from_str(self.rate)
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
    key: str
    type: TypeEnum

    def __init__(self, key: str, type: TypeEnum) -> None:
        self.key = key
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'ConsensusPubkey':
        assert isinstance(obj, dict)
        key = from_str(obj.get("key"))
        type = TypeEnum(obj.get("@type"))
        return ConsensusPubkey(key, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["key"] = from_str(self.key)
        result["@type"] = to_enum(TypeEnum, self.type)
        return result


class Description:
    details: str
    identity: str
    moniker: str
    security_contact: str
    website: str

    def __init__(self, details: str, identity: str, moniker: str, security_contact: str, website: str) -> None:
        self.details = details
        self.identity = identity
        self.moniker = moniker
        self.security_contact = security_contact
        self.website = website

    @staticmethod
    def from_dict(obj: Any) -> 'Description':
        assert isinstance(obj, dict)
        details = from_str(obj.get("details"))
        identity = from_str(obj.get("identity"))
        moniker = from_str(obj.get("moniker"))
        security_contact = from_str(obj.get("security_contact"))
        website = from_str(obj.get("website"))
        return Description(details, identity, moniker, security_contact, website)

    def to_dict(self) -> dict:
        result: dict = {}
        result["details"] = from_str(self.details)
        result["identity"] = from_str(self.identity)
        result["moniker"] = from_str(self.moniker)
        result["security_contact"] = from_str(self.security_contact)
        result["website"] = from_str(self.website)
        return result


class RestakeClass:
    address: str
    minimum_reward: float
    run_time: Union[List[str], str]

    def __init__(self, address: str, minimum_reward: float, run_time: Union[List[str], str]) -> None:
        self.address = address
        self.minimum_reward = minimum_reward
        self.run_time = run_time

    @staticmethod
    def from_dict(obj: Any) -> 'RestakeClass':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        minimum_reward = from_float(obj.get("minimum_reward"))
        run_time = from_union([lambda x: from_list(from_str, x), from_str], obj.get("run_time"))
        return RestakeClass(address, minimum_reward, run_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["minimum_reward"] = to_float(self.minimum_reward)
        result["run_time"] = from_union([lambda x: from_list(from_str, x), from_str], self.run_time)
        return result


class ValidatorStatus(Enum):
    BOND_STATUS_BONDED = "BOND_STATUS_BONDED"
    BOND_STATUS_UNBONDED = "BOND_STATUS_UNBONDED"
    BOND_STATUS_UNBONDING = "BOND_STATUS_UNBONDING"


class ChainElement:
    address: str
    commission: Optional[Commission]
    consensus_pubkey: Optional[ConsensusPubkey]
    delegator_shares: Optional[str]
    description: Optional[Description]
    hex_address: Optional[str]
    identity: Optional[str]
    jailed: Optional[bool]
    keybase_image: Optional[str]
    min_self_delegation: Optional[str]
    mintscan_image: Optional[str]
    missed_blocks: Optional[int]
    moniker: Optional[str]
    name: Optional[str]
    operator_address: Optional[str]
    path: Optional[str]
    profile: Optional[ChainProfile]
    rank: Optional[int]
    restake: Optional[RestakeClass]
    status: Optional[ValidatorStatus]
    tokens: Optional[str]
    unbonding_height: Optional[int]
    unbonding_time: Optional[datetime]
    uptime: Optional[float]

    def __init__(self, address: str, commission: Optional[Commission], consensus_pubkey: Optional[ConsensusPubkey], delegator_shares: Optional[str], description: Optional[Description], hex_address: Optional[str], identity: Optional[str], jailed: Optional[bool], keybase_image: Optional[str], min_self_delegation: Optional[str], mintscan_image: Optional[str], missed_blocks: Optional[int], moniker: Optional[str], name: Optional[str], operator_address: Optional[str], path: Optional[str], profile: Optional[ChainProfile], rank: Optional[int], restake: Optional[RestakeClass], status: Optional[ValidatorStatus], tokens: Optional[str], unbonding_height: Optional[int], unbonding_time: Optional[datetime], uptime: Optional[float]) -> None:
        self.address = address
        self.commission = commission
        self.consensus_pubkey = consensus_pubkey
        self.delegator_shares = delegator_shares
        self.description = description
        self.hex_address = hex_address
        self.identity = identity
        self.jailed = jailed
        self.keybase_image = keybase_image
        self.min_self_delegation = min_self_delegation
        self.mintscan_image = mintscan_image
        self.missed_blocks = missed_blocks
        self.moniker = moniker
        self.name = name
        self.operator_address = operator_address
        self.path = path
        self.profile = profile
        self.rank = rank
        self.restake = restake
        self.status = status
        self.tokens = tokens
        self.unbonding_height = unbonding_height
        self.unbonding_time = unbonding_time
        self.uptime = uptime

    @staticmethod
    def from_dict(obj: Any) -> 'ChainElement':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        commission = from_union([Commission.from_dict, from_none], obj.get("commission"))
        consensus_pubkey = from_union([ConsensusPubkey.from_dict, from_none], obj.get("consensus_pubkey"))
        delegator_shares = from_union([from_none, from_str], obj.get("delegator_shares"))
        description = from_union([Description.from_dict, from_none], obj.get("description"))
        hex_address = from_union([from_none, from_str], obj.get("hexAddress"))
        identity = from_union([from_none, from_str], obj.get("identity"))
        jailed = from_union([from_bool, from_none], obj.get("jailed"))
        keybase_image = from_union([from_none, from_str], obj.get("keybase_image"))
        min_self_delegation = from_union([from_none, from_str], obj.get("min_self_delegation"))
        mintscan_image = from_union([from_none, from_str], obj.get("mintscan_image"))
        missed_blocks = from_union([from_int, from_none], obj.get("missedBlocks"))
        moniker = from_union([from_none, from_str], obj.get("moniker"))
        name = from_union([from_none, from_str], obj.get("name"))
        operator_address = from_union([from_none, from_str], obj.get("operator_address"))
        path = from_union([from_none, from_str], obj.get("path"))
        profile = from_union([ChainProfile.from_dict, from_none], obj.get("profile"))
        rank = from_union([from_int, from_none], obj.get("rank"))
        restake = from_union([RestakeClass.from_dict, from_none], obj.get("restake"))
        status = from_union([ValidatorStatus, from_none], obj.get("status"))
        tokens = from_union([from_none, from_str], obj.get("tokens"))
        unbonding_height = from_union([from_none, lambda x: int(from_str(x))], obj.get("unbonding_height"))
        unbonding_time = from_union([from_datetime, from_none], obj.get("unbonding_time"))
        uptime = from_union([from_float, from_none], obj.get("uptime"))
        return ChainElement(address, commission, consensus_pubkey, delegator_shares, description, hex_address, identity, jailed, keybase_image, min_self_delegation, mintscan_image, missed_blocks, moniker, name, operator_address, path, profile, rank, restake, status, tokens, unbonding_height, unbonding_time, uptime)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["commission"] = from_union([lambda x: to_class(Commission, x), from_none], self.commission)
        result["consensus_pubkey"] = from_union([lambda x: to_class(ConsensusPubkey, x), from_none], self.consensus_pubkey)
        result["delegator_shares"] = from_union([from_none, from_str], self.delegator_shares)
        result["description"] = from_union([lambda x: to_class(Description, x), from_none], self.description)
        result["hexAddress"] = from_union([from_none, from_str], self.hex_address)
        result["identity"] = from_union([from_none, from_str], self.identity)
        result["jailed"] = from_union([from_bool, from_none], self.jailed)
        result["keybase_image"] = from_union([from_none, from_str], self.keybase_image)
        result["min_self_delegation"] = from_union([from_none, from_str], self.min_self_delegation)
        result["mintscan_image"] = from_union([from_none, from_str], self.mintscan_image)
        result["missedBlocks"] = from_union([from_int, from_none], self.missed_blocks)
        result["moniker"] = from_union([from_none, from_str], self.moniker)
        result["name"] = from_union([from_none, from_str], self.name)
        result["operator_address"] = from_union([from_none, from_str], self.operator_address)
        result["path"] = from_union([from_none, from_str], self.path)
        result["profile"] = from_union([lambda x: to_class(ChainProfile, x), from_none], self.profile)
        result["rank"] = from_union([from_int, from_none], self.rank)
        result["restake"] = from_union([lambda x: to_class(RestakeClass, x), from_none], self.restake)
        result["status"] = from_union([lambda x: to_enum(ValidatorStatus, x), from_none], self.status)
        result["tokens"] = from_union([from_none, from_str], self.tokens)
        result["unbonding_height"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.unbonding_height)
        result["unbonding_time"] = from_union([lambda x: x.isoformat(), from_none], self.unbonding_time)
        result["uptime"] = from_union([to_float, from_none], self.uptime)
        return result


class PurpleProfile:
    identity: str
    name: str
    schema: Schema

    def __init__(self, identity: str, name: str, schema: Schema) -> None:
        self.identity = identity
        self.name = name
        self.schema = schema

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleProfile':
        assert isinstance(obj, dict)
        identity = from_str(obj.get("identity"))
        name = from_str(obj.get("name"))
        schema = Schema(obj.get("$schema"))
        return PurpleProfile(identity, name, schema)

    def to_dict(self) -> dict:
        result: dict = {}
        result["identity"] = from_str(self.identity)
        result["name"] = from_str(self.name)
        result["$schema"] = to_enum(Schema, self.schema)
        return result


class ValidatorDataValidator:
    chains: List[ChainElement]
    identity: str
    name: str
    path: str
    profile: PurpleProfile

    def __init__(self, chains: List[ChainElement], identity: str, name: str, path: str, profile: PurpleProfile) -> None:
        self.chains = chains
        self.identity = identity
        self.name = name
        self.path = path
        self.profile = profile

    @staticmethod
    def from_dict(obj: Any) -> 'ValidatorDataValidator':
        assert isinstance(obj, dict)
        chains = from_list(ChainElement.from_dict, obj.get("chains"))
        identity = from_str(obj.get("identity"))
        name = from_str(obj.get("name"))
        path = from_str(obj.get("path"))
        profile = PurpleProfile.from_dict(obj.get("profile"))
        return ValidatorDataValidator(chains, identity, name, path, profile)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chains"] = from_list(lambda x: to_class(ChainElement, x), self.chains)
        result["identity"] = from_str(self.identity)
        result["name"] = from_str(self.name)
        result["path"] = from_str(self.path)
        result["profile"] = to_class(PurpleProfile, self.profile)
        return result


class ValidatorData:
    repository: Repository
    validator: ValidatorDataValidator

    def __init__(self, repository: Repository, validator: ValidatorDataValidator) -> None:
        self.repository = repository
        self.validator = validator

    @staticmethod
    def from_dict(obj: Any) -> 'ValidatorData':
        assert isinstance(obj, dict)
        repository = Repository.from_dict(obj.get("repository"))
        validator = ValidatorDataValidator.from_dict(obj.get("validator"))
        return ValidatorData(repository, validator)

    def to_dict(self) -> dict:
        result: dict = {}
        result["repository"] = to_class(Repository, self.repository)
        result["validator"] = to_class(ValidatorDataValidator, self.validator)
        return result


class ChainValidatorsData:
    name: str
    validators: List[ChainElement]

    def __init__(self, name: str, validators: List[ChainElement]) -> None:
        self.name = name
        self.validators = validators

    @staticmethod
    def from_dict(obj: Any) -> 'ChainValidatorsData':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        validators = from_list(ChainElement.from_dict, obj.get("validators"))
        return ChainValidatorsData(name, validators)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["validators"] = from_list(lambda x: to_class(ChainElement, x), self.validators)
        return result


def all_chains_data_from_dict(s: Any) -> AllChainsData:
    return AllChainsData.from_dict(s)


def all_chains_data_to_dict(x: AllChainsData) -> Any:
    return to_class(AllChainsData, x)


def chain_data_from_dict(s: Any) -> ChainData:
    return ChainData.from_dict(s)


def chain_data_to_dict(x: ChainData) -> Any:
    return to_class(ChainData, x)


def all_validators_data_from_dict(s: Any) -> AllValidatorsData:
    return AllValidatorsData.from_dict(s)


def all_validators_data_to_dict(x: AllValidatorsData) -> Any:
    return to_class(AllValidatorsData, x)


def validator_data_from_dict(s: Any) -> ValidatorData:
    return ValidatorData.from_dict(s)


def validator_data_to_dict(x: ValidatorData) -> Any:
    return to_class(ValidatorData, x)


def chain_validators_data_from_dict(s: Any) -> ChainValidatorsData:
    return ChainValidatorsData.from_dict(s)


def chain_validators_data_to_dict(x: ChainValidatorsData) -> Any:
    return to_class(ChainValidatorsData, x)

