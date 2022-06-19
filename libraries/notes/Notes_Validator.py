from requests import Response
from robot.api.deco import not_keyword, keyword
from robot.api import logger
import json


def _Get_Status(response: Response):
    response_status = response.status_code
    return response_status


@keyword('Is Notes Added')
def Is_Note_Added(response: Response):
    response_status = _Get_Status(response)
    if response_status == 201:
        response_body = response.text  # this will return json as string
        response_body = json.loads(response_body)  # Converted to Dict
        note_id = response_body['offerContainer'][0]['note'][0]['id']
        log_message = f'Note added Successfully with Note ID: {note_id}'
        logger.info(log_message,html=True,also_console=True)
        return note_id
    else:
        log_message = f'Note Can Not be Added : {response_status}'
        logger.error(log_message,html=True)
        return ''
