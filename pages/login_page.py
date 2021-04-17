from common.bases.base_page import BasePage
from locators.login_locator import LoginLocator
from selenium.webdriver.support import expected_conditions as EC #方法1需要导入该包
from selenium.webdriver.support.wait import WebDriverWait  #方法1需要导入该包

"""
1. 方法2：将方法1优化了登录失败时的三种测试用例，提高了代码简洁性和可读性
2. 信息封装了两个方法，其功能为：①判断文本信息是否存在 ； ② 返回对应登录失败的提示文本
3. 封装的方法在base_page.py中，方法名为：
    ① wait_element_visible
    ② get_element_text
"""

#收到conftest传过来的登录界面后，定位用户名，密码，登录框，同时输入数据（用户名，密码）
class LoginPage(BasePage):
    #在用户名和密码框内输入数据
    def login(self,username,password):
        self.send_data(LoginLocator.username_loc,username) #在用户名框里发送用户名
        self.send_data(LoginLocator.password_loc,password) #在密码框里发送密码
        self.click_element(LoginLocator.login_btn_loc)    # 点击登录按钮





     #方法2：调用在base_page里面的获取文本信息方法
    def get_logout_text(self,msg=''):

        #将获得的页面文本信息返回
        return self.get_element_text(LoginLocator.logout_text_loc,msg)


    def get_accout_login_text(self,msg=''):
        """
        通过判断“账号登录”这个文本在页面是否出现，若出现则返回text，未出现返回none
        :param msg:
        :return:
        """
        return self.get_element_text(LoginLocator.login_erro_msg_text_loc, msg)



    def get_username_password_wrong_text(self, msg=''):
        """
        当用户名或密码输入错误时，判断“账号或密码错误”提示文本是否存在页面，若存在则返回text，否则返回none
        :param msg:
        :return:
        """
        return self.get_element_text(LoginLocator.login_erro_msg_wrong_username_passwd, msg)






"""
    #方法1：
    #登录成功后，判断元素“退出”是否在当前页面
    def is_logout_text_exist(self):
        
        #方法1注释：
        #通过判断“退出”这个文本在页面是否出现，若出现则返回true，否则返回false
        #:return:
        方法2注释：
       通过判断“退出”这个文本在页面是否出现，若出现则返回text，否则返回null
        

        try:
            WebDriverWait(self.driver, 20). \
            ntil(EC.visibility_of_element_located(LoginLocator.logout_text_loc))
            return True
        except Exception as e:
            print('%s' % e)
            return False





    #登录失败后，页面显示窗口抖动
    def is_account_login_text_exist(self):
    
        # 定位“账号登录”这个文本在页面是否登录成功,出现则登录不成功,否则登录成功

        try:
            WebDriverWait(self.driver, 20). \
                until(EC.visibility_of_element_located(LoginLocator.login_erro_msg_text_loc))
            return True
        except Exception as e:
            print('%s' % e)
            return False



    #登录失败后，页面显示：账号或密码错误
    def is_username_password_wrong_exist(self):
        
        通过定位“账号或密码错误”这个文本在页面是否登录成功，出现则登录不成功，否则登录成功
        
        try:
            WebDriverWait(self.driver, 20). \
                until(EC.visibility_of_element_located(LoginLocator.login_erro_msg_wrong_username_passwd))
            return True
        except Exception as e:
            print('%s' % e)
            return False
"""
