*** Settings ***
Library            CountriesLibrary.py




*** Keywords ***
Switch to Etteplan Finland
    [Tags]  Finland
    Choose Suomi from dropdown
    Finnish homepage should be open

Switch to Etteplan Sweden
    [Tags]  Sweden
    Choose Sverige from dropdown
    Swedish homepage should be open

Switch to Etteplan Netherlands
    [Tags]  Netherlands
    Choose Nederland from dropdown
    Dutch homepage should be open

Switch to Etteplan Germany
    [Tags]  Germany
    Choose Deutchland from dropdown
    German homepage should be open
    
Switch to Etteplan Denmark
    [Tags]  Denmark
    Choose Danmark from dropdown
    Danish homepage should be open

Switch to Etteplan China
    [Tags]  China
    Choose Chinese from dropdown
    Chinese homepage should be open


Switch to Etteplan Global English      # Cannot be used if already on that page!
    [Tags]  English
    Choose Global English from dropdown
    English homepage should be open