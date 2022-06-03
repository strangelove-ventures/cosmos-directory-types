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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


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
        provider = from_union([from_str, from_none], obj.get("provider"))
        return Grpc(address, provider)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["provider"] = from_union([from_str, from_none], self.provider)
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
    authz: Optional[bool]
    bonded_tokens: Optional[str]
    total_supply: Optional[str]
    actual_block_time: Optional[float]
    calculated_apr: Optional[float]

    def __init__(self, authz: Optional[bool], bonded_tokens: Optional[str], total_supply: Optional[str], actual_block_time: Optional[float], calculated_apr: Optional[float]) -> None:
        self.authz = authz
        self.bonded_tokens = bonded_tokens
        self.total_supply = total_supply
        self.actual_block_time = actual_block_time
        self.calculated_apr = calculated_apr

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleParams':
        assert isinstance(obj, dict)
        authz = from_union([from_bool, from_none], obj.get("authz"))
        bonded_tokens = from_union([from_str, from_none], obj.get("bonded_tokens"))
        total_supply = from_union([from_str, from_none], obj.get("total_supply"))
        actual_block_time = from_union([from_float, from_none], obj.get("actual_block_time"))
        calculated_apr = from_union([from_float, from_none], obj.get("calculated_apr"))
        return PurpleParams(authz, bonded_tokens, total_supply, actual_block_time, calculated_apr)

    def to_dict(self) -> dict:
        result: dict = {}
        result["authz"] = from_union([from_bool, from_none], self.authz)
        result["bonded_tokens"] = from_union([from_str, from_none], self.bonded_tokens)
        result["total_supply"] = from_union([from_str, from_none], self.total_supply)
        result["actual_block_time"] = from_union([to_float, from_none], self.actual_block_time)
        result["calculated_apr"] = from_union([to_float, from_none], self.calculated_apr)
        return result


class PurpleStatus(Enum):
    KILLED = "killed"
    LIVE = "live"


class AllChainsDataChain:
    name: str
    path: str
    chain_name: str
    network_type: NetworkType
    pretty_name: str
    chain_id: str
    status: PurpleStatus
    symbol: Optional[str]
    denom: Optional[str]
    decimals: Optional[int]
    image: Optional[str]
    height: Optional[int]
    best_apis: BestApis
    params: PurpleParams
    coingecko_id: Optional[str]

    def __init__(self, name: str, path: str, chain_name: str, network_type: NetworkType, pretty_name: str, chain_id: str, status: PurpleStatus, symbol: Optional[str], denom: Optional[str], decimals: Optional[int], image: Optional[str], height: Optional[int], best_apis: BestApis, params: PurpleParams, coingecko_id: Optional[str]) -> None:
        self.name = name
        self.path = path
        self.chain_name = chain_name
        self.network_type = network_type
        self.pretty_name = pretty_name
        self.chain_id = chain_id
        self.status = status
        self.symbol = symbol
        self.denom = denom
        self.decimals = decimals
        self.image = image
        self.height = height
        self.best_apis = best_apis
        self.params = params
        self.coingecko_id = coingecko_id

    @staticmethod
    def from_dict(obj: Any) -> 'AllChainsDataChain':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        path = from_str(obj.get("path"))
        chain_name = from_str(obj.get("chain_name"))
        network_type = NetworkType(obj.get("network_type"))
        pretty_name = from_str(obj.get("pretty_name"))
        chain_id = from_str(obj.get("chain_id"))
        status = PurpleStatus(obj.get("status"))
        symbol = from_union([from_str, from_none], obj.get("symbol"))
        denom = from_union([from_str, from_none], obj.get("denom"))
        decimals = from_union([from_int, from_none], obj.get("decimals"))
        image = from_union([from_str, from_none], obj.get("image"))
        height = from_union([from_int, from_none], obj.get("height"))
        best_apis = BestApis.from_dict(obj.get("best_apis"))
        params = PurpleParams.from_dict(obj.get("params"))
        coingecko_id = from_union([from_str, from_none], obj.get("coingecko_id"))
        return AllChainsDataChain(name, path, chain_name, network_type, pretty_name, chain_id, status, symbol, denom, decimals, image, height, best_apis, params, coingecko_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["path"] = from_str(self.path)
        result["chain_name"] = from_str(self.chain_name)
        result["network_type"] = to_enum(NetworkType, self.network_type)
        result["pretty_name"] = from_str(self.pretty_name)
        result["chain_id"] = from_str(self.chain_id)
        result["status"] = to_enum(PurpleStatus, self.status)
        result["symbol"] = from_union([from_str, from_none], self.symbol)
        result["denom"] = from_union([from_str, from_none], self.denom)
        result["decimals"] = from_union([from_int, from_none], self.decimals)
        result["image"] = from_union([from_str, from_none], self.image)
        result["height"] = from_union([from_int, from_none], self.height)
        result["best_apis"] = to_class(BestApis, self.best_apis)
        result["params"] = to_class(PurpleParams, self.params)
        result["coingecko_id"] = from_union([from_str, from_none], self.coingecko_id)
        return result


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


class AllChainsData:
    repository: Repository
    chains: List[AllChainsDataChain]

    def __init__(self, repository: Repository, chains: List[AllChainsDataChain]) -> None:
        self.repository = repository
        self.chains = chains

    @staticmethod
    def from_dict(obj: Any) -> 'AllChainsData':
        assert isinstance(obj, dict)
        repository = Repository.from_dict(obj.get("repository"))
        chains = from_list(AllChainsDataChain.from_dict, obj.get("chains"))
        return AllChainsData(repository, chains)

    def to_dict(self) -> dict:
        result: dict = {}
        result["repository"] = to_class(Repository, self.repository)
        result["chains"] = from_list(lambda x: to_class(AllChainsDataChain, x), self.chains)
        return result


class Apis:
    rpc: List[Grpc]
    rest: List[Grpc]
    grpc: List[Grpc]

    def __init__(self, rpc: List[Grpc], rest: List[Grpc], grpc: List[Grpc]) -> None:
        self.rpc = rpc
        self.rest = rest
        self.grpc = grpc

    @staticmethod
    def from_dict(obj: Any) -> 'Apis':
        assert isinstance(obj, dict)
        rpc = from_list(Grpc.from_dict, obj.get("rpc"))
        rest = from_list(Grpc.from_dict, obj.get("rest"))
        grpc = from_list(Grpc.from_dict, obj.get("grpc"))
        return Apis(rpc, rest, grpc)

    def to_dict(self) -> dict:
        result: dict = {}
        result["rpc"] = from_list(lambda x: to_class(Grpc, x), self.rpc)
        result["rest"] = from_list(lambda x: to_class(Grpc, x), self.rest)
        result["grpc"] = from_list(lambda x: to_class(Grpc, x), self.grpc)
        return result


class Binaries:
    linux_amd64: str
    linux_arm64: Optional[str]
    darwin_amd64: Optional[str]
    windows_amd64: Optional[str]

    def __init__(self, linux_amd64: str, linux_arm64: Optional[str], darwin_amd64: Optional[str], windows_amd64: Optional[str]) -> None:
        self.linux_amd64 = linux_amd64
        self.linux_arm64 = linux_arm64
        self.darwin_amd64 = darwin_amd64
        self.windows_amd64 = windows_amd64

    @staticmethod
    def from_dict(obj: Any) -> 'Binaries':
        assert isinstance(obj, dict)
        linux_amd64 = from_str(obj.get("linux/amd64"))
        linux_arm64 = from_union([from_str, from_none], obj.get("linux/arm64"))
        darwin_amd64 = from_union([from_str, from_none], obj.get("darwin/amd64"))
        windows_amd64 = from_union([from_str, from_none], obj.get("windows/amd64"))
        return Binaries(linux_amd64, linux_arm64, darwin_amd64, windows_amd64)

    def to_dict(self) -> dict:
        result: dict = {}
        result["linux/amd64"] = from_str(self.linux_amd64)
        result["linux/arm64"] = from_union([from_str, from_none], self.linux_arm64)
        result["darwin/amd64"] = from_union([from_str, from_none], self.darwin_amd64)
        result["windows/amd64"] = from_union([from_str, from_none], self.windows_amd64)
        return result


class Codebase:
    git_repo: str
    recommended_version: str
    compatible_versions: List[str]
    binaries: Optional[Binaries]

    def __init__(self, git_repo: str, recommended_version: str, compatible_versions: List[str], binaries: Optional[Binaries]) -> None:
        self.git_repo = git_repo
        self.recommended_version = recommended_version
        self.compatible_versions = compatible_versions
        self.binaries = binaries

    @staticmethod
    def from_dict(obj: Any) -> 'Codebase':
        assert isinstance(obj, dict)
        git_repo = from_str(obj.get("git_repo"))
        recommended_version = from_str(obj.get("recommended_version"))
        compatible_versions = from_list(from_str, obj.get("compatible_versions"))
        binaries = from_union([Binaries.from_dict, from_none], obj.get("binaries"))
        return Codebase(git_repo, recommended_version, compatible_versions, binaries)

    def to_dict(self) -> dict:
        result: dict = {}
        result["git_repo"] = from_str(self.git_repo)
        result["recommended_version"] = from_str(self.recommended_version)
        result["compatible_versions"] = from_list(from_str, self.compatible_versions)
        result["binaries"] = from_union([lambda x: to_class(Binaries, x), from_none], self.binaries)
        return result


class Explorer:
    kind: str
    url: str
    tx_page: str
    account_page: Optional[str]

    def __init__(self, kind: str, url: str, tx_page: str, account_page: Optional[str]) -> None:
        self.kind = kind
        self.url = url
        self.tx_page = tx_page
        self.account_page = account_page

    @staticmethod
    def from_dict(obj: Any) -> 'Explorer':
        assert isinstance(obj, dict)
        kind = from_str(obj.get("kind"))
        url = from_str(obj.get("url"))
        tx_page = from_str(obj.get("tx_page"))
        account_page = from_union([from_str, from_none], obj.get("account_page"))
        return Explorer(kind, url, tx_page, account_page)

    def to_dict(self) -> dict:
        result: dict = {}
        result["kind"] = from_str(self.kind)
        result["url"] = from_str(self.url)
        result["tx_page"] = from_str(self.tx_page)
        result["account_page"] = from_union([from_str, from_none], self.account_page)
        return result


class FeeToken:
    denom: str
    fixed_min_gas_price: int

    def __init__(self, denom: str, fixed_min_gas_price: int) -> None:
        self.denom = denom
        self.fixed_min_gas_price = fixed_min_gas_price

    @staticmethod
    def from_dict(obj: Any) -> 'FeeToken':
        assert isinstance(obj, dict)
        denom = from_str(obj.get("denom"))
        fixed_min_gas_price = from_int(obj.get("fixed_min_gas_price"))
        return FeeToken(denom, fixed_min_gas_price)

    def to_dict(self) -> dict:
        result: dict = {}
        result["denom"] = from_str(self.denom)
        result["fixed_min_gas_price"] = from_int(self.fixed_min_gas_price)
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


class FluffyParams:
    authz: bool
    actual_block_time: float
    actual_blocks_per_year: float
    unbonding_time: int
    max_validators: int
    blocks_per_year: Optional[int]
    block_time: Optional[float]
    community_tax: Optional[float]
    base_inflation: float
    total_supply: str
    bonded_tokens: str
    bonded_ratio: float
    estimated_apr: Optional[float]
    calculated_apr: float
    minting_epoch_provision: Optional[float]
    epoch_duration: Optional[int]
    year_minting_provision: Optional[int]

    def __init__(self, authz: bool, actual_block_time: float, actual_blocks_per_year: float, unbonding_time: int, max_validators: int, blocks_per_year: Optional[int], block_time: Optional[float], community_tax: Optional[float], base_inflation: float, total_supply: str, bonded_tokens: str, bonded_ratio: float, estimated_apr: Optional[float], calculated_apr: float, minting_epoch_provision: Optional[float], epoch_duration: Optional[int], year_minting_provision: Optional[int]) -> None:
        self.authz = authz
        self.actual_block_time = actual_block_time
        self.actual_blocks_per_year = actual_blocks_per_year
        self.unbonding_time = unbonding_time
        self.max_validators = max_validators
        self.blocks_per_year = blocks_per_year
        self.block_time = block_time
        self.community_tax = community_tax
        self.base_inflation = base_inflation
        self.total_supply = total_supply
        self.bonded_tokens = bonded_tokens
        self.bonded_ratio = bonded_ratio
        self.estimated_apr = estimated_apr
        self.calculated_apr = calculated_apr
        self.minting_epoch_provision = minting_epoch_provision
        self.epoch_duration = epoch_duration
        self.year_minting_provision = year_minting_provision

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyParams':
        assert isinstance(obj, dict)
        authz = from_bool(obj.get("authz"))
        actual_block_time = from_float(obj.get("actual_block_time"))
        actual_blocks_per_year = from_float(obj.get("actual_blocks_per_year"))
        unbonding_time = from_int(obj.get("unbonding_time"))
        max_validators = from_int(obj.get("max_validators"))
        blocks_per_year = from_union([from_int, from_none], obj.get("blocks_per_year"))
        block_time = from_union([from_float, from_none], obj.get("block_time"))
        community_tax = from_union([from_float, from_none], obj.get("community_tax"))
        base_inflation = from_float(obj.get("base_inflation"))
        total_supply = from_str(obj.get("total_supply"))
        bonded_tokens = from_str(obj.get("bonded_tokens"))
        bonded_ratio = from_float(obj.get("bonded_ratio"))
        estimated_apr = from_union([from_float, from_none], obj.get("estimated_apr"))
        calculated_apr = from_float(obj.get("calculated_apr"))
        minting_epoch_provision = from_union([from_float, from_none], obj.get("minting_epoch_provision"))
        epoch_duration = from_union([from_int, from_none], obj.get("epoch_duration"))
        year_minting_provision = from_union([from_int, from_none], obj.get("year_minting_provision"))
        return FluffyParams(authz, actual_block_time, actual_blocks_per_year, unbonding_time, max_validators, blocks_per_year, block_time, community_tax, base_inflation, total_supply, bonded_tokens, bonded_ratio, estimated_apr, calculated_apr, minting_epoch_provision, epoch_duration, year_minting_provision)

    def to_dict(self) -> dict:
        result: dict = {}
        result["authz"] = from_bool(self.authz)
        result["actual_block_time"] = to_float(self.actual_block_time)
        result["actual_blocks_per_year"] = to_float(self.actual_blocks_per_year)
        result["unbonding_time"] = from_int(self.unbonding_time)
        result["max_validators"] = from_int(self.max_validators)
        result["blocks_per_year"] = from_union([from_int, from_none], self.blocks_per_year)
        result["block_time"] = from_union([to_float, from_none], self.block_time)
        result["community_tax"] = from_union([to_float, from_none], self.community_tax)
        result["base_inflation"] = to_float(self.base_inflation)
        result["total_supply"] = from_str(self.total_supply)
        result["bonded_tokens"] = from_str(self.bonded_tokens)
        result["bonded_ratio"] = to_float(self.bonded_ratio)
        result["estimated_apr"] = from_union([to_float, from_none], self.estimated_apr)
        result["calculated_apr"] = to_float(self.calculated_apr)
        result["minting_epoch_provision"] = from_union([to_float, from_none], self.minting_epoch_provision)
        result["epoch_duration"] = from_union([from_int, from_none], self.epoch_duration)
        result["year_minting_provision"] = from_union([from_int, from_none], self.year_minting_provision)
        return result


class PersistentPeer:
    id: str
    address: str
    provider: Optional[str]

    def __init__(self, id: str, address: str, provider: Optional[str]) -> None:
        self.id = id
        self.address = address
        self.provider = provider

    @staticmethod
    def from_dict(obj: Any) -> 'PersistentPeer':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        address = from_str(obj.get("address"))
        provider = from_union([from_str, from_none], obj.get("provider"))
        return PersistentPeer(id, address, provider)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["address"] = from_str(self.address)
        result["provider"] = from_union([from_str, from_none], self.provider)
        return result


class Peers:
    seeds: List[PersistentPeer]
    persistent_peers: List[PersistentPeer]

    def __init__(self, seeds: List[PersistentPeer], persistent_peers: List[PersistentPeer]) -> None:
        self.seeds = seeds
        self.persistent_peers = persistent_peers

    @staticmethod
    def from_dict(obj: Any) -> 'Peers':
        assert isinstance(obj, dict)
        seeds = from_list(PersistentPeer.from_dict, obj.get("seeds"))
        persistent_peers = from_list(PersistentPeer.from_dict, obj.get("persistent_peers"))
        return Peers(seeds, persistent_peers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["seeds"] = from_list(lambda x: to_class(PersistentPeer, x), self.seeds)
        result["persistent_peers"] = from_list(lambda x: to_class(PersistentPeer, x), self.persistent_peers)
        return result


class ChainDataChain:
    schema: str
    chain_name: str
    chain_id: str
    pretty_name: str
    status: PurpleStatus
    network_type: NetworkType
    bech32_prefix: str
    genesis: Genesis
    daemon_name: str
    node_home: str
    key_algos: List[str]
    slip44: int
    fees: Optional[Fees]
    codebase: Codebase
    peers: Peers
    apis: Apis
    explorers: List[Explorer]
    name: str
    path: str
    symbol: str
    denom: str
    decimals: int
    coingecko_id: str
    image: str
    height: int
    best_apis: BestApis
    params: FluffyParams

    def __init__(self, schema: str, chain_name: str, chain_id: str, pretty_name: str, status: PurpleStatus, network_type: NetworkType, bech32_prefix: str, genesis: Genesis, daemon_name: str, node_home: str, key_algos: List[str], slip44: int, fees: Optional[Fees], codebase: Codebase, peers: Peers, apis: Apis, explorers: List[Explorer], name: str, path: str, symbol: str, denom: str, decimals: int, coingecko_id: str, image: str, height: int, best_apis: BestApis, params: FluffyParams) -> None:
        self.schema = schema
        self.chain_name = chain_name
        self.chain_id = chain_id
        self.pretty_name = pretty_name
        self.status = status
        self.network_type = network_type
        self.bech32_prefix = bech32_prefix
        self.genesis = genesis
        self.daemon_name = daemon_name
        self.node_home = node_home
        self.key_algos = key_algos
        self.slip44 = slip44
        self.fees = fees
        self.codebase = codebase
        self.peers = peers
        self.apis = apis
        self.explorers = explorers
        self.name = name
        self.path = path
        self.symbol = symbol
        self.denom = denom
        self.decimals = decimals
        self.coingecko_id = coingecko_id
        self.image = image
        self.height = height
        self.best_apis = best_apis
        self.params = params

    @staticmethod
    def from_dict(obj: Any) -> 'ChainDataChain':
        assert isinstance(obj, dict)
        schema = from_str(obj.get("$schema"))
        chain_name = from_str(obj.get("chain_name"))
        chain_id = from_str(obj.get("chain_id"))
        pretty_name = from_str(obj.get("pretty_name"))
        status = PurpleStatus(obj.get("status"))
        network_type = NetworkType(obj.get("network_type"))
        bech32_prefix = from_str(obj.get("bech32_prefix"))
        genesis = Genesis.from_dict(obj.get("genesis"))
        daemon_name = from_str(obj.get("daemon_name"))
        node_home = from_str(obj.get("node_home"))
        key_algos = from_list(from_str, obj.get("key_algos"))
        slip44 = from_int(obj.get("slip44"))
        fees = from_union([Fees.from_dict, from_none], obj.get("fees"))
        codebase = Codebase.from_dict(obj.get("codebase"))
        peers = Peers.from_dict(obj.get("peers"))
        apis = Apis.from_dict(obj.get("apis"))
        explorers = from_list(Explorer.from_dict, obj.get("explorers"))
        name = from_str(obj.get("name"))
        path = from_str(obj.get("path"))
        symbol = from_str(obj.get("symbol"))
        denom = from_str(obj.get("denom"))
        decimals = from_int(obj.get("decimals"))
        coingecko_id = from_str(obj.get("coingecko_id"))
        image = from_str(obj.get("image"))
        height = from_int(obj.get("height"))
        best_apis = BestApis.from_dict(obj.get("best_apis"))
        params = FluffyParams.from_dict(obj.get("params"))
        return ChainDataChain(schema, chain_name, chain_id, pretty_name, status, network_type, bech32_prefix, genesis, daemon_name, node_home, key_algos, slip44, fees, codebase, peers, apis, explorers, name, path, symbol, denom, decimals, coingecko_id, image, height, best_apis, params)

    def to_dict(self) -> dict:
        result: dict = {}
        result["$schema"] = from_str(self.schema)
        result["chain_name"] = from_str(self.chain_name)
        result["chain_id"] = from_str(self.chain_id)
        result["pretty_name"] = from_str(self.pretty_name)
        result["status"] = to_enum(PurpleStatus, self.status)
        result["network_type"] = to_enum(NetworkType, self.network_type)
        result["bech32_prefix"] = from_str(self.bech32_prefix)
        result["genesis"] = to_class(Genesis, self.genesis)
        result["daemon_name"] = from_str(self.daemon_name)
        result["node_home"] = from_str(self.node_home)
        result["key_algos"] = from_list(from_str, self.key_algos)
        result["slip44"] = from_int(self.slip44)
        result["fees"] = from_union([lambda x: to_class(Fees, x), from_none], self.fees)
        result["codebase"] = to_class(Codebase, self.codebase)
        result["peers"] = to_class(Peers, self.peers)
        result["apis"] = to_class(Apis, self.apis)
        result["explorers"] = from_list(lambda x: to_class(Explorer, x), self.explorers)
        result["name"] = from_str(self.name)
        result["path"] = from_str(self.path)
        result["symbol"] = from_str(self.symbol)
        result["denom"] = from_str(self.denom)
        result["decimals"] = from_int(self.decimals)
        result["coingecko_id"] = from_str(self.coingecko_id)
        result["image"] = from_str(self.image)
        result["height"] = from_int(self.height)
        result["best_apis"] = to_class(BestApis, self.best_apis)
        result["params"] = to_class(FluffyParams, self.params)
        return result


class ChainData:
    repository: Repository
    chain: ChainDataChain

    def __init__(self, repository: Repository, chain: ChainDataChain) -> None:
        self.repository = repository
        self.chain = chain

    @staticmethod
    def from_dict(obj: Any) -> 'ChainData':
        assert isinstance(obj, dict)
        repository = Repository.from_dict(obj.get("repository"))
        chain = ChainDataChain.from_dict(obj.get("chain"))
        return ChainData(repository, chain)

    def to_dict(self) -> dict:
        result: dict = {}
        result["repository"] = to_class(Repository, self.repository)
        result["chain"] = to_class(ChainDataChain, self.chain)
        return result


class ValidatorChain:
    name: str
    address: str
    restake: Union[bool, str]

    def __init__(self, name: str, address: str, restake: Union[bool, str]) -> None:
        self.name = name
        self.address = address
        self.restake = restake

    @staticmethod
    def from_dict(obj: Any) -> 'ValidatorChain':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        address = from_str(obj.get("address"))
        restake = from_union([from_bool, from_str], obj.get("restake"))
        return ValidatorChain(name, address, restake)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["address"] = from_str(self.address)
        result["restake"] = from_union([from_bool, from_str], self.restake)
        return result


class Profile:
    name: str
    identity: str

    def __init__(self, name: str, identity: str) -> None:
        self.name = name
        self.identity = identity

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        identity = from_str(obj.get("identity"))
        return Profile(name, identity)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["identity"] = from_str(self.identity)
        return result


class AllValidatorsDataValidator:
    path: str
    name: str
    identity: str
    chains: List[ValidatorChain]
    profile: Profile

    def __init__(self, path: str, name: str, identity: str, chains: List[ValidatorChain], profile: Profile) -> None:
        self.path = path
        self.name = name
        self.identity = identity
        self.chains = chains
        self.profile = profile

    @staticmethod
    def from_dict(obj: Any) -> 'AllValidatorsDataValidator':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        name = from_str(obj.get("name"))
        identity = from_str(obj.get("identity"))
        chains = from_list(ValidatorChain.from_dict, obj.get("chains"))
        profile = Profile.from_dict(obj.get("profile"))
        return AllValidatorsDataValidator(path, name, identity, chains, profile)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        result["name"] = from_str(self.name)
        result["identity"] = from_str(self.identity)
        result["chains"] = from_list(lambda x: to_class(ValidatorChain, x), self.chains)
        result["profile"] = to_class(Profile, self.profile)
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


class RestakeClass:
    address: str
    run_time: Union[List[str], str]
    minimum_reward: int

    def __init__(self, address: str, run_time: Union[List[str], str], minimum_reward: int) -> None:
        self.address = address
        self.run_time = run_time
        self.minimum_reward = minimum_reward

    @staticmethod
    def from_dict(obj: Any) -> 'RestakeClass':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        run_time = from_union([lambda x: from_list(from_str, x), from_str], obj.get("run_time"))
        minimum_reward = from_int(obj.get("minimum_reward"))
        return RestakeClass(address, run_time, minimum_reward)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["run_time"] = from_union([lambda x: from_list(from_str, x), from_str], self.run_time)
        result["minimum_reward"] = from_int(self.minimum_reward)
        return result


class ValidatorStatus(Enum):
    BOND_STATUS_BONDED = "BOND_STATUS_BONDED"
    BOND_STATUS_UNBONDED = "BOND_STATUS_UNBONDED"
    BOND_STATUS_UNBONDING = "BOND_STATUS_UNBONDING"


class ChainElement:
    name: Optional[str]
    address: str
    restake: Optional[RestakeClass]
    moniker: str
    identity: Optional[str]
    hex_address: str
    uptime: Optional[float]
    missed_blocks: int
    operator_address: str
    consensus_pubkey: ConsensusPubkey
    jailed: bool
    status: ValidatorStatus
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

    def __init__(self, name: Optional[str], address: str, restake: Optional[RestakeClass], moniker: str, identity: Optional[str], hex_address: str, uptime: Optional[float], missed_blocks: int, operator_address: str, consensus_pubkey: ConsensusPubkey, jailed: bool, status: ValidatorStatus, tokens: str, delegator_shares: str, description: Description, unbonding_height: int, unbonding_time: datetime, commission: Commission, min_self_delegation: str, rank: int, mintscan_image: Optional[str], keybase_image: Optional[str]) -> None:
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
    def from_dict(obj: Any) -> 'ChainElement':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        address = from_str(obj.get("address"))
        restake = from_union([RestakeClass.from_dict, from_none], obj.get("restake"))
        moniker = from_str(obj.get("moniker"))
        identity = from_union([from_str, from_none], obj.get("identity"))
        hex_address = from_str(obj.get("hexAddress"))
        uptime = from_union([from_float, from_none], obj.get("uptime"))
        missed_blocks = from_int(obj.get("missedBlocks"))
        operator_address = from_str(obj.get("operator_address"))
        consensus_pubkey = ConsensusPubkey.from_dict(obj.get("consensus_pubkey"))
        jailed = from_bool(obj.get("jailed"))
        status = ValidatorStatus(obj.get("status"))
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
        return ChainElement(name, address, restake, moniker, identity, hex_address, uptime, missed_blocks, operator_address, consensus_pubkey, jailed, status, tokens, delegator_shares, description, unbonding_height, unbonding_time, commission, min_self_delegation, rank, mintscan_image, keybase_image)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["address"] = from_str(self.address)
        result["restake"] = from_union([lambda x: to_class(RestakeClass, x), from_none], self.restake)
        result["moniker"] = from_str(self.moniker)
        result["identity"] = from_union([from_str, from_none], self.identity)
        result["hexAddress"] = from_str(self.hex_address)
        result["uptime"] = from_union([to_float, from_none], self.uptime)
        result["missedBlocks"] = from_int(self.missed_blocks)
        result["operator_address"] = from_str(self.operator_address)
        result["consensus_pubkey"] = to_class(ConsensusPubkey, self.consensus_pubkey)
        result["jailed"] = from_bool(self.jailed)
        result["status"] = to_enum(ValidatorStatus, self.status)
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
        return result


class ValidatorDataValidator:
    path: str
    name: str
    identity: str
    chains: List[ChainElement]
    profile: Profile

    def __init__(self, path: str, name: str, identity: str, chains: List[ChainElement], profile: Profile) -> None:
        self.path = path
        self.name = name
        self.identity = identity
        self.chains = chains
        self.profile = profile

    @staticmethod
    def from_dict(obj: Any) -> 'ValidatorDataValidator':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        name = from_str(obj.get("name"))
        identity = from_str(obj.get("identity"))
        chains = from_list(ChainElement.from_dict, obj.get("chains"))
        profile = Profile.from_dict(obj.get("profile"))
        return ValidatorDataValidator(path, name, identity, chains, profile)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        result["name"] = from_str(self.name)
        result["identity"] = from_str(self.identity)
        result["chains"] = from_list(lambda x: to_class(ChainElement, x), self.chains)
        result["profile"] = to_class(Profile, self.profile)
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

