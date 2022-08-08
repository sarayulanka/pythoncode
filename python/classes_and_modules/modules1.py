import urllib3

http = urllib3.PoolManager()

resp = http.request('GET', 'https://www.google.com')
print(resp.data)

with open('output.html', 'wb') as out:
    while True:
        data = resp.read()
        if not data:
            break
        out.write(data)

resp.release_conn()
