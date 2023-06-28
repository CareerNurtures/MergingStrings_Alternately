def mergeAlternately(word1, word2):
    merged_string =""
    lenght = [len(word1),len(word2)]
    min_length = min(lenght)

    for i in range(min_length):
        merged_string += word1[i]+word2[i]

    if len(word1)>len(word2):
        max_word = word1
    else:
        max_word = word2

    for i in range(min_length,len(max_word)):
        merged_string += max_word[i]

    return merged_string

input_word1 = input("Enter word 1: ")
input_word2 = input("Enter word 2: ")

merged_string = mergeAlternately(input_word1,input_word2)

print(f"Output : {merged_string}")
