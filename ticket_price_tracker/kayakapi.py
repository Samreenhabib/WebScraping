import requests
import asyncio
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import httpx
cookies = {
    'Apache': 'JACtwQRgugBx13XXsfT0ig-AAABh5Xtzt0-c4-be88AQ',
    'kayak': 'x20fuUdOVYX$nPjPHa5c',
    'kmkid': 'AmFh-l2pEQqxbuSgFN8mBpo',
    'csid': '9fc12574-f0d8-4684-a987-5bc0fa315610',
    '_gcl_au': '1.1.499255299.1681847609',
    '_fbp': 'fb.1.1681847609000.0.7848209989546207',
    '__gads': 'ID=4d9d8cc9c567363c:T=1681847652:S=ALNI_MZrrtt1FYbQs336Da-PnUIRL0Rrbw',
    'tracker_device': '902e2739-366b-43d8-831b-048bc6788811',
    'fs_uid': '#14RXH0#4640800297963520:6125049620451328:::#9ce09663#/1713552856',
    'g_state': '{"i_p":1682621707974,"i_l":3}',
    'cluster': '5',
    'p1.med.sid': 'R-5xNcK9jW_eMuhLKkhaJbN-zuMjLDBx_P_R_AkddX1nLdnax_IGrbRwx2_sKB5Pr',
    'kayak.mc': 'AfpeLNKAfGP8XbQYjn5BP6v3FQdii2fNWkmtyM7tZ9uQrXUoCbxwhlh5_YCIFX8yUeNze24Hq0Zwu07SqNyLt5WJ0vDfZTNGJHXLShWgsQQnQ1gl2vGdcPF64H3JgaJ84KGgYJ_6inUbKnLTkQu-JyzLAhj9w2R38Fj5BWV6OKIUoRcQZTdnbzRBVQ24mARSm49VeFD6jomqR1GJ5iOI3m5M81dwSK8faw2yG3_3zdEDMym1z1HWjlrgU-U2AoQq2k5h8BOM_7-TJYeyNFGV7K6zHFfwkjID7PU_UmPavWsGyljQ1TQU_C18_LeXRILE4v1aByx5-OOTTNvB-MmcIxaTU_0q3w9UJzSH47ts-yasZM33g2Ic38_Oe9B0XAAqa5YtSjOMsZzOxRkl34ZgrXyaThzHLuMCArGBnqdmUGK8MPD5YRfL7MBtk9nRBalULuReNIXvitTrGkuqZTr_lBwp4eJsuCA9nL3J3NPhuHCDhDWc3QSy5gO3Zf7P6cqlHTk7dUlB1RRL-9KCFGhzVlM',
    'amp_6e403e': 'PvZvDXgmLNKaN-VuRh0uK2.c2FtcmVlbmgyQGdtYWlsLmNvbQ==..1gug7nn18.1gug7nn19.0.5.5',
    '_uetsid': 'b125d200de2211ed8d1a390ecf8560fd',
    '_uetvid': 'b1261330de2211edb19e27640256af3d',
    'mst_ADIrlA': 'zKHA5bDTrD3ar_6wP6ybpxITQPtIagLa486H4NuFGUwZgF78M1WSN3ClIVSRW2JWzMgBn7BakmbzAvbNZtUQ7NUlQRRwKNbAEsyiqzwt-zE',
    '__gpi': 'UID=00000c04d3b3c8af:T=1681847652:RT=1682024690:S=ALNI_MabWMPn_QDvo_6I285MZjjykbgcSA',
    'mst_iBfK2w': 'u3TSwSXGLxhFbDy40ZDlaJ5k1d1kTmCUKXmL2zBVLsgZgF78M1WSN3ClIVSRW2JWwPWuqPqfZJc1D6TKSIAH7l9lJ60cMvPIfdH008zNkzA',
    'hiddenParamsKHI-SYD%2F2023-05-05': 'id=1682024677&page_origin=F..RP..M0&src=&searchingagain=&c2s=&po=&personality=&provider=-1&pageType=RP',
}

headers = {
    'authority': 'www.kayak.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ur;q=0.8',
    # 'cookie': 'Apache=JACtwQRgugBx13XXsfT0ig-AAABh5Xtzt0-c4-be88AQ; kayak=x20fuUdOVYX$nPjPHa5c; kmkid=AmFh-l2pEQqxbuSgFN8mBpo; csid=9fc12574-f0d8-4684-a987-5bc0fa315610; _gcl_au=1.1.499255299.1681847609; _fbp=fb.1.1681847609000.0.7848209989546207; __gads=ID=4d9d8cc9c567363c:T=1681847652:S=ALNI_MZrrtt1FYbQs336Da-PnUIRL0Rrbw; tracker_device=902e2739-366b-43d8-831b-048bc6788811; fs_uid=#14RXH0#4640800297963520:6125049620451328:::#9ce09663#/1713552856; g_state={"i_p":1682621707974,"i_l":3}; cluster=5; p1.med.sid=R-5xNcK9jW_eMuhLKkhaJbN-zuMjLDBx_P_R_AkddX1nLdnax_IGrbRwx2_sKB5Pr; kayak.mc=AfpeLNKAfGP8XbQYjn5BP6v3FQdii2fNWkmtyM7tZ9uQrXUoCbxwhlh5_YCIFX8yUeNze24Hq0Zwu07SqNyLt5WJ0vDfZTNGJHXLShWgsQQnQ1gl2vGdcPF64H3JgaJ84KGgYJ_6inUbKnLTkQu-JyzLAhj9w2R38Fj5BWV6OKIUoRcQZTdnbzRBVQ24mARSm49VeFD6jomqR1GJ5iOI3m5M81dwSK8faw2yG3_3zdEDMym1z1HWjlrgU-U2AoQq2k5h8BOM_7-TJYeyNFGV7K6zHFfwkjID7PU_UmPavWsGyljQ1TQU_C18_LeXRILE4v1aByx5-OOTTNvB-MmcIxaTU_0q3w9UJzSH47ts-yasZM33g2Ic38_Oe9B0XAAqa5YtSjOMsZzOxRkl34ZgrXyaThzHLuMCArGBnqdmUGK8MPD5YRfL7MBtk9nRBalULuReNIXvitTrGkuqZTr_lBwp4eJsuCA9nL3J3NPhuHCDhDWc3QSy5gO3Zf7P6cqlHTk7dUlB1RRL-9KCFGhzVlM; amp_6e403e=PvZvDXgmLNKaN-VuRh0uK2.c2FtcmVlbmgyQGdtYWlsLmNvbQ==..1gug7nn18.1gug7nn19.0.5.5; _uetsid=b125d200de2211ed8d1a390ecf8560fd; _uetvid=b1261330de2211edb19e27640256af3d; mst_ADIrlA=zKHA5bDTrD3ar_6wP6ybpxITQPtIagLa486H4NuFGUwZgF78M1WSN3ClIVSRW2JWzMgBn7BakmbzAvbNZtUQ7NUlQRRwKNbAEsyiqzwt-zE; __gpi=UID=00000c04d3b3c8af:T=1681847652:RT=1682024690:S=ALNI_MabWMPn_QDvo_6I285MZjjykbgcSA; mst_iBfK2w=u3TSwSXGLxhFbDy40ZDlaJ5k1d1kTmCUKXmL2zBVLsgZgF78M1WSN3ClIVSRW2JWwPWuqPqfZJc1D6TKSIAH7l9lJ60cMvPIfdH008zNkzA; hiddenParamsKHI-SYD%2F2023-05-05=id=1682024677&page_origin=F..RP..M0&src=&searchingagain=&c2s=&po=&personality=&provider=-1&pageType=RP',
    'referer': 'https://www.kayak.com/flights/KHI-SYD/2023-05-05?sort=bestflight_a',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}
# async def scrape_website(url, headers):
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=headers)
#         response.raise_for_status()
#         html = response.text
        
#     soup = BeautifulSoup(html, 'html.parser')
#     # elements = soup.find_all(class_='your-class-name')
    
#     return soup

# async def main():
#     url = 'https://www.kayak.com/flights/KHI-SYD/2023-05-05?sort=price_a'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
#         'Accept-Language': 'en-US,en;q=0.9',
#     }

url = 'https://www.kayak.com/security/check?out=%2Fflights%2FKHI-SYD%2F2023-05-05%3Fsort%3Dprice_a'
with httpx.Client() as client:
    response = client.get(url, headers=headers, cookies=cookies)
    
    if response.status_code == 302:
        redirect_url = response.headers['Location']
        response = client.get(redirect_url, headers=headers)

    response.raise_for_status()
    html = response.text
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
