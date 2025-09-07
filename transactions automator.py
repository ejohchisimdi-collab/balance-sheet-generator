assets=[]
asset2=[]
liabilities=[]
liabilities2=[]
equity=[]
equity2=[]
revenue=[]
revenue2=[]
expenses=[]
expenses2=[]


while True:
    userChoice=input("Enter\n "
                     "a: to input assets\n"
                     "l: to input liabilities\n"
                     "eq: to input equity\n"
                     "r: to input revenue\n"
                     "ex: to input expenses\n"
                     "f: for final results")

    if userChoice.lower().strip()=="a":
        while True:
            assetsDescription= input("enter description of things owned by the buisness(press q to quit): ")
            if assetsDescription.lower().strip()=="q":
                break
            else:
                assetsPrice=float(input(f"enter price of {assetsDescription} : "))
                assets.append(assetsDescription)
                asset2.append(assetsPrice)


    elif userChoice.lower().strip()=="eq":
        while True:
            equityDescription = input("enter description of owner shares in buisness(press q to quit): ")
            if equityDescription.lower().strip() == "q":
                break
            else:
                equityPrice = float(input(f"enter price of {equityDescription} : "))
                equity.append(equityDescription)
                equity2.append(equityPrice)
    elif userChoice.lower().strip()=="r":
        while True:
            revenueDescription = input("enter description of money earned by the buisness(press q to quit): ")
            if revenueDescription.lower().strip() == "q":
                break
            else:
                revenuePrice = float(input(f"enter price of {revenueDescription} : "))
                revenue.append(revenueDescription)
                revenue2.append(revenuePrice)
    elif userChoice.lower().strip()=="ex":
        while True:
            expensesDescription = input("enter description of expenses incured by the buisness(press q to quit): ")
            if expensesDescription.lower().strip() == "q":
                break
            else:
                expensesPrice = float(input(f"enter price of {expensesDescription} : "))
                expenses.append(expensesDescription)
                expenses2.append(expensesPrice)
    elif userChoice.lower().strip()=="l":
        while True:
            liabilitiesDescription = input("enter description of liabilities of the buisness(press q to quit): ")
            if liabilitiesDescription.lower().strip() == "q":
                break
            else:
                liabilitiesPrice = float(input(f"enter price of {liabilitiesDescription} : "))
                liabilities.append(liabilitiesDescription)
                liabilities2.append(liabilitiesPrice)
    elif userChoice.lower().strip()=="f":
        while True:
            def assetsf():
                print("assets: ")
                for items,prices in zip(assets, asset2):
                    print(f"{items}: {prices:}")
            def equityf():
                print("equity: ")
                for items,prices in zip(equity, equity2):
                 print(f"{items}: {prices:}")

            def revenuef():
                print("revenue: ")
                for items,prices in zip(revenue, revenue2):
                    print(f"{items}: {prices:}")
            def liabilitiesf():
                print("liabilities: ")
                for items,prices in zip(liabilities, liabilities2):
                    print(f"{items}: {prices:}")

            def expensesf():
                print("expenses: ")
                for items,prices in zip(expenses, expenses2):
                    print(f"{items}: {prices:}")

            totalasset = sum(asset2)
            totalequity = sum(equity2)
            totalrevenue = sum(revenue2)
            totalliabilities = sum(liabilities2)
            totalexpenses = sum(expenses2)




            print("---------Balance Sheet----------")
            print("debit")
            assetsf()
            print("--------------")
            expensesf()
            print("-----------------")

            print("credit")
            liabilitiesf()
            print("-----------------")
            revenuef()
            print("-----------------")
            equityf()
            print("-----------------")

            print("balance")
            balance=(totalliabilities+totalrevenue+totalequity)-(totalasset+totalexpenses)
            if balance>0:
                print(f"debit balance:{balance}")
            elif balance==0:
                print("account is balance")
            elif balance<0:
                print(f"credit balance:{balance}")



            x=input("\npress q to quit")
            if x.lower().strip()=="q":
                break
