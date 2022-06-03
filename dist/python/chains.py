# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = index_from_dict(json.loads(json_string))

from typing import Optional, Any, List, TypeVar, Callable, Type, cast
from enum import Enum


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


class REST:
    address: str
    provider: Optional[str]

    def __init__(self, address: str, provider: Optional[str]) -> None:
        self.address = address
        self.provider = provider

    @staticmethod
    def from_dict(obj: Any) -> 'REST':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        provider = from_union([from_str, from_none], obj.get("provider"))
        return REST(address, provider)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["provider"] = from_union([from_str, from_none], self.provider)
        return result


class BestApis:
    rest: List[REST]
    rpc: List[REST]

    def __init__(self, rest: List[REST], rpc: List[REST]) -> None:
        self.rest = rest
        self.rpc = rpc

    @staticmethod
    def from_dict(obj: Any) -> 'BestApis':
        assert isinstance(obj, dict)
        rest = from_list(REST.from_dict, obj.get("rest"))
        rpc = from_list(REST.from_dict, obj.get("rpc"))
        return BestApis(rest, rpc)

    def to_dict(self) -> dict:
        result: dict = {}
        result["rest"] = from_list(lambda x: to_class(REST, x), self.rest)
        result["rpc"] = from_list(lambda x: to_class(REST, x), self.rpc)
        return result


class NetworkType(Enum):
    MAINNET = "mainnet"


class Params:
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
    def from_dict(obj: Any) -> 'Params':
        assert isinstance(obj, dict)
        authz = from_union([from_bool, from_none], obj.get("authz"))
        bonded_tokens = from_union([from_str, from_none], obj.get("bonded_tokens"))
        total_supply = from_union([from_str, from_none], obj.get("total_supply"))
        actual_block_time = from_union([from_float, from_none], obj.get("actual_block_time"))
        calculated_apr = from_union([from_float, from_none], obj.get("calculated_apr"))
        return Params(authz, bonded_tokens, total_supply, actual_block_time, calculated_apr)

    def to_dict(self) -> dict:
        result: dict = {}
        result["authz"] = from_union([from_bool, from_none], self.authz)
        result["bonded_tokens"] = from_union([from_str, from_none], self.bonded_tokens)
        result["total_supply"] = from_union([from_str, from_none], self.total_supply)
        result["actual_block_time"] = from_union([to_float, from_none], self.actual_block_time)
        result["calculated_apr"] = from_union([to_float, from_none], self.calculated_apr)
        return result


class Status(Enum):
    KILLED = "killed"
    LIVE = "live"


class Chain:
    name: str
    path: str
    chain_name: str
    network_type: NetworkType
    pretty_name: str
    chain_id: str
    status: Status
    symbol: Optional[str]
    denom: Optional[str]
    decimals: Optional[int]
    image: Optional[str]
    height: Optional[int]
    best_apis: BestApis
    params: Params
    coingecko_id: Optional[str]

    def __init__(self, name: str, path: str, chain_name: str, network_type: NetworkType, pretty_name: str, chain_id: str, status: Status, symbol: Optional[str], denom: Optional[str], decimals: Optional[int], image: Optional[str], height: Optional[int], best_apis: BestApis, params: Params, coingecko_id: Optional[str]) -> None:
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
    def from_dict(obj: Any) -> 'Chain':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        path = from_str(obj.get("path"))
        chain_name = from_str(obj.get("chain_name"))
        network_type = NetworkType(obj.get("network_type"))
        pretty_name = from_str(obj.get("pretty_name"))
        chain_id = from_str(obj.get("chain_id"))
        status = Status(obj.get("status"))
        symbol = from_union([from_str, from_none], obj.get("symbol"))
        denom = from_union([from_str, from_none], obj.get("denom"))
        decimals = from_union([from_int, from_none], obj.get("decimals"))
        image = from_union([from_str, from_none], obj.get("image"))
        height = from_union([from_int, from_none], obj.get("height"))
        best_apis = BestApis.from_dict(obj.get("best_apis"))
        params = Params.from_dict(obj.get("params"))
        coingecko_id = from_union([from_str, from_none], obj.get("coingecko_id"))
        return Chain(name, path, chain_name, network_type, pretty_name, chain_id, status, symbol, denom, decimals, image, height, best_apis, params, coingecko_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["path"] = from_str(self.path)
        result["chain_name"] = from_str(self.chain_name)
        result["network_type"] = to_enum(NetworkType, self.network_type)
        result["pretty_name"] = from_str(self.pretty_name)
        result["chain_id"] = from_str(self.chain_id)
        result["status"] = to_enum(Status, self.status)
        result["symbol"] = from_union([from_str, from_none], self.symbol)
        result["denom"] = from_union([from_str, from_none], self.denom)
        result["decimals"] = from_union([from_int, from_none], self.decimals)
        result["image"] = from_union([from_str, from_none], self.image)
        result["height"] = from_union([from_int, from_none], self.height)
        result["best_apis"] = to_class(BestApis, self.best_apis)
        result["params"] = to_class(Params, self.params)
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


class Index:
    repository: Repository
    chains: List[Chain]

    def __init__(self, repository: Repository, chains: List[Chain]) -> None:
        self.repository = repository
        self.chains = chains

    @staticmethod
    def from_dict(obj: Any) -> 'Index':
        assert isinstance(obj, dict)
        repository = Repository.from_dict(obj.get("repository"))
        chains = from_list(Chain.from_dict, obj.get("chains"))
        return Index(repository, chains)

    def to_dict(self) -> dict:
        result: dict = {}
        result["repository"] = to_class(Repository, self.repository)
        result["chains"] = from_list(lambda x: to_class(Chain, x), self.chains)
        return result


def index_from_dict(s: Any) -> Index:
    return Index.from_dict(s)


def index_to_dict(x: Index) -> Any:
    return to_class(Index, x)
