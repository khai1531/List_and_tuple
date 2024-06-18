def english_to_vietnamese_translator():

    english_to_vietnamese_dict = {
        "hello": "xin chào",
        "goodbye": "tạm biệt",
        "thank you": "cảm ơn",
        "please": "vui lòng",
        "computer": "máy tính",
        "book": "sách",
        "pen": "bút",
        "apple": "táo",
        "orange": "cam",
        "banana": "chuối"
    }


    english_word = input("Enter an English word to translate: ").lower()
    if english_word in english_to_vietnamese_dict:

        vietnamese_translation = english_to_vietnamese_dict[english_word]
        print(f"{english_word} in Vietnamese is: {vietnamese_translation}")
    else:
        print(f"Sorry, '{english_word}' is not found in the dictionary.")

english_to_vietnamese_translator()
