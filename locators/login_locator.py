from selenium.webdriver.common.by import By

class LoginLocator:
    username_loc = (By.ID,'txtUsername')  #圆括号代表元组，定位到用户名输入框
    password_loc = (By.ID,'txtPassword')  #定位密码输入框，定位方式可选择
    login_btn_loc = (By.CLASS_NAME,'sso-btn-login')#定位登录框，定位方式可选则
    #登录成功
    logout_text_loc = (By.XPATH, '//*[@id="logout_ok"]')  # 通过判断页面出现“退出”按钮表示登录成功
    #登录失败，定位web页面元素
    login_erro_msg_text_loc = (By.XPATH,'/html/body/div[2]/div/div/form/div[1]/span')  #输入框抖动，定位‘账号登录’
    login_erro_msg_wrong_username_passwd = (By.XPATH,'/html/body/div[2]/div/div/form/div[2]/span') #定位‘账号或密码错误 ’




