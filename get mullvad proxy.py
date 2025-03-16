import requests

response = requests.get("https://api.mullvad.net/www/relays/all/")
data = response.json()


proxy_list = [
    f"socks5://{entry['socks_name']}:{entry['socks_port']}"
    for entry in data if 'socks_name' in entry and 'socks_port' in entry
]

# Sauvegarder dans un fichier texte
file_path = "mullvad_socks5_proxies.txt"
with open(file_path, "w") as file:
    file.write("\n".join(proxy_list))