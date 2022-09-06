def check(text):
    if not (text.isalpha() or text.isdigit() or text.isspace()):
        special_characters = "_"
        
        if any(c in special_characters for c in text):
            print("true")
        else:
            print("flase")        
    else:
        print("true")
