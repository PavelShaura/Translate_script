from googletrans import Translator
from colorama import init, Fore

init(autoreset=True)
print(Fore.LIGHTBLACK_EX + 'version 1.0')
print(Fore.LIGHTBLACK_EX + '[!] This program translate text for english, french and spanish. You Welcome!')
print(Fore.LIGHTBLACK_EX + '[!] Powered by Pavel Shaura')
print(Fore.LIGHTBLACK_EX + '[!] https://github.com/PavelShaura')


def translate_fo_me():
    translator = Translator()
    print(Fore.YELLOW + '*' * 30)
    lang = input('[?] Напишите с какого языка переводим?: \n Примеры: \nen - английский \nes - испанский \nfr - '
                 'французский \n')
    if lang == 'en':
        message = input(f'[!] Вставте текст для перевода(выбран английский): \n')
        print(Fore.YELLOW + '************Перевод***********')
        translation = translator.translate(text=message, src=lang, dest='ru')
        return print(Fore.LIGHTBLUE_EX + translation.text)
    elif lang == 'es':
        message = input(f'[!] Вставте текст для перевода(выбран испанский): \n')
        print(Fore.YELLOW + '************Перевод***********')
        translation = translator.translate(text=message, src=lang, dest='ru')
        return print(Fore.LIGHTBLUE_EX + translation.text)
    elif lang == 'fr':
        message = input(f'[!] Вставте текст для перевода(выбран французкийй): \n')
        print(Fore.YELLOW + '************Перевод***********')
        translation = translator.translate(text=message, src=lang, dest='ru')
        return print(Fore.LIGHTBLUE_EX + translation.text)
    else:
        print(Fore.RED + '[!]Не правильно выбран язык')


def main():
    while True:
        print()
        translate_fo_me()


if __name__ == '__main__':
    main()
