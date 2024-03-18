import requests
import hashlib


def get_api_data(query):
    res = 'https://api.pwnedpasswords.com/range/' + query
    req = requests.get(res)
    if req.status_code != 200:
        raise RuntimeError(f'error fetching {req.status_code}')
    return req


def get_hashes_data(hashes, check_hashes):
    hack = (line.split(':') for line in hashes.text.splitlines())
    for h, c in hack:
        print(h, c)


def api_data_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]
    hashing = get_api_data(first5_char)
    get_hashes_data(hashing, tail)


api_data_check('pasword123')
