import requests

class Utils:
    Host_URL='http://test.coinfex.com'
    Host_URL2='https://www.jex.com'


    headers={
        'Host': 'test.coinfex.com',
        'Connection': 'keep-alive',
        'accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/65.0.3325.162 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        'headerToken': ''
    }

    def http_get_request(self,url,params):
        response=requests.get(self.Host_URL+url,params,headers=self.headers)
        try:
            if response.status_code==200:
                return response.json()
            else:
                return
        except Exception as e:
            print("httpGet failed,detail is:%s,%s"%(response.text,e))
            return


    def http_post_requset(self,url,params):
        response=requests.post(self.Host_URL+url,params,headers=self.headers)
        try:
            if response.status_code==200:
                return response.json()
            else:
                return
        except Exception as e:
            print("httpPost failed,detail is:%s,%s"%(response.text,e))



    def http_get_request2(self,url,params):
        response=requests.get(self.Host_URL2+url,params,headers=self.headers)
        try:
            if response.status_code==200:
                return response.json()
            else:
                return
        except Exception as e:
            print("httpGet failed,detail is:%s,%s"%(response.text,e))
            return