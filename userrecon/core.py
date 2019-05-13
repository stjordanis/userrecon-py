#!/usr/bin/env python3

from time import time

import asyncio
import json
import sys

try:
    from userrecon.version import __version__, __author__
    from userrecon.social_networks import links

    import aiohttp
except ModuleNotFoundError as error:
    print('[-] error: {}'.format(error))
    sys.exit(1)

def print_sexy_banner():
    print("""                                                                    
  __  __________  _____________  _________  ____        ____  __  __
 / / / / ___/ _ \\/ ___/ ___/ _ \\/ ___/ __ \\/ __ \\______/ __ \\/ / / /
/ /_/ (__  )  __/ /  / /  /  __/ /__/ /_/ / / / /_____/ /_/ / /_/ / 
\\__,_/____/\\___/_/  /_/   \\___/\\___/\\____/_/ /_/     / .___/\\__, /  
       {}Version: {} | Author: {}{}           /_/    /____/   
""".format('\033[32m', __version__, __author__, '\033[0m'))

async def check_status(session, social_network, url, username):
    
    global results
    results = {}

    url = url.format(username)
    try:
        async with session.get(url) as resp:
            print('\033[33m[!] {:10}: {}\033[0m\033[J'.format(social_network, url), end='\r')
            if resp.status == 200:
                print('\033[32m[+] {:10}: {}\033[0m\033[J'.format(social_network, url))
                results[social_network] = url
        return resp.release()
    except:
        pass

async def verify_username(username):
    
    print('[*] checking username {}{}{} in {} social networks'.format(
        '\033[1m', username, '\033[0m', len(links.keys())
    ))
    start = time()
    async with aiohttp.ClientSession() as session:
        tasks = [
            check_status(session, social_network, url, username)
            for social_network, url in links.items() 
        ]
        await asyncio.gather(*tasks)
        print('[*] {}{}{} results found in: {:.2f} segs.\033[J'.format(
            '\033[1m', len(results.keys()), '\033[0m', time()-start
        ))

def generate_json_file(filename):

    output = json.dumps(results, indent=2)
    with open('{}.json'.format(filename), 'w') as f:
        f.write(output)
        print('[*] file {} was created'.format(filename))

