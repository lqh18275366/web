from run import img_dir
import time
from run import logger
from selenium.webdriver.support import expected_conditions as EC  #用于判断页面中某元素存在
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime  #调用datetime.now（）使用



class BasePage:
    def __init__(self,driver):
        self.driver = driver

    #查找页面元素
    def search_element(self,locator):
        return self.driver.find_element(*locator)  # 定位找到element在web页面的位置
    #点击页面元素
    def click_element(self,locator):
        self.search_element(locator).click()   #点击 元素
    #向编辑输入框传入数据
    def send_data(self,locator,data):
        #在发送数据之前，调用清除输入框内容
        #self.clear_text(locator) #清除数据框内容，由于加了刷新页面的函数，所以不用再清空输入框内的数据
        self.search_element(locator).send_keys(data)  #向被定位的框里输入数据
    #截图
    def save_picture(self,msg=''):
        img_path = img_dir + '{0}-{1}.png'.format(msg, time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime()))
        try:
            self.driver.save_screenshot(img_path)  #screenshot:截图
            logger.info('截图成功，图片保存路径为：{}'.format(img_path))
        except Exception as e:
            logger.info('截图失败,{}'.format(msg))
            logger.info(e)

    #清除输入框内容
    def clear_text(self,locator):
        self.search_element(locator).clear()

    # 判断等待20秒成功获取页面的文本信息  等待页面元素可见
    def wait_element_visible(self,locator, msg=''):
        try:
            now = datetime.now()  #找页面时间是的时间
            WebDriverWait(self.driver, 20). \
                until(EC.visibility_of_element_located(locator))  #找locator定位的页面元素，等待某个元素可见
            end = datetime.now()  #收到页面元素时的时间
            total_time = (end-now).total_seconds()  #在找页面元素所耗费的时间
            #{0}对应locator，{1}对应total_time
            logger.info('end total time of waiting for {0} bisible is {1}'.format(locator,total_time))
        except Exception as e:
            logger.info(e)
            self.driver.sava_picture(msg)   #若出现异常则截图当前页面



    #获取页面元素的文本信息
    def get_element_text(self,locator,msg =''):
        self.wait_element_visible(locator,msg='')  #调用base_page.py文件内的方法wait_element_bisible去判断定位的元素存在
        # 定位的元素存在，则使用方法search_element(locator)找到这个元素
        # 再通过.text得到web页面显示的文字信息
        # 最后return返回 符合要求的文字信息
        return self.search_element(locator).text





