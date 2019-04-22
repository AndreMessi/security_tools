import requests
re = requests.get('http://165.227.106.113/header.php', headers={'user-agent': 'Sup3rS3cr3tAg3nt', 'referer': 'awesomesauce.com'})
print(re.text)