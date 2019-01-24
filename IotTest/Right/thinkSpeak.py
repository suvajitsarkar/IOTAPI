import http.client, urllib
def updateCloud(key,f1,f2=-99,f3=-99,f4=-99):
    if(f2==-99):
        params = urllib.parse.urlencode({'field1': f1, 'key':key })
    else:
        params = urllib.parse.urlencode({'field1': f1, 'field2': f2, 'field3': f3, 'field4': f4, 'key':key }) 
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print("connection failed")
