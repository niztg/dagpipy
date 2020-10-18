## Documentation for dagpipy
A Python API Wrapper for https://dagpi.xyz/, the fast and free image API.

#### Table of Contents:
- [Client](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#client)
- [ImageURL](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#imageurl)
- [Enums](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#enums)
- [Objects]()
- [Exceptions]()


# Client
<h2><em>class</em> dagpipy.Client(<em>token</em>)</h2>
The Client class which interacts with the API itself. 

<br>**Paramters:**<br>
`token` (str): The authorization token which you can get from https://dagpi.xyz/

### get_image(<em>option, url, **kwargs</em>)
Get an image from the Image API

**Parameters:**<br>
`option` ([ImageOptions](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipyimageoptions)): The image option you want to retrieve<br>
`url` (Union\[str, [ImageURL](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#imageurl)]): The url of the image you want to manipulate<br>
`**kwargs` (Optional): The parameters used in the API request. These vary depending on the `option` param. See the [ImageOptions]() or [dagpi](https://dagpi.docs.apiary.io/#reference/images-api) docs to see what these are for each specific case.

**Return type:**<br>
[io.BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO)

**Raises:**<br>
[InvalidToken](): If your token was invalid.<br>
[InvalidImageURL](): If the image url you passed in was invalid.<br>
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

<hr>

# ImageURL
<h2><em>class</em> dagpipy.ImageURL(<em>url</em>)</h2>
Class that validates image urls.

<br>**Parameters:**<br>
`url` (str): An image url

**Raises:**<br>
[InvalidImageURL](): When the image url you passed in was invalid.


# Enums
## <em>class</em> dagpipy.ImageOptions
The `option` param used in the [Client.get_image](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#get_imageoption-url-kwargs) function.

### wanted
For a wanted image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.wanted,
    url=url
)
```

### tweet
For a tweet image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.tweet,
    url=url,
    username='example username',
    text='cool tweet'
)
```

### quote
For a quote image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.quote,
    url=url,
    name='example username',
    text='cool quote'
)
```

### thought_image
For a thought image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.thought_image,
    url=url,
#    name='example username',
#    text='cool quote'
)
```

### obama
For the Obama Meme image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.obama,
    url=url
)
```

### bad
For a bad boy >:(

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.bad,
    url=url
)
```

### hitler
Worse than hitler!

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.hitler,
    url=url
)
```

### angel
An angel

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.angel,
    url=url
)
```


### trash
POV: You

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.trash,
    url=url
)
```


### satan
el diablo

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.satan,
    url=url
)
```

### sobel
Idk what this means

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.sobel,
    url=url
)
```

### hogend
Idk what this means either

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.hogend,
    url=url
)
```

### paint
Paint on something

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.paint,
    url=url
)
```

### night
Scary darkness

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.night,
    url=url
)
```

### polaroid
Polaroid

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.polaroid,
    url=url
)
```

### solar
sunlight

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.solar,
    url=url
)
```


### edge
edgy

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.edge,
    url=url
)
```

### evil
Eeeevil

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.evil,
    url=url
)
```

### blur
Blurify an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.blur,
    url=url
)
```

### invert
Invert an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.invert,
    url=url
)
```

### pixel
Pixelate an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.pixel,
    url=url
)
```

### ascii
Ascii-fy an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.ascii,
    url=url
)
```

### deepfry
🅱

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.deepfry,
    url=url
)
```

### sepia
Make an image into sepia

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.deepfry,
    url=url
)
```

### wasted
Duhduh wasteeed

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.wasted,
    url=url
)
```

### triggered
Brrrr

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.triggered,
    url=url
)
```

### jail
Criminal

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.jail,
    url=url
)
```

### gay
🏳️‍🌈

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.gay,
    url=url
)
```

### jail
Criminal

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.jail,
    url=url
)
```

### colours/colors
Colours

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.colours,
    url=url
)
```

### rgb_data
Get the rgb data of an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.rgb_data,
    url=url
)
```

### whyareyougay
Why are you gay image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.whyareryougay,
    url=url,
    url2=url
)
```

### five_guys_one_girl
this meme

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.five_guys_one_girl,
    url=url,
    url2=url
)
```

## <em>class</em> dagpipy.Games
The `option` parameter in the [Client.get_game](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#get_gameoption) function. 

### whos_that_pokemon
Returns the [Pokemon]() object when used

**Example:**
```py
client.get_game(
    option=dagpipy.ImageOptions.whos_that_pokemon,
)
```

### logo_guessing
Returns the [LogoGame]() object when used

**Example:**
```py
client.get_game(
    option=dagpipy.ImageOptions.logo_guessing,
)
```

### roast
Returns the [Roast]() object when used

**Example:**
```py
client.get_game(
    option=dagpipy.ImageOptions.roast,
)
```


### yo_mama
Returns the [YoMama]() object when used

**Example:**
```py
client.get_game(
    option=dagpipy.ImageOptions.yo_mama,
)
```

### pickupline
Returns the [PickupLine]() object when used

**Example:**
```py
client.get_game(
    option=dagpipy.ImageOptions.pickupline,
)
```

### waifu
Returns the [Waifu]() object when used

**Example:**
```py
client.get_game(
    option=dagpipy.ImageOptions.waifu,
)
```


### joke
Returns the [Joke]() object when used

**Example:**
```py
client.get_game(
    option=dagpipy.ImageOptions.joke,
)
```
