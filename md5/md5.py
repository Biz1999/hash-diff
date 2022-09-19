from hashlib import md5


def generate_md5(phrase):
    solution = md5(phrase.encode('utf-8')).hexdigest()
    print(f"{phrase}, {solution}")
    return solution
