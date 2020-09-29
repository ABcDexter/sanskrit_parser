from sanskrit_parser import enable_console_logger
from sanskrit_parser.base.sanskrit_base import SLP1
import sanskrit_parser.generator.ach_sandhi as ach_sandhi
import sanskrit_parser.generator.sutra_engine as sutra
from sanskrit_parser.generator.paninian_object import PaninianObject

import logging
enable_console_logger(logging.DEBUG)

test_list = [
    ("gaRa", "upadeSaH", "gaRopadeSaH"),
    ("rAma", "eti", "rAmEti"),
    ("rAma", "iti", "rAmeti"),
    ("tyaktvA", "uttizTa", "tyaktvottizTa"),
    ("tava", "ozTaH", "tavOzTaH"),
    ("deva", "fzi", "devarzi"),
    ("gavi", "asmAkam", "gavyasmAkam"),
    ("kavI", "etau", "kavyetau"),
    ("gavi", "iha", "gavIha"),
    ("kavI", "iha", "kavIha"),
    ("kavO", "asmAkam", "kavAvasmAkam"),
    ("AgacCa", "atra", "AgacCAtra"),
    ("yAne", "eti", "yAnayeti"),
    ("yAne", "atra", "yAnetra"),
    ("yAne", "AgacCati", "yAnayAgacCati"),
    ("vizRo", "ava", "vizRova"),
    ]


def test_static():
    for s in test_list:
        l = PaninianObject(s[0], SLP1)
        r = PaninianObject(s[1], SLP1)
        r = sutra.SutraEngine.sandhi(l, r, sandhi_sutra_list)
        assert ("".join([_r.canonical() for _r in list(r)])==s[2])

sandhi_sutra_list = ach_sandhi.sutra_list
test_static()
