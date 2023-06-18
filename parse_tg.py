import json
filename = "veronika"
with_names = True

with open(filename + ".json", encoding="utf-8") as f:
    content = json.load(f)["messages"]

results = []
for item in content:
    if not "from" in item:
        continue
    is_sticker = "sticker_emoji" in item
    prefix = f"{item['from']}: " if with_names else ""
    plain_text = ""
    for c in item["text"]:
        if type(c) is str:
            plain_text += c
        else:
            plain_text += c["text"]
    if "\n" in plain_text:
        continue
    is_text = len(plain_text) > 0
    assert not is_sticker or not is_text
    if is_sticker:
        results += [prefix + item["sticker_emoji"]]
    elif is_text:
        results += [prefix + plain_text]

print(len(results), "messages")

with open(f"{filename}_messages_{['anon', 'names'][with_names]}.txt", "w", encoding="utf-8") as f:
    for line in results:
        f.write(line + "\n")
