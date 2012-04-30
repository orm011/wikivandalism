from wkv_common import *

def ip_to_country(ip_addr_string):
    try:
        ans = requests.get("http://freegeoip.net/json/" + ip_addr_string)
    except:
        raise Exception("error in request:" + "http://freegeoip.net/json/" + ip_addr_string)

    if ans.ok:
        return str(simplejson.loads(ans.text).get('country_code'))
    else:
        raise Exception(ans.__str__())

        

def test_ip_to_country():
    assert ip_to_country("18.18.18.18") == "US"
    
