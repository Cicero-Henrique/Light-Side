
import argparse
import configparser
import csv
import functools
import gzip
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

CONFIG = {}


class cupp:

    def read_config(self, filename):
        """Read the given configuration file and update global variables to
        reflect changes (CONFIG)."""

        if os.path.isfile(filename):

            # global CONFIG

            # Reading configuration file
            config = configparser.ConfigParser()
            config.read(filename)

            CONFIG["global"] = {
                "years": config.get("years", "years").split(","),
                "chars": config.get("specialchars", "chars").split(","),
                "numfrom": config.getint("nums", "from"),
                "numto": config.getint("nums", "to"),
                "wcfrom": config.getint("nums", "wcfrom"),
                "wcto": config.getint("nums", "wcto"),
                "threshold": config.getint("nums", "threshold"),
                "alectourl": config.get("alecto", "alectourl"),
                "dicturl": config.get("downloader", "dicturl"),
            }

            # 1337 mode configs, well you can add more lines if you add it to
            # the config file too.
            leet = functools.partial(config.get, "leet")
            leetc = {}
            letters = {"a", "i", "e", "t", "o", "s", "g", "z"}

            for letter in letters:
                leetc[letter] = config.get("leet", letter)

            CONFIG["LEET"] = leetc

            return True

        else:
            print("Configuration file " + filename + " not found!")
            sys.exit("Exiting.")

            return False

    def make_leet(self, x):
        """convert string to leet"""
        for letter, leetletter in CONFIG["LEET"].items():
            x = x.replace(letter, leetletter)
        return x

    # for concatenations...
    def concats(self, seq, start, stop):
        for mystr in seq:
            for num in range(start, stop):
                yield mystr + str(num)

    # for sorting and making combinations...
    def komb(self, seq, start, special=""):
        for mystr in seq:
            for mystr1 in start:
                yield mystr + special + mystr1

    def print_to_file(self, filename, unique_list_finished):
        f = open(filename, "w")
        unique_list_finished.sort()
        f.write(os.linesep.join(unique_list_finished))
        f.close()
        f = open(filename, "r")
        lines = 0
        for line in f:
            lines += 1
        f.close()
        print(
            "[+] Saving dictionary to \033[1;31m"
            + filename
            + "\033[1;m, counting \033[1;31m"
            + str(lines)
            + " words.\033[1;m"
        )
        print(
            "[+] Now load your pistolero with \033[1;31m"
            + filename
            + "\033[1;m and shoot! Good luck!"
        )

    def interactive(self, profile):
        print("\r\n[+] Insert the information about the victim to make a dictionary")
        print("[+] If you don't know all the info, just hit enter when asked! ;)\r\n")

        profile["nick"] = input("> Nickname: ").lower()
        birthdate = input("> Birthdate (DDMMYYYY): ")
        while len(birthdate) != 0 and len(birthdate) != 8:
            print("\r\n[-] You must enter 8 digits for birthday!")
            birthdate = input("> Birthdate (DDMMYYYY): ")
        profile["birthdate"] = str(birthdate)

        profile["wife"] = input("> Partners) name: ").lower()
        profile["wifen"] = input("> Partners) nickname: ").lower()
        wifeb = input("> Partners) birthdate (DDMMYYYY): ")
        while len(wifeb) != 0 and len(wifeb) != 8:
            print("\r\n[-] You must enter 8 digits for birthday!")
            wifeb = input("> Partners birthdate (DDMMYYYY): ")
        profile["wifeb"] = str(wifeb)
        print("\r\n")

        profile["kid"] = input("> Child's name: ").lower()
        profile["kidn"] = input("> Child's nickname: ").lower()
        kidb = input("> Child's birthdate (DDMMYYYY): ")
        while len(kidb) != 0 and len(kidb) != 8:
            print("\r\n[-] You must enter 8 digits for birthday!")
            kidb = input("> Child's birthdate (DDMMYYYY): ")
        profile["kidb"] = str(kidb)
        print("\r\n")

        profile["pet"] = input("> Pet's name: ").lower()
        profile["company"] = input("> Company name: ").lower()
        print("\r\n")

        answer = input("> Do you want to add special chars at the end of words? Y/[N]: ").lower()
        if(answer == 'y'):
            profile["spechars1"] = True
        else:
            profile["spechars1"] = False

        answer = input("> Do you want to add some random numbers at the end of words? Y/[N]:").lower()
        if(answer == 'y'):
            profile["randnum"] = True
        else:
            profile["randnum"] = False

        answer = input("> Leet mode? (i.e. leet = 1337) Y/[N]: ").lower()
        if(answer == 'y'):
            profile["leetmode"] = True
        else:
            profile["leetmode"] = False

        self.generate_wordlist_from_profile(profile)  # generate the wordlist

    def rip_birthday(self, date):
        birthday_slices = [
            date[-2:],
            date[-3:],
            date[-4:],
            date[1:2],
            date[3:4],
            date[:2],
            date[2:4]
        ]
        return birthday_slices

    def birthday_combinations(self, birthday_slices):
        birthday_comb = []
        for aux1 in birthday_slices:
            birthday_comb.append(aux1)
            for aux2 in birthday_slices:
                if birthday_slices.index(aux1) != birthday_slices.index(aux2):
                    birthday_comb.append(aux1 + aux2)
                    for aux3 in birthday_slices:
                        if (
                            birthday_slices.index(aux1) != birthday_slices.index(aux2)
                            and birthday_slices.index(aux2) != birthday_slices.index(aux3)
                            and birthday_slices.index(aux1) != birthday_slices.index(aux3)
                        ):
                            birthday_comb.append(aux1 + aux2 + aux3)

        return birthday_comb

    def names_combinations(self, names):
        combinations = []
        for name in names:
            combinations.append(name)
            for kombina2 in names:
                if names.index(name) != names.index(kombina2) and names.index(
                    name.title()
                ) != names.index(kombina2.title()):
                    combinations.append(name + kombina2)

        return combinations

    def generate_combinations_array(self, array, birthday):
        new_combinations = list(self.komb(array, birthday))
        new_combinations += list(self.komb(array, birthday))
        return new_combinations

    def generate_wordlist_from_profile(self, profile):
        """ Generates a wordlist from a given profile """

        chars = CONFIG["global"]["chars"]
        years = CONFIG["global"]["years"]
        numfrom = CONFIG["global"]["numfrom"]
        numto = CONFIG["global"]["numto"]

        profile["spechars"] = []

        if profile["spechars1"] == True:
            for spec1 in chars:
                profile["spechars"].append(spec1)
                for spec2 in chars:
                    profile["spechars"].append(spec1 + spec2)
                    for spec3 in chars:
                        profile["spechars"].append(spec1 + spec2 + spec3)

        print("\r\n[+] Now making a dictionary...")

        # Now me must do some string modifications...

        # Birthdays first

        # Convert first letters to uppercase...

        nameup =    profile["name"].title()
        surnameup = profile["surname"].title()
        nickup =    profile["nick"].title()
        wifeup =    profile["wife"].title()
        wifenup =   profile["wifen"].title()
        kidup =     profile["kid"].title()
        kidnup =    profile["kidn"].title()
        petup =     profile["pet"].title()
        companyup = profile["company"].title()

        wordsup = []
        wordsup = list(map(str.title, profile["words"]))

        word = profile["words"] + wordsup

        # reverse a name

        rev_name = profile["name"][::-1]
        rev_nameup = nameup[::-1]
        rev_nick = profile["nick"][::-1]
        rev_nickup = nickup[::-1]
        rev_wife = profile["wife"][::-1]
        rev_wifeup = wifeup[::-1]
        rev_kid = profile["kid"][::-1]
        rev_kidup = kidup[::-1]

        reverse = [
            rev_name,
            rev_nameup,
            rev_nick,
            rev_nickup,
            rev_wife,
            rev_wifeup,
            rev_kid,
            rev_kidup,
        ]
        rev_n = [rev_name, rev_nameup, rev_nick, rev_nickup]
        rev_w = [rev_wife, rev_wifeup]
        rev_k = [rev_kid, rev_kidup]
        # Let's do some serious work! This will be a mess of code, but...
        # who cares? :)

        # Birthdays combinations

        birth_slices = self.rip_birthday(profile["birthdate"])
        birthday_comb = self.birthday_combinations(birth_slices)

        # For a woman...

        wife_birth_slices = self.rip_birthday(profile["wifeb"])
        wife_birthday_comb = self.birthday_combinations(wife_birth_slices)

        # and a child...

        kid_birth_slices = self.rip_birthday(profile["kidb"])
        kid_birthday_comb = self.birthday_combinations(kid_birth_slices)

        # string combinations....

        comb_pet_company = [profile["pet"], petup, profile["company"], companyup]

        victim_names = [
            profile["name"],
            profile["surname"],
            profile["nick"],
            nameup,
            surnameup,
            nickup,
        ]

        wife_names = [
            profile["wife"],
            profile["wifen"],
            wifeup,
            wifenup,
            profile["surname"],
            surnameup,
        ]

        kid_names = [
            profile["kid"],
            profile["kidn"],
            kidup,
            kidnup,
            profile["surname"],
            surnameup,
        ]

        comb_victim_names = self.names_combinations(victim_names)

        comb_wife_names = self.names_combinations(wife_names)

        comb_kid_names = self.names_combinations(kid_names)

        all_combinations = {}

        all_combinations[0] = self.generate_combinations_array(comb_victim_names, birthday_comb)
        all_combinations[1] = self.generate_combinations_array(comb_wife_names, wife_birthday_comb)
        all_combinations[2] = self.generate_combinations_array(comb_kid_names, kid_birthday_comb)

        all_combinations[3] = self.generate_combinations_array(comb_victim_names, years)
        all_combinations[4] = self.generate_combinations_array(comb_pet_company, years)
        all_combinations[5] = self.generate_combinations_array(comb_wife_names, years)
        all_combinations[6] = self.generate_combinations_array(comb_kid_names, years)

        all_combinations[7] = self.generate_combinations_array(word, birthday_comb)
        all_combinations[8] = self.generate_combinations_array(word, wife_birthday_comb)
        all_combinations[9] = self.generate_combinations_array(word, kid_birthday_comb)
        all_combinations[10] =  self.generate_combinations_array(word, years)

        all_combinations[11] =  self.generate_combinations_array(reverse, years)
        all_combinations[12] =  self.generate_combinations_array(rev_w, wife_birthday_comb)
        all_combinations[13] =  self.generate_combinations_array(rev_k, kid_birthday_comb)
        all_combinations[14] =  self.generate_combinations_array(rev_n, birthday_comb)

        if profile["randnum"] == True:
            all_combinations[15] = list(self.concats(word, numfrom, numto))
            all_combinations[16] = list(self.concats(comb_victim_names, numfrom, numto))
            all_combinations[17] = list(self.concats(comb_pet_company, numfrom, numto))
            all_combinations[18] = list(self.concats(comb_wife_names, numfrom, numto))
            all_combinations[19] = list(self.concats(comb_kid_names, numfrom, numto))
            all_combinations[20] = list(self.concats(reverse, numfrom, numto))

        komb001 = [""]
        komb002 = [""]
        komb003 = [""]
        komb004 = [""]
        komb005 = [""]
        komb006 = [""]
        if len(profile["spechars"]) > 0:
            komb001 = list(self.komb(comb_victim_names, profile["spechars"]))
            komb002 = list(self.komb(comb_pet_company, profile["spechars"]))
            komb003 = list(self.komb(comb_wife_names, profile["spechars"]))
            komb004 = list(self.komb(comb_kid_names, profile["spechars"]))
            komb005 = list(self.komb(word, profile["spechars"]))
            komb006 = list(self.komb(reverse, profile["spechars"]))

        print("[+] Sorting list and removing duplicates...")

        komb_unique = {}
        for i in range(0, len(all_combinations)):
            komb_unique[i] = list(dict.fromkeys(all_combinations[i]).keys())

        komb_unique01 = list(dict.fromkeys(comb_victim_names).keys())
        komb_unique02 = list(dict.fromkeys(comb_pet_company).keys())
        komb_unique03 = list(dict.fromkeys(comb_wife_names).keys())
        komb_unique04 = list(dict.fromkeys(comb_kid_names).keys())
        komb_unique05 = list(dict.fromkeys(word).keys())
        komb_unique07 = list(dict.fromkeys(komb001).keys())
        komb_unique08 = list(dict.fromkeys(komb002).keys())
        komb_unique09 = list(dict.fromkeys(komb003).keys())
        komb_unique010 = list(dict.fromkeys(komb004).keys())
        komb_unique011 = list(dict.fromkeys(komb005).keys())
        komb_unique012 = list(dict.fromkeys(komb006).keys())

        uniqlist = (
            birthday_comb
            + wife_birthday_comb
            + kid_birthday_comb
            + reverse
            + komb_unique01
            + komb_unique02
            + komb_unique03
            + komb_unique04
            + komb_unique05
        )

        for i in range(1, 21):
            uniqlist += komb_unique[i]

        uniqlist += (
            komb_unique07
            + komb_unique08
            + komb_unique09
            + komb_unique010
            + komb_unique011
            + komb_unique012
        )
        unique_lista = list(dict.fromkeys(uniqlist).keys())
        unique_leet = []
        if profile["leetmode"] == True:
            for (x) in (unique_lista):  # if you want to add more leet chars, you will need to add more lines in cupp.cfg too...

                x = self.make_leet(x)  # convert to leet
                unique_leet.append(x)

        unique_list = unique_lista + unique_leet

        unique_list_finished = []
        unique_list_finished = [
            x
            for x in unique_list
            if len(x) < CONFIG["global"]["wcto"] and len(x) > CONFIG["global"]["wcfrom"]
        ]

        self.print_to_file(profile["name"] + ".txt", unique_list_finished)

    # the main function
    # def main():
    #     """Command-line interface to the cupp utility"""

    #     # read_config(os.path.join(os.path.dirname(os.path.realpath(__file__)), "cupp.cfg"))
    #     interactive()

    # if __name__ == "__main__":
    #     main()

    def __init__(self, profile):
        # self.__profile = profile
        self.read_config(os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "cupp.cfg"))
        self.interactive(profile)

    @property
    def profile(self):
        return self.__profile
