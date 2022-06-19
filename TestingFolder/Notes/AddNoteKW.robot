*** Settings ***
Library     Notes
Library    Notes_Validator
Variables   Notes_Variables

Resource    ../CreateShoppingCart/CreateShoppingCartKW.robot

*** Variables ***

*** Keywords ***
KW-Add Note On OfferContainer
    ${shoppingCartID}   ${OCID} =    KW-Create ShoppingCart With OfferContainer
    ${response}=    Note On Offer Container    ${note_oc_json}   ${shoppingCartID}  ${OCID[0]}
    ${note_id}=     Is Notes Added     ${response}
    should not be empty     ${note_id}





