# Simple Banking System

> This project is a good representation of a simple banking system. A user can create a bank account, log into it with the correct credentials and perform various actions. Also we use 
for the first time a database to store all the data, specifically we use the SQL. From HyperSkill academy: ```Everything goes digital these days, and so does money. Today, most people have credit cards, which save us time, energy and nerves. From not having to carry a wallet full of cash to consumer protection, cards make our lives easier in many ways. In this project, you will develop a simple banking system with database.
In this project, you will find out how the banking system works and learn about SQL. We'll also see how Luhn algorithm can help us avoid mistakes when entering the card number. As an overall result, you'll get new experience in Python.```

> banking system,hyperskill,academy,pycharm,bank account,credit card,luhn algorithm,jetbrains

> Gifs and pictures are from Hyperskill's academy. I do not own them.

## Below is an example of the script's usage.
- TO BE ADDED

## Example

```python
# There is a user - friendly menu that handles everything. You just need to insert the desired input.
---
```

### Setup

- You need to import the "sqlite3" module
- You need to import the "random" module
Both are included in the code.


## Features

The script offers the following:
- Gives the opportunity to create an account and shows the credit card number and pin.
  - The credit card number isnt random. The first 6 digits represent a VISA card and the last digit complies with the Luhn Algorithm.
- You can login using the correct credential and:
  - See the balance (default is 0)
  - Transfer money (Handles errors like, sending to yourself, sending to invalid credit card number, or sending more than you have)
  - Close the account (Deletes the account from database)
  - Log out
  

## FAQ

- **How many accounts can I create?**
  - Theoretically, infinite. All acounts are stored to a database with a name "cards3.sdb"
 
- **What is the Luhn Algorithm?**
  - Luhn algorithm is something used by the banks to prevent someone creating random credit cards. In a simplified way the last digit of the card is generated so all 16 digits 
  pass a specific if statement. More info at the link: https://en.wikipedia.org/wiki/Luhn_algorithm

---

## Support


Reach out to me at one of the following places!


---

## Donations (Optional)


---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)
