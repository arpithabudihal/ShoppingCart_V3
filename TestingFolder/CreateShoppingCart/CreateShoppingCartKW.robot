*** Settings ***
Library    CreateShoppingCart
Library    CreateSCValidator
Variables   CreateSCVariables

*** Variables ***


*** Keywords ***
KW-Create Empty ShoppingCart
    [Tags]    Create SC
    ${response}=    Create Empty ShoppingCart   ${create_empty_sc_json}
    ${sc_id}=   Check ShoppingCart ID    ${response}
    should not be empty    ${sc_id}
    [Return]    ${sc_id}


KW-Create ShoppingCart With OfferContainer
    [Tags]    Create SC
    ${response}=    Create ShoppingCart with OC and CI    ${create_sc_json}
    ${sc_id}=   Check ShoppingCart ID    ${response}
    log to console    ShoppingCart ID is:${sc_id}
    should not be empty    ${sc_id}
    ${oc_count}=    Check OC Count    ${response}
    should be equal    ${1}    ${oc_count}
    ${oc_ids}=  Check OC ID    ${response}
    should not be empty    ${oc_ids[0]}
    log to console    OfferContainer ID is:${oc_ids[0]}
    ${cartitem_id}=     Check CartItem ID    ${response}
    log to console    CartItem ID is:${cartitem_id}
    should not be empty     ${cartitem_id}
    #check cart total price      ${response}
    [Return]    ${sc_id}    ${oc_ids}





