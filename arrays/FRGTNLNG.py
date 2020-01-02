for _ in range(int(input())):
    num_forgotten_words, num_modern_phrases = map(int, input().split())
    forgotten_words_list = input().split()
    modern_words = {}
    for i in range(num_modern_phrases):
        modern_words_list = input().split()[1:] # the first element is length of list
        for word in modern_words_list:
            modern_words[word] = True
    for word in forgotten_words_list:
        if word in modern_words:
            print('YES', end = ' ')
        else:
            print('NO', end = ' ')
    print('')
