import dagpipy
from secrets import token

client = dagpipy.Client(token)

url = dagpipy.ImageURL("https://cdn.discordapp.com/avatars/731228973001867304/0e587564754286e061716f57713449b9.png?size=1024")
whyareyougay = client.get_image(
    dagpipy.ImageOptions.angel,
    url=url
)
print(whyareyougay)