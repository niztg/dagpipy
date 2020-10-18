import dagpipy
from secrets import TOKEN
from PIL import Image


client = dagpipy.Client(TOKEN)
url = dagpipy.ImageURL(
    "https://www.gettyimages.ca/gi-resources/images/500px/983794168.jpg"
)

bad = client.get_image(
    option=dagpipy.ImageOptions.bad,
    url=url,
)

bad_image = Image.open(bad)
bad_image.show()

tweet = client.get_image(
    option=dagpipy.ImageOptions.tweet,
    url=url,
    username="dagpipy",
    text="amazing"
)

tweet_image = Image.open(tweet)
tweet_image.show()

whyareyougay = client.get_image(
    option=dagpipy.ImageOptions.whyareyougay,
    url=url,
    url2=url
)

whyareyougay_image = Image.open(whyareyougay)
whyareyougay_image.show()

wtp = client.get_game(
    option=dagpipy.Games.whos_that_pokemon
)
print(wtp.name)
print(wtp.question)
print(wtp.answer)
print(wtp.types)
print(wtp.abilities)
print(wtp.ascii)

logogame = client.get_game(
    option=dagpipy.Games.logo_guessing
)

print(logogame.question)
print(logogame.answer)
print(logogame.brand)
print(logogame.difficulty)
print(logogame.wiki)

roast = client.get_game(
    option=dagpipy.Games.roast
)

print(roast.roast)

joke = client.get_game(
    option=dagpipy.Games.joke
)
print(joke.id)
print(joke.joke)

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
