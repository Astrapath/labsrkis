list = ["http://www.example.com", "https://www.example.com"]
http_only = [a for a in list if a.startswith("http://")]
print(http_only)