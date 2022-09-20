from hashlib import md5


def generate_md5(phrase):
    return md5(phrase.encode('utf-8')).hexdigest()
