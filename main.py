import requests
import random


class Http189:
    def __init__(self,uid,pwd):
        self.uid=uid
        self.pwd=pwd
        self.pwdEnc=''
        self.step=0
        self.http=requests.Session()
        self.headers={"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    def step1(self):
        print("init...")
        self.step=0
        res=self.http.get("http://ah.189.cn/sso/login?returnUrl=%2Fservice%2Faccount%2Finit.action",headers=self.headers)
        if(res.status_code==200):
            self.step=1
    def step2(self):
        if(self.step!=1):return 
        print("get captcha...")
        key=''.join([random.choice(list('0123456789')) for i in range(15)])
        res=self.http.get("http://ah.189.cn/sso/VImage.servlet?random=0."+key)
        if(res.status_code==200):
            f=open('yzm.jpg','wb')
            f.write(res.content)
            f.close()
            self.step=2
    def step3(self):
        if(self.step!=2):return True
##########################这里加入验证码识别模块
        print("wait input captcha:")
        yzm=input("Captcha:")
###########################加密密码
        # pubkey='a5aeb8c636ef1fda5a7a17a2819e51e1ea6e0cceb24b95574ae026536243524f322807df2531a42139389674545f4c596db162f6e6bbb26498baab074c036777'
        # N= '10001'
        #对密码做rsa加密
        self.pwdEnc='75c7e154d4451c3d9784a35b61ea99ee943330ab84ab992c70b650d80c7291c023975965f8867da28d0146afdf62043cbb4d920a4df4b52ff9bab463c567757b'
##########
        data={
            'ssoAuth':'null'
            ,'returnUrl':'/service/account/init.action'
            ,'sysId':'1003'
            ,'loginType':'4'
            ,'accountType':'9'
            ,'latnId':'551'
            ,'loginName':self.uid
            ,'passType':'0'
            ,'passWord':self.pwdEnc
            ,'validCode':yzm
            ,'csrftoken':''
        }
        print("Login...")
        res=self.http.post('http://ah.189.cn/sso/LoginServlet',data=data)
        if(res.text.find('验证码错误,请重新输入验证码。')!=-1):
            print('wrong captcha')
        elif(res.text.find("请输入安徽省电信手机号码!")!=-1):
            print("wrong phone")
        else:
            print(res.text)
        
if __name__=='__main__':
    obj=Http189('18939489380','39239903')
    obj.step1()
    obj.step2()
    obj.step3()