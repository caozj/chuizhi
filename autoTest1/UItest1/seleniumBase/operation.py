from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

class operationBase():

    #打开Firefox浏览器,打开对应地址（*以后传入浏览器类型，重写方法，保证支持多个浏览器）
    def openChrome(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def setURL(self,url):
        self.driver.get(url)


    #元素定位方法,增加错误提示
    def operationBase_find_element(self, by,value):
        if by =='by_id':
            by_what='id'
        else:
            by_what=by
        try:
            #页面查找元素，取消异常捕获
            element=self.driver.find_element(by_what,value)
            return element
        except:
            print(u"    --页面中未能找到元素:by=%s,value=%s" % (by_what, value)+'\n')

    #元素定位方法,增加错误提示
    def operationBase_find_elements(self,by,value):
        try:
            #页面查找元素，取消异常捕获
            element=self.driver.find_elements(by,value)
            return element
        except:
            print(u"    --页面中未能找到元素:by=%s,value=%s" % (by, value)+'\n')


    # 鼠标移动方法,传入menu 作为移动到的对象
    def moveMouse(self, menu):
        webdriver.ActionChains(self.driver).move_to_element(menu).perform()


    #跳转最新页面
    def switchToNew(self):
        #获取当前所有窗口句柄
        handles=self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
        return  handles


    #跳转会原页面
    def switchToOld(self):
        handles=self.driver.window_handles
        length=len(handles)

    #输入文本
    def input(self,element,content):
        element.click()
        element.clear()
        element.send_keys(content)

    #关闭浏览器
    def close(self):
        self.driver.close()

    #公共断言
