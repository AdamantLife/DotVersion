## Builtin Modules
import itertools

## Third Party Modules
from al_decorators import SignatureDecorator

def _caststring(bargs):
    """ Used to convert the first non-self arg for a function into a DotVersion
        (by first casting as string and then to DotVersion). """
    if bargs.args:
        for k,v in bargs.arguments.items():
            if k == "self": continue
            break
        try: v = DotVersion(str(v))
        except: pass
        else:
            bargs.arguments[k] = v

class DotVersion():
    """A container class to allow for easy comparisons between versions with dot-dilineation (i.e.- 1.2.03.40) """
    _version = "0"
    caststring_factory = SignatureDecorator.factory(_caststring)
    def expand(version):
        return [int(ver) for ver in version.split(".")]
    def __init__(self,version):
        self.version = version
    @property
    def version(self):
        return self._version
    @version.setter
    def version(self,version):
        try: DotVersion.expand(str(version))
        except:
            raise ValueError("Invalid Version Number")
        else:
            self._version = str(version)
    @property
    def expanded(self):
        return DotVersion.expand(self.version)
        
    @caststring_factory
    def __eq__(self,other):
        if isinstance(other,DotVersion):
            for v1,v2 in itertools.zip_longest(self.expanded,other.expanded,fillvalue = 0):
                ## If any pairing doesn't match, the DotVersions are not equal
                if v1!=v2: return False
            return True
        return NotImplemented
    @caststring_factory
    def __lt__(self,other):
        if isinstance(other,DotVersion):
            for v1,v2 in itertools.zip_longest(self.expanded,other.expanded,fillvalue = 0):
                ## If v1 is greater than v2 (wherever it is), then the whole DotVersion is not Less
                if v1 > v2: return False
                ## If v1  is less than v2 (wherever it is), then the whole DotVersion is less
                if v1 < v2: return True
                ## The alternative is that the current index is the same,
                ## in which case continue to the next index
            return False
        return NotImplemented
    @caststring_factory
    def __le__(self,other):
        op_result = self == other
        return op_result if op_result is NotImplemented else op_result or self < other
    def __gt__(self,other):
        op_result = self <= other
        return op_result if op_result is NotImplemented else not op_result
    def __ge__(self,other):
        op_result = self < other
        return op_result if op_result is NotImplemented else not op_result
    @caststring_factory
    def __add__(self,other):
        if isinstance(other,DotVersion):
            out = []
            for v1,v2 in itertools.zip_longest(self.expanded, other.expanded, fillvalue = 0):
                out.append(str(v1+v2))
            return DotVersion(".".join(out))
        return NotImplemented
    @caststring_factory
    def __radd__(self,other):
        return self + other

    def __hash__(self):
        return hash(str(self))
    def __str__(self):
        return self.version
    def __repr__(self):
        return f"{self.__class__.__name__}({self.version})"
