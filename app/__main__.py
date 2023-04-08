"""
Main app module for running all spiders
"""
from addressbg import AddressbgSpider
from arcoreal import ArcorealSpider
from avista import AvistaSpider
from bezkomisiona import BezkomisionaSpider
from bulgarianproperties import BulgarianpropertiesSpider
from era import EraSpider
from imotbg import ImotbgSpider
from imoti import ImotiSpider
from luximmo import LuximmoSpider
from mirelabg import MirelabgSpider
from novdom1 import Novdom1Spider
from place2live import Place2liveSpider
from primoplus import PrimoplusSpider
from superimoti import SuperimotiSpider
from ues import UesSpider
from yourhome import YourhomeSpider
from run_spiders import execute


spider_list = [AddressbgSpider, ArcorealSpider, AvistaSpider, BezkomisionaSpider, BulgarianpropertiesSpider,
               EraSpider, ImotbgSpider, LuximmoSpider, MirelabgSpider, Novdom1Spider, Place2liveSpider,
               PrimoplusSpider, SuperimotiSpider, UesSpider, YourhomeSpider, ImotiSpider]


execute(spider_list=spider_list)
