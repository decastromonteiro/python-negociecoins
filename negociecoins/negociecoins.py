# coding=utf-8
import requests
import datetime
import json
from .auth_header import amx_authorization_header


# noinspection PyUnboundLocalVariable
class NegocieCoinsPublic:
    def __init__(self, version='v3', coin='btcbrl'):
        self.url = 'https://broker.negociecoins.com.br/api/{version}/{coin}/{action}'
        self.version = version
        self.coin = coin

    def get_ticker(self, action='ticker'):
        """https://broker.negociecoins.com.br/api/v3/btcbrl/ticker"""
        response = requests.get(self.url.format(version=self.version, coin=self.coin, action=action))

        response.close()
        return response.json()

    def get_orderbook(self, action='orderbook'):
        """https://broker.negociecoins.com.br/api/v3/btcbrl/orderbook"""
        response = requests.get(self.url.format(version=self.version, coin=self.coin, action=action))

        response.close()
        return response.json()

    def get_trades(self, method='trades'):
        """https://broker.negociecoins.com.br/api/v3/btcbrl/trades"""
        response = requests.get(self.url.format(version=self.version, coin=self.coin, method=method))

        response.close()
        return response.json()


# noinspection PyUnboundLocalVariable
class NegocieCoinsTrade:
    def __init__(self, _id, _key, version='v1'):
        # noinspection PyCompatibility
        super().__init__()
        self._id = _id
        self._key = _key
        self.version = version
        self.url = "https://broker.negociecoins.com.br/tradeapi/{version}/{action}"

    def get_user_balance(self, action='user/balance', method='GET'):
        """ https://broker.negociecoins.com.br/tradeapi/v1/user/balance"""
        api_token = amx_authorization_header(id=self._id, key=self._key, method=method, body=None,
                                             url=self.url.format(version=self.version, action=action))

        auth_header = {'Authorization': '{api_token}'.format(api_token=api_token)}

        response = requests.get(self.url.format(version=self.version, action=action), headers=auth_header)

        response.close()
        return response.json()

    def get_user_orders(self, page=1, page_size=50, pair='BRLBTC', _type='buy', status='pending',
                        start_id=1, end_id=9999999, action='user/orders', method='POST',
                        start_date=(datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                        end_date=datetime.datetime.now().strftime('%Y-%m-%d')):
        """ https://broker.negociecoins.com.br/tradeapi/v1/user/orders"""

        data_dict = {'page': page, 'pageSize': page_size, 'pair': pair, 'type': _type, 'status': status,
                     'startId': start_id, 'endId': end_id, 'startDate': start_date, 'endDate': end_date}

        api_token = amx_authorization_header(id=self._id, key=self._key, method=method, body=json.dumps(data_dict),
                                             url=self.url.format(version=self.version, action=action))

        auth_header = {'Authorization': '{api_token}'.format(api_token=api_token)}

        response = requests.post(url=self.url.format(version=self.version, action=action),
                                 json=data_dict,
                                 headers=auth_header)

        response.close()
        return response.json()

    def get_order(self, orderid, action='user/order/{orderid}', method='GET'):
        """https://broker.negociecoins.com.br/tradeapi/v1/user/order/{ orderId }"""

        if not orderid:
            raise NotImplementedError

        api_token = amx_authorization_header(id=self._id, key=self._key, method=method, body=None,
                                             url=self.url.format(version=self.version,
                                                                 action=action.format(orderid=orderid)))

        auth_header = {'Authorization': '{api_token}'.format(api_token=api_token)}

        response = requests.get(self.url.format(version=self.version, action=action.format(orderid=orderid)),
                                headers=auth_header)

        return response.json()

    def create_order(self, coin_volume: int, price: int, broker_id=None, user_id=None, pair='BRLBTC', _type='buy',
                     action='user/order', method='POST'):
        """https://broker.negociecoins.com.br/tradeapi/v1/user/order"""

        data_dict = {'pair': pair, 'type': _type, 'volume': coin_volume, 'price': price}
        if broker_id:
            data_dict.update({'brokerID': broker_id})
        if user_id:
            data_dict.update({'userID': user_id})

        api_token = amx_authorization_header(id=self._id, key=self._key, method=method, body=json.dumps(data_dict),
                                             url=self.url.format(version=self.version, action=action))

        auth_header = {'Authorization': '{api_token}'.format(api_token=api_token)}

        response = requests.post(url=self.url.format(version=self.version, action=action),
                                 json=data_dict,
                                 headers=auth_header)

        response.close()
        return response.json()

    def delete_order(self, orderid, method='DELETE', action='user/order/{orderid}'):
        """https://broker.negociecoins.com.br/tradeapi/v1/user/order/{ orderId }"""

        if not orderid:
            raise NotImplementedError

        api_token = amx_authorization_header(id=self._id, key=self._key, method=method, body=None,
                                             url=self.url.format(version=self.version,
                                                                 action=action.format(orderid=orderid)))

        auth_header = {'Authorization': '{api_token}'.format(api_token=api_token)}

        response = requests.delete(url=self.url.format(version=self.version, action=action.format(orderid)),
                                   headers=auth_header)

        response.close()
        return response.json()
