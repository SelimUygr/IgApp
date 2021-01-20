from start import WebDriverWait,By,EC,Keys,webdriver,sleep,starting
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class cleaner:
    def __init__(self,driver,dailyunfollow):
        self.driver = driver
        self.dailyunfollow = dailyunfollow

    def findUnfollowers(self):
        # Defined one list to keep followers in
        followers_list = []
        unfollowers_list = []

        # Go to profile
        self.driver.get('https://www.instagram.com/mmhhmmttat/')
        # Get number of followers from followers tab for set the for loop 
        elem = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')))
        followers_count = int(elem.text)
        # Click the followers tab
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'))).click()

        # Set the for loop
        for i in range(1,followers_count):
            # Move to every single followers for seeing all of them
            element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,f'/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]')))
            element_name = element.find_element_by_tag_name('span').text
            if element_name not in followers_list:
                followers_list.append(element_name)
            else:
                pass
            ActionChains(self.driver).move_to_element(element).perform()


        # Go to profile
        self.driver.get('https://www.instagram.com/mmhhmmttat/')
        # Click the followings tab
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'))).click()
        
        # Set the for loop
        for x in range(1,self.dailyunfollow):
            # Set element2 for get reference in actionchains 
            element2 = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,f'/html/body/div[5]/div/div/div[2]/ul/div/li[{x}]')))
            ActionChains(self.driver).move_to_element(element2).perform()
            # Get username
            element2_name = element2.find_element_by_tag_name('span').text
            # Get button
            element2_button = element2.find_element_by_tag_name('button')
            if element2_name not in followers_list:
                unfollowers_list.append(element2_name)
                element2_button.click()
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[6]/div/div/div/div[3]/button[1]'))).click()
            else:
                pass
            # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Cleaning unfollowers WELL-DONE ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓