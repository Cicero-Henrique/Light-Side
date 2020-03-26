class backup:

    def write_in_file(self, profile):
        f = open("backupFile.txt", "w")
        f.write("name:" + profile["name"] + "\n")
        f.write("work:" + profile["work"] + "\n")
        f.write("study:" + profile["study"] + "\n")
        f.write("cities:" + profile["hometown"] + "\n")
        f.write("words:" + profile["words"] + "\n")
        f.close()

    def read_from_file(self):
        profile = []
        f = open("backupFile.txt", "r")
        for line in f:
            profile[line.split(":")[0]] = line.split(":")[1]

        return profile


    def __init__(self, profile):
        self.write_in_file(profile)
        # profile = self.read_from_file()

        print(profile)
