def permute(s, ans, result):
    if len(s) == 0:          # base case
        result.append(ans)
        return

    for i in range(len(s)):
        ch = s[i]                    # pick one character
        rest = s[:i] + s[i+1:]       # remaining characters
        permute(rest, ans + ch, result)


result = []
permute("abc", "", result)

print(result)
