def count_words(sentence):
    # Remove leading and trailing whitespaces
    sentence = sentence.strip()
    
    # Split the sentence by whitespace
    words = sentence.split()
    
    # Return the number of words
    return len(words)

def main():
    # Prompt user for input
    input_sentence = input("Enter a sentence or paragraph: ")
    
    # Call count_words function to get the word count
    word_count = count_words(input_sentence)
    
    # Display the result
    print("Number of words:", word_count)

if __name__ == "__main__":
    main()
