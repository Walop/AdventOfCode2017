with open("input") as file:
    input_txt = file.read()
    phrases = input_txt.split("\n")
    valid = 0
    for phrase in phrases:
        phrase_valid = True
        word_list = list()
        for word in phrase.split(" "):
            sorted_word = sorted(list(word))
            for sw in word_list:
                if sorted_word == sw:
                    phrase_valid = False
                    break
                if phrase_valid == False:
                    break
            if phrase_valid:
                word_list.append(sorted_word)
            else:
                break
        if phrase_valid:
            valid += 1
        
    print(valid)
