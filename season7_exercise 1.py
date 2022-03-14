def get_gheymat_float(gheymat):
    x=gheymat.index(',')
    if x==-1:
        return float(gheymat)
    else:
        gheymat_float=gheymat[:x]+gheymat[x+1:]
        return float(gheymat_float)
import requests

r=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
gheymat=(r.json()['bpi']['USD']['rate'])
print(get_gheymat_float(gheymat))