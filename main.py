import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Tu bot {bot.user} esta en linea!')
    
@bot.command()
async def saludar(ctx,*, mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'hola':
        
        await ctx.send('Hola, ¿cómo estás?')
        
    elif mensaje == 'chao':
        
        await ctx.send('bye')
    
    elif mensaje == 'la buena':
        
        await ctx.send('la buena tambien')

        import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def en_linea():
    print(f'Tu bot {bot.user} esta en linea!')
    
@bot.command()
async def saludar(ctx,*, mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'hola':
        
        await ctx.send('Hola, ¿cómo estás?')
        
    elif mensaje == 'chao':
        
        await ctx.send('bye')
    
    elif mensaje == 'la buena':
        
        await ctx.send('la buena tambien')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

        
token = ''
bot.run(token)
