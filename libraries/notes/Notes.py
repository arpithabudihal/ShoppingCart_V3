'''
This Module will act as custom RobotFramework Library and will contain Custom Keywords related to
Create ShoppingCart
'''
from requests import Response
from libraries.main import global_variables
from libraries.main.ShoppingCartMain import ShoppingCartMain
from libraries.main import ShoppingCartDataUtil
from libraries.main.api import NoteOCAPI
from robot.api.deco import keyword, library

# Initialize ShoppingCartMain module's Tool class to access all its shared methods
tools = ShoppingCartMain()


@library
class Notes:
    # Initialize Data Mapper to make changes in base Json data from data sheet
    ''' Need to Change Shopping cart create config sheet name and data sheet name from config and data files if
    required '''
    # ***** Following Variables based on API under TEST****
    # ****************************************************
    cfg_sheet_name = 'Notes'
    data_sheet_name = 'Notes'
    # ****************************************************
    # Initiating CreateSC Data Transform Class and Calling Data Mapper function to modify data according to Data Sheet
    c = ShoppingCartDataUtil.ShoppingCartDataUtil(cfg_sheet_name=cfg_sheet_name, data_sheet_name=data_sheet_name)
    c._data_mapper()

    # get token, base_url and endpoint from global variable module .
    token = global_variables.token
    base_url = global_variables.base_url
    NotesOC_endpoint = global_variables.note_on_offer_container_api
    # Set default header
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    @keyword('Note On Offer Container')
    def Note_On_Offer_Container(self, request_json, shoppingCartId, offerContainerId):
        # Following line will map {shoppingCartId} in api end point with variable shoppingCartId.
        NotesOC_endpoint = self.NotesOC_endpoint.format(shoppingCartId=shoppingCartId,offerContainerId=offerContainerId)
        # print(NotesOC_endpoint)
        response: Response = NoteOCAPI(baseURL=self.base_url,
                                      apiEndPoint=NotesOC_endpoint, headers=self.headers,
                                      body=request_json)
        # print(response.text)
        return response



# *********************Following Code is for Code Testing Purpose Only **********************
# *******************************************************************************************
# from libraries.notes.Notes_Variables import note_oc_json
# from libraries.createsc.CreateSCVariables import create_sc_json
# from libraries.createsc.CreateShoppingCart import CreateShoppingCart
# from libraries.createsc.CreateSCValidator import Check_ShoppingCart_ID, Check_OC_ID,Check_CartItem_ID
# createsc = CreateShoppingCart()
# Create_ShoppingCart_response = createsc.Create_ShoppingCart(request_json=create_sc_json)
# shoppingCartId = Check_ShoppingCart_ID(Create_ShoppingCart_response)
# offerContainerIds = Check_OC_ID(Create_ShoppingCart_response)
# offerContainerId = offerContainerIds[0]
#
# notes = Notes()
# note_resp = notes.Note_On_Offer_Container(note_oc_json,shoppingCartId=shoppingCartId,offerContainerId=offerContainerId)

