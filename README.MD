# 登录安徽189网站的项目

> 用python的requests模拟登陆.
> 问题来了,完成这个登录流程要有几个步骤呢?

- 1:打开登录页面, 获取一个JSESSIONID_SSO的cookie
    http://ah.189.cn/sso/login?returnUrl=%2Fservice%2Faccount%2Finit.action
- 2:登录需要输入帐号,密码,验证码, 因此我们需要获取验证码到本地.验证码网址是固定的,末尾那个数字是什么鬼,那是随机数字,服务器缓存图片一般会按网址缓存,你加了随机,它返回给你的图片就不会从缓存中读取,这是一种设计.
    http://ah.189.cn/sso/VImage.servlet?random=0.653461813411035
- 3:然后看图片输入验证码

- 4:提交登录的数据中,密码被加密了,rsa加密方式,key在这里.
```//用来对密码进行加密
var key =  bodyRSA();   
function bodyRSA()   
{   
    setMaxDigits(130);   
    return new RSAKeyPair("10001","","a5aeb8c636ef1fda5a7a17a2819e51e1ea6e0cceb24b95574ae026536243524f322807df2531a42139389674545f4c596db162f6e6bbb26498baab074c036777");    
}
```
    这里需要用到python的rsa模块

- 5:POST提交登陆数据.
        
![test](https://github.com/challengeYY/ah_189/blob/master/TEST.PNG)
------------

- 1:这里还没处理验证码识别模块
- 2:这里没有正确手机帐号密码,没处理完登陆后的信息判断
- 3:这里没有处理密码rsa加密步骤,暂时没找到python好用的rsa模块.
