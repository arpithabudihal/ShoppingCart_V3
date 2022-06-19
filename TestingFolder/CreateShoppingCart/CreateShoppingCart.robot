*** Settings ***
#Library    CreateShoppingCart
#Library    CreateSCValidator
#Variables   CreateSCVariables
Resource    CreateShoppingCartKW.robot

*** Variables ***


*** Test Cases ***
TC1-Create Empty ShoppingCart
    [Tags]    Create SC
    KW-Create Empty ShoppingCart


TC2-Create ShoppingCart With OfferContainer
    [Tags]    Create SC
    KW-Create ShoppingCart With OfferContainer






