song = """When an eel gravs your arm,
... And it causes great harm,
... That's - a moray!"""

print(song)



Question = [
    "We dont serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"]

Answer = [
    "An explidng sheep.",
    "No, i'm a frayed knot.",
    "'Pop!' goes the weasel."
]

for i in range(len(Question)):
    print(f"Q:{Question[i]}",
          f"\nA: {Answer[i]}")
    

print("My kitty cat likes %s,\nMy kitty cat likes %s,\nMy kitty cat fell on his %s \nAnd now thinks he's a %s" % ('roast beef', 'ham', 'head', 'clam'))

salution, name, product, verbed, room, animals, percent, spokesman, job_title, amount = 'Colleague', 'Ken', 'PC', 'exploded', 'room','animals','percent', 'spokesman', 'job_title', 'amount'

letter = f"""Dear {salution} {name},


Thank you for your letter. We are sorry that our {product} 
{verbed} in your {room}. Please note that it should never 
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling. 
We will send you another {product} that, in out tests, 
is {percent}% less likely to have {verbed}.
    
Thank you for your support.
Sincerely,
{spokesman}
{job_title}"""

letter = letter.format(product, verbed, room, room, animals, amount, product, percent, verbed,spokesman, job_title)
print(letter)

W_names = 'Duck {}, pumpkin {}, spitz {}'
print(W_names.format('ducker', 'pumpker', 'spitzer'))

W_names = f'Duck {'duckerr'}, pumpkin {'pumpkerr'}, spitz {'spitzerr'}'
print(W_names)