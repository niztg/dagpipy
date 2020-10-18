## Documentation for dagpipy
A Python API Wrapper for https://dagpi.xyz/, the fast and free image API.

#### Table of Contents:
- [Client]()
- [ImageURL]()
- [Enums]()
- [Objects]()
- [Exceptions]()


# Client
<h2><em>class</em> dagpipy.<strong>Client</strong>(<em>token</em>)</h2>
The Client class which interacts with the API itself. 

<br>**Paramters:**<br>
`token` (str): The authorization token which you can get from https://dagpi.xyz/

### get_image(<em>option, url, **kwargs</em>)
Get an image from the Image API

**Parameters:**<br>
`option` ([ImageOptions]()): The image option you want to retrieve<br>
`url` (Union\[str, [ImageURL]()]): The url of the image you want to manipulate<br>
`**kwargs` (Optional): The parameters used in the API request. These vary depending on the `option` param. See the [ImageOptions]() or [dagpi](https://dagpi.docs.apiary.io/#reference/images-api) docs to see what these are for each specific case.

**Return type:**<br>
[io.BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO)

**Raises:**<br>
[InvalidToken](): If your token was invalid<br>
[InvalidArgs](): If you passed in invalid kwargs for the given option parameter, or if your image was too big.<br>
[ResponseError](): If you are being rate limited, or there is an internal server error.<br>

**Examples:**<br>
```py
from PIL import Image

bad = client.get_image(
    option=dagpipy.ImageOptions.bad,
    url=url
)

bad_image = Image.open(bad)
bad_image.show()
```

```py
from PIL import Image

tweet = client.get_image(
    option=dagpipy.ImageOptions.tweet,
    url=url,
    username="dagpipy",
    text="amazing"
)

tweet_image = Image.open(tweet)
tweet_image.show()
```

```py
from PIL import Image

whyareyougay = client.get_image(
    option=dagpipy.ImageOptions.whyareyougay,
    url=url,
    url2=url
)

whyareyougay_image = Image.open(whyareyougay)
whyareyougay_image.show()
```

### get_game(<em>option</em>)
Get an object from the Data API

**Parameters:**<br>
`option` ([Games]()): The object you want to retrieve. 

**Return type:**<br>
Union\[[Pokemon](), [LogoGame](), [Roast](), [YoMama](), [PickupLine](), [Joke](), [Waifu]()]

**Raises:**<br>
[InvalidToken](): If your token was invalid

**Examples:**<br>
```py
wtp = client.get_game(
    option=dagpipy.Games.whos_that_pokemon
)
print(wtp.name)
print(wtp.question)
print(wtp.answer)
print(wtp.types)
print(wtp.abilities)
```

```py
joke = client.get_game(
    option=dagpipy.Games.joke
)
print(joke.id)
print(joke.joke)
```
