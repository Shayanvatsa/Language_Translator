
get_ipython().system('pip install googletrans==4.0.0-rc1')

from googletrans import Translator

def translate_text(text, input_language, output_language):
    translator = Translator()
    translation = translator.translate(text, input=input_language, output=output_language)
    return translation.text

def main():
    print("Language Translator")
    print("Languages Supported:-")
    print("English: en, Spanish: es, French: fr, German: de, Hindi: hi, Chinese: zh-CN")
    
    input_language = input("Enter the source language code (e.g., en for English):- ")
    output_language = input("Enter the outputination language code (e.g., fr for French):- ")
    text_to_translate = input("Enter the text to translate:- ")

    translated_text = translate_text(text_to_translate, input_language, output_language)
    print("Translated Text:-")
    print(translated_text)

if __name__ == "__main__":
    main()
