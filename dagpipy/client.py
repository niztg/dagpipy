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
ERRORS = {
    403: InvalidToken(),
    413: InvalidArgs('The image you passed in was too large!'),
    422: InvalidArgs(),
    429: ResponseError('You are being rate limited!'),
    500: ResponseError('Server error. Try again later.')

}
# Constants


class Client:
    def __init__(
            self,
            token: str,
    ):
        self.auth = token

    def get_image(
            self,
            option: ImageOptions,
            url: Union[ImageURL, str],
            **kwargs  # other stuff
    ):
        response = get(
            url=URL.format("image/{0}/".format(option)),
            params=dict(url=str(ImageURL(url)), **kwargs),
            headers={'Authorization': self.auth}
        )
        error = ERRORS.get(response.status_code)
        if error:
            raise error
        return BytesIO(response.content)

    def get_game(
            self,
            option: Games
    ):
        response = get(
            url=URL.format("data/{0}".format(option)),
            headers={"Authorization": self.auth}
        ).json()
        error = ERRORS.get(response.status_code)
        if error:
            raise error
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