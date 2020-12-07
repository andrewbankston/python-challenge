import re

def paragraphAnalyzer(file):

    word_length = []
    sentence_length = []

    with open(file, 'r') as text:
        lines = text.read()
       
        sentences = re.split('.\n\n|\S.[.] (?=[A-Z])|[.] (?=[A[a-z]-Z[a-z]])', lines)
        sentence_count = len(sentences)
        words = re.split(' |\n\n', lines)
        word_count = len(words)
        
    for word in words:
        word_length.append(len(word))
        avg_word_length = round(sum(word_length)/len(word_length), 2)
        
    for sentence in sentences:
        sentence_length.append(len(re.split(' |-', sentence)))
        avg_sentence_length = sum(sentence_length)/len(sentence_length)

    print("Paragraph Analysis")
    print("---------------")
    print(f"Approximate Word Count: {word_count}")
    print(f"Approximate Sentence Count: {sentence_count}")
    print(f"Average Letter Count: {avg_word_length}")
    print(f"Average Sentence Length: {avg_sentence_length}")   
    
        
paragraphAnalyzer('Resources/paragraph_3.txt')