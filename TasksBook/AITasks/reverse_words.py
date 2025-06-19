
def reverse_words(sentence):
    answer = sentence.split(' ')
    answer = ' '.join(answer[::-1])
    return answer

print(reverse_words("Hello world from Python"))

