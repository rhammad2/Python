# text_analysis_reconstruction.py

def load_file(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    return text


def count_sentences(text):
    sentence_count = 0
    for ch in text:
        if ch == "." or ch == "!" or ch == "?":
            sentence_count += 1

    if sentence_count == 0:
        sentence_count = 1

    return sentence_count


def count_words(text):
    words = text.split()
    return len(words)


def count_syllables_in_word(word):
    word = word.lower()
    vowels = "aeiouy"
    syllables = 0
    previous_vowel = False

    for ch in word:
        is_vowel = ch in vowels
        if is_vowel and not previous_vowel:
            syllables += 1
        previous_vowel = is_vowel

    if word.endswith("e") and syllables > 1:
        syllables -= 1

    if syllables == 0:
        syllables = 1

    return syllables


def count_syllables(text):
    words = text.split()
    total = 0

    for w in words:
        w = w.strip(".,!?;:()[]{}\"'")
        if w != "":
            total += count_syllables_in_word(w)

    return total


def calculate_flesch(word_count, sentence_count, syllable_count):
    score = 206.835 - 1.015 * (word_count / sentence_count) - 84.6 * (syllable_count / word_count)
    return score


def main():
    input_file = input("Enter filename: ")

    text = load_file(input_file)

    sentence_count = count_sentences(text)
    word_count = count_words(text)
    syllable_count = count_syllables(text)

    flesch_score = calculate_flesch(word_count, sentence_count, syllable_count)

    print("\n--- TEXT ANALYSIS RESULTS ---")
    print("Sentences:", sentence_count)
    print("Words:", word_count)
    print("Syllables:", syllable_count)
    print("Flesch Score:", round(flesch_score, 2))


if __name__ == "__main__":
    main()
