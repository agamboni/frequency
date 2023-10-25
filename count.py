import sys

def word_frequency_count(file_name, topN):
    try:
        with open(file_name, 'r') as file:
             text= file.read()
        list_of_words= text.split()

        count_words= {}
        for word in list_of_words:
            if word in count_words:
                count_words[word]+=1
            else:
                count_words[word]=1
        sorted_words= sorted(count_words.items(), key=lambda x:x[1], reverse= True)

        for i in range(topN):
            print("key: ", sorted_words[i][0] ,"value: ", sorted_words[i][1])  

    except Exception as e:
        print(e)

N= int(sys.argv[1])
file= 'file.txt'
word_frequency_count(file ,N)