import pyshorteners, pyperclip

url = input("Paste your long URL: ")
short = pyshorteners.Shortener().tinyurl.short(url)
pyperclip.copy(short)

print(f"✅ Short URL copied to clipboard:\n{short}")
