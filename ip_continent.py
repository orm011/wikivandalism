from wkv_common import *

def ip_to_country(ip_addr_string):
    req = "http://freegeoip.net/json/" + ip_addr_string
    #teehee, not really a wikipedia req.
    ans = simplejson.loads(make_wikipedia_request(req))
    return str(ans.get('country_code'))

def test_ip_to_country():
    assert ip_to_country("18.18.18.18") == "US"
    
