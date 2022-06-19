'''
This Module will act as custom RobotFramework Library and will contain Custom Keywords related to
Create ShoppingCart
'''
from requests import Response
from libraries.main import global_variables
from libraries.main import ShoppingCartDataUtil
from libraries.main.ShoppingCartMain import ShoppingCartMain
from libraries.main.api import CreateShoppingCartAPI
from robot.api.deco import keyword, library

# Initialize ShoppingCartMain module's Tool class to access all its shared methods
tools = ShoppingCartMain()


@library
class CreateShoppingCart:
    # Initialize Data Mapper to make changes in base Json data from data sheet
    ''' Need to Change Shopping cart create config sheet name and data sheet name from config and data files if 
    required '''
    # ***** Following Variables based on API under TEST****
    # ****************************************************
    cfg_sheet_name = 'CreateShoppingCart'
    data_sheet_name = 'CreateShoppingCart'
    # ****************************************************
    # Initiating CreateSC Data Transform Class and Calling Data Mapper function to modify data according to Data Sheet
    c = ShoppingCartDataUtil.ShoppingCartDataUtil(cfg_sheet_name=cfg_sheet_name,data_sheet_name=data_sheet_name)
    c._data_mapper()

    # get token, base_url and endpoint from global variable module .
    token = global_variables.token
    base_url = global_variables.base_url
    create_shopping_cart_endpoint = global_variables.create_shopping_cart_api
    # Set default header
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    @keyword('Create Empty ShoppingCart')
    def Create_Empty_ShoppingCart(self, request_json):
        response = CreateShoppingCartAPI(baseURL=self.base_url, apiEndPoint=self.create_shopping_cart_endpoint,
                                         headers=self.headers,
                                         body=request_json)
        return response

    @keyword('Create ShoppingCart with OC and CI')
    def Create_ShoppingCart(self, request_json):
        response: Response = CreateShoppingCartAPI(baseURL=self.base_url,
                                                   apiEndPoint=self.create_shopping_cart_endpoint, headers=self.headers,
                                                   body=request_json)
        return response




# *********************Following Code is for Code Testing Purpose Only **********************
# *******************************************************************************************
# from libraries.createsc.CreateSCVariables import create_empty_sc_json,create_sc_json
# newc = CreateShoppingCart()
# Create_Empty_ShoppingCart_response = newc.Create_Empty_ShoppingCart(request_json=create_empty_sc_json)
# print(Create_Empty_ShoppingCart_response.status_code, Create_Empty_ShoppingCart_response.text)

# Create_ShoppingCart_response = newc.Create_ShoppingCart(request_json=create_sc_json)
# print(Create_ShoppingCart_response.status_code, Create_ShoppingCart_response.text)
