# DataProcessingAndStorage

Description:
An in-memory key-value database that supports the following functions:
1. begin_transaction()
2. put(key, value)
3. get(key)
4. commit()
5. rollback()

Setup:
1. Install Python 3
2. Download ec.py
3. Run this command in your terminal after opening python file: python ec.py

Testing:
The commands supported by the files are below, alongside the expected input format.

1. get [key] &emsp; &emsp; &emsp;# Return the value associated with the key or null if the key doesn’t exist.
2. put [key] [value] &emsp; &emsp; &emsp;       # Will create a new key with the provided value or update the value of a key
3. begin_transact&emsp; &emsp; &emsp;          # Initiates a transaction
4. commit&emsp; &emsp; &emsp;                  # Commits actions made during a transaction
5. rollback&emsp; &emsp; &emsp;                # Erases any changes that were going to be made by a transaction
6. help&emsp; &emsp; &emsp;                    # Prints this command list
7. quit&emsp; &emsp; &emsp;                    # Terminates the program

Assignment Modifications:
I think it would be helpful to go into expectations for other types of edge cases. For example, what should happen if someone attempts to create a new transaction while one is already in progress, since that wasn't covered in the Fig 2 example. I think it would also be good to have us explain why database should abide by the principles demonstrated in the specifications, and provide examples of what issues could arise if we don't meet a certain requirement, to ensure we understand the importance of these design choices. 

