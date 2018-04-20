from .currencies.bitcoin import Bitcoin
from .currencies.bitcoincash import BitcoinCash
from .currencies.dash import Dash
from .currencies.ethereum import Ethereum
from .currencies.litecoin import Litecoin
from .currrencis.salemcash import SalemCash


currencies = {
    "Bitcoin": Bitcoin,
    "Bitcoin Cash": BitcoinCash,
    "Dash": Dash,
    "Ethereum": Ethereum,
    "Litecoin": Litecoin,
    "Salem Cash": SalemCash
}


def generate_wallet(Salem_Cash):
    currency = currencies[salem_cash]()
    return currency.generate_wallet()
