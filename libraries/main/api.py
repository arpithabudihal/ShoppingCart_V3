'''
This is Main Module part pf Main Package which contains Shared Methods those can be called in any HighLevel code base.
Created by Arpitha B Date:24th May 2022
Last Modified by Arpitha B Date:27th May 2022
'''
import requests
from requests import Response
from requests.models import Response
import json


def CreateShoppingCartAPI(baseURL: str, apiEndPoint: str, headers: dict, body: str) -> Response:
    '''
    This Function will do POST request to Create Shopping Cart API
    :param baseURL: Base URL
    :param apiEndPoint: API End Point
    :param headers: Request Headers
    :param body: Request Body
    :return: Response of Post Request
    '''
    url = baseURL + apiEndPoint
    try:
        response: Response = requests.post(url, headers=headers, data=body)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response


def AddOCAPI(baseURL: str, apiEndPoint: str, headers: dict, body) -> Response:
    url = baseURL + apiEndPoint
    try:
        response: Response = requests.post(url, headers=headers, data=body)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response


def UpdateOCsAPI(baseURL: str, apiEndPoint: str, headers: dict, body) -> Response:
    url = baseURL + apiEndPoint
    try:
        response: Response = requests.put(url, headers=headers, data=body)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response


def NoteOCAPI(baseURL: str, apiEndPoint: str, headers: dict, body) -> Response:
    url = baseURL + apiEndPoint
    # print(url)
    try:
        response: Response = requests.post(url, headers=headers, data=body)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response