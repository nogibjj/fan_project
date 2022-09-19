from xml.sax.handler import property_interning_dict
from dbtool.dbst import querydb

def test_placeholder():
    pass

def test_connection():
    assert len(querydb()) == 2