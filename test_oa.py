class test_oa:
    one_on_one_session =  "/html/body/div[1]/div/header/div/div/div/section[2]/div/div/div[2]/div/div/div/div/nav/ul/li[5]/a"


    def _init_(self, driver):
        self.driver = driver

    def oneonone(self,page1):
        self.driver.find_element_by_xpath(self.one_on_one_session)

