from typing import Union

from requests import post, get
from simplejson import JSONDecodeError

from dagpipy.models import *
from .enums import ImageOptions, Games
from .exceptions import *

__all__ = (
    'Client'
)

URL = "https://dagpi.tk/api/{0}"

class Client:
    def __init__(
            self,
            token: str,
    ):
        self.token = token

    def get_image(
            self,
            option: ImageOptions,
            url: Union[ImageURL, str],
            **kwargs  # other stuff
    ):
        if not isinstance(url, ImageURL):
            url = imageurl.ImageURL(url)
        headers = {'token': self.token, 'url': url}
        for k, v in kwargs.items():
            if not isinstance(v, str):
                headers[k] = str(v)
            else:
                headers[k] = v
        response = post(URL.format(option), headers=headers)
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
        response = get(URL.format(option), headers={'token': self.token}).json()
        error = response.get('error')
        if error:
            raise ResponseError(error)
        lookup = {
            "wtp": Pokemon,
            "logogame": LogoGame
        }
        model = lookup.get(option.value)
        return model(response)

    def get_qr_code(self, text):
        response = post(URL.format("qrcode"), headers={"token": self.token, "text": text})
        try:
            data = response.json()
        except:
            raise InvalidArgs()
        error = data.get('error')
        if error:
            raise ResponseError(str(error))

        return data.get('url')
