from hashlib import sha256


def generate_sha256(phrase):
    return sha256(phrase.encode('utf-8')).hexdigest()
    
