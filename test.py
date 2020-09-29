import dagpipy

TOKEN = "wBNEsM746ixNkDdmgWYDTqQYZN2GDTzPgzlWUO58rl6rtO4JDAVgJ72zfFcfbpei"

client = dagpipy.Client(TOKEN)

url = dagpipy.ImageURL("https://cdn.discordapp.com/avatars/731228973001867304/0e587564754286e061716f57713449b9.png?size=1024")
whyareyougay = client.get_game(
    dagpipy.Games.logo_guessing,
)
print(whyareyougay.difficulty)