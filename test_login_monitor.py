# Python automation script
# Application name : 1.moibit.io, 2.moi-id, 3.marketplace, 4.grafana
# Author : Niyog V
# Test scenario : Login test to all our websites and monitoring each ip name under monitor.moibit.io

from selenium import webdriver
import warnings

from selenium.webdriver.common.by import By

warnings.filterwarnings("ignore", category=DeprecationWarning)
import time
import pytest

class Test_dashboard_market:

    @pytest.fixture() # Fixtures are used as pre-defined before running the actual function(moibit.io)
    def test_invoke(self):
        self.driver=webdriver.Chrome(executable_path='/Applications/chromedriver')
        self.driver.get('https://dashboard.moibit.io/')
        self.driver.maximize_window()

    @pytest.fixture()# Fixtures are used as pre-defined before running the actual function(marketplace)
    def test_invoke1(self):
        self.driver=webdriver.Chrome(executable_path='/Applications/chromedriver')
        self.driver.get('https://market.moiverse.io/')
        self.driver.maximize_window()
        yield
        self.driver.quit()

    @pytest.fixture()# Fixtures are used as pre-defined before running the actual function(moi-id)
    def test_invoke2(self):
        self.driver=webdriver.Chrome(executable_path='/Applications/chromedriver')
        self.driver.get('https://iome.ai/')
        self.driver.maximize_window()
        yield
        self.driver.quit()

    @pytest.fixture()# Fixtures are used as pre-defined before running the actual function(grafana)
    def test_invoke3(self):
        self.driver=webdriver.Chrome(executable_path='/Applications/chromedriver')
        self.driver.get('https://monitor.moinet.io/login')
        self.driver.maximize_window()
        yield
        self.driver.quit()


# This is a main function, where it login to  moibit
    def test_Moibit(self,test_invoke):
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/nav/p/a/span').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys('')
        self.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys('')
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(10)
        try: # The selenium checks whether the title of page is matching or not if not it throws an assertion error
            if self.driver.title=='MoiBit':
                assert True
            else:
                assert False
        finally:
            self.driver.quit()

    # This is a main function, where it login to marketplace
    def test_Market(self,test_invoke1):
        self.driver.find_element(By.XPATH,'//div[@class="styles_connect__nsylu styles_menuLink__17kgw"]').click()
        user=self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[1]/div[10]/div/div[2]/div/div/div/div[2]/div/div/input')
        user.send_keys('')
        password=self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[1]/div[10]/div/div[2]/div/div/div/div[3]/div/div/input')
        password.send_keys('')
        self.driver.find_element(By.XPATH,"//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained']").click()
        time.sleep(10)
        try: # The selenium checks whether the title of page is matching or not if not it throws an assertion error
            if self.driver.title=='MOIVerse Marketplace':
                assert True
            else:
                assert False
        finally:
            self.driver.find_element(By.XPATH,"//div[@class='styles_account__3MgT6 styles_menuLink__17kgw']").click()
            self.driver.find_element(By.XPATH,"//div[@class='styles_signOut__2OO-k']").click()
            time.sleep(2)

    # This is a main function, where it login to moi-id
    def test_Moi_id(self,test_invoke2):
        self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys('')
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys('')
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(10)
        try: # The selenium checks whether the title of page is matching or not if not it throws an assertion error
            if self.driver.title=='Moi-Id':
                assert True
            else:
                assert False
        finally:
            self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div/div/div[2]/div').click()
            time.sleep(2)

    # This is a main function, where it login to montor.moibit.io and scrolls down to each ip name and  checks everything looks good
    def test_Monitor(self,test_invoke3):
        self.driver.find_element(By.XPATH,"//input[@name='user']").send_keys('')
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys('')
        self.driver.find_element(By.XPATH,"//button[@aria-label='Login button']").click()
        time.sleep(4)
        try: # The selenium checks whether the title of page is matching or not if not it throws an assertion error
            if self.driver.title=='Home - Grafana':
                assert True
            else:
                assert False
        finally:
            self.driver.find_element(By.LINK_TEXT,'Moinet Alpha Dashboard').click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,"//a[@class='css-10l6kcd']").click()
            self.driver.find_element(By.XPATH,"//div[@class='variable-options-column']/a[2]").click()
            self.driver.find_element(By.XPATH,"//div[@class='submenu-controls']").click()
            time.sleep(2)
            DN_6=self.driver.find_element(By.XPATH,'//*[@id="panel-16"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",DN_6)
            time.sleep(2)
            DN_4=self.driver.find_element(By.XPATH,'//*[@id="panel-294"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",DN_4)
            time.sleep(2)
            vmi=self.driver.find_element(By.XPATH,'//*[@id="panel-308"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",vmi)
            time.sleep(2)
            premium_node_3=self.driver.find_element(By.XPATH,'//*[@id="panel-322"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",premium_node_3)
            time.sleep(2)
            DN_1=self.driver.find_element(By.XPATH,'//*[@id="panel-336"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",DN_1)
            time.sleep(2)
            premium_node_2=self.driver.find_element(By.XPATH,'//*[@id="panel-350"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",premium_node_2)
            time.sleep(2)
            premium_node_1=self.driver.find_element(By.XPATH,'//*[@id="panel-364"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",premium_node_1)
            time.sleep(2)
            DN_3=self.driver.find_element(By.XPATH,'//*[@id="panel-378"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",DN_3)
            time.sleep(2)
            loadbalancer=self.driver.find_element(By.XPATH,'//*[@id="panel-392"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",loadbalancer)
            time.sleep(2)
            validator_1=self.driver.find_element(By.XPATH,'//*[@id="panel-406"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",validator_1)
            time.sleep(2)
            moiid_webapp=self.driver.find_element(By.XPATH,'//*[@id="panel-420"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",moiid_webapp)
            time.sleep(2)
            moibit_webapp=self.driver.find_element(By.XPATH,'//*[@id="panel-434"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",moibit_webapp)
            time.sleep(2)
            DN_2=self.driver.find_element(By.XPATH,'//*[@id="panel-448"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",DN_2)
            time.sleep(2)
            validator_2=self.driver.find_element(By.XPATH,'//*[@id="panel-462"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",validator_2)
            time.sleep(2)
            validator_4=self.driver.find_element(By.XPATH,'//*[@id="panel-476"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",validator_4)
            time.sleep(2)
            validator_3=self.driver.find_element(By.XPATH,'//*[@id="panel-490"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",validator_3)
            time.sleep(2)
            DN_5=self.driver.find_element(By.XPATH,'//*[@id="panel-504"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",DN_5)
            time.sleep(2)
            validator_5=self.driver.find_element(By.XPATH,'//*[@id="panel-518"]/div/div[1]/div/div[2]/div/div/div/div/div/div/span')
            self.driver.execute_script("arguments[0].scrollIntoView();",validator_5)
            time.sleep(2)
            self.driver.find_element(By.XPATH,'/html/body/grafana-app/sidemenu/div[3]/div[1]/a/span').click()
            self.driver.find_element(By.XPATH,'/html/body/grafana-app/sidemenu/div[3]/div[1]/ul/li[3]/a').click()
















