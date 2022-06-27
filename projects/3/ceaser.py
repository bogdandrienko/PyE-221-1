# -*- coding: utf-8 -*-

# @Date    : 2018-10-12
# @Author  : Peng Shiyu

class CaesarCipher(object):
    """
    Цезарь шифрование и дешифрование
    """

    def __crypt(self, char, key):
        """
                 Зашифровать одну букву, смещение
                 @param char: {str} один символ
                 @param key: {num} смещение
                 @return: {str} зашифрованный символ
        """
        if not char.isalpha():
            return char
        else:
            base = "A" if char.isupper() else "a"
            return chr((ord(char) - ord(base) + key) % 26 + ord(base))

    def encrypt(self, char, key):
        """
                 Шифровать персонажей
        """
        return self.__crypt(char, key)

    def decrypt(self, char, key):
        """
                 Расшифровать символы
        """
        return self.__crypt(char, -key)

    def __crypt_text(self, func, text, key):
        """
               Зашифровать текст
               @param char: {str} текст
               @param key: {num} смещение
               @return: {str} зашифрованный текст
       """
        lines = []
        for line in text.split("\n"):
            words = []
            for word in line.split(" "):
                chars = []
                for char in word:
                    chars.append(func(char, key))
                words.append("".join(chars))
            lines.append(" ".join(words))
        return "\n".join(lines)

    def encrypt_text(self, text, key):
        """
                 Зашифровать текст
        """
        return self.__crypt_text(self.encrypt, text, key)

    def decrypt_text(self, text, key):
        """
                 Расшифровать текст
        """
        return self.__crypt_text(self.decrypt, text, key)


if __name__ == '__main__':
    plain = """
    you know? I love you!
    """
    key = 3

    cipher = CaesarCipher()

    # Шифрование
    print(cipher.encrypt_text(plain, key))
    # brx nqrz? L oryh brx!

    # Расшифровать
    print(cipher.decrypt_text("brx nqrz? L oryh brx!", key))
    # you know? I love you!

