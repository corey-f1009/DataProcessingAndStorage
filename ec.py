class InMemoryDB:
    def __init__(self):
        self.transact = None
        self.committed = {}

    def get(self, key):
        if key in self.committed:
            return self.committed[key]
        else:
            return None
        
    def put(self, key, value):
        if self.transact == None:
            raise Exception("Transaction not in progress")
        self.transact[key] = value
        print("Successful entry")

    def beginTransaction(self):
        if self.transact != None:
            raise Exception("Transaction already in progress")
        self.transact = {}
        print("Started transaction")

    def commit(self):
        if self.transact == None:
            raise Exception("Nothing to commit")
        for key, value in self.transact.items():
            self.committed[key] = value
        self.transact = None
        print("Committed")

    def rollback(self):
        if self.transact == None:
            raise Exception("Nothing to rollback")
        self.transact = None
        print("Rolled back")

def helpMenu():
    print("Commands/Formats:")
    print(" get <key>")
    print(" put <key> <value>")
    print(" begin_transact")
    print(" commit")
    print(" rollback")
    print(" help")
    print(" quit")

def commandHandling(argv, db):
    if len(argv) <1:
        helpMenu()
        return True
    command = argv[0]
    if command == "get":
       if len(argv) > 1:    
        print(db.get(argv[1]))
    elif command == "put":
       if len(argv) > 2:    
        db.put(argv[1], argv[2])
    elif command == "begin_transact":
       db.beginTransaction()
    elif command == "commit":
       db.commit()
    elif command == "rollback":
       db.rollback()
    elif command == "help":
       helpMenu()
    elif command == "quit":
       return False
    return True
    
if __name__ == "__main__":
    db = InMemoryDB()
    helpMenu()
    while True:
        input = input("Enter command: ")    
        argv = input.strip().split()
        if not commandHandling(argv, db):
            break