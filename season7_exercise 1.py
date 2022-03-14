def get_gheymat_float(gheymat):
    x=gheymat.index(',')
    if x==-1:
        return float(gheymat)
    else:
        gheymat_float=gheymat[:x]+gheymat[x+1:]
        return float(gheymat_float)

def informize(gheymat):
    api_key="376F337149506F644E6D72314A6E4E59456652423530765851744757702B2F46386F6D324A4562373346303D"
    url="https://api.kavenegar.com/v1/%s/sms/send.json" %api_key
    pay_load={'receptor':'+989013219653','message':'price is %s$'%gheymat}
    respons=requests.post(url,pay_load)
    print(respons)
import requests

r=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
gheymat=(r.json()['bpi']['USD']['rate'])
informize(gheymat)
# print(gheymat)
