import requests 
from pystyle import Colors,Write

banner = """
$$$$$$$\   $$$$$$\   $$$$$$\  
$$  ____| $$  __$$\ $$  __$$\ 
$$ |      $$ /  \__|$$ /  $$ |
$$$$$$$\  $$$$$$$\   $$$$$$  |
\_____$$\ $$  __$$\ $$  __$$< 
$$\   $$ |$$ /  $$ |$$ /  $$ |
\$$$$$$  | $$$$$$  |\$$$$$$  |
 \______/  \______/  \______/ \n"""
Write.Print(banner,Colors.rainbow)
Write.Input("[Press enter to start checking the tokens]:",Colors.blue_to_cyan)
with open("tokens.txt", "r") as file:
        tokens = [line.replace('\n', '') for line in file.readlines() if line != '\n']
        for token in tokens:
            m = "*"
            r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
            if r1.status_code <= 299:
                Write.Print(f"Valid token {token}\n",Colors.blue_to_purple)
            else:
                Write.Print(f"Invalid token {token}\n",Colors.blue_to_red)
