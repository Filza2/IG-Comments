try:
    import re
    from time import sleep 
    from requests import post,get
    from colorama import Fore
except ModuleNotFoundError:exit(f"[!] Module Missing !")
done,error=0,0
print(f"""
{Fore.LIGHTMAGENTA_EX}
██╗ ██████╗        ██████╗███╗   ███╗
██║██╔════╝       ██╔════╝████╗ ████║
██║██║  ███╗█████ ██║     ██╔████╔██║
██║██║   ██║╚════ ██║     ██║╚██╔╝██║
██║╚██████╔╝      ╚██████╗██║ ╚═╝ ██║
╚═╝ ╚═════╝        ╚═════╝╚═╝     ╚═╝{Fore.RESET}
       By @TweakPY - @vv1ck""")
print("=====================================")
user=input(f"[{Fore.RED}?{Fore.WHITE}] username : ")
pess=input(f"[{Fore.RED}?{Fore.WHITE}] Password : ")
comment=input(f"[{Fore.RED}?{Fore.WHITE}] Your text : ")
purl=input(f"[{Fore.RED}?{Fore.WHITE}] Post URL : ")
print("=====================================")
rlogin=post('https://i.instagram.com/api/v1/web/accounts/login/ajax/',headers={'Host': 'i.instagram.com','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Csrftoken': '5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect','X-Instagram-Ajax': '1d6caaf37cd2','X-Ig-App-Id': '936619743392459','X-Asbd-Id': '437806','X-Ig-Www-Claim': '0','Content-Type': 'application/x-www-form-urlencoded','Content-Length': '311','Origin': 'https://www.instagram.com','Referer': 'https://www.instagram.com/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Te': 'trailers'},data={'username': user,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{pess}','queryParams': "{}",'optIntoOneTap': 'false','stopDeletionNonce ': "",'trustedDeviceRecords': "{}"})
if ("userId") in rlogin.text:
    sis=rlogin.cookies['sessionid']
    usrid=rlogin.cookies['ds_user_id']
    csrftoken=rlogin.cookies['csrftoken']
    try:
        rpostid=get(purl,headers={'Host': 'www.instagram.com','Cookie': f'ig_did=48DF9A55-3AE0-4E69-A2BF-C3BA619FC3A9; datr=fokcha5d_g_EJAFfBYIhAV; mid=YUwsIgAEAAE9dTZpLC77ShIUfgML; ig_nrcb=1; rur="ASH\05453382614549\0541693349501:01f77a483f0e1591d09b1a21b5d5f3e01f11b384c6ee15042c3618e207a9a5cc01ba05bf"; csrftoken={csrftoken}; ds_user_id={usrid}; sessionid={sis}; shbid="13700\05453382614549\0541693349216:01f72e7c5b641a124b38c18103ae9b992019b2f00c6ecdab7e084600776e5ef1224eafc4"; shbts="1661813216\05453382614549\0541693349216:01f75811021cf843330153d64bf420990df41e31150967eff0d36935abe411d4b57fb350"','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Cache-Control': 'max-age=0','Te': 'trailers'})
        post_web_id=str(re.findall('"media_id":"(.*?)",',rpostid.text)[0]).split(',')[0]
    except:
        print(Fore.RED+'[!] Failed , Error in video/Post URL  !')
        print(Fore.YELLOW+'[!] You can try now Enter Post id Manually ..\n')
        print(Fore.RED+'[!] Note , You can retry post url if you dont know post id -Need restart the tool\n\n')
        post_web_id=input(f'[{Fore.RED}?{Fore.WHITE}] Post id : ')
    while True:
        sleep(7.1)#sleep - time between sending comments
        rcm=post(f'https://i.instagram.com/api/v1/web/comments/{post_web_id}/add/',headers={'Host': 'i.instagram.com','Cookie': f'ig_did=48DF9A55-3AE0-4E69-A2BF-C3BA619FC3A9; datr=focKY2lS1iM_g_EvWfBYIhAV; mid=YUwsIgAEAAE9dTZpLC77ShIUfgML; ig_nrcb=1; rur="ASH\05453382614549\0541693349258:01f7a49e91d4e68a931a0d36868392ac3b80c726ec6fbec5f08cc9e519ecadfb7eae5014"; csrftoken={csrftoken}; ds_user_id={usrid}; sessionid={sis}; shbid="13700\05453382614549\0541693349216:01f72e7c5b641a124b38c18103ae9b992019b2f00c6ecdab7e084600776e5ef1224eafc4"; shbts="1661813216\05453382614549\0541693349216:01f75811021cf843330153d64bf420990df41e31150967eff0d36935abe411d4b57fb350"','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Csrftoken': f'{csrftoken}','X-Instagram-Ajax': '8156e35dd9ba','X-Ig-App-Id': '936619743392459','X-Asbd-Id': '198387','X-Ig-Www-Claim': '0','Content-Type': 'application/x-www-form-urlencoded','Content-Length': '24','Origin': 'https://www.instagram.com','Referer': 'https://www.instagram.com/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same'},data=f'comment_text={comment}')
        if '"status":"ok"' in rcm.text:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET}',end=' ')
            done+=1
        elif 'Please' in rcm.text:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET}',end='')
            error+=1
        elif '"status":"fail"' in rcm.text:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET}',end='')
            error+=1
        elif 'feedback_title' in rcm.text:print(f"{Fore.RED}[!] {rcm.json()['feedback_title']} , Feed Back Message : {rcm.json()['feedback_message']} , ");exit()
        elif '"spam":true' in rcm.text:exit('[!] Try Again Later , spam_comments **ban')
        else:exit('[!] Error ...')
elif ("two_factor") in rlogin.text:exit('[!] Binary verification !')
elif ("checkpoint_url") in rlogin.text:exit('[!] Account Secure !')
else:exit('[!] The username or password is wrong !')
