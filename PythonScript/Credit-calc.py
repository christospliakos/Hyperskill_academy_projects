from math import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str,
                    help="type of payment")
parser.add_argument("--principal", type=float, help="Credit Principal")
parser.add_argument("--periods", type=int, help="Periods for payment")
parser.add_argument("--payment", type=float, help="Monthly payment")
parser.add_argument("--interest", type=float, help="Credit interest")

args = parser.parse_args()


def months(cr_princ_P, mon_paym, cr_inter):
    # cr_princ_P = float(input("Enter credit principal:\n> "))
    # mon_paym = float(input("Enter monthly payment:\n> "))
    # cr_inter = float(input("Enter credit interest:\n >"))
    nomin_inter_i = cr_inter / (12 * 100)
    no_months = ceil(log((mon_paym / (mon_paym - (nomin_inter_i * cr_princ_P))), (1 + nomin_inter_i)))
    years = no_months // 12
    months = no_months % 12
    if years == 0:
        print(f"You need {no_months} to repay this credit!")
    else:
        if months == 0:
            print(f"You need {years} years to repay this credit!")
        else:
            print(f"You need {years} years and {months} months to repay this credit!")
    overpayment = (mon_paym * no_months) - floor(cr_princ_P)
    print(f"Overpayment = {int(overpayment)}")


def annuity_mon_paym(cr_princ_P, count_periods, cr_inter):
    # cr_princ_P = float(input("Enter credit principal:\n> "))
    # count_periods = float(input("Enter count of periods:\n> "))
    # cr_inter = float(input("Enter credit interest:\n >"))
    nomin_inter_i = cr_inter / (12 * 100)
    annuity = cr_princ_P * ((nomin_inter_i * pow((1 + nomin_inter_i), count_periods)) / (
            (pow((1 + nomin_inter_i), count_periods)) - 1))
    print(f"Your annuity payment = {ceil(annuity)}!")
    overpayment = (ceil(annuity) * count_periods) - floor(cr_princ_P)
    print(f"Overpayment = {int(overpayment)}")


def credit_princ(mon_paym, count_periods, cr_inter):
    # mon_paym = float(input("Enter monthly payment:\n> "))
    # count_periods = float(input("Enter count of periods:\n> "))
    # cr_inter = float(input("Enter credit interest:\n >"))
    nomin_inter_i = cr_inter / (12 * 100)
    cred_prin_P = mon_paym / ((nomin_inter_i * pow((1 + nomin_inter_i), count_periods)) / (
            (pow((1 + nomin_inter_i), count_periods)) - 1))
    print(f"Your credit principal = {floor(cred_prin_P)}!")
    overpayment = (mon_paym * count_periods) - floor(cred_prin_P)
    print(f"Overpayment = {int(overpayment)}")


def differentiate_payment(cr_principal, count_periods, cr_inter):
    nomin_inter_i = cr_inter / (12 * 100)
    total_payment = 0
    for i in range(1, count_periods + 1):
        D = (cr_principal / count_periods) + (nomin_inter_i * (cr_principal - ((cr_principal * (i - 1)) / count_periods)))
        print(f"Month {i}: paid out {ceil(D)}")
        total_payment += ceil(D)
    overpayment = total_payment - cr_principal
    print(f"\nOverpayment = {int(overpayment)}")


n_none_args = 0
n_negative = 0
for arg in vars(args):
    if getattr(args, arg) is None:
        n_none_args += 1
    if (getattr(args, arg) is not None) and (arg != "type"):
        if float(getattr(args, arg)) < 0:
            n_negative += 1

if n_none_args > 1:
    print("Incorrect parameters1")
else:
    if args.type != 'diff' and args.type != "annuity":
        print("Incorrect parameters2")
    elif args.type == "diff" and args.payment is not None:
        print("Incorrect parameters3")
    elif args.interest is None:
        print("Incorrect parameters4")
    elif n_negative > 0:
        print("Incorrect parameters5")
    else:
        if args.type == "annuity":
            if args.payment is None:
                annuity_mon_paym(float(args.principal), float(args.periods), float(args.interest))
            elif args.principal is None:
                credit_princ(float(args.payment), float(args.periods), float(args.interest))
            elif args.periods is None:
                months(float(args.principal), float(args.payment), float(args.interest))
        elif args.type == "diff":
            differentiate_payment(float(args.principal), int(args.periods), float(args.interest))
