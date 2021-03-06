## Documentation for dagpipy
A Python API Wrapper for https://dagpi.xyz/, the fast and free image API.

#### Table of Contents:
- [Client](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#client)
    - [get_image](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#get_imageoption-url-kwargs)
    - [get_game](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#get_gameoption)
- [ImageURL](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#imageurl)
- [Enums](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#enums)
    - [ImageOptions](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipyimageoptions)
    - [Games](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipygames)
- [Objects](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#objects)
    - [Pokemon](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipypokemon)
    - [LogoGame](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipylogogame)
    - [Roast](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipyroast)
    - [YoMama](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipyyomama)
    - [PickupLine](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipypickupline)
    - [Joke](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipyjoke)
    - [Waifu](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipywaifu)
    - [Series](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipyseries)
    - [Creator](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipycreator)
- [Exceptions](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#exceptions)
    - [InvalidToken](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#exception-dagpipyinvalidtoken)
    - [InvalidArgs](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#exception-dagpipyinvalidargs)
    - [ResponseError](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#exception-dagpipyresponseerror)
    - [InvalidImageURL](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#exception-dagpipyinvalidimageurl)


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
`**kwargs` (Optional): The parameters used in the API request. These vary depending on the `option` param. See the [ImageOptions](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipyimageoptions) or [dagpi](https://dagpi.docs.apiary.io/#reference/images-api) docs to see what these are for each specific case.

**Return type:**<br>
[io.BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO)

**Raises:**<br>
[InvalidToken](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#exception-dagpipyinvalidtoken): If your token was invalid.<br>
[InvalidImageURL](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#exception-dagpipyinvalidargs): If the image url you passed in was invalid.<br>
[InvalidArgs](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#exception-dagpipyresponseerror): If you passed in invalid kwargs for the given option parameter, or if your image was too big.<br>
[ResponseError](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#exception-dagpipyinvalidimageurl): If you are being rate limited, or there is an internal server error.<br>

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
`option` ([Games](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipygames)): The object you want to retrieve. 

**Return type:**<br>
Union\[[Pokemon](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipypokemon), [LogoGame](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipylogogame), [Roast](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipyroast), [YoMama](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipyyomama), [PickupLine](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipypickupline), [Joke](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipyjoke), [Waifu](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipywaifu)]

**Raises:**<br>
[InvalidToken](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#exception-dagpipyinvalidtoken): If your token was invalid

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
[InvalidImageURL](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#exception-dagpipyinvalidimageurl): When the image url you passed in was invalid.


# Enums
## <em>class</em> dagpipy.ImageOptions
The `option` param used in the [Client.get_image](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#get_imageoption-url-kwargs) function.

### pixel
Pixelate an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.pixel,
    url=url
)
```

### colors/colours
Get an images top 5 colours

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.colours,
    url=url
)
```

### wanted
Get a wanted poster of an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.wanted,
    url=url
)
```

### triggered
Get a triggered gif of an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.triggerd,
    url=url
)
```

### wasted
Get a GTA V wasted screen of an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.wasted,
    url=url
)
```

### five_guys_one_girl
This meme

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.five_guys_one_girl,
    url=url,
    url2=url2
)
```

### whyareyougay
You are gay

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.whyareyougay,
    url=url,
    url2=url2
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

### sobel
Sobel filter on an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.sobel,
    url=url
)
```

### hog
Histogram of Oriented Gradients

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.hog,
    url=url
)
```

### blur
Blurs an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.blur,
    url=url
)
```

### rgb
Get rgb information of an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.rgb,
    url=url
)
```

### angel
Make an image angelic

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.angel,
    url=url
)
```

### satan
Make an image the devil

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.satan,
    url=url
)
```

### hitler
Make an image as bad as Hitler!

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.hitler,
    url=url
)
```

### obama
Make an image into Obama awarding himself

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.obama,
    url=url
)
```

### bad
Bad boy!

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.bad,
    url=url
)
```

### sith
Laughs in sithlord

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.sith,
    url=url
)
```

### sith
Laughs in sithlord

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.sith,
    url=url
)
```

### jail
Put an image in jail

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.jail,
    url=url
)
```

### gay
Make an image gay

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.gay,
    url=url
)
```

### trash
Make an image trash

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.trash,
    url=url
)
```

### deepfry
Deepfries an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.deepfry,
    url=url
)
```

### ascii
Ascii-fies an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.ascii,
    url=url
)
```

### charcoal
Turns an image into a charcoal sketch

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.charcoal,
    url=url
)
```

### poster
Posterizes an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.poster,
    url=url
)
```

### sepia
Makes the image in sepia tone

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.sepia,
    url=url
)
```

### polaroid
Makes a polaroid of an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.polaroid,
    url=url
)
```

### swirl
Swirls an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.swirl,
    url=url
)
```

### swirl
Swirls an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.swirl,
    url=url
)
```

### paint
Turns an image into an oil painting

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.paint,
    url=url
)
```

### night
Turns day into night in an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.night,
    url=url
)
```

### solar
Solarizes an image

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.solar,
    url=url
)
```

### thought_image
Makes an image and text into a thought

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.thought_image,
    url=url,
    text='Hmm yes thinking'
)
```

### tweet
Generates a fake tweet

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.tweet,
    url=url,
    username='Tweeter Expert',
    text='tweet'
)
```

### discord
Generates a a discord quote

**Example:**
```py
client.get_image(
    option=dagpipy.ImageOptions.tweet,
    url=url,
    username='discord user',
    text='lmao discord'
)
```

## <em>class</em> dagpipy.Games
The `option` parameter in the [Client.get_game](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#get_gameoption) function. 

### whos_that_pokemon
Returns the [Pokemon](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipypokemon) object when used

**Example:**
```py
client.get_game(
    option=dagpipy.Games.whos_that_pokemon,
)
```

### logo_guessing
Returns the [LogoGame](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipylogogame) object when used

**Example:**
```py
client.get_game(
    option=dagpipy.Games.logo_guessing,
)
```

### roast
Returns the [Roast](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipyroast) object when used

**Example:**
```py
client.get_game(
    option=dagpipy.Games.roast,
)
```


### yo_mama
Returns the [YoMama](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipyyomama) object when used

**Example:**
```py
client.get_game(
    option=dagpipy.Games.yo_mama,
)
```

### pickupline
Returns the [PickupLine](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipypickupline) object when used

**Example:**
```py
client.get_game(
    option=dagpipy.Games.pickupline,
)
```

### waifu
Returns the [Waifu](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipywaifu) object when used

**Example:**
```py
client.get_game(
    option=dagpipy.Games.waifu,
)
```


### joke
Returns the [Joke](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#class-dagpipyjoke) object when used

**Example:**
```py
client.get_game(
    option=dagpipy.Games.joke,
)
```

# Objects
The objects that can be returned in the [Client.get_game](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#get_gameoption) function. You can not access or instantiate these objects.

## <em>class</em> dagpipy.Pokemon
The object returned when using [Games.whos_that_pokemon](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#whos_that_pokemon) as the option param in [Client.get_game](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#get_gameoption)

**Supported Operations:**<br>
str(x): Returns the question image

### question
The question image

**Type:**<br>
str

### answer
The answer image

**Type:**<br>
str

### name
The Pokemon's name

**Type:**<br>
str

### types
The Pokemon's types 

**Type:**<br>
list

### abilities
The Pokemon's abilities

**Type:**<br>
list

### ascii
An ascii drawing of the Pokemon

**Type:**<br>
str

### id
The pokedex number of the Pokemon

**Type:**<br>
int

### link
An ascii drawing of the Pokemon

**Type:**<br>
str

### weight
The pokemon's weight

**Type:**<br>
float

### height
The pokemon's height

**Type:**<br>
float

### data
The raw dict data

**Type:**<br>
dict

**Example:**
```py
wtp = client.get_game(
    option=dagpipy.Games.whos_that_pokemon
)
print(wtp.name)
print(wtp.question)
print(wtp.answer)
print(wtp.types)
print(wtp.abilities)
print(wtp.ascii)
```

## <em>class</em> dagpipy.LogoGame
The object returned when using [Games.logogame](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#logo_guessing) as the option param in [Client.get_game](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#get_gameoption)

**Supported Operations:**<br>
str(x): The question image

### question
The question image

**Type:**<br>
str

### answer
The answer image

**Type:**<br>
str

### brand
The brand name

**Type:**<br>
str

### wiki
A wiki url of the brand

**Type:**<br>
str

### hint
A hint of the brand

**Type:**<br>
str

### clue
A clue of the brand

**Type:**<br>
str


### difficulty
The difficulty of the question. Could be easy or hard

**Type:**<br>
str

**Example:**<br>
```py
logogame = client.get_game(
    option=dagpipy.Games.logo_guessing
)

print(logogame.question)
print(logogame.answer)
print(logogame.brand)
print(logogame.difficulty)
print(logogame.wiki)
```

## <em>class</em> dagpipy.Roast
The object returned when using [Games.roast](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#roast) as the option param in [Client.get_game](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#get_gameoption)

**Supported Operations:**<br>
str(x): Returns the roast

### roast
Returns a random roast

**Type:**<br>
str

**Example:**<br>
```py
roast = client.get_game(
    option=dagpipy.Games.roast
)

print(roast.roast)
```

## <em>class</em> dagpipy.YoMama
The object returned when using [Games.yo_mama](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#yo_mama) as the option param in [Client.get_game](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#get_gameoption)

**Supported Operations:**<br>
str(x): Returns the yo mama joke

### description
Returns a random yo mama joke

**Type:**<br>
str

**Example:**<br>
```py
yomama = client.get_game(
    option=dagpipy.Games.yo_mama
)

print(yomama.description)
```

## <em>class</em> dagpipy.PickupLine
The object returned when using [Games.pickupline](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#pickupline) as the option param in [Client.get_game](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#get_gameoption). Warning: has a high chance to be NSFW

**Supported Operations:**<br>
str(x): Returns the pick up line

### category
Returns the category of the joke

**Type:**<br>
str

### joke
Returns the pick up line

**Type:**<br>
str

**Example:**<br>
```py
pickup = client.get_game(
    option=dagpipy.Games.pickupline
)

print(pickup.category)
print(pickup.joke)
```

## <em>class</em> dagpipy.Joke
The object returned when using [Games.joke](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#joke) as the option param in [Client.get_game](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#get_gameoption). Warning: has a chance to be NSFW

**Supported Operations:**<br>
str(x): Returns the joke

### id
Returns the id of the joke

**Type:**<br>
int

### joke
Returns the joke

**Type:**<br>
str


**Example:**<br>
```py
joke = client.get_game(
    option=dagpipy.Games.joke
)

print(joke.id)
print(joke.joke)
```
## <em>class</em> dagpipy.Waifu
The object returned when using [Games.waifu](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#waifu) as the option param in [Client.get_game](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md#get_gameoption).

**Supported Operations:**
str(x): Returns the name and description of the waifu.

### age
Returns the age of the waifu

### birthday_day
Returns the birthday day of the waifu

### birthday_month
Returns the birthday month of the waifu

### blood_type
Returns the blood type of the waifu

### bust
Returns the bust of the waifu

### description
Returns the description of the waifu

### display_picture
Returns the display picture of the waifu

### height
Returns the height of the waifu

### hip
Returns the hip of the waifu

### husbando
Returns the husbando of the waifu

### id
Returns the id of the waifu

### like rank
Returns the like rank of the waifu

### likes
Returns the likes of the waifu

### name
Returns the name of the waifu

### nsfw
Returns if the waifu is nsfw 

### origin
Returns the origin of the waifu

### original_name
Returns the original name of the waifu

### popularity_rank
Returns the popularity rank of the waifu

### romaji_name
Returns the romaji name of the waifu

### slug
Returns the slug of the waifu

### tags
Returns the tags of the waifu

### trash
Returns the trash of the waifu

### trash_rank
Returns the trash rank of the waifu

### url
Returns the url of the waifu

### waist
Returns the waist of the waifu

### weight
Returns the weight of the waifu

### creator
Returns the creator of the waifu

**Type:**<br>
[dagpipy.Creator]()

### series
Returns the series of the waifu

**Type:**<br>
[dagpipy.Series]()

### appearances
Returns a list of series the waifu was in

**Type:**<br>
List\[[dagpipy.Series]()]

**Example:**<br>
```py
waifu = client.get_game(
    option=dagpipy.Games.waifu
)

print(waifu.name)
print(waifu.description)
print(waifu.display_picture)
print(waifu.like_rank)
print(waifu.creator.name)
print(waifu.creator.id)
print(waifu.series.description)
```

## <em>class</em> dagpipy.Series

**Supported Operations:**<br>
str(x): Returns the name of the series

### airing_start
Returns the start of the airing of the series

**Type:**<br>
str

### airing_end
Returns the start of the airing of the series

**Type:**<br>
str

### description
Returns the description of the series

**Type:**<br>
str

### display_picture
Returns the display picture of the series

**Type:**<br>
str

### name
Returns the name of the series

**Type:**<br>
str

### original_name
Returns the original name of the series

**Type:**<br>
str

### release
Returns the release of the series

**Type:**<br>
str

### romaji_name
Returns the romaji name of the series

**Type:**<br>
str

### slug
Returns the slug of the series

**Type:**<br>
str

### studio
Returns the studio of the series

**Type:**<br>
str

## <em>class</em> dagpipy.Creator
The creator of a given waifu

**Supported Operations:**<br>
str(x): Returns the creator's name

### name 
The name of the creator

### id
The id of the creator

# Exceptions

## <em>exception</em> dagpipy.InvalidToken
Raised when the token you pass in is invalid (400)

## <em>exception</em> dagpipy.InvalidArgs
Raised when invalid arguments are passed in. (413, 422)

## <em>exception</em> dagpipy.ResponseError
Raised when there's an error with the API or you are being rate limited. (429, 500)

## <em>exception</em> dagpipy.InvalidImageURL
Raised when you pass in an invalid image url

### [Back to the top](https://github.com/niztg/dagpipy/blob/master/DOCUMENTATION.md)
