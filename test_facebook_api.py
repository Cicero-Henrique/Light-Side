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
                word = word + profile["words"][i] + "; "
            except UnicodeEncodeError:
                print("skip")
        
        
        
        # WARNING
        
        f.write("words:" + word.encode("utf-8") + "\n")
        
        # WARNING
        
        
        
        
        
        f.close()

    def read_from_file(self):
        profile = []
        f = open("backupFile.txt", "r")
        for line in f:
            type = line.split(":")[0]
            content = line.split(":")[1]
            content =  content.split("; ")
            profile[type] = content

        return profile


    def __init__(self, profile):
        self.write_in_file(profile)
        # profile = self.read_from_file()

        print(profile)
