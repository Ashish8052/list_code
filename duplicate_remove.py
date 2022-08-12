
duplicate = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
final_list=[]
for num in duplicate:
    if num not in final_list:
        final_list.append(num)
print(final_list)   