'''
This Module will act as custom RobotFramework Library and will contain Custom Keywords related to
Create ShoppingCart
'''
from requests import Response
from libraries.main import global_variables
from libraries.main.ShoppingCartMain import ShoppingCartMain
from libraries.main import ShoppingCartDataUtil
from libraries.main.api import AddOCAPI
from robot.api.deco import keyword, library

# Initialize ShoppingCartMain module's Tool class to access all its shared methods
tools = ShoppingCartMain()


@library
class AddOC:
    # Initialize Data Mapper to make changes in base Json data from data sheet
    ''' Need to Change Shopping cart create config sheet name and data sheet name from config and data files if
    required '''
    # ***** Following Variables based on API under TEST****
    # ****************************************************
    cfg_sheet_name = 'AddOC'
    data_sheet_name = 'AddOC'
    # ****************************************************
    # Initiating CreateSC Data Transform Class and Calling Data Mapper function to modify data according to Data Sheet
    c = ShoppingCartDataUtil.ShoppingCartDataUtil(cfg_sheet_name=cfg_sheet_name, data_sheet_name=data_sheet_name)
    c._data_mapper()

    # get token, base_url and endpoint from global variable module .
    token = global_variables.token
    base_url = global_variables.base_url
    AddOC_endpoint = global_variables.add_offer_container_api
    # Set default header
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    @keyword('Add Single Offer Container')
    def Add_OfferContainer(self, request_json, shoppingCartId):
        # Following line will map {shoppingCartId} in api end point with variable shoppingCartId.
        AddOC_endpoint = self.AddOC_endpoint.format(shoppingCartId=shoppingCartId)
        response: Response = AddOCAPI(baseURL=self.base_url,
                                      apiEndPoint=AddOC_endpoint, headers=self.headers,
                                      body=request_json)
        return response


# *********************Following Code is for Code Testing Purpose Only **********************
# *******************************************************************************************
# from libraries.addoc.AddOCVariables import add_oc_json
# from libraries.createsc.CreateSCVariables import create_empty_sc_json,create_sc_json
# from libraries.createsc.CreateShoppingCart import CreateShoppingCart
# createsc = CreateShoppingCart()
# addOC = AddOC()
#
# Create_Empty_ShoppingCart_response = createsc.Create_Empty_ShoppingCart(request_json=create_empty_sc_json)
# print(Create_Empty_ShoppingCart_response.status_code, Create_Empty_ShoppingCart_response.text)
#
# # Create_ShoppingCart_response = newc.Create_ShoppingCart(request_json=create_sc_json)
# # print(Create_ShoppingCart_response.status_code, Create_ShoppingCart_response.text)
