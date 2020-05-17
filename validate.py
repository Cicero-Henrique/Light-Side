class Validate:

    def from_dict_to_list(self, dict1):
        unique = []
        for arr in dict1.values():
            unique = unique + arr

        return unique

    def first_look(self, word):
        chars = ['"""', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
                    ';', '<', '=', '>', '?', '@', '[', '"\"', ']', '^', '_', '`', '{', '|', '}', '~']
        contains_digit = False
        contains_spec_char = False
        if(len(word) < 8):
            print("Your password is weak because it's too short!")
            return True

        for character in word:
            if character.isdigit():
                contains_digit = True
            if(character in chars):
                contains_spec_char = True
            if contains_digit and contains_spec_char:
                break

        if(not contains_digit):
            print("Your password is weak because it not contains any number!")
            return True

        if(not contains_spec_char):
            print("Warning! Consider using special characters.")

        return False

    def is_weak(self, data):
        password = input("What is the password to validate: ")
        weak = self.first_look(password)
        if(not weak):
            for word in data:
                if word.lower() in password.lower() and word != '':
                    weak = True
                    print("Your password is weak, I found " + word + " in your profile.")
                    return weak

        return weak

    def __init__(self, profile):
        profile = self.from_dict_to_list(profile)
        want_finish = False
        while not want_finish:
            if (not self.is_weak(profile)):
                print("Congratulations, this passwords looks fine.")
            op = "C"
            while (op.lower() != 'n' or op.lower() != 'y'):
                op = input("Do you want to try another password? Y/N ")
                if(op.lower() == 'n' or op.lower() == 'y'):
                    break
            if(op.lower() == "n"):
                want_finish = True

