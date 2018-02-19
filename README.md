python-negociecoins
======

negociecoins is a Python Wrapper for Negociecoins API

Installation
======

```bash
git clone https://github.com/decastromonteiro/python-negociecoins.git
cd python-negociecoins
python setup.py install
```

Basic Usage
======

Below you can see some of the available BitcoinTrade API methods you can use:

```python
import negociecoins
nc_public = negociecoins.NegocieCoinsPublic()
nc_public.get_ticker()
nc_trade = negociecoins.NegocieCoinsTrade(_id='yourID', _key='yourKey==')
nc_trade.get_user_balance()
nc_trade.create_order(coin_volume=0.002, price=34000, _type='sell')
```

References
======
* [NegocieCoins Public API Documentation](https://www.negociecoins.com.br/documentacao-api)
* [NegocieCoins Trade API Documentation](https://www.negociecoins.com.br/documentacao-tradeapi)

# TODO
Implement unit tests
