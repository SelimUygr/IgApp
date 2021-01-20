from start import WebDriverWait,By,EC,Keys,webdriver,sleep,starting
from selenium.webdriver.common.action_chains import ActionChains
class choosen_Following:
    def __init__(self,driver,dailyFollow,hashtag):
        self.driver = driver
        #Get hashtag for specify the community we want to get attention from
        self.hashtag = hashtag
        #Same usage as recommendedFollow
        self.dailyFollow = dailyFollow

    # Setting everything to be ready for following people
    def set(self):
        # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Go to mainpage in case of any error occure ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ 
        if self.driver.current_url != 'https://www.instagram.com/':
            self.driver.get('https://www.instagram.com/')
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[3]/button[2]'))).click()
        # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Setting everything well-done ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ 
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))).send_keys(self.hashtag)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div/div[2]/div/span'))).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'))).click()
    
    # Following dailyFollow times people we want from choosen instagram page
    def followAllFollowers(self):
        for i in range(1,self.dailyFollow):
            # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Scrolling down while doing the task well-done ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ 
            element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,f'/html/body/div[5]/div/div/div[2]/ul/div/li[{i}]')))
            ActionChains(self.driver).move_to_element(element).perform()

            # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Getting the button text well-done ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ 
            element_button = element.find_element_by_tag_name('button')

            # ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓ Finally following algorithm WELL-DONE ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓
            if element_button.text == "Follow":
                element_button.click()
            else:
                pass
