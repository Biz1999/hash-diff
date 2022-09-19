import re

from hashlib import md5
from sha256.sha256 import generate_sha256

def main():
    print("------------------------ HASH DIFF --------------------------")
    print("Comparando do arquivo hashes.txt...\n")

    sentences = []

    with open('hashes.txt') as file:
        sentences = file.readlines()
    
    for sentence in sentences:
        if sentence == "\n":
            sentences.remove(sentence)

    for sentence in sentences:
        substring_position = find_sub_string(sentence, "\"")

        phrase = sentence[1:substring_position].strip()

        hashes = sentence.replace(f"\"{phrase}\"", "").split(" - ")
        
        print(diff(phrase, "A primeira das instituições criadas por Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior de Administração de Negócios de São Paulo - ESAN/SP."))

        # actual_md5 = hashes[-1].strip()
        # actual_sha256 = hashes[-2].strip()

        # expected_md5 = generate_md5(phrase)
        # expected_sha256 = generate_sha256(phrase)

        # print(actual_md5, expected_md5)
        # print(actual_sha256, expected_sha256)
    

def find_sub_string(sentence, string):
	return sentence.find(string, sentence.find(string)+1)

def diff(actual, expected):
    return actual == expected

def generate_md5(phrase):
    solution = md5(phrase.encode('utf-8')).hexdigest()
    print(f"{phrase}, {solution}")
    return solution


if __name__ == "__main__":
    main()