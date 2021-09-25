try:
    import re
    from time import sleep 
    from requests import post
    from instabot import Bot
    from colorama import Fore
except Exception as b:exit(f"[!] Download The libs Please:\n{b}")
done=0
b=Bot
error=0
print(f"""
{Fore.LIGHTMAGENTA_EX}██╗ ██████╗       {Fore.MAGENTA} ██████╗███╗   ███╗
{Fore.LIGHTMAGENTA_EX}██║██╔════╝       {Fore.MAGENTA}██╔════╝████╗ ████║
{Fore.LIGHTMAGENTA_EX}██║██║  ███╗█████╗{Fore.MAGENTA}██║     ██╔████╔██║
{Fore.LIGHTMAGENTA_EX}██║██║   ██║╚════╝{Fore.MAGENTA}██║     ██║╚██╔╝██║
{Fore.LIGHTMAGENTA_EX}██║╚██████╔╝      {Fore.MAGENTA}╚██████╗██║ ╚═╝ ██║
{Fore.LIGHTMAGENTA_EX}╚═╝ ╚═════╝        {Fore.MAGENTA}╚═════╝╚═╝     ╚═╝{Fore.RESET}
<\> {Fore.RED}@TweakPY - @vv1ck{Fore.RESET}""")
print("=====================================")
user=input("[+] username: ")
pess=input("[+] Password: ")
tx=input("[+] Your text: ")
Post=input("[+] Post URL: ")
print("=====================================")
idd=b.get_media_id_from_link(b,link=Post)
localid=re.findall('https://www.instagram.com/p/(.*?)/',Post)[0]
slp=int(7.1)
headLG={
    'Host': 'www.instagram.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': '*/*',
    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': '5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect',
    'X-Instagram-AJAX': '1d6caaf37cd2',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '437806',
    'X-IG-WWW-Claim': '0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '347',
    'Origin': 'https://www.instagram.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/accounts/login/',
    'Cookie': 'ig_did=7B796F1F-ADE7-429C-8ADB-9B131663E5E4; datr=2kDRYNWmjctteBSnOqogPrxv; csrftoken=5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect; mid=YNIa4QALAAGoeESFP8axY9NfC9t3; ig_nrcb=1',
    'TE': 'Trailers'}
go=post('https://www.instagram.com/accounts/login/ajax/',headers=headLG,data={'username': user,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{pess}','queryParams': "{}",'optIntoOneTap': 'false','stopDeletionNonce ': "",'trustedDeviceRecords': "{}"})
if ("userId") in go.text:
    sis=go.cookies['sessionid']
    usrid=go.cookies['ds_user_id']
    csrftoken=go.cookies['csrftoken']
    headCOM={
        'Host': 'www.instagram.com',
        'Cookie': f'ig_did=48DF9A55-3AE0-4E69-A2BF-C3BA619FC3A9; ig_nrcb=1; csrftoken={csrftoken}; mid=YUwsIgAEAAE9dTZpLC77ShIUfgML; rur="LDC\05448404647391\0541664111625:01f73a151d28656485cea3fc4b780ffbb837b548857cdcab6a3eb85722f692a87edc37f1"; ds_user_id={usrid}; sessionid={sis}; shbid="1955\05448404647391\0541664111382:01f79faf21b62dd2ae6ab37e4dcbb62842d01d394831c98c0f2303b8453697380f1ce304"; shbts="1632575382\05448404647391\0541664111382:01f7f86a62d097f4532e8b1496bce7e368d878f71e9ee49828f1035ad6ad15184c80b2a8"',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'X-Csrftoken': f'{csrftoken}',
        'X-Instagram-Ajax': '8156e35dd9ba',
        'X-Ig-App-Id': '936619743392459',
        'X-Asbd-Id': '198387',
        'X-Ig-Www-Claim': 'hmac.AR2YqBSgUuDy5-IC3dy-VRWZmnoU_a2AGY_8JNeBNyHkdTF6',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '47',
        'Origin': 'https://www.instagram.com',
        'Referer': f'https://www.instagram.com/p/{localid}/',
        'Te': 'trailers'}
    while True:
        sleep(slp)
        ct=post(f'https://www.instagram.com/web/comments/{idd}/add/',headers=headCOM,data={'comment_text': tx,'replied_to_comment_id': ''})
        if '"status":"ok"' in ct.text:
            print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET}')
            done+=1
        elif 'Please' in ct.text:
            print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET}')
            error+=1
        else:
            print(f'[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET}')
            error+=1
elif ("two_factor") in go.text:exit('[⛔️] Binary verification !')
elif ("checkpoint_url") in go.text:exit('[⚠️] Account Secure !')
else:exit('[✖️] The username or password or post id is wrong !')