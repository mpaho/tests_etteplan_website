*** Settings ***

Library            CountriesLibrary.py
Resource           countries.resource
Test Setup         Open Browser To Homepage
Test Teardown      Close browser

*** Test Cases ***

Check Etteplan countries dropdown

    Switch to Etteplan Finland
    Switch to Etteplan Global English
    Switch to Etteplan Finland
    Get Country Id
    Navigate To Current Country Homepage By Clicking Logo
    Sleep    5
    #Switch to Etteplan Finland
    #Get Country Id
    #Switch to Etteplan Sweden
    #Get Country Id
    #Switch to Etteplan Netherlands
    #Switch to Etteplan Germany
    #Switch to Etteplan Denmark
    #Switch to Etteplan China
    #Switch to Etteplan Global English        
    #Switch to Etteplan Global English 