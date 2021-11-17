from datetime import date

# symbol: capitalized, 1-7 alpha characters
def symbol(sym=""):
    while True:
        try:
            if sym == "":
                sym = input("Please enter the stock symbol: ")

            if len(sym) >= 1 and len(sym) <= 7:
                if sym.isalpha():
                    if sym.isupper():
                        return sym
                    else:
                        print("Symbol must be all uppercase.")
                        sym = input("Please enter stock symbol: ")
                        continue
                else:
                    
                    print("Symbol must only contain alpha characters (a, b, c, ...)")
                    sym = input("Please enter stock symbol: ")
                    continue

            else:
                print("Symbol must be between 1-7 characters in length.")
                sym = input("Please enter stock symbol: ")
                continue

        except Exception as err:
            print("There has been an error.")
            print(err)
            sym = input("Please enter stock symbol: ")
            continue


# chart type: 1 numeric character, 1 or 2
def chart_type(ct=""):
    while True:
        try:
            if ct == "":
                ct = input("Please select chart type: ")

            try: ct = int(ct)
            except:
                print("Please enter the numbers 1 or 2.")
                ct = input("Please select chart type: ")
                continue

            if ct == 1: return "Line"
            elif ct == 2: return "Bar"
            else:
                print("Please enter either 1 or 2.")
                ct = input("Please select chart type: ")
                continue

        except Exception as err:
            print("There has been an error.")
            print(err)
            ct = input("Please select chart type: ")
            continue


# time series: 1 numeric character, 1 - 4
def time_series(ts=""):
    while True:
        try:
            if ts == "":
                ts = input("Please select time series: ")

            try: ts = int(ts)
            except: 
                print("Please enter the numbers 1, 2, 3, or 4.")
                ts = input("Please select time series: ")
                continue
                
            if ts == 1: return "Intraday"
            elif ts == 2: return "Daily"
            elif ts == 3: return "Weekly"
            elif ts == 4: return "Monthly"
            else: 
                print("Please enter 1, 2, 3, or 4.")
                ts = input("Please select time series: ")
                continue

        except Exception as err:
            print("There has been an error. ")
            print(err)
            ts = input("Please select time series: ")
            continue



# start date: date type YYYY-MM-DD
def start_date(sd=""):
    while True:
        if sd == "":
            sd = input("Please enter start date (YYYY-MM-DD): ")

        try: s_split = sd.split("-")
        except: 
            print("Please enter the date in YYYY-MM-DD format.")
            sd = input("Please enter start date (YYYY-MM-DD): ")
            continue
        if len(s_split[0]) == 4:
            if len(s_split[1]) == 2:
                if len(s_split[2]) == 2:
                    y = int(s_split[0])
                    m = int(s_split[1])
                    d = int(s_split[2])

                    s_date = date(y, m, d)
                    return s_date.strftime('%Y-%m-%d')
                else:
                    print("Please enter the date in YYYY-MM-DD format.")
                    sd = input("Please enter start date (YYYY-MM-DD): ")
                    continue
            else:
                print("Please enter the date in YYYY-MM-DD format.")
                sd = input("Please enter start date (YYYY-MM-DD): ")
                continue
        else:
            print("Please enter the date in YYYY-MM-DD format.")
            sd = input("Please enter start date (YYYY-MM-DD): ")
            continue

# end date: date type YYYY-MM-DD
def end_date(ed=""):
    while True:
        if ed == "":
            ed = input("Please enter end date (YYYY-MM-DD): ")

        try: e_split = ed.split("-")
        except: 
            print("Please enter the date in YYYY-MM-DD format.")
            ed = input("Please enter end date (YYYY-MM-DD): ")
            continue
        if len(e_split[0]) == 4:
            if len(e_split[1]) == 2:
                if len(e_split[2]) == 2:
                    y = int(e_split[0])
                    m = int(e_split[1])
                    d = int(e_split[2])

                    e_date = date(y, m, d)
                    return e_date.strftime('%Y-%m-%d')
                else:
                    print("Please enter the date in YYYY-MM-DD format.")
                    ed = input("Please enter end date (YYYY-MM-DD): ")
                    continue
            else:
                print("Please enter the date in YYYY-MM-DD format.")
                ed = input("Please enter end date (YYYY-MM-DD): ")
                continue
        else:
            print("Please enter the date in YYYY-MM-DD format.")
            ed = input("Please enter end date (YYYY-MM-DD): ")
            continue


def main():
    while True:
        try:
            s = symbol()

            print("Chart Type")
            print("1. Line")
            print("2. Bar\n")

            ct = chart_type()

            print("Time Series")
            print("1. Intraday")
            print("2. Daily")
            print("3. Weekly")
            print("4. Monthly")

            ts = time_series()
            sd = start_date()
            ed = end_date()

            print("The following data will be tested:\n")

            print("Stock Symbol: " + s)
            print("Chart Type: " + ct)
            print("Time Series: " + ts)
            print("Start Date: " + sd)
            print("End date: " + ed)

            repeat = input("\nWould you like to perform another test? (y/n): ")

            if repeat != 'y':
                break

        except Exception as err:
            print("There has been an error.")
            print(err)
            continue

# commented out so unit test can be ran
# main()
