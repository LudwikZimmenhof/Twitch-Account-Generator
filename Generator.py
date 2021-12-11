import requests
import json
import speech_recognition as sr
import random
import string
import os
import subprocess
import re
import imaplib
import email
import time
import uuid
import threading
import glob
import os
import glob
import base64


version = "1.0.0"


xD = """
SERIOUSLY?
Okay, okay.
But
Think about whether or not you want to do this.
You know, if you share it, there might not be any more updates.
Believe me I spent a lot of time on this so please keep it to yourself. :3
"""

def error(error):
    open('error.txt', 'a').write(error + '\n\n')


class Login():
    key = None
        
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


def get_windows_uuid():
    try:
        txt = subprocess.check_output("wmic csproduct get uuid").decode()
        match = re.search(r"\bUUID\b[\s\r\n]+([^\s\r\n]+)", txt)
        if match is not None:
            txt = match.group(1)
            if txt is not None:
                txt = re.sub(r"[^0-9A-Fa-f]+", "", txt)
                if len(txt) == 32:
                    return uuid.UUID(txt)
    except:
        None
        

def login(key):
    session = requests.session()
    x = session.get(f"http://51.178.2.109:10000/api/v1/bypass/auth?key={key}&hwid=" + str(get_windows_uuid())).text
    
    if x == "unauthorized":
        return "false"
    elif x == "authorized":
        return "true"
    else: 
        return "false"
    
def cls():
    os.system('cls')
    
class stats:
    gened = 0
    invalid = 0
    hits = 0


    
class th():
    acctive = 0
    now = 0
    proxy = None
    veryfi = None
    
    
def gen():


    captcha = ("captcha-" + ((''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(10)))))
    folder = f'data/{captcha}.wav'
    
    try:

        lines = open('useragents.txt').read().splitlines()
        userAgent =random.choice(lines)

        lines = open('proxy.txt').read().splitlines()
        prox1 =random.choice(lines)
        xtype = str(th.proxy)
        session = requests.Session()
        proxies_paid = {'https': f'{xtype}://{prox1}'}
        
        url = "https://nojs-game3-prod-eu-west-1.arkoselabs.com/fc/api/nojs/?pkey=E5554D43-23CC-1982-971D-6A2262A2CA24&lang=eng"
        headers = {
        'user-agent': userAgent,
        'Referer': 'https://www.twitch.tv/signup',
        'Origin': 'https://www.twitch.tv'
        }

        x = session.post(url, headers=headers, proxies=proxies_paid, timeout=20).text
        start = x.find('name="session-token" value="') + 28
        end = x.find('"', start)
        id = x[start:end]
        
        try:
            headers = {
            'user-agent': userAgent
            }
            x = session.get(f'https://api.funcaptcha.com/fc/get_audio/?session_token={id}&analytics_tier=40&r=eu-west-1&game=0&language=eng&d=1', headers=headers ,proxies=proxies_paid, timeout=20)
            open(folder, 'wb').write(x.content)
                

            sample_audio = sr.AudioFile(folder)
            r = sr.Recognizer()
            
            with sample_audio as source:
                audio = r.record(source)
            key = r.recognize_google(audio)

                
            x = key.replace("-", "")
            x = x.replace(" ", "")
            numeric_filter = filter(str.isdigit, x)
            anser = "".join(numeric_filter)
            numbers = sum(c.isdigit() for c in anser)
            
            os.remove(folder)

                
            if int(numbers) > 3 and int(numbers) < 10:

                headers = {'user-agent': userAgent,}
                url = "https://client-api.arkoselabs.com/fc/audio/"
                data = {'session_token':id, 'language':'eng', 'r':'us-west-2', 'audio_type':2, 'response':anser, 'analytics_tier':40}

                x = session.post(url=url,data=data, proxies=proxies_paid, timeout=20)

                if x.json()['response'] == 'correct':
                    def validate_username():
                                            
                                            linesx = open('username.txt', encoding="utf8").read().splitlines()
                                            username =random.choice(linesx)
                                            ints = ['1','2','3','4','5','6','7','8','9']
                                            if th.veryfi == "y":
                                                mailx = ((''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(12))) + "@oxytool.net")
                                            elif th.veryfi == "n":
                                                mailx = ((''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(12))) + "@gmail.com")
                                            nickname = username + (''.join(random.SystemRandom().choice(ints) for _ in range(random.randint(2, 6))) + ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(1)))
                                            haslo1 = ((''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(12))) + (''.join(random.SystemRandom().choice(string.ascii_uppercase)) ))             
                                            bio = "OXYPASS | " + (''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(4)))
                                            session = requests.session()
                                            
                                       
                                            data = [{
                                                "operationName": "UsernameValidator_User",
                                                "extensions": {
                                                    "persistedQuery": {
                                                        "sha256Hash": "fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660",
                                                        "version": 1
                                                    }
                                                },
                                                "variables": {
                                                    'username': nickname
                                                }
                                            }]

                                            headers = {
                                                "Accept": "*/*",
                                                "Content-Type": "text/plain;charset=UTF-8",
                                                "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
                                                "Referer": "https://www.twitch.tv/signup",
                                                'sec-fetch-dest': 'empty',
                                                'sec-fetch-mode': 'cors',
                                                'sec-fetch-site': 'same-site',
                                                'X-Device-Id': '25abf78f8feaa150'
                                            }

                                            session = requests.session()
                                            session_result = session.post("https://gql.twitch.tv/gql", data=json.dumps(data), headers=headers, timeout=20)
                                            starte = session_result.text.find('{"isUsernameAvailable":') + 23
                                            ende = session_result.text.find('},', starte)
                                            idd = session_result.text[starte:ende]

                                            print(session_result.text)

                                            if idd == "true":


                                                stats.hits = stats.hits + 1


                                                headers = {
                                                            'user-agent': userAgent,
                                                            'origin': 'https://www.twitch.tv', 'referer': 'https://www.twitch.tv/', 'sec-fetch-dest': 'empty',
                                                            'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site'
                                                            }

                                                data = {
                                                "username": nickname,
                                                "password": haslo1,
                                                "email": mailx,
                                                "birthday": {
                                                "day": random.randint(1, 28),
                                                "month": random.randint(3, 12),
                                                "year": random.randint(1980, 2000),
                                                },
                                                "client_id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
                                                "arkose": {
                                                "token": f"{id}|r=us-west-2|metabgclr=transparent|guitextcolor=%23000000|metaiconclr=%23757575|meta=3|lang=en|pk=E5554D43-23CC-1982-971D-6A2262A2CA24|at=40|sup=1|rid=25|atp=2|cdn_url=https://cdn.arkoselabs.com/fc|lurl=https://audio-us-west-2.arkoselabs.com|surl=https://client-api.arkoselabs.com"
                                                }}

                                                session_result = session.post("https://passport.twitch.tv/register",data=json.dumps(data),headers=headers,timeout=20, proxies=proxies_paid)
                                                print(session_result.text)
                                                if 'Please complete the CAPTCHA correctly.' in session_result.text:
                                                    stats.invalid = stats.invalid + 1

                                                if 'access_token' in session_result.text:
                                                    token = session_result.json()['access_token']
                                                    open('token.txt', 'a').write(f'{token}\n')
                                                    open('account.txt', 'a').write(f'{nickname}:{haslo1}\n')
                                                    stats.gened = stats.gened + 1
                                                    
                                                    startp = session_result.text.find('ID":"') + 5
                                                    endp = session_result.text.find('"', startp)
                                                    idp = session_result.text[startp:endp]


                                                
                                                    data = '[{"event":"device_id_debug","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100631,"url":"https://www.twitch.tv/friends","client_time":1637100631.128,"local_storage_device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","client_assigned_device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","device_id_same":"true","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"experiment_branch","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100631.652,"login":nickname,"user_id":idp,"experiment_id":"cef566dc-5836-4f83-8ca6-12839d08426c","experiment_group":"control","experiment_name":"vx_disco_search_suggestions_v1_logged_in","experiment_version":17276,"experiment_type":"user_id","client_app":"twilight","logged_in":"true"}},{"event":"experiment_branch","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100631.689,"login":nickname,"user_id":idp,"experiment_id":"e3f98642-92df-404b-a7eb-21da0473a96b","experiment_group":"control","experiment_name":"kr_jp_string_test","experiment_version":14021,"experiment_type":"user_id","client_app":"twilight","logged_in":"true"}},{"event":"experiment_branch","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100631.714,"login":nickname,"user_id":idp,"experiment_id":"e19f9b03-2c70-4e1b-b33f-3bf73e865f5b","experiment_group":"variant","experiment_name":"vxp_leftnav_nocache","experiment_version":11817,"experiment_type":"device_id","client_app":"twilight","logged_in":"true"}},{"event":"ad_manager_mounted","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100631.727,"client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"experiment_branch","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100631.745,"login":nickname,"user_id":idp,"experiment_id":"7ff6a29e-5681-45ed-ad66-46d35a9549bc","experiment_group":"variant-b","experiment_name":"Twilight Player Core NPM Distribution (Public)","experiment_version":17865,"experiment_type":"device_id","client_app":"twilight","logged_in":"true"}},{"event":"client_availability","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100631.762,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","name":"TopNav__TwitchPrimeCrown","category":"Ability to make a living streaming","is_available":"true","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"client_availability","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100631.762,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","name":"TopNav__BitsButton","category":"Ability to make a living streaming","is_available":"true","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"experiment_branch","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100631.776,"login":nickname,"user_id":idp,"experiment_id":"ce577266-68fa-40eb-8c07-5ae30488338f","experiment_group":"control","experiment_name":"vxp_left_nav_hover_logged_in","experiment_version":11418,"experiment_type":"user_id","client_app":"twilight","logged_in":"true"}},{"event":"pageview","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100631.827,"benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","bornuser":"false","browser":userAgent,"browser_family":"chrome","browser_version":"95.0","collapse_right":"false","collapse_left":"true","localstorage_device_id":"3b8df4f20daf975d","location":"friends.list","page_session_id":"25fa2afd1e00af54","referrer":"https://www.twitch.tv/friends","referrer_domain":"www.twitch.tv","session_device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","theme":"light","viewport_height":961,"viewport_width":818,"client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp,"is_turbo":"false","language":"PL"}},{"event":"benchmark_fetch_start","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100630.434,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","lost_visibility":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_app_booted","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100631.1301,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","lost_visibility":"false","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","time_from_fetch":699,"client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_custom_event","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100631.828,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","benchmark":250,"destination":"friends.list","duration":144,"group":"page","is_app_launch":"true","key":"first-cue","label":"First Paint","lost_visibility":"false","page_component_name":"FriendsPage","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"onboarding_web","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100632.255,"source":"new_signup","action":"start","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"consent_dialog_shown","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100632.344,"consent_session_id":"9ff016f5-d5ff-4bde-b560-b36a519a590a","privacy_law":"GDPR","user_id":idp,"client_app":"twilight","login":nickname,"logged_in":"true"}},{"event":"ad_sdk_declined","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100632.346,"sdk":"AAX","sdk_decline_reason":"no_consent","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_complete_transition","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100632.4318001,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","lost_visibility":"false","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","is_app_launch":"true","time_from_fetch":2001,"client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100631.7053,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNav","component_id":"7","parent_component_id":"1","lost_visibility":"false","is_pre_pageload":"true","relative_start_time":1274,"is_critical":"true","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100632.4313998,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNav","component_id":"7","parent_component_id":"1","parent_component":"Root","time_from_initializing":0.726,"duration":726,"lost_visibility":"false","relative_start_time":1274,"is_pre_pageload":"true","is_critical":"true","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100631.714,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavPersonalSections","component_id":"8","parent_component_id":"7","lost_visibility":"false","is_pre_pageload":"true","relative_start_time":1283,"is_critical":"true","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100632.4313998,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavPersonalSections","component_id":"8","parent_component_id":"7","parent_component":"SideNav","time_from_initializing":0.717,"duration":717,"lost_visibility":"false","relative_start_time":1283,"is_pre_pageload":"true","is_critical":"true","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"experiment_branch","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100632.453,"login":nickname,"user_id":idp,"experiment_id":"a5870914-ca72-48a8-b03d-829f6bac16be","experiment_group":"control","experiment_name":"left_nav_few_follows","experiment_version":14187,"experiment_type":"user_id","client_app":"twilight","logged_in":"true"}},{"event":"experiment_branch","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100632.457,"login":nickname,"user_id":idp,"experiment_id":"145ddca3-2724-45ed-9ded-3bf9d2e79811","experiment_group":"control","experiment_name":"vx_left_nav_category_click_thru","experiment_version":14189,"experiment_type":"device_id","client_app":"twilight","logged_in":"true"}},{"event":"experiment_branch","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100632,"url":"https://www.twitch.tv/friends","client_time":1637100632.458,"login":nickname,"user_id":idp,"experiment_id":"a1fa14d1-a9bd-40a0-83df-c5b6767d5a28","experiment_group":"control","experiment_name":"vx_left_nav_creator_color","experiment_version":14235,"experiment_type":"device_id","client_app":"twilight","logged_in":"true"}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4547,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"Side Nav Header","component_id":"11","parent_component_id":"10","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2024,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4989,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"Side Nav Header","component_id":"11","parent_component_id":"10","parent_component":"SideNavList","time_from_initializing":0.044,"duration":44,"lost_visibility":"false","relative_start_time":2024,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4583,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavCard","component_id":"12","parent_component_id":"10","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2027,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4991999,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavCard","component_id":"12","parent_component_id":"10","parent_component":"SideNavList","time_from_initializing":0.041,"duration":41,"lost_visibility":"false","relative_start_time":2027,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4612,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavCard","component_id":"13","parent_component_id":"10","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2030,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4995,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavCard","component_id":"13","parent_component_id":"10","parent_component":"SideNavList","time_from_initializing":0.038,"duration":38,"lost_visibility":"false","relative_start_time":2030,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4665,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavCard","component_id":"14","parent_component_id":"10","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2036,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4996002,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavCard","component_id":"14","parent_component_id":"10","parent_component":"SideNavList","time_from_initializing":0.033,"duration":33,"lost_visibility":"false","relative_start_time":2036,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4715,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavCard","component_id":"15","parent_component_id":"10","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2041,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4997,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavCard","component_id":"15","parent_component_id":"10","parent_component":"SideNavList","time_from_initializing":0.028,"duration":28,"lost_visibility":"false","relative_start_time":2041,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4753,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavCard","component_id":"16","parent_component_id":"10","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2044,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4997,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavCard","component_id":"16","parent_component_id":"10","parent_component":"SideNavList","time_from_initializing":0.024,"duration":24,"lost_visibility":"false","relative_start_time":2044,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4778998,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavCard","component_id":"17","parent_component_id":"10","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2047,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4997,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavCard","component_id":"17","parent_component_id":"10","parent_component":"SideNavList","time_from_initializing":0.022,"duration":22,"lost_visibility":"false","relative_start_time":2047,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4541001,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavList","component_id":"10","parent_component_id":"8","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2023,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.5007,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"SideNavList","component_id":"10","parent_component_id":"8","parent_component":"SideNavPersonalSections","time_from_initializing":0.047,"duration":47,"lost_visibility":"false","relative_start_time":2023,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"bttv_check","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.502,"is_bttv":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"ffz_check","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.502,"is_ffz":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.4896998,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"TrackingManager","component_id":"18","parent_component_id":"1","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2059,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"client_availability","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.505,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","bornuser":"false","browser":userAgent,"browser_family":"chrome","browser_version":"95.0","collapse_right":"false","collapse_left":"true","localstorage_device_id":"3b8df4f20daf975d","location":"friends.list","referrer":"https://www.twitch.tv/friends","referrer_domain":"www.twitch.tv","session_device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","theme":"light","viewport_height":961,"viewport_width":818,"name":"SideNavPersonalSectionsComponent","category":"Ability to discover content","is_available":"true","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"client_availability","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.505,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","bornuser":"false","browser":userAgent,"browser_family":"chrome","browser_version":"95.0","collapse_right":"false","collapse_left":"true","localstorage_device_id":"3b8df4f20daf975d","location":"friends.list","referrer":"https://www.twitch.tv/friends","referrer_domain":"www.twitch.tv","session_device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","theme":"light","viewport_height":961,"viewport_width":818,"name":"SideNavPersonalSectionsComponent","category":"Ability to discover content","is_available":"true","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.537,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"Side Nav Header","component_id":"20","parent_component_id":"19","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2106,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.5437,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"Side Nav Header","component_id":"20","parent_component_id":"19","parent_component":"OnlineFriends","time_from_initializing":0.007,"duration":7,"lost_visibility":"false","relative_start_time":2106,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.5361001,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"OnlineFriends","component_id":"19","parent_component_id":"7","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2105,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"experiment_branch","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.545,"login":nickname,"user_id":idp,"experiment_id":"1f7e7664-f082-44cc-847e-e57dec0a6bb9","experiment_group":"variant1","experiment_name":"vx_defer","experiment_version":13011,"experiment_type":"device_id","client_app":"twilight","logged_in":"true"}},{"event":"client_availability","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.545,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","bornuser":"false","browser":userAgent,"browser_family":"chrome","browser_version":"95.0","collapse_right":"false","collapse_left":"true","localstorage_device_id":"3b8df4f20daf975d","location":"friends.list","referrer":"https://www.twitch.tv/friends","referrer_domain":"www.twitch.tv","session_device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","theme":"light","viewport_height":961,"viewport_width":818,"name":"OnlineFriends","category":"Ability to discover content","is_available":"true","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.5489,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"OnlineFriends","component_id":"19","parent_component_id":"7","parent_component":"SideNav","time_from_initializing":0.013,"duration":13,"lost_visibility":"false","relative_start_time":2105,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"onboarding_modal_opened","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.612,"client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"item_display","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.633,"channel_id":416083610,"content_type":"live","game":"Minecraft","game_id":"27471","is_live":"true","is_promotion":"false","item_page":"twitch_socialcolumn","item_position":3,"item_tracking_id":"33aee116-741c-4eaa-96e6-890d5b069ba8:3","location":"friends.list","login":nickname,"model_tracking_id":"33aee116-741c-4eaa-96e6-890d5b069ba8:3","page_session_id":"25fa2afd1e00af54","promotions_campaign_id":"","section":"recommended_channels","stream_ccu":1759,"vod_id":"null","client_app":"twilight","logged_in":"true","user_id":idp}},{"event":"item_display","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.638,"channel_id":29468517,"content_type":"live","game":"Crab Game","game_id":"673760473","is_live":"true","is_promotion":"false","item_page":"twitch_socialcolumn","item_position":1,"item_tracking_id":"33aee116-741c-4eaa-96e6-890d5b069ba8:1","location":"friends.list","login":nickname,"model_tracking_id":"33aee116-741c-4eaa-96e6-890d5b069ba8:1","page_session_id":"25fa2afd1e00af54","promotions_campaign_id":"","section":"recommended_channels","stream_ccu":2510,"vod_id":"null","client_app":"twilight","logged_in":"true","user_id":idp}},{"event":"item_display","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.641,"channel_id":82197170,"content_type":"live","game":"Grand Theft Auto V","game_id":"32982","is_live":"true","is_promotion":"false","item_page":"twitch_socialcolumn","item_position":0,"item_tracking_id":"33aee116-741c-4eaa-96e6-890d5b069ba8:0","location":"friends.list","login":nickname,"model_tracking_id":"33aee116-741c-4eaa-96e6-890d5b069ba8:0","page_session_id":"25fa2afd1e00af54","promotions_campaign_id":"","section":"recommended_channels","stream_ccu":11787,"vod_id":"null","client_app":"twilight","logged_in":"true","user_id":idp}},{"event":"item_display","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.644,"channel_id":102098555,"content_type":"live","game":"Crab Game","game_id":"673760473","is_live":"true","is_promotion":"false","item_page":"twitch_socialcolumn","item_position":4,"item_tracking_id":"33aee116-741c-4eaa-96e6-890d5b069ba8:4","location":"friends.list","login":nickname,"model_tracking_id":"33aee116-741c-4eaa-96e6-890d5b069ba8:4","page_session_id":"25fa2afd1e00af54","promotions_campaign_id":"","section":"recommended_channels","stream_ccu":1363,"vod_id":"null","client_app":"twilight","logged_in":"true","user_id":idp}},{"event":"item_display","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.646,"channel_id":32027530,"content_type":"live","game":"Grand Theft Auto V","game_id":"32982","is_live":"true","is_promotion":"false","item_page":"twitch_socialcolumn","item_position":2,"item_tracking_id":"33aee116-741c-4eaa-96e6-890d5b069ba8:2","location":"friends.list","login":nickname,"model_tracking_id":"33aee116-741c-4eaa-96e6-890d5b069ba8:2","page_session_id":"25fa2afd1e00af54","promotions_campaign_id":"","section":"recommended_channels","stream_ccu":3976,"vod_id":"null","client_app":"twilight","logged_in":"true","user_id":idp}},{"event":"item_display","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.665,"channel_id":36954803,"content_type":"live","game":"ALTF4","game_id":"791968461","is_live":"true","is_promotion":"false","item_page":"twitch_socialcolumn","item_position":5,"item_tracking_id":"33aee116-741c-4eaa-96e6-890d5b069ba8:5","location":"friends.list","login":nickname,"model_tracking_id":"33aee116-741c-4eaa-96e6-890d5b069ba8:5","page_session_id":"25fa2afd1e00af54","promotions_campaign_id":"","section":"recommended_channels","stream_ccu":4175,"vod_id":"null","client_app":"twilight","logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.6808,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"VerifyEmail","component_id":"21","parent_component_id":"1","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2250,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"client_availability","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.692,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","bornuser":"false","browser":userAgent,"browser_family":"chrome","browser_version":"95.0","collapse_right":"false","collapse_left":"true","localstorage_device_id":"3b8df4f20daf975d","location":"friends.list","referrer":"https://www.twitch.tv/friends","referrer_domain":"www.twitch.tv","session_device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","theme":"light","viewport_height":961,"viewport_width":818,"name":"Whispers_ThreadsBar","category":"Ability to create and interact with a community","feature":"Whispers","reason":"Whispers GQL or component error","is_available":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.7078998,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"OnsiteNotificationToastManager","component_id":"22","parent_component_id":"2","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2277,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.7103,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"OnsiteNotificationToastManager","component_id":"22","parent_component_id":"2","parent_component":"TopNav","time_from_initializing":0.002,"duration":2,"lost_visibility":"false","relative_start_time":2277,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"chat_connection_timing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100632.834,"timing":1105.5999999940395,"client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100633.0161002,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"VerifyEmail","component_id":"21","parent_component_id":"1","parent_component":"Root","time_from_initializing":0.335,"duration":335,"lost_visibility":"false","relative_start_time":2250,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"client_availability","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100633.016,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","bornuser":"false","browser":userAgent,"browser_family":"chrome","browser_version":"95.0","collapse_right":"false","collapse_left":"true","localstorage_device_id":"3b8df4f20daf975d","location":"friends.list","referrer":"https://www.twitch.tv/friends","referrer_domain":"www.twitch.tv","session_device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","theme":"light","viewport_height":961,"viewport_width":818,"name":"Whispers_ThreadsBar","category":"Ability to create and interact with a community","feature":"Whispers","is_available":"true","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100633.018,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"WhisperCenter","component_id":"23","parent_component_id":"2","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2587,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100633.0231001,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"WhisperCenter","component_id":"23","parent_component_id":"2","parent_component":"TopNav","time_from_initializing":0.005,"duration":5,"lost_visibility":"false","relative_start_time":2587,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"client_availability","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100633.024,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","bornuser":"false","browser":userAgent,"browser_family":"chrome","browser_version":"95.0","collapse_right":"false","collapse_left":"true","localstorage_device_id":"3b8df4f20daf975d","location":"friends.list","referrer":"https://www.twitch.tv/friends","referrer_domain":"www.twitch.tv","session_device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","theme":"light","viewport_height":961,"viewport_width":818,"name":"Whispers","category":"Ability to create and interact with a community","feature":"Whispers","is_available":"true","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100633.1721,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"AmazonAds","component_id":"24","parent_component_id":"18","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2741,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100633.1741002,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"AmazonAds","component_id":"24","parent_component_id":"18","parent_component":"TrackingManager","time_from_initializing":0.002,"duration":2,"lost_visibility":"false","relative_start_time":2741,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_initializing","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100633.1732,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"Comscore","component_id":"25","parent_component_id":"18","lost_visibility":"false","is_pre_pageload":"false","relative_start_time":2742,"is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100633.1758,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"Comscore","component_id":"25","parent_component_id":"18","parent_component":"TrackingManager","time_from_initializing":0.003,"duration":3,"lost_visibility":"false","relative_start_time":2742,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"benchmark_component_interactive","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100633.1761,"benchmark_session_id":"31230dacc6228040","page_session_id":"25fa2afd1e00af54","benchmark_server_id":"11b95cf2158d485bae16a896c6fdf89b","destination":"friends.list","location":"friends.list","page_component_name":"FriendsPage","component":"TrackingManager","component_id":"18","parent_component_id":"1","parent_component":"Root","time_from_initializing":0.686,"duration":686,"lost_visibility":"false","relative_start_time":2059,"is_pre_pageload":"false","is_critical":"false","client_app":"twilight","login":nickname,"logged_in":"true","user_id":idp}},{"event":"crown_interaction","properties":{"app_session_id":"57ff3d12b39a8672","app_version":"f14e4795-c261-449a-99a3-1eabd8017565","device_id":"guK2ClqYwqLKhd4QqCmD4HJyoSh4mQqA","domain":"twitch.tv","host":"www.twitch.tv","platform":"web","preferred_language":"pl-PL","referrer_host":"www.twitch.tv","referrer_url":"","received_language":"en","tab_session_id":"fcb193f732a99874","batch_time":1637100633,"url":"https://www.twitch.tv/friends","client_time":1637100633.177,"has_prime":"false","number_of_offers":47,"action":"offers_loaded","user_agent":userAgent,"client_app":"twilight","login":nickname,"logged_in":'"true"',"user_id":idp}}]'
                                                    
                                                    data = data.replace('userAgent', f'"{userAgent}"')
                                                    data = data.replace('nickname', f'"{nickname}"')
                                                    data = data.replace('idp', idp)
                                                    data = data.replace('"true"', 'true')
                                                    data = data.replace('"false"', 'false')

                                                    encodedBytes = base64.b64encode(data.encode("utf-8"))
                                                    encodedStr = str(encodedBytes, "utf-8")



                                                    headers = {
                                                        'authority': 'video-edge-d8f652.pdx01.abs.hls.ttvnw.net',
                                                        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                                                        'sec-ch-ua-mobile': '?0',
                                                        'user-agent': userAgent,
                                                        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
                                                        'accept': '*/*',
                                                        'origin': 'https://www.twitch.tv',
                                                        'sec-fetch-site': 'cross-site',
                                                        'sec-fetch-mode': 'cors',
                                                        'sec-fetch-dest': 'empty',
                                                        'referer': 'https://www.twitch.tv/',
                                                        'accept-language': 'pl-PL,pl;q=0.9',
                                                    }

                                                    data = {
                                                    'data': encodedStr
                                                    }

                                                    requests.post('https://video-edge-d8f652.pdx01.abs.hls.ttvnw.net/v1/segment/CrqTDJEHWRFaOecD1tS6cjUUZfayclK4Axr1qB9aDtarJ9OJtjDOP1zQkUXkTgjt5pTQ19pZq2VyM8GYtEqcNuJ89_1sUFzXyuXj2myWycSxjScrDKuFUfpaPWczmtvy59lLBFI5ysqvS6c0hzCmlY9QNnxAiRo0StoF9A2jWcXUD9MsrueqKFn1xGm5pAxKUmSYFCDoTwwu_-l81yOplsBJsHYH0wMkFlPhD3EzkTTRvRFbWDN-1D2OMbU_KAqwmmFJK_cX4VX1l63fYDuhxF5bU3SG2ArCUSC_NhbxqAU5PDVU_5gDvAAK0E6CvcLqtSWAoDaU1fgTV2sKPRnepMJ6FwPzcrizxXk0I9h7djMulBwFhm_GtQlieWTq-5ktRAONPx11eWX-h6m3vx96oej-TNgpZwN029grVS7jI0r1avS7WJAqJnyEDzn1Xzc9ie3hg4oBzakG5ka4JBBZPEM4r25zVZ98X5QID9GPFjZfOgL1AxNLjRk37HcbHK-FQ-XAdCH4wbGb7xdnniwPG11tbjQRK8DsVenAxMKF6Rn7DdW5w6vXNV5rGGPKWmZD4Roz6-L59SmB-zRwbIC1HGiALEeI1I1B-SRQvrf4IEOeUdMxypSqzjamfM610SX3xI9str7qyGChSRtic0VPT8HOIi5nAZd1wKB8DE-x56ExRaEvticq_R-vUyBluiRdFe1i1v_7exSAnOebdhJhy9OXqZAivOhe5AXrTPLLxKBtXxGkj5UUV5i1qDZppX2pCcHKdLy7XPwnMV24T-EAbbC-PIF.ts', headers=headers, data=data, proxies=proxies_paid, timeout=20)


                                                    headers = {
                                                        'Connection': 'keep-alive',
                                                        'Pragma': 'no-cache',
                                                        'Cache-Control': 'no-cache',
                                                        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                                                        'Accept-Language': 'pl-PL',
                                                        'sec-ch-ua-mobile': '?0',
                                                        'Client-Version': 'e8881750-cfb7-4ff7-aaae-132abb1e8259',
                                                        'Authorization': f'OAuth {token}',
                                                        'Content-Type': 'text/plain;charset=UTF-8',
                                                        'User-agent': userAgent,
                                                        'Client-Session-Id': '671362f9f83b6729',
                                                        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                                                        'X-Device-Id': 'O1MrFLwPyZ2byJzoLFT0K5XNlORNRQ9F',
                                                        'sec-ch-ua-platform': '"Windows"',
                                                        'Accept': '*/*',
                                                        'Origin': 'https://dashboard.twitch.tv',
                                                        'Sec-Fetch-Site': 'same-site',
                                                        'Sec-Fetch-Mode': 'cors',
                                                        'Sec-Fetch-Dest': 'empty',
                                                        'Referer': 'https://dashboard.twitch.tv/',
                                                    }

                                                    data = [{"operationName":"UpdateUserProfile","variables":{"input":{"displayName":nickname,"description":bio,"userID":idp}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"991718a69ef28e681c33f7e1b26cf4a33a2a100d0c7cf26fbff4e2c0a26d15f2"}}}]

                                                    requests.post('https://gql.twitch.tv/gql', headers=headers,data=json.dumps(data),timeout=20, proxies=proxies_paid)
                                                    
                                                
                                                    if th.veryfi == "y":
                                                        try:
                                                            SERVER = "imap.franus.beep.pl"
                                                            EMAIL = "voxy"
                                                            PASSWORD = "Weryfikacja2021@!"
                                                            time.sleep(5)

                                                            mail = imaplib.IMAP4_SSL(SERVER)
                                                            mail.login(EMAIL, PASSWORD)
                                                            mail.select('inbox')

                                                            status, data = mail.search(None, 'ALL')
                                                            mail_ids = []
                                                            for block in data:
                                                                mail_ids += block.split()
                                                            for i in mail_ids:
                                                                status, data = mail.fetch(i, '(RFC822)')
                                                                for response_part in data:
                                                                    if isinstance(response_part, tuple):
                                                                        message = email.message_from_bytes(response_part[1])
                                                                        mail_from = message['from']
                                                                        mail_subject = message['subject']
                                                                        if message.is_multipart():
                                                                            mail_content = ''
                                                                            for part in message.get_payload():
                                                                                if part.get_content_type() == 'text/plain':
                                                                                    mail_content += part.get_payload()
                                                                        else:
                                                                            mail_content = message.get_payload()
                                                                        
                                                                        nick = nickname.lower()
                                                                        if nick in mail_content:
                                                                            try:
                                                                                start = mail_subject.find('=?UTF-8?Q?') + 10
                                                                                end = mail_subject.find('_', start)
                                                                                code = mail_subject[start:end]

                                                                                
                                                                                headers = {
                                                                                    'Connection': 'keep-alive',
                                                                                    'sec-ch-ua': '^\^Google',
                                                                                    'Accept-Language': 'pl-PL',
                                                                                    'sec-ch-ua-mobile': '?0',
                                                                                    'Client-Version': '41922a81-adbe-4e8b-9e2d-cf7379faa045',
                                                                                    'Authorization': f'OAuth {token}',
                                                                                    'Content-Type': 'text/plain;charset=UTF-8',
                                                                                    'user-agent': userAgent,
                                                                                    'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                                                                                    'sec-ch-ua-platform': '^\^Windows^^',
                                                                                    'Accept': '*/*',
                                                                                    'Origin': 'https://www.twitch.tv',
                                                                                    'Sec-Fetch-Site': 'same-site',
                                                                                    'Sec-Fetch-Mode': 'cors',
                                                                                    'Sec-Fetch-Dest': 'empty',
                                                                                    'Referer': 'https://www.twitch.tv/',
                                                                                }
                                                                                
                                                                                data = [{"operationName":"ValidateVerificationCode","variables":{"input":{"code":code,"key":idp,"address":mailx}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"05eba55c37ee4eff4dae260850dd6703d99cfde8b8ec99bc97a67e584ae9ec31"}}}]
                                                                                requests.post("https://gql.twitch.tv/gql", headers=headers, data=json.dumps(data), proxies=proxies_paid, timeout=20)
                                                                                
                                
                                                                            except Exception as e:
                                                                                #print(e)
                                                                                None
                                                        except Exception as e:
                                                            None
                                                            #print(e)
                                            elif idd == "false":
                                                validate_username()                    
                    validate_username()
                else:
                    stats.invalid = stats.invalid + 1
                    
            else:
                stats.invalid = stats.invalid + 1
        except Exception as e:
            None
            #print(e)
    except Exception as e:
        #print(e)
        try:
            os.remove(folder)
        except:
            None
        
    
def menu():
    
    cls()
    

        
    class Animation():
        notcomplete = "true"
    
    def animation():
        
        
        animation = [
        "[        ]",
        "[=       ]",
        "[===     ]",
        "[====    ]",
        "[=====   ]",
        "[======  ]",
        "[======= ]",
        "[========]",
        "[ =======]",
        "[  ======]",
        "[   =====]",
        "[    ====]",
        "[     ===]",
        "[      ==]",
        "[       =]",
        "[        ]",
        "[        ]"
        ]

        

        i = 0

        while True:
            x = Animation.notcomplete
            if x == "true":
                print(animation[i % len(animation)], end='\r')
                time.sleep(0.05)
                i += 1
            else:
                break
    
    x = threading.Thread(target=animation).start()
    
    
    session = requests.session()
    x = session.get(f"http://51.178.2.109:10000/api/v2/version").text
    
    
    if x == version:
        time.sleep(1)
        Animation.notcomplete = "false"
    else:
        exit()
    Animation.notcomplete = "false"
    
    try:
        files = glob.glob('data/*')
        for f in files:
            os.remove(f)
    except:
        None
    
    cls()
    
    
    
    print(""" 
        
  .d88b.  db    db db    db 
 .8P  Y8. `8b  d8' `8b  d8' 
 88    88  `8bd8'   `8bd8'  
 88    88  .dPYb.     88    
 `8b  d8' .8P  Y8.    88    
  `Y88P'  YP    YP    YP    
  
                TOKEN GENERATOR v2
                                        
""")
    
    
    
    
                
    if 1 == 1:
        prYellow("\n | 1 -> http \n | 2 -> socks4")
        type = int(input("\n : "))
        
        prYellow("\n | Threads")
        tha = int(input("\n : "))
        

        
        if type == 1:
            th.proxy = 'http'
        elif type == 2:
            th.proxy = 'socks4'
            
        
        prYellow("\n | Email verify? Y/N")
        veryfi = input("\n : ")
        
        if veryfi == "Y" or veryfi == "y":
            th.veryfi = "y"
        cls()
        
        
        class Xdas():
            thstart = 0
            
        Xdas.thstart = int(threading.active_count())
        
        
        start_time = time.time()


        def title():
            while True:
                timex = " %s  " % (time.time() - start_time)
                sep = '.'
                stripped = timex.split(sep, 1)[0]
                xnow = int(threading.active_count()) - Xdas.thstart
                
                def tps():
                    try:
                        if int(stats.gened) == 0:
                            return 0
                        else:
                            cxtime = float(stripped) / 60
                            xxtime = cxtime / 60
                            xxx = str(int(stats.gened) / xxtime)
                            strippedx = xxx.split(sep, 1)[0]

                            return strippedx
                    except Exception as s:
                        print(s)
                        return 0

                timex = " %s  " % (time.time() - start_time)
                sep = '.'
                stripped = timex.split(sep, 1)[0]
                xnow = int(threading.active_count()) - Xdas.thstart
                
                
                def print_stats():
                    
                    prLightPurple("\n \n \n ")
                    prGreen(f" |   ACCOUNT GENED: {stats.gened}")
                    prYellow(f" |   CAPTCHA SOLVED: {stats.hits}")
                    prRed(f" |   INVALID: {stats.invalid}\n")
                    print(f"  |   THREADS: {xnow}")
                    print(f"  |   TIME: {stripped}")
                    print(f"  |   TPH: " + str(tps()))
                print_stats()
                
                time.sleep(1)
                cls()
                    
        def check():
            while True:
                time.sleep(300)
                xlogin = login(Login.key)
                if xlogin == "false":
                    print("\n  INVALID KEY")
                    time.sleep(1)
                    exit()
                elif xlogin == "true": 
                    None
                    

                        
        threading.Thread(target=check).start()
        #threading.Thread(target=title).start()
        

        
        while True:
            

            
            
            xnow = int(threading.active_count()) - Xdas.thstart
            if xnow < tha:
                threading.Thread(target=gen).start()  

threading.Thread(target=menu).start()


