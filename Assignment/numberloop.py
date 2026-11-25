# Loop throught the numbers, if higher or equal to 50,
# display the number with pass beside it,
# else display the number with fail beside it

scores = [45, 78, 62, 31, 88, 73, 11]
dis_number = [0]


for s in scores:
    if s >= 50:
        print(f"{s} PASS")
    else:
        print(f"{s} FAIL")
   