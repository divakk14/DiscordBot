import time
import discord
import random
# import sqlite3
# import json
# import codecsgit
import pymongo

TOKEN = 'OTU4NTA3MDU1MjU2MzM4NDgz.YkOVQg.0-qrQOpGOtZ83ruPrnELdZ64log'

client = discord.Client()
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    conn = pymongo.Mongoclient("mongodb+srv://divakkm14:kumar.1432@cluster0.7jc5xsn.mongodb.net/?retrywrites=true&w=majority")
    timestamp = str(message.guild.created_at)
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    servername = str(message.guild)

    conn.server_info()
    print("opened database successfully")
    mydb = conn['mydatabase']
    mycol = mydb['DIVAK_bot']
    mydict = {"user_name": username, "user_message": user_message, "time_stamp": timestamp, "channel_name": channel,
              "server_name": servername}
    x = mycol.insert_one(mydict)
    print(mydb.list_collection_names())

    if message.author == client.user:
        return
    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'see you later {username}!')
            return
        elif user_message.lower() == 'wassup':
            await message.channel.send(f'nothing much. you tell? {username}')
            return
        elif user_message.lower() == '!random':
            response = f'this is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return
    if user_message.lower() == '!anywhere':
        await message.channel.send('this can be used anywhere!')
        return

client.run(TOKEN)

# # conn = sqlite3.connect('discord.db')
# # conn = sqlite3.connect('database.db')
# # print("database opened successfully")
# # cursor = conn.cursor()
# # sql = ('''create table if not exists divak_discord(
# #    user_name char(50),
# #    user_message text,
# #    time_stamp text,
# #    channels_name char(50),
# #    servers_name char(50))''')
# # cursor.execute(sql)
# # sql2 = ('''select * from divak_discord ''')
# # cursor.execute(sql2)
# # records = cursor.fetchall()
# ## for record in records:
# ## print(message)
# # with open('data.txt' , 'a') as f:
# #    f.write(str(message.guild.created_at)+ " "+
# #            str()