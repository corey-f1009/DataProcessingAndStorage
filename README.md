# DataProcessingAndStorage

Description:
An in-memory key-value database that supports the following functions:
a. begin_transaction()
b. put(key, value)
c. get(key)
d. commit()
e. rollback()

Setup:
1. Install Python 3
2. Download ec.py
3. Run this command in your terminal after opening python file: python ec.py

Testing:
The commands supported by the files are below, alongside the expected input format.

get <key>               # Return the value associated with the key or null if the key doesn’t exist.
put <key> <value>       # Will create a new key with the provided value or update the value of a key
begin_transact          # Initiates a transaction
commit                  # Commits actions made during a transaction
rollback                # Erases any changes that were going to be made by a transaction
help                    # Prints this command list
quit                    # Terminates the program

Assignment Modifications:
I think it would be helpful to go into expectations for other types of edge cases. For example, what should happen if someone attempts to create a new transaction while one is already in progress, since that wasn't covered in the Fig 2 example. I think it would also be good to have us explain why database should abide by the principles demonstrated in the specifications, and provide examples of what issues could arise if we don't meet a certain requirement, to ensure we understand the importance of these design choices. 

