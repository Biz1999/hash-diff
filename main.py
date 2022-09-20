from md5.md5 import generate_md5
from sha256.sha256 import generate_sha256
from tabulate import tabulate


def main():
    print("------------------------ HASH DIFF --------------------------")
    print("Comparando arquivo hashes.txt...\n")

    md5_diffs = [["Frase", "MD5 - atual", "MD5 - gerado", "Comparação"]]
    sha256_diffs = [["Frase", "SHA256 - atual", "SHA256 - gerado", "Comparação"]]

    with open('hashes.txt', encoding="utf-8", errors="ignore") as file:
        sentences = file.readlines()

    for sentence in sentences:
        substring_position = find_sub_string(sentence, "\"")

        phrase = sentence[1:substring_position].strip()

        hashes = sentence.replace(f"\"{phrase}\"", "").split(" - ")

        actual_md5 = hashes[-1].strip()
        actual_sha256 = hashes[-2].strip()

        expected_md5 = generate_md5(phrase)
        expected_sha256 = generate_sha256(phrase)

        md5_diffs.append([phrase[:20]+"...", actual_md5, expected_md5, diff(actual_md5, expected_md5)])
        sha256_diffs.append([phrase[:20]+"...", actual_sha256, expected_sha256, diff(actual_sha256, expected_sha256)])

    md5_table = tabulate(md5_diffs, headers="firstrow", tablefmt="grid")
    sha256_table = tabulate(sha256_diffs, headers="firstrow", tablefmt="grid")

    with open("tables.txt", "w", encoding="utf-8") as tables:
        tables.write(f"MD5 - COMPARAÇÕES\n{md5_table}\n\n")
        tables.write(f"SHA256 - COMPARAÇÕES\n{sha256_table}")

    print("Tabelas salvas!")


def find_sub_string(sentence, string):
    return sentence.find(string, sentence.find(string) + 1)


def diff(actual, expected):
    return actual == expected


if __name__ == "__main__":
    main()
