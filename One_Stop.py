#Description: Program that allows users to enter and calculate customer insurance policy information
#Date 11/20/2023
#Author: Samantha Thorne

#Import necessary modules
import datetime
import FormatValues as FV

#Assign program constants

NEXT_POL_NUM = 1944
BASIC_PREM_RATE = 869.00
EXTRA_CAR_DISC_RATE = .25
EXTRA_LIAB_RATE = 130.00
GLASS_COV_RATE = 86.00
LOAN_CAR_RATE = 58.00
HST_RATE = .15
PROCESS_FEE_RATE = 39.99 

#Define program functions

def ProvChecker():
    #Checks for valid province among list
    ProvLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NV"]

    while True:
        global Prov 

        Prov = input("Enter the customer's province (XX): ").upper()

        if Prov == "":
            print("Province cannot be blank - please re-enter.")
        elif len(Prov) != 2:
            print("Province must be two characters long - please re-enter.")
        elif Prov not in ProvLst:
            print("Province is invalid - please re-enter.")
        else:
            break




def PayOption():
    #User enters payment choice and downpayment if necessary
    PayOptLst = ["Full", "Monthly", "Down Pay"]
    global PayOpt
    global DownPay
    DownPay = 0.00
    while True:
        PayOpt = input("Enter customers desired payment option (Full, Monthly, or Down Pay): ").title()
        if PayOpt not in PayOptLst:
            print("Payment option must be Full, Monthly or Down Pay - please re-enter.")
        else:
            if PayOpt == "Down Pay":
                while True:
                    try:
                        DownPay = float(input("Enter the down payment amount (###.##): "))   
                    except: 
                        print("Down payment must be entered, using digits and periods only - please re-enter.")
                    else:
                        break
            break




def PrevClaim():
    #Creates a list of previous claims, their dates and costs
    global ClaimDatesLst
    global ClaimAmtLst
    global ClaimAmtDSP
    ClaimDatesLst = ["2021-02-25", "2022-03-15", "2023-08-30"]
    ClaimAmtLst = ["$2,000.00", "$300.00", "$10,000.00"]

    while True:
            ClaimDateStr = input("Enter the previous claim date (YYYY-MM-DD, press ENTER to end): ")
            if ClaimDateStr == "":
                    break
            else:
                ClaimDate = datetime.datetime.strptime(ClaimDateStr, "%Y-%m-%d")
                ClaimDateDSP = datetime.datetime.strftime(ClaimDate,"%Y-%m-%d")
                ClaimDatesLst.append(ClaimDateDSP)

                while True:
                            try:
                                ClaimAmt = float(input("Enter the claim amount (####.##): "))
                                ClaimAmtDSP = FV.FDollar2(ClaimAmt)
                                ClaimAmtLst.append(ClaimAmtDSP)
                            except: 
                                    print("Claim amount must be entered, using digits and periods only - please re-enter.")
                            else:
                                break
    
        
        
            


     


#Start main program

while True:
    
    while True:
        CustFN = input("Enter the customer's first name (Type End to quit): ").title()
        if CustFN == "":
            print("First name cannot be blank - please re-enter.")
        else:
            break

    if CustFN == "End":
            print()
            print("Thank you for choosing One Stop Insurance")
            print()
            break


    while True:
        CustLN = input("Enter the customer's last name: ").title()
        if CustLN == "":
            print("Last name cannot be blank - please re-enter.")
        else:
            break
            
    while True:
        StAdd = input("Enter the customer's street address: ").title()
        if StAdd == "":
            print("Street Address cannot be blank - please re-enter.")
        else:
            break
    
    while True:
        City = input("Enter the customer's city: ").title()
        if City == "":
            print("City cannot be blank - please re-enter.")
        else:
            break


    ProvChecker()

    while True:
        PostCode = input("Enter the customer's postal code (A9A9A9): ").upper()
        PostCodeDSP = PostCode[:3] + " " + PostCode[3:]
        if PostCode == "":
            print("Postal code cannot be blank - please re-enter.")
            PostCodeDSP = PostCode[:3] + " " + PostCode[3:]
        else:
            break
    
    while True:
        PhoneNum = input("Enter the customer's phone number (9999999999): ")
        PhoneNumDSP = "(" + PhoneNum[:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:]
        if PhoneNum == "":
            print("Last name cannot be blank - please re-enter.")
        else:
            break

    while True:   
        try:
            CarNum = int(input("Enter the number of cars being insured: "))
        except:
            print("Number of cars must be entered as digits only - please re-enter.")
        else:
            break

            
    
    while True:
        ExtraLiab = input("Would the customer like extra liability insurance (Y / N): ").upper()
        if ExtraLiab == "":
            print("This question must be answered with a Y or N - Please re-enter")
        else:
            if ExtraLiab == "N":
                ExtraLiabCost = 0
            else:
                ExtraLiabCost = EXTRA_LIAB_RATE
            break

    ExtraLiabCostDSP = FV.FDollar2(ExtraLiabCost)

    while True:
        GlassCov = input("Would the customer like additional glass coverage (Y / N): ").upper()
        if GlassCov == "":
            print("This question must be answered with a Y or N - Please re-enter")
        else:
            if GlassCov == "N":
                GlassCovCost = 0
            else:
                GlassCovCost = GLASS_COV_RATE
            break
    
    GlassCovCostDSP = FV.FDollar2(GlassCovCost)

    while True:
        LoanCar = input("Would the customer like loan car coverage (Y / N): ").upper()
        if LoanCar == "":
            print("This question must be answered with a Y or N - Please re-enter")
        else:
            if LoanCar == "N":
                LoanCarCost = 0
            else:
                LoanCarCost = LOAN_CAR_RATE
            break

    LoanCarCostDSP = FV.FDollar2(LoanCarCost)

    PayOption()

    PrevClaim()

    FullName = CustFN + " " + CustLN

    ExtraCars = CarNum - 1

    CarDisc = ExtraCars * BASIC_PREM_RATE * EXTRA_CAR_DISC_RATE
    CarDiscDSP = FV.FDollar2(CarDisc)

    InsurePrem = BASIC_PREM_RATE * CarNum - CarDisc
    InsurePremDSP = FV.FDollar2(InsurePrem)

    ExtraCosts = ExtraLiabCost + GlassCovCost + LoanCarCost
    ExtraCostsDSP = FV.FDollar2(ExtraCosts)

    TotInsurePrem = InsurePrem + ExtraCosts
    TotInsurePremDSP = FV.FDollar2(TotInsurePrem)

    Hst = TotInsurePrem * HST_RATE
    HstDSP = FV.FDollar2(Hst)

    TotCost = TotInsurePrem + Hst
    TotCostDSP = FV.FDollar2(TotCost)

    if PayOpt == "Full":
        MonthPayDSP = "Paid Off"
    else:
        MonthPay = (PROCESS_FEE_RATE + (TotCost-DownPay)) / 8
        MonthPayDSP = FV.FDollar2(MonthPay)
    
    DownPayDsp = FV.FDollar2(DownPay)

    InvoiceDate = datetime.datetime.now()

    NewMonth = int(InvoiceDate.month) + 1

    NewYear = int(InvoiceDate.year) + 1

    if InvoiceDate.month != 12: #December is the only month that will change the year
        FirstPayDate = str(InvoiceDate.year) + "-" + str(NewMonth) + "-01"
    else:
        FirstPayDate = str(NewYear) + "-01-01"

    

    print()
    print()
    print(f"                       One Stop Insurance Company")
    print(f"                             124 Fiscal Ave")
    print(f"                         St John's, Nl, A2H 7Z3")
    print(f"                           INSURANCE RECEIPT:")
    print()
    print(f"----------------------------------------------------------------------")
    print()
    print(f"   {NEXT_POL_NUM}")
    print(f"   {FullName:<25s}          Cars Insured:              {CarNum:>2d}")
    print(f"   {StAdd:<25s}          Extra Liability Coverage:   {ExtraLiab:<1s}")
    print(f"   {City:<15s}, {Prov:<2s}, {PostCodeDSP:<7s}       Glass Coverage:             {GlassCov:<1s}")
    print(f"   {PhoneNumDSP:<14s}                     Loan Car Coverage:          {LoanCar:<1s}")
    print()
    print(f"----------------------------------------------------------------------")
    print()

    print(f"                           Extra Car Discount (25%):     {CarDiscDSP:>10s}")
    print(f"                           Insurance Premium:            {InsurePremDSP:>10s}")
    print(f"                           ----------------------------------------")
    print(f"                           Extra Liability Coverage:     {ExtraLiabCostDSP:>10s}")
    print(f"                           Glass Coverage:               {GlassCovCostDSP:>10s}")
    print(f"                           Loan Car Coverage:            {LoanCarCostDSP:>10s}")
    print(f"                           ----------------------------------------")
    print(f"                           Total Insurance Premium:      {TotInsurePremDSP:>10s}")
    print(f"                           HST (15%):                    {HstDSP:>10s}")
    print(f"                           Total Cost:                   {TotCostDSP:>10s}")
    print()
    print(f"                           Down Payment:                 {DownPayDsp:>10s}")
    print(f"                           Monthly Payment:              {MonthPayDSP:>10s}")
    print()
    print(f"----------------------------------------------------------------------")
    print(f"   Invoice Date: {InvoiceDate:<10s}   First Payment Due: {FirstPayDate:<10s}")
    print()
    print(f"                              Past Claims")
    print()
    print(f"                  Claim #   Claim Date      Amount")
    print(f"                  --------------------------------")
    
    ClaimNum = 1
    for claim in ClaimDatesLst:

        ClaimAmt = ClaimAmtLst[ClaimNum-1]

        print(f"                   {ClaimNum:>2d}.      {claim:<10s}  {ClaimAmt:>10s}")

        ClaimNum += 1
    
    print()
    print()






    
