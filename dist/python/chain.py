# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = cosmoshub_from_dict(json.loads(json_string))
#     result = juno_from_dict(json.loads(json_string))
#     result = osmosis_from_dict(json.loads(json_string))

from typing import Any, List, Optional, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


class Grpc:
    address: str
    provider: str

    def __init__(self, address: str, provider: str) -> None:
        self.address = address
        self.provider = provider

    @staticmethod
    def from_dict(obj: Any) -> 'Grpc':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        provider = from_str(obj.get("provider"))
        return Grpc(address, provider)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["provider"] = from_str(self.provider)
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

    def __init__(self, kind: str, url: str, tx_page: str) -> None:
        self.kind = kind
        self.url = url
        self.tx_page = tx_page

    @staticmethod
    def from_dict(obj: Any) -> 'Explorer':
        assert isinstance(obj, dict)
        kind = from_str(obj.get("kind"))
        url = from_str(obj.get("url"))
        tx_page = from_str(obj.get("tx_page"))
        return Explorer(kind, url, tx_page)

    def to_dict(self) -> dict:
        result: dict = {}
        result["kind"] = from_str(self.kind)
        result["url"] = from_str(self.url)
        result["tx_page"] = from_str(self.tx_page)
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


class PurpleParams:
    authz: bool
    actual_block_time: float
    actual_blocks_per_year: float
    unbonding_time: int
    max_validators: int
    blocks_per_year: int
    block_time: float
    community_tax: float
    base_inflation: float
    bonded_ratio: float
    bonded_tokens: str
    total_supply: str
    estimated_apr: float
    calculated_apr: float

    def __init__(self, authz: bool, actual_block_time: float, actual_blocks_per_year: float, unbonding_time: int, max_validators: int, blocks_per_year: int, block_time: float, community_tax: float, base_inflation: float, bonded_ratio: float, bonded_tokens: str, total_supply: str, estimated_apr: float, calculated_apr: float) -> None:
        self.authz = authz
        self.actual_block_time = actual_block_time
        self.actual_blocks_per_year = actual_blocks_per_year
        self.unbonding_time = unbonding_time
        self.max_validators = max_validators
        self.blocks_per_year = blocks_per_year
        self.block_time = block_time
        self.community_tax = community_tax
        self.base_inflation = base_inflation
        self.bonded_ratio = bonded_ratio
        self.bonded_tokens = bonded_tokens
        self.total_supply = total_supply
        self.estimated_apr = estimated_apr
        self.calculated_apr = calculated_apr

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleParams':
        assert isinstance(obj, dict)
        authz = from_bool(obj.get("authz"))
        actual_block_time = from_float(obj.get("actual_block_time"))
        actual_blocks_per_year = from_float(obj.get("actual_blocks_per_year"))
        unbonding_time = from_int(obj.get("unbonding_time"))
        max_validators = from_int(obj.get("max_validators"))
        blocks_per_year = from_int(obj.get("blocks_per_year"))
        block_time = from_float(obj.get("block_time"))
        community_tax = from_float(obj.get("community_tax"))
        base_inflation = from_float(obj.get("base_inflation"))
        bonded_ratio = from_float(obj.get("bonded_ratio"))
        bonded_tokens = from_str(obj.get("bonded_tokens"))
        total_supply = from_str(obj.get("total_supply"))
        estimated_apr = from_float(obj.get("estimated_apr"))
        calculated_apr = from_float(obj.get("calculated_apr"))
        return PurpleParams(authz, actual_block_time, actual_blocks_per_year, unbonding_time, max_validators, blocks_per_year, block_time, community_tax, base_inflation, bonded_ratio, bonded_tokens, total_supply, estimated_apr, calculated_apr)

    def to_dict(self) -> dict:
        result: dict = {}
        result["authz"] = from_bool(self.authz)
        result["actual_block_time"] = to_float(self.actual_block_time)
        result["actual_blocks_per_year"] = to_float(self.actual_blocks_per_year)
        result["unbonding_time"] = from_int(self.unbonding_time)
        result["max_validators"] = from_int(self.max_validators)
        result["blocks_per_year"] = from_int(self.blocks_per_year)
        result["block_time"] = to_float(self.block_time)
        result["community_tax"] = to_float(self.community_tax)
        result["base_inflation"] = to_float(self.base_inflation)
        result["bonded_ratio"] = to_float(self.bonded_ratio)
        result["bonded_tokens"] = from_str(self.bonded_tokens)
        result["total_supply"] = from_str(self.total_supply)
        result["estimated_apr"] = to_float(self.estimated_apr)
        result["calculated_apr"] = to_float(self.calculated_apr)
        return result


class PersistentPeer:
    id: str
    address: str

    def __init__(self, id: str, address: str) -> None:
        self.id = id
        self.address = address

    @staticmethod
    def from_dict(obj: Any) -> 'PersistentPeer':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        address = from_str(obj.get("address"))
        return PersistentPeer(id, address)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["address"] = from_str(self.address)
        return result


class Seed:
    id: str
    address: str
    provider: Optional[str]

    def __init__(self, id: str, address: str, provider: Optional[str]) -> None:
        self.id = id
        self.address = address
        self.provider = provider

    @staticmethod
    def from_dict(obj: Any) -> 'Seed':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        address = from_str(obj.get("address"))
        provider = from_union([from_str, from_none], obj.get("provider"))
        return Seed(id, address, provider)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["address"] = from_str(self.address)
        result["provider"] = from_union([from_str, from_none], self.provider)
        return result


class PurplePeers:
    seeds: List[Seed]
    persistent_peers: List[PersistentPeer]

    def __init__(self, seeds: List[Seed], persistent_peers: List[PersistentPeer]) -> None:
        self.seeds = seeds
        self.persistent_peers = persistent_peers

    @staticmethod
    def from_dict(obj: Any) -> 'PurplePeers':
        assert isinstance(obj, dict)
        seeds = from_list(Seed.from_dict, obj.get("seeds"))
        persistent_peers = from_list(PersistentPeer.from_dict, obj.get("persistent_peers"))
        return PurplePeers(seeds, persistent_peers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["seeds"] = from_list(lambda x: to_class(Seed, x), self.seeds)
        result["persistent_peers"] = from_list(lambda x: to_class(PersistentPeer, x), self.persistent_peers)
        return result


class CosmoshubChain:
    schema: str
    chain_name: str
    chain_id: str
    pretty_name: str
    status: str
    network_type: str
    bech32_prefix: str
    genesis: Genesis
    daemon_name: str
    node_home: str
    key_algos: List[str]
    slip44: int
    fees: Fees
    codebase: Codebase
    peers: PurplePeers
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
    params: PurpleParams

    def __init__(self, schema: str, chain_name: str, chain_id: str, pretty_name: str, status: str, network_type: str, bech32_prefix: str, genesis: Genesis, daemon_name: str, node_home: str, key_algos: List[str], slip44: int, fees: Fees, codebase: Codebase, peers: PurplePeers, apis: Apis, explorers: List[Explorer], name: str, path: str, symbol: str, denom: str, decimals: int, coingecko_id: str, image: str, height: int, best_apis: BestApis, params: PurpleParams) -> None:
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
    def from_dict(obj: Any) -> 'CosmoshubChain':
        assert isinstance(obj, dict)
        schema = from_str(obj.get("$schema"))
        chain_name = from_str(obj.get("chain_name"))
        chain_id = from_str(obj.get("chain_id"))
        pretty_name = from_str(obj.get("pretty_name"))
        status = from_str(obj.get("status"))
        network_type = from_str(obj.get("network_type"))
        bech32_prefix = from_str(obj.get("bech32_prefix"))
        genesis = Genesis.from_dict(obj.get("genesis"))
        daemon_name = from_str(obj.get("daemon_name"))
        node_home = from_str(obj.get("node_home"))
        key_algos = from_list(from_str, obj.get("key_algos"))
        slip44 = from_int(obj.get("slip44"))
        fees = Fees.from_dict(obj.get("fees"))
        codebase = Codebase.from_dict(obj.get("codebase"))
        peers = PurplePeers.from_dict(obj.get("peers"))
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
        params = PurpleParams.from_dict(obj.get("params"))
        return CosmoshubChain(schema, chain_name, chain_id, pretty_name, status, network_type, bech32_prefix, genesis, daemon_name, node_home, key_algos, slip44, fees, codebase, peers, apis, explorers, name, path, symbol, denom, decimals, coingecko_id, image, height, best_apis, params)

    def to_dict(self) -> dict:
        result: dict = {}
        result["$schema"] = from_str(self.schema)
        result["chain_name"] = from_str(self.chain_name)
        result["chain_id"] = from_str(self.chain_id)
        result["pretty_name"] = from_str(self.pretty_name)
        result["status"] = from_str(self.status)
        result["network_type"] = from_str(self.network_type)
        result["bech32_prefix"] = from_str(self.bech32_prefix)
        result["genesis"] = to_class(Genesis, self.genesis)
        result["daemon_name"] = from_str(self.daemon_name)
        result["node_home"] = from_str(self.node_home)
        result["key_algos"] = from_list(from_str, self.key_algos)
        result["slip44"] = from_int(self.slip44)
        result["fees"] = to_class(Fees, self.fees)
        result["codebase"] = to_class(Codebase, self.codebase)
        result["peers"] = to_class(PurplePeers, self.peers)
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
        result["params"] = to_class(PurpleParams, self.params)
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


class Cosmoshub:
    repository: Repository
    chain: CosmoshubChain

    def __init__(self, repository: Repository, chain: CosmoshubChain) -> None:
        self.repository = repository
        self.chain = chain

    @staticmethod
    def from_dict(obj: Any) -> 'Cosmoshub':
        assert isinstance(obj, dict)
        repository = Repository.from_dict(obj.get("repository"))
        chain = CosmoshubChain.from_dict(obj.get("chain"))
        return Cosmoshub(repository, chain)

    def to_dict(self) -> dict:
        result: dict = {}
        result["repository"] = to_class(Repository, self.repository)
        result["chain"] = to_class(CosmoshubChain, self.chain)
        return result


class FluffyPeers:
    seeds: List[PersistentPeer]
    persistent_peers: List[PersistentPeer]

    def __init__(self, seeds: List[PersistentPeer], persistent_peers: List[PersistentPeer]) -> None:
        self.seeds = seeds
        self.persistent_peers = persistent_peers

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyPeers':
        assert isinstance(obj, dict)
        seeds = from_list(PersistentPeer.from_dict, obj.get("seeds"))
        persistent_peers = from_list(PersistentPeer.from_dict, obj.get("persistent_peers"))
        return FluffyPeers(seeds, persistent_peers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["seeds"] = from_list(lambda x: to_class(PersistentPeer, x), self.seeds)
        result["persistent_peers"] = from_list(lambda x: to_class(PersistentPeer, x), self.persistent_peers)
        return result


class JunoChain:
    schema: str
    chain_name: str
    status: str
    network_type: str
    pretty_name: str
    chain_id: str
    bech32_prefix: str
    slip44: int
    genesis: Genesis
    codebase: Codebase
    daemon_name: str
    node_home: str
    key_algos: List[str]
    peers: FluffyPeers
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
    params: PurpleParams

    def __init__(self, schema: str, chain_name: str, status: str, network_type: str, pretty_name: str, chain_id: str, bech32_prefix: str, slip44: int, genesis: Genesis, codebase: Codebase, daemon_name: str, node_home: str, key_algos: List[str], peers: FluffyPeers, apis: Apis, explorers: List[Explorer], name: str, path: str, symbol: str, denom: str, decimals: int, coingecko_id: str, image: str, height: int, best_apis: BestApis, params: PurpleParams) -> None:
        self.schema = schema
        self.chain_name = chain_name
        self.status = status
        self.network_type = network_type
        self.pretty_name = pretty_name
        self.chain_id = chain_id
        self.bech32_prefix = bech32_prefix
        self.slip44 = slip44
        self.genesis = genesis
        self.codebase = codebase
        self.daemon_name = daemon_name
        self.node_home = node_home
        self.key_algos = key_algos
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
    def from_dict(obj: Any) -> 'JunoChain':
        assert isinstance(obj, dict)
        schema = from_str(obj.get("$schema"))
        chain_name = from_str(obj.get("chain_name"))
        status = from_str(obj.get("status"))
        network_type = from_str(obj.get("network_type"))
        pretty_name = from_str(obj.get("pretty_name"))
        chain_id = from_str(obj.get("chain_id"))
        bech32_prefix = from_str(obj.get("bech32_prefix"))
        slip44 = from_int(obj.get("slip44"))
        genesis = Genesis.from_dict(obj.get("genesis"))
        codebase = Codebase.from_dict(obj.get("codebase"))
        daemon_name = from_str(obj.get("daemon_name"))
        node_home = from_str(obj.get("node_home"))
        key_algos = from_list(from_str, obj.get("key_algos"))
        peers = FluffyPeers.from_dict(obj.get("peers"))
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
        params = PurpleParams.from_dict(obj.get("params"))
        return JunoChain(schema, chain_name, status, network_type, pretty_name, chain_id, bech32_prefix, slip44, genesis, codebase, daemon_name, node_home, key_algos, peers, apis, explorers, name, path, symbol, denom, decimals, coingecko_id, image, height, best_apis, params)

    def to_dict(self) -> dict:
        result: dict = {}
        result["$schema"] = from_str(self.schema)
        result["chain_name"] = from_str(self.chain_name)
        result["status"] = from_str(self.status)
        result["network_type"] = from_str(self.network_type)
        result["pretty_name"] = from_str(self.pretty_name)
        result["chain_id"] = from_str(self.chain_id)
        result["bech32_prefix"] = from_str(self.bech32_prefix)
        result["slip44"] = from_int(self.slip44)
        result["genesis"] = to_class(Genesis, self.genesis)
        result["codebase"] = to_class(Codebase, self.codebase)
        result["daemon_name"] = from_str(self.daemon_name)
        result["node_home"] = from_str(self.node_home)
        result["key_algos"] = from_list(from_str, self.key_algos)
        result["peers"] = to_class(FluffyPeers, self.peers)
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
        result["params"] = to_class(PurpleParams, self.params)
        return result


class Juno:
    repository: Repository
    chain: JunoChain

    def __init__(self, repository: Repository, chain: JunoChain) -> None:
        self.repository = repository
        self.chain = chain

    @staticmethod
    def from_dict(obj: Any) -> 'Juno':
        assert isinstance(obj, dict)
        repository = Repository.from_dict(obj.get("repository"))
        chain = JunoChain.from_dict(obj.get("chain"))
        return Juno(repository, chain)

    def to_dict(self) -> dict:
        result: dict = {}
        result["repository"] = to_class(Repository, self.repository)
        result["chain"] = to_class(JunoChain, self.chain)
        return result


class FluffyParams:
    authz: bool
    actual_block_time: float
    actual_blocks_per_year: float
    unbonding_time: int
    max_validators: int
    bonded_ratio: float
    minting_epoch_provision: float
    epoch_duration: int
    year_minting_provision: int
    bonded_tokens: str
    total_supply: str
    base_inflation: float
    calculated_apr: float

    def __init__(self, authz: bool, actual_block_time: float, actual_blocks_per_year: float, unbonding_time: int, max_validators: int, bonded_ratio: float, minting_epoch_provision: float, epoch_duration: int, year_minting_provision: int, bonded_tokens: str, total_supply: str, base_inflation: float, calculated_apr: float) -> None:
        self.authz = authz
        self.actual_block_time = actual_block_time
        self.actual_blocks_per_year = actual_blocks_per_year
        self.unbonding_time = unbonding_time
        self.max_validators = max_validators
        self.bonded_ratio = bonded_ratio
        self.minting_epoch_provision = minting_epoch_provision
        self.epoch_duration = epoch_duration
        self.year_minting_provision = year_minting_provision
        self.bonded_tokens = bonded_tokens
        self.total_supply = total_supply
        self.base_inflation = base_inflation
        self.calculated_apr = calculated_apr

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyParams':
        assert isinstance(obj, dict)
        authz = from_bool(obj.get("authz"))
        actual_block_time = from_float(obj.get("actual_block_time"))
        actual_blocks_per_year = from_float(obj.get("actual_blocks_per_year"))
        unbonding_time = from_int(obj.get("unbonding_time"))
        max_validators = from_int(obj.get("max_validators"))
        bonded_ratio = from_float(obj.get("bonded_ratio"))
        minting_epoch_provision = from_float(obj.get("minting_epoch_provision"))
        epoch_duration = from_int(obj.get("epoch_duration"))
        year_minting_provision = from_int(obj.get("year_minting_provision"))
        bonded_tokens = from_str(obj.get("bonded_tokens"))
        total_supply = from_str(obj.get("total_supply"))
        base_inflation = from_float(obj.get("base_inflation"))
        calculated_apr = from_float(obj.get("calculated_apr"))
        return FluffyParams(authz, actual_block_time, actual_blocks_per_year, unbonding_time, max_validators, bonded_ratio, minting_epoch_provision, epoch_duration, year_minting_provision, bonded_tokens, total_supply, base_inflation, calculated_apr)

    def to_dict(self) -> dict:
        result: dict = {}
        result["authz"] = from_bool(self.authz)
        result["actual_block_time"] = to_float(self.actual_block_time)
        result["actual_blocks_per_year"] = to_float(self.actual_blocks_per_year)
        result["unbonding_time"] = from_int(self.unbonding_time)
        result["max_validators"] = from_int(self.max_validators)
        result["bonded_ratio"] = to_float(self.bonded_ratio)
        result["minting_epoch_provision"] = to_float(self.minting_epoch_provision)
        result["epoch_duration"] = from_int(self.epoch_duration)
        result["year_minting_provision"] = from_int(self.year_minting_provision)
        result["bonded_tokens"] = from_str(self.bonded_tokens)
        result["total_supply"] = from_str(self.total_supply)
        result["base_inflation"] = to_float(self.base_inflation)
        result["calculated_apr"] = to_float(self.calculated_apr)
        return result


class TentacledPeers:
    seeds: List[Seed]
    persistent_peers: List[Seed]

    def __init__(self, seeds: List[Seed], persistent_peers: List[Seed]) -> None:
        self.seeds = seeds
        self.persistent_peers = persistent_peers

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledPeers':
        assert isinstance(obj, dict)
        seeds = from_list(Seed.from_dict, obj.get("seeds"))
        persistent_peers = from_list(Seed.from_dict, obj.get("persistent_peers"))
        return TentacledPeers(seeds, persistent_peers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["seeds"] = from_list(lambda x: to_class(Seed, x), self.seeds)
        result["persistent_peers"] = from_list(lambda x: to_class(Seed, x), self.persistent_peers)
        return result


class OsmosisChain:
    schema: str
    chain_name: str
    status: str
    network_type: str
    pretty_name: str
    chain_id: str
    bech32_prefix: str
    daemon_name: str
    node_home: str
    genesis: Genesis
    key_algos: List[str]
    slip44: int
    fees: Fees
    codebase: Codebase
    peers: TentacledPeers
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

    def __init__(self, schema: str, chain_name: str, status: str, network_type: str, pretty_name: str, chain_id: str, bech32_prefix: str, daemon_name: str, node_home: str, genesis: Genesis, key_algos: List[str], slip44: int, fees: Fees, codebase: Codebase, peers: TentacledPeers, apis: Apis, explorers: List[Explorer], name: str, path: str, symbol: str, denom: str, decimals: int, coingecko_id: str, image: str, height: int, best_apis: BestApis, params: FluffyParams) -> None:
        self.schema = schema
        self.chain_name = chain_name
        self.status = status
        self.network_type = network_type
        self.pretty_name = pretty_name
        self.chain_id = chain_id
        self.bech32_prefix = bech32_prefix
        self.daemon_name = daemon_name
        self.node_home = node_home
        self.genesis = genesis
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
    def from_dict(obj: Any) -> 'OsmosisChain':
        assert isinstance(obj, dict)
        schema = from_str(obj.get("$schema"))
        chain_name = from_str(obj.get("chain_name"))
        status = from_str(obj.get("status"))
        network_type = from_str(obj.get("network_type"))
        pretty_name = from_str(obj.get("pretty_name"))
        chain_id = from_str(obj.get("chain_id"))
        bech32_prefix = from_str(obj.get("bech32_prefix"))
        daemon_name = from_str(obj.get("daemon_name"))
        node_home = from_str(obj.get("node_home"))
        genesis = Genesis.from_dict(obj.get("genesis"))
        key_algos = from_list(from_str, obj.get("key_algos"))
        slip44 = from_int(obj.get("slip44"))
        fees = Fees.from_dict(obj.get("fees"))
        codebase = Codebase.from_dict(obj.get("codebase"))
        peers = TentacledPeers.from_dict(obj.get("peers"))
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
        return OsmosisChain(schema, chain_name, status, network_type, pretty_name, chain_id, bech32_prefix, daemon_name, node_home, genesis, key_algos, slip44, fees, codebase, peers, apis, explorers, name, path, symbol, denom, decimals, coingecko_id, image, height, best_apis, params)

    def to_dict(self) -> dict:
        result: dict = {}
        result["$schema"] = from_str(self.schema)
        result["chain_name"] = from_str(self.chain_name)
        result["status"] = from_str(self.status)
        result["network_type"] = from_str(self.network_type)
        result["pretty_name"] = from_str(self.pretty_name)
        result["chain_id"] = from_str(self.chain_id)
        result["bech32_prefix"] = from_str(self.bech32_prefix)
        result["daemon_name"] = from_str(self.daemon_name)
        result["node_home"] = from_str(self.node_home)
        result["genesis"] = to_class(Genesis, self.genesis)
        result["key_algos"] = from_list(from_str, self.key_algos)
        result["slip44"] = from_int(self.slip44)
        result["fees"] = to_class(Fees, self.fees)
        result["codebase"] = to_class(Codebase, self.codebase)
        result["peers"] = to_class(TentacledPeers, self.peers)
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


class Osmosis:
    repository: Repository
    chain: OsmosisChain

    def __init__(self, repository: Repository, chain: OsmosisChain) -> None:
        self.repository = repository
        self.chain = chain

    @staticmethod
    def from_dict(obj: Any) -> 'Osmosis':
        assert isinstance(obj, dict)
        repository = Repository.from_dict(obj.get("repository"))
        chain = OsmosisChain.from_dict(obj.get("chain"))
        return Osmosis(repository, chain)

    def to_dict(self) -> dict:
        result: dict = {}
        result["repository"] = to_class(Repository, self.repository)
        result["chain"] = to_class(OsmosisChain, self.chain)
        return result


def cosmoshub_from_dict(s: Any) -> Cosmoshub:
    return Cosmoshub.from_dict(s)


def cosmoshub_to_dict(x: Cosmoshub) -> Any:
    return to_class(Cosmoshub, x)


def juno_from_dict(s: Any) -> Juno:
    return Juno.from_dict(s)


def juno_to_dict(x: Juno) -> Any:
    return to_class(Juno, x)


def osmosis_from_dict(s: Any) -> Osmosis:
    return Osmosis.from_dict(s)


def osmosis_to_dict(x: Osmosis) -> Any:
    return to_class(Osmosis, x)
