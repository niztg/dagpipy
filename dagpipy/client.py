from typing import Union

from requests import Session

from dagpipy.models import *
from .enums import ImageOptions, Games
from .exceptions import *

__all__ = (
    'Client'
)

URL = "https://dagpi.tk/api/{0}"


class Client(Session):
    def __init__(
            self,
            token: str,
    ):
        super().__init__()
        self.token = token

    def get_image(
            self,
            option: ImageOptions,
            url: Union[ImageURL, str],
            **kwargs  # other stuff
    ):
        if not isinstance(url, ImageURL):
            url = ImageURL(url)
        try:
            response = self.post(URL.format(option), headers=dict(token=self.token, url=str(url), **kwargs))\
                .json()
        except:
            raise InvalidArgs()
        error = response.get('error')
        if error:
            raise ResponseError(str(error))

        return response.get('url')

    def get_game(
            self,
            option: Games
    ):
        response = self.get(URL.format(option), headers=dict(token=self.token)).json()
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
        response = self.post(URL.format("qrcode"), headers=dict(token=self.token, text=text))
        try:
            data = response.json()
        except:
            raise InvalidArgs()
        error = data.get('error')
        if error:
            raise ResponseError(str(error))

        return data.get('detail')
