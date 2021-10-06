from playwright.sync_api import sync_playwright


import logging


class EtteplanLibrary():

    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page= None


    # Test setup

    def open_browser_to_homepage(self):
        '''This keyword opens the browser and navigates to Etteplan homepage. Acts as a test or suite setup for further testing.'''
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True).new_context()
        self.page = self.browser.new_page()
        self.page.goto("https://www.etteplan.com/")
        self.page.wait_for_load_state()
        if self.page.title() != "Engineering company with a Difference | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <'Engineering company with a Difference | Etteplan'>")
        #self.page.screenshot(path="screenshot_homepage.png")
        logging.info(f"Landed on page <{self.page.title()}>")



    def navigate_to_homepage(self):
        '''A keyword to navigate to Etteplan homepage using hardcoded url. '''
        self.page.goto("https://www.etteplan.com/")
        self.page.wait_for_load_state()
        if self.page.title() != "Engineering company with a Difference | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <'Engineering company with a Difference | Etteplan'>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def get_country_id(self):

        cid = self.page.get_attribute('//html', 'lang')
        logging.info(f"Country id is <{cid}>")
        return cid


    def navigate_to_section_our_services(self):

        self.page.wait_for_selector('//ul[@class="menu-main level-0"]//a[@href="/services"]')
        self.page.click('//ul[@class="menu-main level-0"]//a[@href="/services"]')
        self.page.wait_for_load_state()


    def our_services_section_should_be_open(self):
        if self.page.title() != "Our Services | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <'Our Services | Etteplan'>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def navigate_to_section_solutions_for_you(self):

        self.page.wait_for_selector('//ul[@class="menu-main level-0"]//a[@href="/solutions"]')
        self.page.click('//ul[@class="menu-main level-0"]//a[@href="/solutions"]')
        self.page.wait_for_timeout(2000) #The page was slow today
        self.page.wait_for_load_state


    def solutions_section_should_be_open(self):
        if self.page.title() != "Solutions for you | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <Solutions for you | Etteplan>")
        logging.info(f"Landed on page <{self.page.title()}>")
    
    
    def navigate_to_section_references(self):

        #self.page.wait_for_selector('//ul[@class="menu-main level-0"]//a[@href="/references"]')
        self.page.click('//ul[@class="menu-main level-0"]//a[@href="/references"]')
        self.page.wait_for_load_state()


    def references_section_should_be_open(self):
        #self.page.wait_for_timeout(5000)
        if self.page.title() != "References | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <References | Etteplan>")
        logging.info(f"Landed on page <{self.page.title()}>")
    
    
    def navigate_to_section_careers(self):

        self.page.wait_for_selector('//ul[@class="menu-main level-0"]//a[@href="/careers"]')
        self.page.click('//ul[@class="menu-main level-0"]//a[@href="/careers"]')
        self.page.wait_for_load_state()

    
    def careers_section_should_be_open(self):

        if self.page.title() != "Careers with a difference | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <Careers with a difference | Etteplan>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def navigate_to_section_inverstors(self):

        self.page.wait_for_selector('//ul[@class="menu-main level-0"]//a[@href="/investors"]')
        self.page.click('//ul[@class="menu-main level-0"]//a[@href="/investors"]')
        self.page.wait_for_load_state()


    def investors_section_should_be_open(self):

        if self.page.title() != "Investors | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <Investors | Etteplan>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def navigate_to_section_about_us(self):

        self.page.wait_for_selector('//ul[@class="menu-main level-0"]//a[@href="/about-us"]')
        self.page.click('//ul[@class="menu-main level-0"]//a[@href="/about-us"]')
        self.page.wait_for_load_state()


    def about_us_section_should_be_open(self):
        if self.page.title() != "About Etteplan | Etteplan":
            raise AssertionError(f"The title was <{self.page.title}> when expected title was <'About Etteplan | Etteplan'>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def navigate_to_section_contact(self):

        self.page.wait_for_selector('//ul[@class="menu-main level-0"]//a[@href="/contact-us"]')
        self.page.click('//ul[@class="menu-main level-0"]//a[@href="/contact-us"]')
        self.page.wait_for_load_state()


    def contact_us_section_should_be_open(self):

        if self.page.title() != "Contact us | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <'Contact us | Etteplan'>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def navigate_to_testing_and_test_laboratory(self):
        
        self.page.click('//a[@href="https://www.etteplan.com/services/testing-and-test-laboratory"]')
        self.page.wait_for_load_state()


    def testing_and_test_laboratory_page_should_be_open(self):
        if self.page.title() != "Testing and Test Laboratory | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <Testing and Test Laboratory | Etteplan>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def navigate_to_software_test_automation(self):
        '''A keyword to navigate to "Software test automation" page from "Testing and test laboratory"'''

        self.page.wait_for_selector('//span[@class="field-content"] //a[@href="/services/testing-and-test-laboratory/software-test-automation"]')
        self.page.click('//span[@class="field-content"] //a[@href="/services/testing-and-test-laboratory/software-test-automation"]')
        self.page.wait_for_load_state()


    def software_test_automation_page_should_be_open(self):

        if self.page.title() != "Software Test Automation Service| Etteplan | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <Software Test Automation Service| Etteplan | Etteplan>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def choose_suomi_from_dropdown(self):
        '''A keyword to navigate to Etteplan's Finnish homepage using the dropdown menu in site header. 
        In case the current page is the same one as the seeked one, the keyword is skipped.'''

        url = self.page.get_attribute('//head/link[1]', 'href')
        logging.info(f"Test started from <{url}>")
        if url != 'https://www.etteplan.com/fi':
            self.page.click('//div[@class="language-switcher"]')
            self.page.wait_for_selector('//li[@class="langcode-fi"]', timeout=5000)
            self.page.click('//li[@class="langcode-fi"]')
            self.page.wait_for_load_state
            self.page.wait_for_timeout(2000)  # Not reliable without the wait
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
            self.page.wait_for_selector('//li[@class="langcode-sv"]', timeout=5000)
            self.page.click('//li[@class="langcode-sv"]')
            self.page.wait_for_load_state
            self.page.wait_for_timeout(2000) # Not reliable without the wait
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
            self.page.wait_for_selector('//li[@class="langcode-nl"]', timeout=5000)
            self.page.click('//li[@class="langcode-nl"]')
            self.page.wait_for_load_state
            self.page.wait_for_timeout(2000) # Not reliable without the wait
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
            self.page.wait_for_selector('//li[@class="langcode-de"]', timeout=5000)
            self.page.click('//li[@class="langcode-de"]')
            self.page.wait_for_load_state
            self.page.wait_for_timeout(2000) # Not reliable without the wait
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
            self.page.wait_for_selector('//li[@class="langcode-dk"]', timeout=5000)
            self.page.click('//li[@class="langcode-dk"]')
            self.page.wait_for_load_state
            self.page.wait_for_timeout(2000) # Not reliable without the wait
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
            self.page.wait_for_selector('//li[@class="langcode-pl"]', timeout=5000)
            self.page.wait_for_load_state
            self.page.wait_for_timeout(2000) # Not reliable without the wait
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
            self.page.wait_for_selector('//li[@class="langcode-en"]', timeout=5000)
            self.page.click('//li[@class="langcode-en"]')
            self.page.wait_for_load_state(timeout=5000)
            self.page.wait_for_timeout(2000) # Not reliable without the wait
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
            self.page.wait_for_selector('//li[@class="langcode-cn"]', timeout=5000)
            self.page.click('//li[@class="langcode-cn"]')
            self.page.wait_for_load_state
            self.page.wait_for_timeout(2000) # Not reliable without the wait
        else:
            logging.info("The test was skipped because current url was the same as the requested one")


    def chinese_homepage_should_be_open(self):

        if self.page.title() != "与众不同的工程设计公司 | Etteplan":
            raise AssertionError(f"The title was <{self.page.title()}> when expected title was <与众不同的工程设计公司 | Etteplan>")
        logging.info(f"Landed on page <{self.page.title()}>")


    def navigate_to_current_country_homepage_by_clicking_logo(self):

        cid = self.page.get_attribute('//html', 'lang')   
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


    def search_for(self, item='Test automation'):
        '''A keyword for using the search bar. The search item can is given as an argument. Deafult search item is "Test automation"'''

        self.page.fill('#edit-keys', item)   
        logging.info(f"The searched item was <{item}>")
        self.page.click('#edit-submit')


    def search_results_should_appear(self):
        self.page.wait_for_selector('//a[@href="/search"]')
        if self.page.is_visible('//a[@href="/search"]') == False:
            raise AssertionError(f'Something went wrong, no search was done.')


    # Teardown
    def close_browser(self):
        """Closes browser and stops Playwright."""
        self.browser.close()
        self.playwright.stop()
        logging.info('Closed browsers and stopped Playwright')