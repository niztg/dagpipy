from typing import Union

from requests import Session

from .models import *
from .enums import ImageOptions, Games
from .exceptions import *

__all__ = (
    'Client'
)

URL = "https://api.dagpi.xyz/{0}"
SESSION = Session()


class Client:
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
        try:
            response = SESSION.post(
                url=URL.format("image/{}".format(option)),
                headers=dict(token=self.token, url=str(ImageURL(url)), **kwargs)
            ).json()
        except:
            raise InvalidArgs()
        error = response.get('error')
        if error:
            raise ResponseError(error)

        return response.get('url')

    def get_game(
            self,
            option: Games
    ):
        response = SESSION.get(
            url=URL.format(option),
            headers=dict(token=self.token)
        ).json()
        error = response.get('error')
        if error:
            raise ResponseError(error)
        lookup = {
            "wtp": Pokemon,
            "logogame": LogoGame
        }
        model = lookup.get(option.value)
        return model(response)