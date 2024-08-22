emojis = {
    ":)": "😀", #ctrl+cmd+space
    ":(": "😟"
}

message = input("> ")
words = message.split(" ")
output = ""
for word in words:
    output += emojis.get(word, word)+ " "

print(output)
