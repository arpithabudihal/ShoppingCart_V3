from requests import Response
from robot.api.deco import not_keyword, keyword
from robot.api import logger
import json
from libraries.main.ShoppingCartMain import ShoppingCartMain


def _search_sc_id_db(sc_id):
    tools = ShoppingCartMain()
    cursor, client = tools.get_db_data(dbname='shoppingcart', collection_name='shoppingcart')
    query_result = cursor.find_one({"_id": sc_id})
    tools.close_db_connection(client)
    return query_result['_id']


def _get_price_from_db(price_id):
    tools = ShoppingCartMain()
    cursor, client = tools.get_db_data(dbname='shoppingcart', collection_name='productofferingprice')
    query_result = cursor.find_one({"_id": price_id})
    tools.close_db_connection(client)
    product_offer_price = query_result['price']['value']
    try:
        tax_on_productoffer = query_result['tax'][0]['taxRate']
    except:
        tax_on_productoffer = 0.0
    return product_offer_price, tax_on_productoffer


@keyword('Check Status Code')  # Create Shopping Cart Will return 201 if created Successfully.
def Check_Status_Code(response: Response):
    response_status = response.status_code
    return response_status


@keyword('Check ShoppingCart ID')  # Should not be Empty
def Check_ShoppingCart_ID(response: Response):
    response_status = Check_Status_Code(response)
    if response_status == 201:
        response_body = response.text  # this will return json as string
        response_body = json.loads(response_body)  # Converted to Dict
        sc_id = response_body['id']
        # # Following Condition will check the Shopping cart ID generated by response present in DB or not
        db_result = _search_sc_id_db(sc_id)
        if not db_result:
            log_message = f'Shopping Cart not created in Database: {response_status}'
            logger.error(log_message, html=True)
            return ''
        else:
            log_message = f'Shopping Cart Created Successfully with ID: {sc_id}'
            logger.info(log_message, html=True, also_console=True)
            return sc_id
    else:
        log_message = f'Shopping Cart not created with status Code: {response_status}'
        logger.error(log_message, html=True)
        return ''


@keyword('Check OC Count')  # Will return how many offer container in Shopping cart
def Check_OC_Count(response: Response):
    response_body = json.loads(response.text)
    try:
        offer_containers = response_body['offerContainer']
        oc_count = len(offer_containers)
        return oc_count
    except:
        oc_count = 0
        log_message = f'Shopping Cart Response do not contain any Offer Container'
        logger.info(log_message, html=True, also_console=True)
        return oc_count


@keyword('Check OC ID')
def Check_OC_ID(response: Response)-> list:
    oc_ids = []
    oc_count = Check_OC_Count(response)
    if oc_count>0:
        response_body = json.loads(response.text)
        for i in range(oc_count):
            oc_id = response_body['offerContainer'][i]['id']
            oc_ids.append(oc_id)
    else:
        log_message = f'Shopping Cart Response do not contain any Offer Container'
        logger.error(log_message, html=True)
    # oc_ids.append("testidsjlhf821973481")
    return oc_ids


@keyword('Check CartItem ID')  # This will fetch first CartItem ID from First OC Only
def Check_CartItem_ID(response: Response):
    oc_count = Check_OC_Count(response)
    if oc_count > 0:
        response_body = json.loads(response.text)
        cartitem_id = response_body['offerContainer'][0]['cartItem'][0]['id']
        return cartitem_id
    else:
        log_message = f'There is no Offer Container in Response to get the Cart Item ID'
        logger.error(log_message, html=True)
        return ''

def _get_prices(response: Response):
    oc_count = Check_OC_Count(response)
    price_id = ''
    price_data = {}
    if oc_count > 0:
        response_body = json.loads(response.text)
        try:
            # Fetching price ID from first OC and its First Cart Item
            price_id=response_body['offerContainer'][0]['cartItem'][0]['itemPrice'][0]['priceId']
        except:
            print ('No Price Defined for Product Offer exists in First Level OC and First Level Cart Item')
        if price_id:
            product_offer_price_from_db, tax_on_productoffer_from_db =_get_price_from_db(price_id)
            cart_total_price = response_body['cartTotalPrice'][0]['price']
            offer_container_total_price = response_body['offerContainer'][0]['offerContainerTotalPrice'][0]['price']
            item_total_price = response_body['offerContainer'][0]['cartItem'][0]['itemTotalPrice'][0]['price']
            price_data['product_offer_price_from_db'] = product_offer_price_from_db
            price_data['tax_on_productoffer_from_db'] = tax_on_productoffer_from_db
            price_data['cart_total_price'] = cart_total_price
            price_data['offer_container_total_price'] = offer_container_total_price
            price_data['item_total_price'] = item_total_price

    return price_data

@keyword('Check Cart Total Price')
def Check_Cart_Total_Price(response: Response):
    price_data = _get_prices(response)
    oc_count = Check_OC_Count(response)
    if 0 < oc_count <= 1:
        dutyFreeAmount = float(price_data['cart_total_price']['dutyFreeAmount']['value'])
        taxIncludedAmount = float(price_data['cart_total_price']['taxIncludedAmount']['value'])
        dutyFreeAlteredAmount = float(price_data['cart_total_price']['dutyFreeAlteredAmount']['value'])
        taxIncludedAlteredAmount = float(price_data['cart_total_price']['taxIncludedAlteredAmount']['value'])

        log_message=(dutyFreeAmount,taxIncludedAmount,dutyFreeAlteredAmount,taxIncludedAlteredAmount)
        logger.info(log_message, html=True, also_console=True)
        logger.info(price_data['product_offer_price_from_db'], html=True, also_console=True)

        assert dutyFreeAmount == float(price_data['product_offer_price_from_db'])
        assert dutyFreeAlteredAmount == float(price_data['product_offer_price_from_db'])


        if float(price_data['tax_on_productoffer_from_db']) >0:
            price_after_tax = float(price_data['product_offer_price_from_db'])*(1+(float(price_data['tax_on_productoffer_from_db'])/100))
            assert taxIncludedAmount == price_after_tax
            assert taxIncludedAlteredAmount == price_after_tax
            logger.info(price_after_tax, html=True, also_console=True)
        else:
            assert taxIncludedAmount == float(price_data['product_offer_price_from_db'])
            assert taxIncludedAlteredAmount == float(price_data['product_offer_price_from_db'])
    else: #Write Logic here to get total of multiple OC
        pass



