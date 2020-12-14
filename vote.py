import discord
from selenium import webdriver
from time import sleep

draft = "https://www.strawpoll.me/#?savedPoll=%7B%22title%22:%22Vote%22,%22dupcheck%22:%221%22,%22multi%22:true,%22captcha%22:false,%22options%22:%5B%22Heave-Ho%22,%22Duck%2520Game%22,%22Stellaris%22,%22Minecraft%22,%22Postal%25202%22,%22Civ%25205%22,%22Minion%2520Masters%22,%22Transform%2520Mice%22,%22Prison%2520Architect%22,%22The%2520Escapist%22,%22G-Mod%22,%22Half%2520Life%2520-%2520Sven%2520Coop%22,%22Rust%22,%22Counter%2520Strike%22,%22Space%2520Engineers%22,%22Terraria%22,%22Factorio%22,%22Borderlands%25202%252F3%22,%22GTA%2520V%22,%22Speed%2520Runners%22,%22Don't%2520Starve%22,%22Bro-Force%22,%22Stick%2520fight%22,%22Bloons%2520TD%22,%22Hearts%2520of%2520Iron%25204%22,%22Killing%2520Floor%25202%22,%22Rainbow%2520Six%2520Siege%22,%22Insurgency%22,%22Pay%2520Day%25202%22%5D%7D"
async def vote(message):
    try:
        driver = webdriver.Chrome('C:/bin/chromedriver.exe')
        driver.get(draft)
        button = driver.find_element_by_id("create-button")
        button.click()
        sleep(5)
        cur_url = (driver.current_url)
        e = discord.Embed(title="VOTE", description="Vote For Your Games using the above link, Or Check the results", url=cur_url)
        await message.channel.send(embed=e)
        sleep(90)
        driver.quit()
    except:
        print("Webdrive Failed")
