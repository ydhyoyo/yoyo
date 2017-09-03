test_dir = r"D:\kuangjia\test_case"
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = "D:\\kuangjia\\report\\"+now+"resut.html"
fp = open(filename,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title=u'测试报告',
                                       description=u'报告概述')
discover = unittest.defaultTestLoader.discover(start_dir=test_dir,
                                                pattern="test*.py",
                                                top_level_dir=None)
print (discover)
#runner = unittest.TextTestRunner()
runner.run(discover)


#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import  unittest
import time
class YouJian(unittest.TestCase):
    def setUp(self):
        time.sleep(5)
        self.smtpserver = "smtp.qq.com"
        self.port = 465
        self.user = "928621285@qq.com"
        self.psw = "trpwsoutcctqbbga"
        self.receiver = "928621285@qq.com"
        self.body = '<pre><hl>测试报告</hl></pre>'#定义邮件正文格式为HTML格式
        self.b = open("D:\\Test_ceshikuangjia\\ceshibaogao\\result.html","r" )
        self.mail_body = self.b.read()
        self.b.close()
        self.msg = MIMEMultipart()
        self.msg['from'] = self.user#发件人
        self.msg["to"] = self.receiver#收件人
        self.msg['subject'] = "哎呦喂"#主题
        #正文
        self.body = MIMEText(self.mail_body,"html","utf-8")
        self.msg.attach(self.body)
        #附件
        self.att = MIMEText(self.mail_body,"base64", "utf-8")
        self.att["Content-Type"] = "application/octet-stream"
        self.att["Content-Disposition"] = 'attachment; filename= "report.html"'
        self.msg.attach(self.att)

        #mag = MIMEText(self.boby,"html","utf-8")
        #self.msg['from'] = self.user#发件人
       # self.msg["to"] = self.receiver#收件人
        #self.msg['subject'] = "哎呦喂"#主题
    def test_001(self):
        #调用发件服务
        self.smtp = smtplib.SMTP_SSL(self.smtpserver,self.port)#连接服务器
        self.smtp.login(self.user,self.psw)  #登录
        self.smtp.sendmail(self.user,self.receiver, self.msg.as_string())
    def tearDown(self):
        self.smtp.quit()
#调用企业邮件
#smtp = smtplib.SMTP()
#smtp.connect(smtpserver,port)
#smtp.login(user,psw)  #登录
#smtp.sendmail(user,receiver, msg.as_string())
#smtp.quit()