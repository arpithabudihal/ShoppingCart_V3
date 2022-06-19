from libraries.main.ShoppingCartMain import ShoppingCartMain
from robot.api.deco import not_keyword


tools = ShoppingCartMain()

@not_keyword
def MyToken():
    '''
    This function reads global sheet which contains base url and token related information
    :return: It will return newly generated token and application base url
    '''
    global_settings = tools.read_conf(sheet_name='global')
    global_settings = global_settings[list(global_settings)[0]]
    token_url = global_settings['token_url']
    app_url = global_settings['api_base_url']
    headers = {"content-type": "application/x-www-form-urlencoded", "Accept-Charset": "UTF-8"}
    data = dict(client_id=global_settings['client_id'], client_secret=global_settings['client_secret'],
                username=global_settings['username'],
                password=global_settings['password'], scope=global_settings['scope'],
                grant_type=global_settings['grant_type'])
    new_token = tools.get_token(token_url=token_url, headers=headers, data=data)
    return new_token, app_url

@not_keyword
def ApiEndPoints() -> dict:
    '''
    Reads all the end points mentioned in end points sheet within main configuration file
    :return: All Application end points in dictionary
    '''
    api_end_points = tools.read_conf(sheet_name='endpoints')
    api_end_points = api_end_points[list(api_end_points)[0]]
    return api_end_points

# Below section will be used to set global variables

token, base_url = MyToken() # setting up token and base url variables

# setting up all api end points variables
# Note ** --> Add All API points here in try section
all_api = ApiEndPoints()
try:
    create_shopping_cart_api = all_api['create_shopping_cart']
    add_offer_container_api = all_api['add_offer_container']
    update_offer_containers_api = all_api['update_offer_containers']
    note_on_offer_container_api = all_api['note_on_offer_container']

except KeyError as e:
    print(f"Key {e} not found in Configuration Excl's Endpoint worksheet")
