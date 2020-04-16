import discord
# import sys
# import os

import asyncio

bot_channel_id = discord.Object(id='554262668622561283')
id_list = ["557439871447203857","557439769106448406","556811421724442649"]

sent_new_message = False
answer_scores = {
    "1": 0,
    "2": 0,
    "3": 0,
   
}
answer_scores_last = {
    "1": 0,
    "2": 0,
    "3": 0,

}


nomarkscore = 100
markscore = 50

bot = discord.Client()
selfbot = discord.Client()

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Loco Trivia",type=1))
   
    await bot.send_message(bot_channel_id, "**READY```LOCO TRIVIA```** ")
   

   

@bot.event
async def on_message(message):
    global sent_new_message
    global answer
    
    global answer_scores
    global answer_scores_last

    if message.server == None:
        return
    if message.content.lower() == "-l":
       if "554283064822333441" in [role.id for role in message.author.roles]:
           sent_new_message =False
           answer_scores = {
                "1": 0,
                "2": 0,
                "3": 0,
           }
           
           answer = " " 
           

@selfbot.event
async def on_ready():
    
    print("Connected to discord.")
    
@selfbot.event
async def on_message(message):
    global answer_scores
    
    global answer
    

    if message.server == None:
        return

   
    if message.channel.id in oot_channel_id_list:
        content = message.content.lower().replace(' ', '').replace("'", "")
        if content == "1":
            answer_scores["1"] += nomarkscore
        elif content == "2":
            answer_scores["2"] += nomarkscore
        elif content == "3":
            answer_scores["3"] += nomarkscore
        
        
        
        
        elif content in ["not1", "n1"]:
            answer_scores["1"] -= nomarkscore
        elif content in ["not2", "n2"]:
            answer_scores["2"] -= nomarkscore
        elif content in ["not3", "n3"]:
            answer_scores["3"] -= nomarkscore
        
        elif content.startswith("not1?") or content.startswith("n1?"):
            answer_scores["1"] -= markscore
        elif content.startswith("not2?") or content.startswith("n2?"):
            answer_scores["2"] -= markscore
        elif content.startswith("not3?") or content.startswith("n3?"):
            answer_scores["3"] -= markscore
        
            
       
       
        else:
            return

        allanswers = answer_scores.values()
        highest = max(allanswers)
        lowest = min(allanswers)
        answer = list(allanswers).index(highest)+1
        

async def send_embed(client, embed):
    return await client.send_message(bot_channel_id, embed=embed)

async def edit_embed(client, old_embed, new_embed):
    return await client.edit_message(old_embed, embed=new_embed)

async def discord_send():
    global sent_new_message
    global answer
    
    global answer_scores_last

    await bot.wait_until_ready()
    await asyncio.sleep(0)

    answer_scores_last = {
        "1": 0,
        "2": 0,
        "3": 0,
        
    }

    answer_message = []
    
    while not bot.is_closed:
	    
        if answer_scores != answer_scores_last:
            
            if answer :
                
                
                
                one_check = ""
                two_check = ""
                three_check = ""
                
                
                    
                
                    
                
                    
                if answer == 1:
                    one_check = " :one:"
                if answer == 2:
                    two_check = " :two:"
                if answer == 3:
                    three_check = " :three:"
                
                if not sent_new_message:
                    
                    embed=discord.Embed(title="LOCO", description="", color=0xadd8e6)
                    embed.add_field(name="A", value=f"{answer_scores['1']}{one_check}", inline=False)
                    embed.add_field(name="B", value=f"{answer_scores['2']}{two_check}", inline=False)
                    embed.add_field(name="C", value=f"{answer_scores['3']}{three_check}", inline=False)
                    

                    embed.set_footer(text=f"", icon_url="")
                   
                    answer_message = await send_embed(bot, embed)
                    sent_new_message = True
                else:
                    
                    embed=discord.Embed(title="LOCO", description="", color=0xadd8e6)
                    embed.add_field(name="A", value=f"{answer_scores['1']}{one_check}", inline=False)
                    embed.add_field(name="B", value=f"{answer_scores['2']}{two_check}", inline=False)
                    embed.add_field(name="C", value=f"{answer_scores['3']}{three_check}", inline=False)			
                    embed.set_footer(text=f"", icon_url="")
                    x = await edit_embed(bot, answer_message, embed)
                    await bot.add_reaction(x,emoji="?")
                    await bot.add_reaction(x,emoji="?")
                    
		    
                answer_scores_last = answer_scores.copy()
                await asyncio.sleep(0)
                continue

        answer_scores_last = answer_scores.copy()
        await asyncio.sleep(0)

loop = asyncio.get_event_loop()
loop.create_task(bot.start("ENTER YOURS"))
loop.create_task(selfbot.start("ENTER YOURS", bot=False))

loop.create_task(discord_send())
loop.run_forever()
