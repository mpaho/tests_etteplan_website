from playwright.sync_api import sync_playwright


import logging


class CountriesLibrary():

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page= None


    # Test setup

    def open_browser_to_homepage(self):
        '''This keyword opens the browser and navigates to Etteplan homepage. Acts as a test or suite setup for further testing.'''
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.firefox.launch(headless=False).new_context()
        self.page = self.browser.new_page()
        self.page.goto("https://www.etteplan.com/")
        self.page.wait_for_load_state()
        if self.page.title() != "Engineering company with a Difference | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <'Engineering company with a Difference | Etteplan'>")
        #self.page.screenshot(path="screenshot_homepage.png")
        logging.info(f"Landed on page <{self.page.title()}>")


    def navigate_to_homepage(self):
        '''A keyword simply to navigate to the home page. May be needed as a starting point fo further testing.'''
        self.page.goto("https://www.etteplan.com/")
        self.page.wait_for_load_state()
        if self.page.title() != "Engineering company with a Difference | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <'Engineering company with a Difference | Etteplan'>")
        logging.info(f"Landed on page <{self.page.title()}>")



    def choose_suomi_from_dropdown(self):
        '''A keyword to navigate to Etteplan's Finnish homepage using the dropdown menu in site header. 
        In case the current page is the same one as the seeked one, the keyword is skipped.'''

        url = self.page.get_attribute('//head/link[1]', 'href')
        logging.info(f"Test started from <{url}>")
        if url != 'https://www.etteplan.com/fi':
            self.page.click('//div[@class="language-switcher"]')
            self.page.click('//li[@class="langcode-fi"]')
            self.page.wait_for_load_state
            self.page.wait_for_timeout(3000)  #Fix the wait
        else:
            logging.info("The test was skipped because current url was the same as the requested one")
    

    def finnish_homepage_should_be_open(self):

        if self.page.title() != "Erilainen suunnittelutoimisto | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <Erilainen suunnittelutoimisto | Etteplan>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def choose_sverige_from_dropdown(self):
        '''A keyword to navigate to Etteplan's Swedish homepage using the dropdown menu in site header. 
        In case the current page is the same one as the seeked one, the keyword is skipped.'''

        url = self.page.get_attribute('//head/link[1]', 'href')
        logging.info(f"Test started from <{url}>")
        if url != 'https://www.etteplan.com/sv':
            self.page.click('//div[@class="language-switcher"]')
            self.page.click('//li[@class="langcode-sv"]')
            self.page.wait_for_load_state
            self.page.wait_for_timeout(3000) #Fix the wait
        else:
            logging.info("The test was skipped because current url was the same as the requested one")


    def swedish_homepage_should_be_open(self):

        if self.page.title() != "Ingenjörsföretag som gör skillnad | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <Ingenjörsföretag som gör skillnad | Etteplan>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def choose_nederland_from_dropdown(self):
        '''A keyword to navigate to Etteplan's Dutch homepage using the dropdown menu in site header. 
        In case the current page is the same one as the seeked one, the keyword is skipped.'''

        url = self.page.get_attribute('//head/link[1]', 'href')
        logging.info(f"Test started from <{url}>")
        if url != 'https://www.etteplan.com/nl':
            self.page.wait_for_selector('//div[@class="language-switcher"]')
            self.page.click('//div[@class="language-switcher"]')
            self.page.wait_for_selector('//li[@class="langcode-nl"]')
            self.page.click('//li[@class="langcode-nl"]')
            self.page.wait_for_load_state
        else:
            logging.info("The test was skipped because current url was the same as the requested one")

    
    def dutch_homepage_should_be_open(self):

        text = self.page.inner_text('//span[contains(text(),"Nederland")]')
        if text != "Nederland":
            raise AssertionError(f"The chosen country was <{text}> when expected country was <Nederland>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def choose_deutchland_from_dropdown(self):
        '''A keyword to navigate to Etteplan's German homepage using the dropdown menu in site header. 
        In case the current page is the same one as the seeked one, the keyword is skipped.'''

        url = self.page.get_attribute('//head/link[1]', 'href')
        logging.info(f"Test started from <{url}>")
        if url != 'https://www.etteplan.com/de':
            self.page.click('//div[@class="language-switcher"]')
            self.page.click('//li[@class="langcode-de"]')
            self.page.wait_for_load_state
            self.page.wait_for_timeout(3000) #Fix the wait
        else:
            logging.info("The test was skipped because current url was the same as the requested one")


    def german_homepage_should_be_open(self):

        if self.page.title() != "Engineering Unternehmen mit dem gewissen Unterschied | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <Engineering Unternehmen mit dem gewissen Unterschied | Etteplan>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def choose_danmark_from_dropdown(self):
        '''A keyword to navigate to Etteplan's Danish homepage using the dropdown menu in site header. 
        In case the current page is the same one as the seeked one, the keyword is skipped.'''

        url = self.page.get_attribute('//head/link[1]', 'href')
        logging.info(f"Test started from <{url}>")
        if url != 'https://www.etteplan.com/dk':
            self.page.click('//div[@class="language-switcher"]')
            self.page.click('//li[@class="langcode-dk"]')
            self.page.wait_for_load_state
        else:
            logging.info("The test was skipped because current url was the same as the requested one")


    def danish_homepage_should_be_open(self):

        text = self.page.inner_text('//span[contains(text(),"Danmark")]')
        if text != "Danmark":
            raise AssertionError(f"The chosen country was <{text}> when expected country was <Danmark>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def choose_polska_from_dropdown(self):
        '''A keyword to navigate to Etteplan's Poish homepage using the dropdown menu in site header. 
        In case the current page is the same one as the seeked one, the keyword is skipped.'''

        url = self.page.get_attribute('//head/link[1]', 'href')
        logging.info(f"Test started from <{url}>")
        if url != 'https://www.etteplan.com/pl':
            self.page.click('//div[@class="language-switcher"]')
            self.page.click('//li[@class="langcode-pl"]')
            self.page.wait_for_load_state
            self.page.wait_for_timeout(3000) #Fix the wait
        else:
            logging.info("The test was skipped because current url was the same as the requested one")


    def polish_homepage_should_be_open(self):

        if self.page.title() != "Engineering company with a Difference - biuro inżynierskie | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <Engineering company with a Difference - biuro inżynierskie | Etteplan>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def choose_global_english_from_dropdown(self):
        '''A keyword to navigate to Etteplan's English homepage using the dropdown menu in site header. 
        In case the current page is the same one as the seeked one, the keyword is skipped.'''
        
        url = self.page.get_attribute('//head/link[1]', 'href')
        logging.info(f"Test started from <{url}>")
        if url != 'https://www.etteplan.com/':
            self.page.wait_for_selector('//div[@class="language-switcher"]', timeout=5000)
            self.page.click('//div[@class="language-switcher"]')
            #self.page.wait_for_selector('//li[@class="langcode-en"]']', timeout=5000)
            self.page.click('//li[@class="langcode-en"]')
            self.page.wait_for_load_state(timeout=5000)
            self.page.wait_for_timeout(3000) #Fix the wait
        else:
            logging.info("The test was skipped because current url was the same as the requested one")


    def english_homepage_should_be_open(self):

        if self.page.title() != "Engineering company with a Difference | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <Engineering company with a Difference | Etteplan>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def choose_chinese_from_dropdown(self):
        '''A keyword to navigate to Etteplan's Chinese homepage using the dropdown menu in site header. 
        In case the current page is the same one as the seeked one, the keyword is skipped.'''

        url = self.page.get_attribute('//head/link[1]', 'href')
        logging.info(f"Test started from <{url}>")
        if url != 'https://www.etteplan.com/cn':
            self.page.click('//div[@class="language-switcher"]')
            self.page.click('//li[@class="langcode-cn"]')
            self.page.wait_for_load_state
            self.page.wait_for_timeout(3000) #Fix the wait
        else:
            logging.info("The test was skipped because current url was the same as the requested one")


    def chinese_homepage_should_be_open(self):

        if self.page.title() != "与众不同的工程设计公司 | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <与众不同的工程设计公司 | Etteplan>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def navigate_to_current_country_homepage_by_clicking_logo(self):

        cid = self.page.get_attribute('//html', 'lang')   # KESKEN
        logging.debug(f"country id is <{cid}>")
        if cid != 'en':
            exp_url = f"https://www.etteplan.com/{cid}"
            logging.debug(f"expected url <{exp_url}>")
        else:
            exp_url = f"https://www.etteplan.com/"

        self.page.wait_for_selector('//div[@id="block-etteplan-branding"]//a[@class="site-logo"]')
        self.page.click('//div[@id="block-etteplan-branding"]//a[@class="site-logo"]')
        url = self.page.get_attribute('//head/link[1]', 'href')
        if exp_url != url:
            raise AssertionError(f"The url was expected to be <{exp_url}> but was <{url}>")


    def get_country_id(self):
        
        cid = self.page.get_attribute('//html', 'lang')
        logging.info(f"Country id is <{cid}>")


    def navigate_to_section_contact(self):

        self.page.wait_for_selector('//ul[@class="menu-main level-0"]//a[@href="/contact-us"]')
        self.page.click('//ul[@class="menu-main level-0"]//a[@href="/contact-us"]')
        self.page.wait_for_load_state()
        if self.page.title() != "Contact us | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <Contact us | Etteplan>")
        logging.info(f"Landed on page <{self.page.title()}>")


    # Teardown
    def close_browser(self):
        """Closes browser and stops Playwright."""
        self.browser.close()
        self.playwright.stop()
        logging.info('Closed browser and stopped Playwright')