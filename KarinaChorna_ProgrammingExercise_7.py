# Karina Chorna
# Programming Exercise 7
# The purpose of this code is to split the user's paragraph into individual sentences and display each one as well
# as the total count of sentences.

import re

# split the user's paragraph into separate sentences
def split_into_sentences(paragraph):
    sentence_endings = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s')
    sentences = sentence_endings.split(paragraph.strip())
    return [s.strip() for s in sentences if s.strip()]

# display each sentence and the total count
def display_sentences(sentences):
    print("\nIndividual Sentences:\n")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")
    print(f"\nTotal number of sentences: {len(sentences)}")

# prompt user to enter their paragraph
def main():
    paragraph = input("Enter a paragraph:\n")
    sentences = split_into_sentences(paragraph)
    display_sentences(sentences)

if __name__ == "__main__":
    main()
