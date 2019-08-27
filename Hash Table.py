# hash table implementation, with folding based hashing algorithm,
# and incremented re-hashing based collision handling
# written by Jasper Law

# Hash table class
class hashTable:
    # Table storage
    table = []
    # Table size. Does not change
    size = 0

    # Constructor - populates the table with empty records
    def __init__(self, _size):
        # Populate
        for i in range(_size):
            self.table.append([0, ""])
        # Store size for later
        self.size = _size

    # Check if the table is full
    def isFull(self):
        # iterate through table
        for item in range(self.getSize()):
            # Check if current record is empty
            if self.getValue(item) == "":
                # If an empty record is found, table is not full
                return False
        # iteration completed, therefore no empty records found, therefore table is full
        return True

    # Update a record
    def changeItem(self, itemHash, key, value):
        self.table[itemHash] = [key, value]

    # Set a record to empty
    def removeItem(self, itemHash):
        self.table[itemHash] = [0, ""]

    # Retrieve a value from the table, using the hash. Hash must be pre-calculated if you wish to retrieve based on key
    def getValue(self, itemHash):
        return self.table[itemHash][1]

    # Return table size
    def getSize(self):
        return self.size

    # Generate a hash from item key
    def makeHash(self, key):
        keyFold = 0
        # Iterate through key
        for character in key:
            # Add ascii value of current character to total fold value
            keyFold += ord(character)
        # Mod the folded number by the size of the table
        hashResult = keyFold % self.getSize()
        # If table is full, say so, and do not check for collisions
        if self.isFull():
            print("Table full")
        # Table is not full, so perform collision detection
        else:
            rehashed = False
            # While the current index is already populated
            while self.getValue(hashResult) != "":
                # Add 1 to fold result, and rehash
                keyFold += 1
                hashResult = keyFold % self.getSize()
                rehashed = True
            # If collision was detected, say so
            if rehashed:
                print("Rehashed", key, "to", hashResult)
        # Return the hash
        return hashResult

    # Print the table out
    def printTable(self):
        print(self.table)


# ===============================================================


# Example; 6 school-goers with IDs (keys) and first names.
# [!] Using first names increases collision likelihood. Would be much better to feed both first and last name into hash

# Initialize table
studentTable = hashTable(6)
# The students
students = [["014B", "John"], ["1641", "Sarah"], ["0FF6", "Abdul"],
            ["003B", "Zeke"], ["0AF4", "Katie"], ["0E11", "Megan"]]

# Iterate through students, but stop if the table is full. Otherwise we'll be overwriting students
studentIndex = 0
while not studentTable.isFull():
    # "shortcut" to current student
    student = students[studentIndex]
    # generate hash
    studentKeyHash = studentTable.makeHash(student[0])
    # add student to table
    studentTable.changeItem(studentKeyHash, student[0], student[1])
    # move onto next student
    studentIndex += 1

# print out the table
studentTable.printTable()
