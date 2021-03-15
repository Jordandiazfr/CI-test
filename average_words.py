def average_words():
    text = input("Please type a sentence so i can calculate the average: ")
    return sum(len(word) for word in text) / len(text)
