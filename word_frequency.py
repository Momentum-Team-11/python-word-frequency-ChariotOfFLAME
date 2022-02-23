STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
    'has', 'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on',
    'that', 'the', 'to', 'were', 'will', 'with'
]

def print_word_freq(file):
    import string
    """Read in `file` and print out the frequency of words in that file."""
    finalWords = {}
    with open(file) as file:
        original = file.read()
        words = original.translate(str.maketrans('', '', string.punctuation))
        words = words.lower().split()
        punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        for word in words:
            if word in STOP_WORDS:
                word = ''
            if word in finalWords:
                finalWords[f"{word}"] += 1
            if word not in finalWords:
                finalWords[f"{word}"] = 1
    print(finalWords)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
