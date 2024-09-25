


class ParkCount(Screen):

    TotalParks = StringProperty("5")
    def addInfo(self):

        global client
        db = client["Main data"]
        
        my_collection = db["Account Info"]
        data = self.ids.Submit2.text
        NameData = [{"Parks": data}]

        global Parks
        self.Parks = self.ids.Submit2.text

        try:
            result = my_collection.insert_many(NameData)
        except pymongo.errors.OperationFailure:
            print("An authentication error was received. Check your database user permissions.")
            sys.exit(1)
        else:
            inserted_count = len(result.inserted_ids)
            print("I inserted %d documents." % inserted_count)
            print("\n")
        self.manager.current = 'EnvironmentalIssues'
    def getInfo(self):
        global client
        db = client["Main data"]
        
        my_collection = db["TotalParks"]
        self.TotalParks = -1
        #Purpose is to get the numebr of bottles
        x = 0
        while self.TotalParks == -1:
            if my_collection.find({'Parks': str(x)}) == True:
                self.TotalParkss = my_collection.find({'Parks': str(x)})