# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = index_from_dict(json.loads(json_string))

from typing import Any, Union, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


class Chain:
    name: str
    address: str
    restake: Union[bool, str]

    def __init__(self, name: str, address: str, restake: Union[bool, str]) -> None:
        self.name = name
        self.address = address
        self.restake = restake

    @staticmethod
    def from_dict(obj: Any) -> 'Chain':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        address = from_str(obj.get("address"))
        restake = from_union([from_bool, from_str], obj.get("restake"))
        return Chain(name, address, restake)

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


class Validator:
    path: str
    name: str
    identity: str
    chains: List[Chain]
    profile: Profile

    def __init__(self, path: str, name: str, identity: str, chains: List[Chain], profile: Profile) -> None:
        self.path = path
        self.name = name
        self.identity = identity
        self.chains = chains
        self.profile = profile

    @staticmethod
    def from_dict(obj: Any) -> 'Validator':
        assert isinstance(obj, dict)
        path = from_str(obj.get("path"))
        name = from_str(obj.get("name"))
        identity = from_str(obj.get("identity"))
        chains = from_list(Chain.from_dict, obj.get("chains"))
        profile = Profile.from_dict(obj.get("profile"))
        return Validator(path, name, identity, chains, profile)

    def to_dict(self) -> dict:
        result: dict = {}
        result["path"] = from_str(self.path)
        result["name"] = from_str(self.name)
        result["identity"] = from_str(self.identity)
        result["chains"] = from_list(lambda x: to_class(Chain, x), self.chains)
        result["profile"] = to_class(Profile, self.profile)
        return result


class Index:
    repository: Repository
    validators: List[Validator]

    def __init__(self, repository: Repository, validators: List[Validator]) -> None:
        self.repository = repository
        self.validators = validators

    @staticmethod
    def from_dict(obj: Any) -> 'Index':
        assert isinstance(obj, dict)
        repository = Repository.from_dict(obj.get("repository"))
        validators = from_list(Validator.from_dict, obj.get("validators"))
        return Index(repository, validators)

    def to_dict(self) -> dict:
        result: dict = {}
        result["repository"] = to_class(Repository, self.repository)
        result["validators"] = from_list(lambda x: to_class(Validator, x), self.validators)
        return result


def index_from_dict(s: Any) -> Index:
    return Index.from_dict(s)


def index_to_dict(x: Index) -> Any:
    return to_class(Index, x)
