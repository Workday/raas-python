from raas.raas import RaaS

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

__all__ = ["RaaS"]

from . import _version
__version__ = _version.get_versions()['version']
