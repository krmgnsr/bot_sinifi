import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba ben {bot.user}!  Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, count_pass = 7):
    karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    sifre = ""
    for i in range(count_pass):
        sifre += random.choice(karakter)
    await ctx.send(sifre)

@bot.command()
async def numbering(ctx, count_num = 0):
    numbers = "123456789"
    number = random.choice(numbers)
    if count_num < 1:
        await ctx.send("It is not a number you can enter")
        
    elif count_num == number:
        await ctx.send("Amazing")

    else:
        await ctx.send("İt was not it:(")

@bot.command()
async def emojing(ctx):
    em_list = (":sweat_smile:", ":grin:", ":cry:", ":sob:", ":rage:", ":face_with_symbols_over_mouth:", ":cold_face:")
    emoji = random.choice(em_list)
    await ctx.send(emoji)

@bot.command()
async def helping(ctx):
    await ctx.send("**HERKESİN KULLANACAĞI KOMUTLAR**\nhello = selam verir \nheh = verdiğiniz sayı kadar he yazar \npassword = verdiğiniz sayı kadar karaktere sahip şifre verir \nnumbering = rastgele sayı seçer verdiğiniz sayı ona eşitse tebrik eder \nemojing = rastgele emoji seçer \ntoss_up = yazı tura atar \ncolor_pick = girdiğiniz sayı kadar rastgele renk seçer \nhappybd = etiketlediğiniz kişinin doğum gününü kutlar \nmultip = verdiğiniz iki sayıyı çarpar \ncounting = verdiğin iki sayı arasından birini seçer \n------------------------------------------------------- \n**ÖZEL KOMUTLAR** \nkick = istenilen kişiyi atar")

    
@bot.command()
async def toss_up(ctx):
    tosses = ("yazı", "tura", "DİK")
    toss = random.choices(tosses, weights=(49, 49, 2))
    await ctx.send(toss[0])

@bot.command()
async def color_pick(ctx, count_clr = 1):
    colors = (" kırmızı", " siyah", " yeşil", " gri", " mavi", " sarı", " beyaz", " turuncu")
    
    clr = ""
    for i in range(count_clr):
        clr += random.choice(colors)

    await ctx.send(clr)

@bot.command()
async def happybd(ctx, person = "a"):
    if len(person) > 1:
        await ctx.send(f"HAPPY BIRTHDAY {person}! btw he doesn't love you much :/")

    else:
        await ctx.send("Bu dalga geçilecek bir şey mi sence???")

@bot.command()
async def multip(ctx, num1 = 0, num2 = 0):
    
    if num1 > 1 and num2 > 1:
        result = num1 * num2
        await ctx.send(result)

    elif num1 < 1 or num2 < 1:
        await ctx.send("Bunu sen de yaparsın")

@bot.command()
async def kick(ctx, user: discord.Member):
    if ctx.author.guild_permissions.kick_members:
        await user.kick()
        await ctx.send(f"{user.name} sunucudan atıldı!")
    else:
        await ctx.send("Bu işlemi yapmal için izniniz yok")


@bot.event
async def on_message(message):
    if not message.author.bot: 
        bannedwrd = ["Amk", "siktir", "sik", "yarrak", "am"]

        for word in bannedwrd:
            if word in message.content.lower(): 
                await message.delete()
                await message.channel.send(f"Küfür etmeyin {message.author.mention}")


                privetchannel1 = await message.author.create_dm()
                await privetchannel1.send("Lütfen yapmayın yoksa atılırsınız")

    await bot.process_commands(message)

@bot.command()
async def counting(ctx, first = 0, end = 0):
    mylist = list(range(first, end + 1))
    picked = random.choice(mylist)
    await ctx.send(picked)
    await ctx.send(f"Umarım hata yapmamışımdır işte listen {mylist}")

@bot.command()
async def turnoff(ctx):
    if bot.author.guild_permissions.kick_members:
        await bot.user.kick()
    else:
        await ctx.send("Yetkiniz yok")

@bot.command()
async def add_role(ctx, role_name: str):
    
    if ctx.author.guild_permissions.kick_members:
        role = discord.utils.get(ctx.guild.roles, name=role_name)

        if role:
            try:
                await ctx.author.add_roles(role)
                await ctx.send(f'{ctx.author.mention}, {role.name} rolü başarıyla eklendi.')
            except Exception as e:
                await ctx.send(f'Hata oluştu: {e}')
        else:
            await ctx.send('Belirtilen rol bulunamadı.')
    else:
        await ctx.send("Yetkiniz yok!")






    


bot.run("your token")
