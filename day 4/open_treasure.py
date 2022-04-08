row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

lists = int(position[0])
lists_indices = int(position[1])

marking_treasure = map[lists-1]
marking_treasure[lists_indices-1]="x"
# print(f"{row1}{row2}{row3}")





print(f"{row1}\n{row2}\n{row3}")