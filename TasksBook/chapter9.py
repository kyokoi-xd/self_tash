def good(names: list[str]) -> list:
    return names

print(good(['Harry', 'Ron', 'Hermione']))

def get_odds():
    for i in range(10):
        if i % 2 != 0:
            yield i
        continue


odds = get_odds()
for odd in odds:
    if odd == 5:
        print(odd)

def test(func):
    def new_func(*args):
        print('start')
        r = func(*args)
        print('end')
        return r
    return new_func

@test
def check():
    print('a')

print(check())


class OopsException(Exception):
    pass

def oops():
    x = input()
    try:
        raise OopsException(x)
    except OopsException as exc:
        print('Caught on oops')


print(oops())