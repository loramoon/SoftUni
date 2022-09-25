import re
valid_urls = []
pattern = r'((w{3})\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
sentence = input()
while sentence:
    matches = re.search(pattern, sentence)
    if matches:
        valid_urls.append(matches.group(0))
    sentence = input()

for valid_url in valid_urls:
    print(valid_url)
