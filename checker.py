import requests 
from pystyle import Colors, Write

banner = """
$$$$$$$\   $$$$$$\   $$$$$$\  
$$  ____| $$  __$$\ $$  __$$\ 
$$ |      $$ /  \__|$$ /  $$ |
$$$$$$$\  $$$$$$$\   $$$$$$  |
\_____$$\ $$  __$$\ $$  __$$< 
$$\   $$ |$$ /  $$ |$$ /  $$ |
\$$$$$$  | $$$$$$  |\$$$$$$  |
 \______/  \______/  \______/ \n"""
Write.Print(banner, Colors.rainbow)
Write.Input("[Press enter to start checking the tokens]:", Colors.blue_to_cyan, interval=0)

def check():
    with open("tokens.txt", "r") as file:
        tokens = [line.replace('\n', '') for line in file.readlines() if line != '\n']
        for token in tokens:
            k = token.split(".")
            m = "*"
            r1 = requests.get('https://discord.com/api/v9/users/@me', headers={"Authorization": token})
            if r1.status_code == 200:
                Write.Print(f"Valid token {k[0]}{m*20}\n", Colors.blue_to_purple, interval=0)
            else:
                Write.Print(f"Invalid token {k[0]}{m*26}\n", Colors.blue_to_red, interval=0)
                
check()
