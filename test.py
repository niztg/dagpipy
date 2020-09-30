import dagpipy

client = dagpipy.Client("aaaa")

url = dagpipy.ImageURL(
    "https://cdn.discordapp.com/avatars/731228973001867304/0e587564754286e061716f57713449b9.png?size=1024")
whyareyougay = client.get_game(
    dagpipy.Games.whos_that_pokemon,
)
print(whyareyougay)
