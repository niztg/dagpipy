from typing import Union

from requests import post, get
from simplejson import JSONDecodeError

from dagpipy.models import pokemon, logo, imageurl
from .enums import ImageOptions, Games
from .exceptions import *

__all__ = (
    'Client'
)

URL = "https://dagpi.tk/api/{0}"


def urlformatter(option):
    return URL.format(str(option))


def makeheaders(token, url, **kwargs):
    _dict = {'token': token, 'url': url}
    for key, value in kwargs.items():
        _dict[key] = value
    return _dict


class Client:
    def __init__(
            self,
            token: str,
    ):
        self.token = token

    def get_image(
            self,
            option: ImageOptions,
            url: Union[imageurl.ImageURL, str],
            **kwargs  # other stuff
    ):
        if not isinstance(url, imageurl.ImageURL):
            url = imageurl.ImageURL(url)
        _kwargs = {}
        for k, v in kwargs.items():
            if not isinstance(v, str):
                try:
                    _kwargs[k] = str(v)
                except:
                    raise InvalidArgs("Expected str or ImageURL types, got {0.__class__.__name__}".format(v))
            else:
                _kwargs[k] = v
        response = post(urlformatter(option), headers=makeheaders(self.token, str(url), **_kwargs))
        try:
            data = response.json()
        except JSONDecodeError:
            raise InvalidArgs()
        error = data.get('error')
        if error:
            raise ResponseError(str(error))

        return data.get('url')

    def get_game(
            self,
            option: Games
    ):
        response = get(urlformatter(option), headers={'token': self.token})
        try:
            data = response.json()
        except Exception as error:
            raise ResponseError(str(error))
        error = data.get('error')
        if error:
            raise ResponseError(error)
        lookup = {
            "wtp": pokemon.Pokemon,
            "logogame": logo.LogoGame
        }
        model = lookup.get(option.value)
        return model(data)

    def get_qr_code(self, text):
        response = post(urlformatter("qrcode"), headers={"token": self.token, "text": text})
        try:
            data = response.json()
        except:
            raise InvalidArgs()
        error = data.get('error')
        if error:
            raise ResponseError(str(error))

        return data.get('url')
