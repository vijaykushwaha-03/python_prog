s = "seilent"
l = "listeen"

if len(s) != len(l):
    print("Not Anagram")
else:
    for ch in s:
        if ch not in l:
            print("Not Anagram")
            break
    else:
        print("Anagram")