*** Settings ***

Library            EtteplanLibrary.py


Suite Setup         Open Browser To Homepage
Suite Teardown      Close browser

*** Test Cases ***


Test the links to main sections
    [Tags]    XRAYT-12

    Navigate to section Our services
    Our Services Section Should Be Open

    Navigate To Section Inverstors
    Investors Section Should Be Open

    Navigate to section Solutions for you
    Solutions Section Should Be Open

    Navigate To Section Contact 
    Contact Us Section Should Be Open

    Navigate To Section Careers
    Careers Section Should Be Open

    Navigate To Section About Us
    About Us Section Should Be Open

    Navigate To Section References
    References Section Should Be Open


Test navigation to homepage by clicking the logo
    [Tags]    XRAYT-6

    Navigate To Section Careers
    Navigate To Current Country Homepage By Clicking Logo
    English Homepage Should Be Open
 

Test Etteplan countries dropdown menu
    [Tags]    countries
    
    Choose Suomi from dropdown
    Finnish homepage should be open

    Choose Sverige from dropdown
    Swedish homepage should be open

    Choose Nederland from dropdown
    Dutch homepage should be open

    Choose Deutchland from dropdown
    German homepage should be open

    Choose Danmark from dropdown
    Danish homepage should be open

    Choose Chinese from dropdown
    Chinese homepage should be open

    Choose Global English from dropdown
    English homepage should be open

Test search field
    [Tags]  XRAYT-7

    Search for   software testing
    Search Results Should Appear


Test navigationg to test automation page
    [Tags]  ta

    Navigate to section Our services
    Our Services Section Should Be Open

    Navigate To Testing And Test Laboratory
    Testing And Test Laboratory Page Should Be Open

    Navigate To Software Test Automation
    Software Test Automation Page Should Be Open


    