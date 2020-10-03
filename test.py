import dagpipy
from secrets import TOKEN

client = dagpipy.Client(TOKEN)

url = dagpipy.ImageURL("https://t8x8a5p2.stackpathcdn.com/wp-content/uploads/2018/05/Birthday-Cake-Recipe-Image-720x720.jpg")
whyareyougay = client.get_game(
    dagpipy.Games.whos_that_pokemon,
)
print(whyareyougay)