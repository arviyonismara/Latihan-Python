# fungsi dari __init__ adalah untuk memberitahu bahwa suatu module adalah milik parent/parent

from . import basic
from . import scientific

from .basic import tambah,kali
from .scientific import pangkat