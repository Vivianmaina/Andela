"""
Word Count lab
"""
def words(words):
    new_words_list = words.split()  #split string into individual words
    total_words = len(words)
    total_occurences = {}
    unique_word = set(new_words_list)  #gets the unique words only
    if total_words == 1:      #if only one word,then it's standard ocurrence is just 1
    	total_occurences[new_words_list[0]] = 1
    else:
        for word in unique_word:
            count = 0
            for item in new_words_list:
        	    if word == item:
        		    count += 1
        		    if word.isdigit() == True:   #checks if there's an integer in the string and converts to integer type
        			    word = int(word)
            total_occurences[word] = count
        return total_occurences       
                