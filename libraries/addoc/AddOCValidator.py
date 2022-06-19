from requests import Response
from robot.api.deco import not_keyword, keyword
from robot.api import logger
import json


def _Get_Status(response: Response):
    response_status = response.status_code
    return response_status


@keyword('Is OfferContainer Added')
def Is_OfferContainer_Added(response: Response):
    response_status = _Get_Status(response)
    if response_status == 201:
        response_body = response.text  # this will return json as string
        response_body = json.loads(response_body)  # Converted to Dict
        sc_id = response_body['id']
        log_message = f'Offer Container added Successfully with ID: {sc_id}'
        logger.info(log_message,html=True,also_console=True)
        return sc_id
    else:
        log_message = f'Offer Container can not be added with status Code: {response_status}'
        logger.error(log_message,html=True)
        return ''
