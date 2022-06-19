*** Settings ***
Library    AddOC
Library    AddOCValidator
Variables   AddOCVariables

Resource    ../CreateShoppingCart/CreateShoppingCartKW.robot

*** Variables ***

*** Keywords ***
KW-Add One OfferContainer
    ${shoppingCartID}=    KW-Create Empty ShoppingCart
    ${response}=    Add Single Offer Container    ${add_oc_json}   ${shoppingCartID}
    Is OfferContainer Added     ${response}
    log to console    ${response}


