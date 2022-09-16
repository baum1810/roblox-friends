import requests
import threading
def rfriends(userid, amount):
    with open('cookies.txt', 'r') as cookies:
        cookies = cookies.read().splitlines()
    batch = []
    for x in cookies:
    
        batch.append(x)
    def send_friend(cookie, userid):
        try:
            with requests.session() as session:
                check = requests.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(cookie)}) #check if the cookie is valid
                if check.status_code == 200:
    
    
                    session.cookies['.ROBLOSECURITY'] = cookie
                    session.headers['x-csrf-token'] = session.post('https://auth.roblox.com/v2/logout',cookies={'.ROBLOSECURITY': str(cookie)}).headers['x-csrf-token']
                    friend = session.post(f'https://friends.roblox.com/v1/users/{userid}/request-friendship')
                    if friend.status_code == 200:
                        print('sent')
                    elif 'The target user is already a friend.' in friend.text:
                        print('already added')
                    else:
                        print(friend.text)
        except:
           print('skipped')

    for x in range(int(amount)):
        cookie = cookies[x]
        threading.Thread(target=send_friend, args=(cookie,userid,)).start()
