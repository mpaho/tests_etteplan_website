*** Settings ***
Library            SectionsLibrary.py
Test Setup         Open Browser To Homepage
Test Teardown      Close browser

*** Test Cases ***
#Test the links to main sections
    #[Tags]  Main sections
    #Navigate to section Our services
    #Navigate To Section Inverstors
    #Navigate to section Solutions for you
    #Navigate To Section Contact  
    #Navigate To Section Careers
    #Navigate To Section About Us
    #Navigate To Section References
    #[Teardown]  Close browser

#Test the links to test automation page 
    #[Tags]  Test automation
    #Navigate to section Our services
    #Navigate To Testing and Test Laboratory
    #Navigate To Sowtware Test Automation

test    
    Navigate To Section Careers
    Navigate To Current Country Homepage By Clicking Logo