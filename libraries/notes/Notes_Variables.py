from libraries.main.ShoppingCartMain import ShoppingCartMain
from robot.api.deco import not_keyword


@not_keyword
def get_json_req() -> dict:
    '''
    This Function will read all json files provided in API configuration sheet available in main
    configuration file.It will read all json file and return the dict of json file as key and json file
     content as value.
    :return:
    '''
    json_request = {}
    # Initialize ShoppingCartMain module's  class to access all its shared methods
    tools = ShoppingCartMain()
    # *****Change Sheet Name according to API Sheet Name under TEST*****
    cfg_sheet_name = 'Notes'

    # Get modified json request body
    # following will fetch all json files : {dict} mentioned in Shopping cart config sheet under config doc.
    json_req_files = tools.get_modified_json_files(cfg_sheet_name=cfg_sheet_name)
    # Below piece of code will read all modified jsons body and will store in dict respective to key in conf file.
    for key, value in json_req_files.items():
        json_request[key] = tools.read_modified_json(filename=json_req_files[key])
    return json_request


json_requests = get_json_req()

# Set all local variables in following section
#       ***** Setting json request body *****
note_oc_json = json_requests['note_oc_json']
# print(note_oc_json)

