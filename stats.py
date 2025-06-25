def string_count(argu):
    file_path = argu;
    with open(file_path) as f:
        file_contents = f.read();
        word_count = file_contents.split();
        count = len(word_count);
        print(f"Found {count} total words")


def char_count(argu):
    char_num = {};
    file_path = argu;
    with open(file_path) as f:
        file_contents = f.read();
        count = file_contents.lower();
        for chars in count:
            if chars in char_num:
                char_num[chars] += 1; 
            else:
                char_num[chars] = 1;
        return char_num



def sorted_list(argu):
    char_list = char_count(argu);
    cleaned_list = {}
    
    
    for keys, value in sorted(char_list.items(), key=lambda item: item[1], reverse=True):
        
        if keys.isalpha():
            cleaned_list.update(char_list);
            
    
            print(f"{keys}: {value}");


