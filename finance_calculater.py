import math
def cal ():


    r = .08

    options=["investment", "bond"]
#   interest eraned plus investment
#   interest on bond(morgage)
    print ("investment - to calculate the amount of interest you'll earn on your investment")
    print ("\nbond - the amount you will pay on a home loan")
    opt=input ("enter either 'investment' or 'bond' from the menu above to proceedn or 'done' to finsih:").lower()

# using a while loop to stop any incorrect inputs 



# giving option for user of bonds or investment
    print ("investment - to calculate the amount of interest you'll earn on your investment")
    print ("bond - the amount you will pay on a home loan")
#if used to create a loop
# keeping  if in line to stay in one loop fo invest ment type choice
    try:
        if opt == "investment":
            print ("lets comcapre different investments")
            intt = int(input("pleases enter your inrest rate. please pick a number between 1-10: "))
            v = intt/100
            k= v*100
            print ("\n1:Simple interst; this is", k, "% add to your intail investment each year")
            print ("\n2:Compound interest;", k, "is add to the end balance each year")
            p = int(input("\nplease enter intial investment amount: "))
            t = int(input("please enter the number of years you would like to invest for: "))
            b = p*math.pow((1 +v),t)
            a =p * (1+v*t)
            print ("\nYour simple interest.For",t,  "years is" , a)
            print ("\ncompound interest. For",t, "years is", b)
            user = int(input("\nplease choose '1' for Simple interset or '2' for Compound interst "))
    
        elif user == 1:
                print ("you have chosen Simple Interest at", k,"%", "with an investment peiord of",t,"years")
                print("Intail investment=",p)
                print("Total return=£", a)
    # elif is used to stop python reading each if stament. so reading indivually
        elif user == 2:
            print ("you have chosen compound at", k, "%", "with an investment peiord of",t)
            print ("Intail investment=",p)
            print("Total return =£", b)
        
        elif opt == "bond":
            p=int(input("please enter present value of house"))
            h= int(input("\nplease enter the amount you would like to borrow for your home: "))
            n=int(input("\nPlease enter the length time you need to borrow for in months: "))
            intt = int(input("pleases enter your inrest rate. please pick a number between 1-10: "))
            v=intt/100
            i=v/12
            payment=(i*p)/(1-(1+i)**(-n))
        
            print("\nthe interest per month is", payment)

        elif opt == "done":
             print ("thank you and your options are {}, {}, {}. ".format(user , payment))

        else:
             print ("sorry {} wrong input. ".format(opt))

    except:
         print("incorrect command")
    
             

while True:
     cal()

