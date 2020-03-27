from unicodedata import normalize

class backup:

    def write_in_file(self, profile):
        f = open("backupFile.txt", "w")
        f.write("name:" + profile["name"] + "\n")

        word = ""
        for work in profile["work"]:
            word = word + work + "; "
        f.write("work:" + word + "\n")

        word = ""
        for study in profile["study"]:
            word = word + study + "; "
        f.write("study:" + word + "\n")

        word = ""
        for city in profile["cities"]:
            word = word + city + "; "
        f.write("cities:" + word + "\n")

        word = ""
        for i in range(0, len(profile["words"])):
            try:
                word = word + str(normalize('NFKD', str(profile["words"][i])).encode('ASCII', 'ignore').decode('ASCII')) + "; "
            except UnicodeEncodeError:
                print("skip")

        f.write("words:" + word + "\n")

        profile["victim_nickname"] = "marky"
        f.write("victim_nickname:" + profile["victim_nickname"] + "\n")
        profile["victim_birthdate"] = "09091990"
        f.write("victim_birthdate:" + profile["victim_birthdate"] + "\n")
        profile["wife_name"] = "megan fox"
        f.write("wife_name:" + profile["wife_name"] + "\n")
        profile["wife_nickname"] = "meggy"
        f.write("wife_nickname:" + profile["wife_nickname"] + "\n")
        profile["wife_birthdate"] = "01011991"
        f.write("wife_birthdate:" + profile["wife_birthdate"] + "\n")
        profile["kid_name"] = "mark; facebookson; brigite"
        f.write("kid_name:" + profile["kid_name"] + "\n")
        profile["kid_nickname"] = "marky; jobson; littleB"
        f.write("kid_nickname:" + profile["kid_nickname"] + "\n")
        profile["kid_birthdate"] = "05052005"
        f.write("kid_birthdate:" + profile["kid_birthdate"] + "\n")
        profile["pet"] = "whatsapp"
        f.write("pet:" + profile["pet"] + "\n")
        profile["company"] = "facebook"
        f.write("company:" + profile["company"] + "\n")

        f.close()

    def read_from_file(self):
        profile = {}
        f = open("backupFile.txt", "r")
        for line in f:
            type = line.split(":")[0]
            content = line.split(":")[1]
            content = content.replace('\n', '')
            content =  content.split("; ")
            profile[type] = content

        return profile

    def __init__(self):
        # self.write_in_file(profile)
        self._profile = self.read_from_file()
        print(self._profile)

    @property
    # moved the logic for returning area to a separate method
    def profile(self):
        return self._profile
