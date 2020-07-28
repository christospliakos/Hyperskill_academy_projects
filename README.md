# Hyperskill - Jetbrains Academy

> This repository is about HyperSkill academy and specifically the one that involves the "Track: Python Developer". It consists of numerous projects that reflect to the real world. It is not just a python tutorial site, it goes way further in the progress of learning to code properly. With HyperSkill academy you can learn how to write efficient, easy to read and powerfull code using all kind of libraries and new things around python.

> Tags: hyperskill,jetbrains,academy,projects,pycharm,python,tutorial,python developer

> Gifs and pictures are from Hyperskill's academy. I do not own them.

## A brief description for the Python Developer track from Hyperskill:

![Python Developer](https://snipboard.io/JOwohg.jpg)

## Example

```python
# python credit_calc.py --type=diff --principal=500000 --periods=60 --interest=10
---
```

### Setup

- You need to import the "argparse" module. (Included in the code)


## Features

The script displays errors at the following situations:
- You cannot enter negative values.
- You must always input 4 variables (including type)
- You must always input interest. The script can not calculate it.
- Differentiated payments doesn't require a "monthly payment". So this input combination will yield to an error.
- Annuity payments must have 3 variables known and 1 unknown. It could be either principal, periods of payment, monthly payment.

## FAQ

- **What types does the script support?**
    - It supports "--type=diff" and "--type=annuity". If you enter anything else (or leave it blank) it will print an error.
    
- **How many variables do I have to input?**
    - You must always input 4 variables (including type). Anything else will yield to an error.

- **Can you explain the variables?**
    Later one I will add a "helpme" but for now:
     - Periods = Months that you are willing to pay for this principal
     - Principal = the amount of money that you have to repay.
     - Interest = Annual interest of your bank (insert it in decimal. example: 2% interest: --interest=2)
     - Payment = Monthly payment that you are willing to pay.

---

## Support


Reach out to me at one of the following places!


---

## Donations (Optional)




---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)


