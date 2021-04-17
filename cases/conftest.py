import pytest, os, sys
from selenium import webdriver
from test_data.url_data import login_url
from pages.login_page import LoginPage
import time
from run import logger
driver = None  #初始化drever

#找到chrom的驱动绝对路径,其中file表示当前文件conftest。py，
execute_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'chromedriver'))
#在执行测试用例钱先打开浏览器并进入网站金融界页面，scope=session：可跨文件跨模块使用，所有.py文件执行前执行session所标识的方法
@pytest.fixture(scope='session')
def handler():
    """
    用于测试用例执行前的数据准备工作和测试用例执行后的数据清理工作
    :return:
    """
    global driver  #将参数drever设置为全局变量，以供方法refresh_page使用
    logger.info('开始执行jrj web项目自动化测试')
    driver = webdriver.Chrome(execute_path)  #调取chrom浏览器
    driver.maximize_window()   #窗口最大化
    driver.get(login_url)    #传入url：金融界
    lg = LoginPage(driver)    #LoginPage(driver)，将金融界登录页面返回给用户登录页面（login_page)
    yield driver,lg
    driver.quit()              #退出浏览器
    logger.info('jrj web 自动化执行结束')


#scope=function:在单个函数执行前调用被装饰的函数，函数默认scope为function
#刷新页面函数
@pytest.fixture(scope='function')
def refresh_page():
    """
    用例执行后刷新页面
    :return:
    """
    #driver.refresh  此语句在本方法（refresh_page )中不能调用方法handler里面的driver参数，需要将方法handler中的driver定义为全局变量
    #在执行refresh_page前需要调用其他方法
    yield    #yield前面无任何语句：在执行完测试用例（函数）前不执行任何语句，用例执行结束后执行被装饰函数中yield之后的语句
    driver.refresh()   #刷新页面语句
    time.sleep(3)  #刷新完页面后等待3秒再执行之后的语句



#运行结果中不出现warn警告
#方法1：在项目根目录下建一个__init__.py文件，将mark标志名称加进文件中
#方法2：在conftest.py文件将mark标志名称加进文件中
#smok:冒烟测试，执行基础功能的测试用例
def pytest_configure(config):
    """
    添加mark标志
    :param config:
    :return:
    """
    markers = ['smoke','last']  #需要将make其他的标志名称加进去：使用逗号隔开，单引号内写入标志名称
    #遍历
    for mark in markers:
        config.addinivalue_line('markers',mark)





