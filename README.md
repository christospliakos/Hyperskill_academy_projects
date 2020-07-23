# Crecit Calculator

> This credit calculator is a HyperSkill Academy project. Quoting from their site "Finance is an important part of the life of any people. Sometimes you think about getting additional income and want to open a deposit account. And sometimes you need additional money right now and want to take a credit or mortgage. Anyway, you may want to calculate different financial indicators to make a decision. Let’s make such an instrument that can help us."
So this is about a credit calculator that works from a command window through argparse and can calculate annual payments and differentiated payments.

> credit_calculator,annuity,hyperskill,jetbrains,argparse,args,sys,parser,principal,interest

> Gifs and pictures are from Hyperskill's academy. I do not own them.

## Below is an example of the script's usage.

![Demonstration](https://media.giphy.com/media/QXaktIFtVh9ugJ31iA/giphy.gif)

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
    - Later one I will add a "helpme" but for now:
      -- Periods = Months that you are willing to pay for this principal
      -- Principal = the amount of money that you have to repay.
      -- Interest = Annual interest of your bank (insert it in decimal. example: 2% interest: --interest=2)
      -- Payment = Monthly payment that you are willing to pay.

---

## Support

Reach out to me at one of the following places!

- Website at <a href="http://fvcproductions.com" target="_blank">`fvcproductions.com`</a>
- Twitter at <a href="http://twitter.com/fvcproductions" target="_blank">`@fvcproductions`</a>
- Insert more social links here.

---

## Donations (Optional)

- You could include a <a href="https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png" target="_blank">Gratipay</a> link as well.

[![Support via Gratipay](https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png)](https://gratipay.com/fvcproductions/)


---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2015 © <a href="http://fvcproductions.com" target="_blank">FVCproductions</a>.
