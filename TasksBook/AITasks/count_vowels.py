
def count_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in s:
        if i.lower() in vowels:
            count += 1
    return count

print(count_vowels('HellO World'))


# Alternative example 2

def count_vowels(s):
    vowerls = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowerls)

print(count_vowels('HellO World'))


#Alternative example 3

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return len(list(filter(lambda char: char in vowels, s)))

print(count_vowels('HellO World'))