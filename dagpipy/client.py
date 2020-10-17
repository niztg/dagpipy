from typing import Union

from requests import get
from io import BytesIO

from .models import *
from .enums import ImageOptions, Games
from .exceptions import *

__all__ = (
    'Client'
)

URL = "https://api.dagpi.xyz/{0}"


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
        response = get(
            url=URL.format("image/{0}/".format(option)),
            params=dict(url=str(ImageURL(url)), **kwargs),
            headers={'Authorization': self.token}
        )
        try:
            return BytesIO(response.content)
        except Exception as error:
            raise InvalidArgs() from error

    def get_game(
            self,
            option: Games
    ):
        response = get(
            url=URL.format("data/{0}".format(option)),
            headers={"Authorization": self.token}
        ).json()
        error = response.get('error')
        if error:
            raise ResponseError(error)
        lookup = {
            "wtp": Pokemon,
            "logogame": LogoGame,
            "roast": Roast,
            "yomama": YoMama,
            "pickupline": PickupLine,
            "joke": Joke
        }
        model = lookup.get(str(option))
        return model(response)