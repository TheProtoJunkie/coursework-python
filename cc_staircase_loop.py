stars = ""
"""
0 i goes to 1 j, makes 1 star...
1 in j becomes 1 i then changes to 2 in j, 
adds 2 stars to 1 star, then 3 stars then 4 to existing list
"""
for i in range(0, 5, 1):
    for j in range(0, i, 1):
        stars += "*"
    print(stars)
