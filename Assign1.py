


## Function that takes in the parameters of Temperature and Windspeed, then calculates the Humidex and windchill accordingly

def tempCheck():
    while True:
        try:

            # Try block that will interpret data input from user and push a value error if input is not acceptable
            test = float(input('Enter a temperature between -50 and 50: '))
            if test < 50 and test > -50:
                try:
                    if test <= 0:
                        # Will begin calculations on winchill
                        print('Calculating windchill.')
                        while True:
                            try:
                                windSpeed = float(input('Enter a wind speed between 1 and 99 km/h: '))


                                ##Begins calculations on windchill
                                if windSpeed >= 1 and windSpeed <= 99:
                                    windChillCalc = 13.12 + 0.6125 * test - 11.37 * windSpeed ** 0.16 + 0.3965 * test * windSpeed ** 0.16
                                    windChill = round(windChillCalc)   ##--> Rounds windchill to whole int

                                    if windChill <= 0 and windChill >= -9:
                                        print(f'The windchill is {windChill}.Low risk.')
                                    elif windChill <= -10 and windChill >= -27:
                                        print(f"The windchill is {windChill}. Moderate risk.")
                                    elif windChill <= -28 and windChill >= -39:
                                        print(f"The windchill is {windChill}. High Risk. Skin can freeze in 10-30 minutes.")
                                    elif windChill < -40:
                                        print(f"The windchill is {windChill}. Very High Risk. Skin can freeze in under 10 minutes.")
                                    else:
                                        print(f"The windchill is {windChill}.")
                                    break
                                else:
                                    print('That wind speed is invalid.')
                            ## if user input is not accaepted it will throw a value-error
                            except ValueError:
                                print('That input is invalid.')
                                continue
                    elif test >= 20:

                        # Will begin calculations on humidex
                        print('Calculating humidex.')
                        while True:
                            try:
                                dewPointCheck = float(input('Enter a dewpoint between -50 and 50: '))
                                ## Begins dewpoint calculations
                                if dewPointCheck < 50 and dewPointCheck > -50 and dewPointCheck <= test:
                                    dewPoint = dewPointCheck
                                    formula = 6.11 * 2.71828 **(5417.7530 * ( 1/273.16 - 1 / (273.16 + dewPoint)))
                                    g = 5/9 * (formula - 10)
                                    humidExCalc = test + g
                                    humidEx = round(humidExCalc)    ##--> Rounds humidex to whole int
                                    if humidEx >= 20 and humidEx <= 29:
                                        print(f"The humidex is {humidEx}. Little or no discomfort.")
                                    elif humidEx >= 30 and humidEx <= 39:
                                        print(f"The humidex is {humidEx}. Some discomfort. ")
                                    elif humidEx >= 30 and humidEx <= 39:
                                        print(f"The humidex is {humidEx}. Great discomfort. Avoid exertion.")
                                    elif humidEx > 45:
                                        print(f"The humidex is {humidEx}. Dangerous. Heat stroke possible.")
                                    else:
                                        print(f"The humidex is {humidEx}.")
                                    break
                                else:
                                    print('That dew point is invalid.')

                            ## if user input is not accepted it will throw a value-error
                            except ValueError:
                                print('That input is invalid.')
                    else:
                        # if the data input is between 0 and 20 it will show the user their input data
                        print("Windchill and humidex are not a factor at this temperature.")
                        return test
                    break
                ## if user input is not accaepted it will throw a value-error
                except ValueError:
                    print('That input is invalid.')
                    continue

            else:
                print('That temperature is invalid.')

        ## if user input is not accaepted it will throw a value-error
        except ValueError:
            print('That input is invalid.')
            continue





##totals function takes data from tempCheck function and prompts the user for data until a certain argument is reached

def totals():
    tempCheck()
    promptUser = ''

    # while loop will continue to run until the user enters n
    while promptUser != 'n':
        promptUser = input('Check another weather condition (Y/N)? ').lower()
        if promptUser == 'y':
            tempCheck()
        elif promptUser == 'n':
            quit()
        else:
            print('That input is invalid.')



totals()
