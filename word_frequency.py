STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
    'has', 'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on',
    'that', 'the', 'to', 'were', 'will', 'with'
]

def print_word_freq(file):
    import string
    finalWords = {}
    finalOutput = []
    finalLines = {}
    with open(file) as file:
        words = file.read().replace("—", " ").translate(str.maketrans('', '', string.punctuation)).lower().split()
        for word in words:
            if word in STOP_WORDS:
                word = None
            if word in finalWords:
                finalWords[f"{word}"] += 1
            if word not in finalWords:
                finalWords[f"{word}"] = 1
        finalWords = sorted(finalWords.items(), key=lambda x: x[1], reverse=True)
        for finalWord, finalNumber in finalWords:
            finalStar = "*" * int(finalNumber)
            finalOutput.append(f"""{finalWord} | {finalNumber} {finalStar}""")
        maximum = len(max(finalOutput, key=len))
        for finalItem in finalOutput:
            finalLength = len(finalItem)
            finalLines[f"{finalItem}"] = finalLength
        finalLines = finalLines.items()
        for output, outputIndent in finalLines:
            output = str(" " * ((maximum - outputIndent) + output.count('*') + len(str(output.count('*'))))) + output
            print(output)


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
