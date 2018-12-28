import discord

TOKEN = 'NTIyMzY3MjI0Njc0MjU0ODcw.DvJ_lQ.78IklW3KfI2K-QdzXLiyEhKS_-4'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('_hello'):
        msg = 'Hello {0.author.mention}! \nI am buuble BOT \nType: \n"_update" for NerdsLab latest updates. \n"_meeting" for next meeting schedule.'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('_meeting'):
        msg = '{0.author.mention}, No meeting has been scheduled this week.'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('_update'):
        msg = '{0.author.mention}, We are not gonna start any project till March_2019.\nStay safe.'.format(message)
        await client.send_message(message.channel, msg)    
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
