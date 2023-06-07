# there is some problem with the display of emojies, otherwise this code works fine 


row1 = ["😀","️🤣","️😅"]
row2 = ["😉","😄","️😃"]
row3 = ["️😎","😇","😂"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position = int(position)
row = position%10 -1
col = int(position/10) -1

map[row][col] = "X"

print(f"{map[row][col]}")

# 1F642
# 😀	Smiling face	U+1F600
# 😃	Smiling face with big eyes	U+1F603
# 😄	Smiling face with smiling eyes	U+1F604
# 😁	Beaming face with smiling eyes	U+1F601
# 😅	Smiling face with tears	U+1F605
# 😆	Grinning face	U+1F606
# 🤣	Rolling on the floor laughing	U+1F923
# 😂	Lauging with tears	U+1F602
# 🙃	Upside down face	U+1F643
# 😉	Winking face	U+1F609
# 😊	Smiling face with smiling eyes	U+1F60A
# 😇	Smiling face with halo	U+1F607
# 😎

print(f"{row1}\n{row2}\n{row3}")

