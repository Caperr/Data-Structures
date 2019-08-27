# Circular queue implementation following this pseudo-code from a computer science textbook.
# Add to queue:
#     Rear <- Rear + 1
#     If Rear = 9 Then Rear <- 0
#     Put DataItem at position Rear in array
# Remove data from queue:
#     Take DataItem from position Front in array
#     Front <- Front + 1
#     If Front = 9 Then Front <- 0
#
# Implementation written by Jasper Law

queue = ["", "", "", "", "", "", "", "", ""]
front = 0
rear = 8


# Print out the queue
def printQueue(front, rear, queue):
    print("\nQueue:", end="")
    for char in queue:
        if char == "":
            print("-", end="")
        else:
            print(char, end="")
    # Print out the current front and rear
    print("\nF" + str(front), "R" + str(rear), end=" ")
    if front < rear:
        print(" " * front + "F" + " " * (rear - front - 1) + "R\n")
    elif front > rear:
        print(" " * rear + "R" + " " * (front - rear - 1) + "F\n")
    else:
        print(" " * front + "X\nFront and rear are both at X\n")


# Take user input for next action
def getDataItem():
    # Take input
    dataItem = input("Enter a character, -, or 'exit': ")
    # Validate input ("-" char is not allowed, as it is reserved for empty places)
    while len(dataItem) != 1 and dataItem != "exit":
        dataItem = input("Enter a character, -, or 'exit': ")
    # Return result
    return dataItem


# Check if an array is empty or not
def isEmpty(array):
    for item in array:
        if item != "":
            return False
    return True


# ----- Main Program -----


# Print initial queue
printQueue(front, rear, queue)
# Get initial action
dataItem = getDataItem()

# Main program loop
while dataItem.lower() != "exit":
    # If removing from the queue
    # If queue is already empty, no action is required
    if dataItem == "-" and not isEmpty(queue):
        # Remove front item
        queue[front] = ""
        # Increment front
        front += 1
        # Move front back to the start of the queue if end is reached
        if front == 9:
            front = 0

    # If adding to the queue
    elif dataItem != "-":
        # Set data item to upper case for neatness
        dataItem = dataItem.upper()
        # Increment rear
        rear += 1
        # Move rear back to the start of the queue is end is reached
        if rear == 9:
            rear = 0

        # Separate handling for rear=0 to prevent index errors
        if rear == 0:
            queue = [dataItem] + queue[0:-1]
        # Insert dataItem into queue
        else:
            queue = queue[0:rear] + [dataItem] + queue[rear:-1]

    # Print queue
    printQueue(front, rear, queue)
    # Get next action
    dataItem = getDataItem()
