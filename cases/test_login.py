from test_data.test_data import success_data
import sys
from run import logger
import pytest
from test_data.test_data import fail_data
import allure


"""
问题
1.发送用户名和密码前清空输入框内容
2.pytest调用fail_data数据类型为列表，data数据类型为字典
3.如何调用刷新页面的函数，达到不将被修饰的函数参数值传给测试用例

"""
@allure.step('步骤1：登录')
def step_1():
    logger.info('准备登录')

@allure.step('开始断言')
def step_2():
    logger.info('准备断言')

@allure.epic('金融界web自动化自测')
@allure.feature('金融界web登录模块')
@pytest.mark.usefixtures('refresh_page')  #调用刷新页面的函数,该类下的测试用例执行结束后都刷新页面
class TestLogin:
    @allure.severity(allure.severity_level.BLOCKER)  #将该用例设置为最严重的等级
    #登录成功
    @pytest.mark.last  #控制测试用例该测试用例最后一个执行
    @allure.story('登录模块-正常登录')
    @allure.title('针对正常登录的测试')
    def test_login_success(self,handler):
        #sys._getframe().f_code.co_name : 获取test_login_success，且打印出
        logger.info('执行{}测试用例'.format(sys._getframe().f_code.co_name))
        logger.info('进入 test_login_success methon')
        logger.info("登录测试—正常数据")
        step_1()
        # 输入正确的用户名，密码进行登录，其中handler【1】表示lg（即，driver.get(login_url) ）
        handler[1].login(success_data['username'],success_data['password'])  #在输入数据前清除输入框里的内容
        logger.info('期望值：{}'.format('退出'))
        logger.info('实际值：{}'.format(handler[1].get_logout_text()))  #is_logout_text_exist()：方法1中定义
        try:
            step_2()
            assert handler[1].get_logout_text()  #登录成功后进行判断是否登录成功
            logger.info('测试用例执行完毕，测试结果： ======pass=====')
            handler[1].save_picture('登录成功并截图')
        except Exception as e:
            logger.info('测试执行完毕，测试结果：=======fail======')
            logger.info(e)
            handler[1].save_picture('登录失败并截图')
    @allure.story('登录模块-异常登陆')
    @allure.title('针对异常登陆的测试')
    #登录失败
    @pytest.mark.parametrize('data',fail_data)
    def test_login_failed(self,handler,data):
        logger.info('执行{}测试用例'.format(sys._getframe().f_code.co_name))
        logger.info('登录测试-异常数据')
        step_1()
        #[1]表示handler的第二个实例
        handler[1].login(data['username'],data['password'])  #输入登录数据前清空输入框内的内容
        logger.info('期望值：{}'.format(True))   #只能写true，因为结果又两个：账号登录 和 账号或密码错误  两个值

        try:
            #用户和密码值为空或者错误时，执行判断语句，否则执行except语句

            if data['username'] =='' or data['password'] == '':
                #使用handler调用login_page的实例，用户和密码为空时
                logger.info('实际值：{}'.format(handler[1].get_account_login_text()))
                step_2()
                assert handler[1].get_account_login_text()
                #其中data的数据类型为字典，fail_data数据类型为列表
                logger.info('{}, 测试用例执行完毕， 测试结果： ========= PASS ========= '.format(data['name']))
                handler[1].save_picture('用户名或密码为空时截图')
            else:
                #用户和密码错误时
                logger.info('实际值：{}'.format(handler[1].get_username_password_wrong_text()))
                step_2()
                assert handler[1].get_username_password_wrong_text()
                logger.info('{}, 测试用例执行完毕， 测试结果： ========= PASS ========= '.format(data['name']))
                handler[1].save_picture('用户名或密码为错误时截图')

        except Exception as e:
            logger.info('出现异常')
            logger.info(e)

