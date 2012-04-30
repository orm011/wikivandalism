from wkv_common import *
import countries

def ip_to_country(ip_addr_string):
    req = "http://freegeoip.net/json/" + ip_addr_string
    #teehee, not really a wikipedia req.
    ans = simplejson.loads(make_wikipedia_request(req))
    return str(ans.get('country_code'))



def get_continent(ip_addr_string):
    country = ip_to_country(ip_addr_string)
    if countries.continents.has_key(country):
        return countries.continents.get(country)
    else:
        raise Exception("unknown country code")

def ip_is_asia(ip_addr_string):
    return get_continent(ip_addr_string) == 'AS'

def ip_is_north_america(ip_addr_string):
    return get_continent(ip_addr_string) == 'NA'

def ip_is_europe(ip_addr_string):
    return get_continent(ip_addr_string) == 'EU'

def test_ip_to_country():
    assert ip_to_country("18.18.18.18") == "US"
    assert ip_is_asia("123.125.114.144") #baidu.com
    assert ip_to_country("95.131.168.181") == "ES" #tuenti.com
    assert ip_is_europe("95.131.168.181") 
    assert ip_is_north_america("65.52.109.147") #prensalibre.com.gt

    
