#QUESTAO 02

urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

dominios = [url[4:-4] for url in urls]

print("URLs:", urls)
print("Domínios:", dominios)

URLs: ['www.google.com', 'www.gmail.com', 'www.github.com', 'www.reddit.com', 'www.yahoo.com']
Domínios: ['google', 'gmail', 'github', 'reddit', 'yahoo']
