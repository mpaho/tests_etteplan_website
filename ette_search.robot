*** Settings ***

Library            SearchLibrary.py

Test Setup         Open Browser To Homepage
Test Teardown      Close browser

*** Test Cases ***

Search

    Search for     
    