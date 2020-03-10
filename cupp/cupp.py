
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

__author__ = "Muris Kurgas"
__license__ = "GPL"
__version__ = "3.2.5-alpha"

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
        """Implementation of the -i switch. Interactively question the user and
        create a password dictionary file based on the answer."""

        print(
            "\r\n[+] Insert the information about the victim to make a dictionary")
        print("[+] If you don't know all the info, just hit enter when asked! ;)\r\n")

        # We need some information first!

        # profile = {}

        # name = input("> First Name: ").lower()
        # while len(name) == 0 or name == " " or name == "  " or name == "   ":
        #     print("\r\n[-] You must enter a name at least!")
        #     name = input("> Name: ").lower()
        # profile["name"] = str(name)

        # profile["surname"] = input("> Surname: ").lower()
        profile["nick"] = input("> Nickname: ").lower()
        birthdate = input("> Birthdate (DDMMYYYY): ")
        while len(birthdate) != 0 and len(birthdate) != 8:
            print("\r\n[-] You must enter 8 digits for birthday!")
            birthdate = input("> Birthdate (DDMMYYYY): ")
        profile["birthdate"] = str(birthdate)

        # print("\r\n")

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

        # Opening the file of likes
        # f = open("pages.txt", "r", encoding="utf-8")
        # likes_list = f.read().replace(" ", "")
        # f.close()
        # likes_list = likes_list.split("\n")
        # #likes_list = likes_list.replace(" ", "")

        # profile["words"] = likes_list

        profile["spechars1"] = input(
            "> Do you want to add special chars at the end of words? Y/[N]: "
        ).lower()

        profile["randnum"] = input(
            "> Do you want to add some random numbers at the end of words? Y/[N]:"
        ).lower()
        profile["leetmode"] = input(
            "> Leet mode? (i.e. leet = 1337) Y/[N]: ").lower()

        self.generate_wordlist_from_profile(profile)  # generate the wordlist

    def rip_birth(self, date):
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

    def generate_wordlist_from_profile(self, profile):
        """ Generates a wordlist from a given profile """

        chars = CONFIG["global"]["chars"]
        years = CONFIG["global"]["years"]
        numfrom = CONFIG["global"]["numfrom"]
        numto = CONFIG["global"]["numto"]

        profile["spechars"] = []

        if profile["spechars1"] == "y":
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

        birth_slices = self.rip_birth(profile["birthdate"])
        birthday_comb = self.birthday_combinations(birth_slices)

        # For a woman...

        wife_birth_slices = self.rip_birth(profile["wifeb"])
        wife_birthday_comb = self.birthday_combinations(wife_birth_slices)

        # and a child...

        kid_birth_slices = self.rip_birth(profile["kidb"])
        kid_birthday_comb = self.birthday_combinations(kid_birth_slices)

        # string combinations....

        kombinaac = [profile["pet"], petup, profile["company"], companyup]

        kombina = [
            profile["name"],
            profile["surname"],
            profile["nick"],
            nameup,
            surnameup,
            nickup,
        ]

        kombinaw = [
            profile["wife"],
            profile["wifen"],
            wifeup,
            wifenup,
            profile["surname"],
            surnameup,
        ]

        kombinak = [
            profile["kid"],
            profile["kidn"],
            kidup,
            kidnup,
            profile["surname"],
            surnameup,
        ]

        kombinaa = []
        for kombina1 in kombina:
            kombinaa.append(kombina1)
            for kombina2 in kombina:
                if kombina.index(kombina1) != kombina.index(kombina2) and kombina.index(
                    kombina1.title()
                ) != kombina.index(kombina2.title()):
                    kombinaa.append(kombina1 + kombina2)

        kombinaaw = []
        for kombina1 in kombinaw:
            kombinaaw.append(kombina1)
            for kombina2 in kombinaw:
                if kombinaw.index(kombina1) != kombinaw.index(kombina2) and kombinaw.index(
                    kombina1.title()
                ) != kombinaw.index(kombina2.title()):
                    kombinaaw.append(kombina1 + kombina2)

        kombinaak = []
        for kombina1 in kombinak:
            kombinaak.append(kombina1)
            for kombina2 in kombinak:
                if kombinak.index(kombina1) != kombinak.index(kombina2) and kombinak.index(
                    kombina1.title()
                ) != kombinak.index(kombina2.title()):
                    kombinaak.append(kombina1 + kombina2)

        kombi = {}
        kombi[1] = list(self.komb(kombinaa, birthday_comb))
        kombi[1] += list(self.komb(kombinaa, birthday_comb, "_"))
        kombi[2] = list(self.komb(kombinaaw, wife_birthday_comb))
        kombi[2] += list(self.komb(kombinaaw, wife_birthday_comb, "_"))
        kombi[3] = list(self.komb(kombinaak, kid_birthday_comb))
        kombi[3] += list(self.komb(kombinaak, kid_birthday_comb, "_"))
        kombi[4] = list(self.komb(kombinaa, years))
        kombi[4] += list(self.komb(kombinaa, years, "_"))
        kombi[5] = list(self.komb(kombinaac, years))
        kombi[5] += list(self.komb(kombinaac, years, "_"))
        kombi[6] = list(self.komb(kombinaaw, years))
        kombi[6] += list(self.komb(kombinaaw, years, "_"))
        kombi[7] = list(self.komb(kombinaak, years))
        kombi[7] += list(self.komb(kombinaak, years, "_"))
        kombi[8] = list(self.komb(word, birthday_comb))
        kombi[8] += list(self.komb(word, birthday_comb, "_"))
        kombi[9] = list(self.komb(word, wife_birthday_comb))
        kombi[9] += list(self.komb(word, wife_birthday_comb, "_"))
        kombi[10] = list(self.komb(word, kid_birthday_comb))
        kombi[10] += list(self.komb(word, kid_birthday_comb, "_"))
        kombi[11] = list(self.komb(word, years))
        kombi[11] += list(self.komb(word, years, "_"))
        kombi[12] = [""]
        kombi[13] = [""]
        kombi[14] = [""]
        kombi[15] = [""]
        kombi[16] = [""]
        kombi[21] = [""]
        if profile["randnum"] == "y":
            kombi[12] = list(self.concats(word, numfrom, numto))
            kombi[13] = list(self.concats(kombinaa, numfrom, numto))
            kombi[14] = list(self.concats(kombinaac, numfrom, numto))
            kombi[15] = list(self.concats(kombinaaw, numfrom, numto))
            kombi[16] = list(self.concats(kombinaak, numfrom, numto))
            kombi[21] = list(self.concats(reverse, numfrom, numto))
        kombi[17] = list(self.komb(reverse, years))
        kombi[17] += list(self.komb(reverse, years, "_"))
        kombi[18] = list(self.komb(rev_w, wife_birthday_comb))
        kombi[18] += list(self.komb(rev_w, wife_birthday_comb, "_"))
        kombi[19] = list(self.komb(rev_k, kid_birthday_comb))
        kombi[19] += list(self.komb(rev_k, kid_birthday_comb, "_"))
        kombi[20] = list(self.komb(rev_n, birthday_comb))
        kombi[20] += list(self.komb(rev_n, birthday_comb, "_"))
        komb001 = [""]
        komb002 = [""]
        komb003 = [""]
        komb004 = [""]
        komb005 = [""]
        komb006 = [""]
        if len(profile["spechars"]) > 0:
            komb001 = list(self.komb(kombinaa, profile["spechars"]))
            komb002 = list(self.komb(kombinaac, profile["spechars"]))
            komb003 = list(self.komb(kombinaaw, profile["spechars"]))
            komb004 = list(self.komb(kombinaak, profile["spechars"]))
            komb005 = list(self.komb(word, profile["spechars"]))
            komb006 = list(self.komb(reverse, profile["spechars"]))

        print("[+] Sorting list and removing duplicates...")

        komb_unique = {}
        for i in range(1, 22):
            komb_unique[i] = list(dict.fromkeys(kombi[i]).keys())

        komb_unique01 = list(dict.fromkeys(kombinaa).keys())
        komb_unique02 = list(dict.fromkeys(kombinaac).keys())
        komb_unique03 = list(dict.fromkeys(kombinaaw).keys())
        komb_unique04 = list(dict.fromkeys(kombinaak).keys())
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
        if profile["leetmode"] == "y":
            for (
                x
            ) in (
                unique_lista
            ):  # if you want to add more leet chars, you will need to add more lines in cupp.cfg too...

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
