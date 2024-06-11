import discord
import random
import asyncio
import os
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.guild_messages = True
intents.messages = True
intents.guilds = True
intents.members = True  # Necessario se vuoi usare membri del server

# Prefisso dei comandi
bot = commands.Bot(command_prefix='/', intents=intents)

# Lista di messaggi casuali
random_messages = [
    #"Sei un membro fantastico del server!",
    #"Continua così, stai facendo un ottimo lavoro!",
    #"Grazie per essere parte della nostra comunità!",
    #"La tua partecipazione è molto apprezzata!",
    #"Sei una parte importante del nostro team!",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vehicula urna at sapien porttitor, nec tempor velit posuere. Donec a fermentum ipsum. Integer ut ligula leo. Suspendisse potenti.\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vehicula urna at sapien porttitor, nec tempor velit posuere. Donec a fermentum ipsum. Integer ut ligula leo. Suspendisse potenti.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vehicula urna at sapien porttitor, nec tempor velit posuere. Donec a fermentum ipsum. Integer ut ligula leo. Suspendisse potenti."
]

@bot.command(name='send_random_messages')
# Solo gli amministratori possono usare questo comando
#@commands.has_permissions(administrator=True)
async def send_random_messages(ctx, member: discord.Member):
    channel_name = ctx.message.channel

    # Trova il canale specifico
    channel = ctx.message.channel
    # discord.utils.get(ctx.guild.text_channels, name=channel_name)

    if channel is None:
        await ctx.send(f'Canale "{channel_name}" non trovato.')
        return

    # Ottieni tutti i membri non bot
    members = [member for member in ctx.guild.members if not member.bot]

    # Se il numero di messaggi richiesti è maggiore del numero di membri, correggilo
    num_messages = min(1, len(members))

    # Seleziona un sottoinsieme casuale dei membri
    selected_members = random.sample(members, num_messages)

    # Simula il bot che sta scrivendo
    async with channel.typing():
        # Imposta la durata della simulazione di scrittura (in secondi)
        await asyncio.sleep(5)  # ad esempio, 3 secondi

    if (member is not None):
        # Scegli un messaggio casuale dalla lista
        message = random.choice(random_messages)
        # Invia il messaggio nel canale specifico menzionando il membro
        await channel.send(f'{member.mention} {message}')
        print(f'Messaggio inviato a {member.name} nel canale {channel.name}')
    else:
        # Itera attraverso i membri selezionati e invia un messaggio casuale
        for member in selected_members:
            # Scegli un messaggio casuale dalla lista
            message = random.choice(random_messages)
            # Invia il messaggio nel canale specifico menzionando il membro
            await channel.send(f'{member.mention} {message}')
            print(f'Messaggio inviato a {member.name} nel canale {channel.name}')

# Avvia il bot
bot.run(TOKEN)
