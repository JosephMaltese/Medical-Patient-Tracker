from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file. Each line in the file stores a list of values separated by a comma.
    The first element on each line is the patient ID, and the rest of the elements contain information regarding the
    visit. Returns a dictionary with the key being the patient ID and the corresponding value being a two-dimensional
    list containing sub-lists that store data from each visit.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    # Defines a dictionary variable that will store each patient ID and the data associated with their corresponding
    # visits.
    patients = {}

    # try-except statement which attempts to open a text file, and catches any IOError that occurs when trying to open
    # the file.
    try:
        # Uses with to open a given text file, read from it, and eventually close it when finished. Names the file
        # object as readFile.
        with open(fileName, 'r') as readFile:
            # Try statement meant to catch any unprecedented errors that occur when reading from the file.
            try:
                # Reads the first line from the file and stores it in a string variable, currentLine.
                currentLine = readFile.readline()

                # While loop which repeats as long as the current line in the file is not an empty string (the end of
                # the file has not been reached).
                while currentLine != '':

                    # Strips the whitespace character \n from the end of the current line.
                    currentLine = currentLine.strip()
                    # Stores the original line as a string in a new variable, originalLineString
                    originalLineString = currentLine
                    # Splits each element of the current line string into a list using the comma as a delimiter. The
                    # variable currentLine, which was previously a string, is now a list variable.
                    currentLine = currentLine.split(',')

                    # Checks if the correct number of elements exist within the list. After the split, there should be
                    # 8 different elements. Otherwise, there is an invalid number of fields in the line and something
                    # is therefore incorrect in the data file.
                    if len(currentLine) != 8:
                        # Prints a message to the user saying there is an incorrect number of fields in the current line
                        print('Invalid number of fields (%d) in line: %s' % (len(currentLine), originalLineString))
                        # Reads the next line in the file.
                        currentLine = readFile.readline()
                        # Proceeds to the start of the while loop.
                        continue

                    # Additional try statement which attempts to convert each element within the currentLine list into
                    # its correct data type. If any ValueError occurs when trying to do this, this means that the
                    # corresponding element within the list was not of the correct data type, and this exception will
                    # be handled.
                    try:
                        # Converts each element within the list (which are currently all string variables) into their
                        # corresponding data type.
                        currentLine[0] = int(currentLine[0])
                        currentLine[2] = float(currentLine[2])
                        currentLine[3] = int(currentLine[3])
                        currentLine[4] = int(currentLine[4])
                        currentLine[5] = int(currentLine[5])
                        currentLine[6] = int(currentLine[6])
                        currentLine[7] = int(currentLine[7])

                        # Creates a list variable that is used to check if the date was given in the correct format by
                        # splitting the date string using '-' as a delimiter.
                        checkDate = currentLine[1].split('-')

                        # If statement which checks to see if the date was given in the wrong format. The first element
                        # of the date should be the year, and should be 4 characters long. The second element should
                        # be the month, so it should be 2 characters long. The third element should be the day, so it
                        # should also be 2 characters. Also, all elements should contain only numeric characters. If
                        # any of these conditions are false, this branch will execute.
                        if len(checkDate[0]) != 4 or checkDate[0].isdigit() == False or len(checkDate[1]) != 2 or checkDate[1].isdigit() == False or len(checkDate[2]) != 2 or checkDate[2].isdigit() == False:
                            # Reads the next line in the file.
                            currentLine = readFile.readline()
                            # Moves to the start of the while loop.
                            continue

                        # If the month is greater than 12 or the day is greater than 31, moves on to the next line
                        # and starts at the top of the while loop.
                        if int(checkDate[1]) > 12 or int(checkDate[2]) > 31:
                            currentLine = readFile.readline()
                            continue

                    # Catches any ValueErrors that occur when trying to convert each element of the currentLine list
                    # into their corresponding data types.
                    except:
                        # Tells the user that invalid data was found on the current line
                        print("Invalid data type in line: %s" % originalLineString)
                        # Reads the next line
                        currentLine = readFile.readline()
                        # Moves to the start of the while loop.
                        continue

                    # If statement which executes if the given temperature is not between the range of 35 to 42.
                    if currentLine[2] < 35 or currentLine[2] > 42:
                        # Tells the user that the temperature on the given line is invalid.
                        print(f"Invalid temperature value (%.2f) in line: %s" % (currentLine[2], originalLineString))
                        # Reads the next line of the file and moves to the start of the while loop.
                        currentLine = readFile.readline()
                        continue
                    # If statement which executes if the given heart rate is not between the range of 30 to 180.
                    if currentLine[3] < 30 or currentLine[3] > 180:
                        # Tells the user that the heart rate on the given line is invalid.
                        print(f"Invalid heart rate value ({currentLine[3]}) in line: {originalLineString}")
                        # Reads the next line of the file and moves to the start of the while loop.
                        currentLine = readFile.readline()
                        continue
                    # If statement which executes if the given respirator rate is not between the range of 5 to 40.
                    if currentLine[4] < 5 or currentLine[4] > 40:
                        # Tells the user that the respiratory rate on the given line is invalid.
                        print("Invalid respiratory rate value (%d) in line: %s" % (currentLine[4], originalLineString))
                        # Reads the next line of the file and moves to the start of the while loop.
                        currentLine = readFile.readline()
                        continue
                    # If statement which executes if the given systolic blood pressure is not between the range of 70
                    # to 200.
                    if currentLine[5] < 70 or currentLine[5] > 200:
                        # Tells the user that the systolic blood pressure on the given line is invalid.
                        print("Invalid systolic blood pressure value (%d) in line: %s" % (currentLine[5], originalLineString))
                        # Reads the next line of the file and moves to the start of the while loop.
                        currentLine = readFile.readline()
                        continue
                    # If statement which executes if the given diastolic blood pressure is not between the range of 40
                    # to 120.
                    if currentLine[6] < 40 or currentLine[6] > 120:
                        # Tells the user that the diastolic blood pressure on the given line is invalid.
                        print("Invalid diastolic blood pressure value (%d) in line: %s" % (currentLine[6], originalLineString))
                        # Reads the next line of the file and moves to the start of the while loop.
                        currentLine = readFile.readline()
                        continue
                    # If statement which executes if the given oxygen saturation is not between the range of 70 to 100.
                    if currentLine[7] < 70 or currentLine[7] > 100:
                        # Tells the user that the oxygen saturation on the given line is invalid.
                        print("Invalid oxygen saturation value (%d) in line: %s" % (currentLine[7], originalLineString))
                        # Reads the next line of the file and moves to the start of the while loop.
                        currentLine = readFile.readline()
                        continue

                    # Creates a list variable to store the data from each visit. This list will be added to the
                    # dictionary storing patient information under the key which corresponds to the patient.
                    listToAdd = []

                    # For loop which iterates 7 times. Adds the patients data relating to their visit to the list
                    # variable. Does not add the element in index position 0, as this corresponds to the patient ID,
                    # and it will instead be used as a key within the dictionary.
                    for i in range(1, len(currentLine)):
                        # Appends the ith element of the data to the list variable.
                        listToAdd.append(currentLine[i])

                    # If a key corresponding to the patient ID of the current line does not exist in the patients
                    # dictionary, then a key will be created.
                    if int(currentLine[0]) not in patients:
                        # Creates a key corresponding to the patient ID on the current line and makes its associated
                        # value an empty list.
                        patients[int(currentLine[0])] = []
                        # Appends the list of data from the visit on the current line to the list associated with the
                        # patient ID key.
                        patients[int(currentLine[0])].append(listToAdd)
                    # This branch executes if a key already does exist for the patient ID of the current line.
                    else:
                        # Appends the list of data from the visit to the list associated with the patient ID key.
                        patients[int(currentLine[0])].append(listToAdd)

                    # Reads the next line of the file.
                    currentLine = readFile.readline()

            # Except statement which tells the user that an unexpected error occurs
            except:
                print("An unexpected error occurred while reading the file.")
                # Reads the next line of the file.
                currentLine = readFile.readline()

    # Except statement which deals with any error that occurs when trying to open the file.
    except IOError:
        # Tells the user that the file could not be found
        print("The file '%s' could not be found." % fileName)
        # Exits the program.
        exit()
    # At the end of the function, the patients dictionary is returned, storing all of the data associated with each
    # visit for each patient.
    return patients


def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID. If the patient ID is equal to 0, displays data for all patients. If
    given a patient ID, the function will display the data for that patient. Data includes visit date, temperature,
    heart rate, respiratory rate, systolic blood pressure, diastolic blood pressure, and oxygen saturation.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """

    # If the patientId argument is equal to 0, this branch will execute.
    if patientId == 0:
        # For loop which iterates through each key in the patients dictionary.
        for patient in patients:
            # prints the key (patient ID)
            print('Patient ID: %s' % patient)
            # For loop which iterates through each visit.
            for visit in patients[patient]:
                # Prints out all the data from the visit.
                print(" Visit Date:", visit[0])
                print("  Temperature:", "%.2f" % visit[1], "C")
                print("  Heart Rate: %d bpm" % visit[2])
                print("  Respiratory Rate: %d bpm" % visit[3])
                print("  Systolic Blood Pressure: %d mmHg" % visit[4])
                print("  Diastolic Blood Pressure: %d mmHg" % visit[5])
                print("  Oxygen Saturation: %d %%" % visit[6])

    # This branch will execute if patientId is not equal to 0.
    else:
        # Try statement which tries to access the value associated with the given key.
        try:
            # Creates a variable, patientVisits, that stores the value (all the visit information) associated with
            # the given key.
            patientVisits = patients[patientId]

            # Prints out the patient ID
            print('Patient ID: %d' % patientId)

            # For loop which iterates through each sublist (visit) within the list that stores all the patient's visits.
            for visit in patientVisits:
                # Prints out the data associated with the given visit. The 0th element in the sublist visit will be the
                # visit date, followed by the temperature, heart rate, respiratory rate, systolic blood pressure,
                # diastolic blood pressure, and then oxygen saturation.
                print(" Visit Date:", visit[0])
                print("  Temperature:", "%.2f" % visit[1], "C")
                print("  Heart Rate: %d bpm" % visit[2])
                print("  Respiratory Rate: %d bpm" % visit[3])
                print("  Systolic Blood Pressure: %d mmHg" % visit[4])
                print("  Diastolic Blood Pressure: %d mmHg" % visit[5])
                print("  Oxygen Saturation: %d %%" % visit[6])
        # Except statement which catches and deals with any key error that occurs when trying to access the value
        # associated with the key given by the user.
        except KeyError:
            # Print statement which tells the user that the key was invalid.
            print( "Patient with ID %d not found." % patientId)


def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient. If patientId is an integer, the
    function will display the average vital signs for that specified patient. Otherwise, if patientId is 0, it will
    the average vital signs for all the patients combined. If the patientId is not found, an error message will be
    printed and the function will end.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """

    # Declare variables that will be used to store the sum of each medical statistic. Initializes the sum of each to 0.
    temp_sum = 0
    heart_sum = 0
    respiratory_sum = 0
    systolic_sum = 0
    diastolic_sum = 0
    oxygen_sum = 0
    # Declare variable which will be used in computing the averages of the statistics.
    num_visits = 0

    # Declares a boolean variable that will be used to determine whether to proceed with the function based on if the
    # given patient ID is valid and if the first argument in the function is given as a dictionary.
    valid = True
    # Declares a boolean variable which will be used to determine whether the average values should be calculated and
    # printed, so that an error does not occur.
    validToPrint = True

    # Try statement which attempts to convert the given patient ID, which is initially a string, into an integer.
    try:
        patientId = int(patientId)
    # This except branch executes if the patientId cannot be converted to an integer, meaning it is invalid.
    except:
        # Tells the user that they gave invalid input.
        print("Error: 'patientId' should be an integer.")
        # Sets valid equal to false, since patientId is not an integer value.
        valid = False

    # Checks if the first argument of the function (patients), is given as a dictionary variable.
    if type(patients) != dict:
        # If patients is not a dictionary, then valid will be set to false.
        valid = False
        # Tells the user that the given argument is not valid.
        print("Error: 'patients' should be a dictionary.")

    # If patientId was successfully converted to an integer and patients is a dictionary, this branch will execute.
    # Otherwise, the function ends.
    if valid:
        # This branch executes if the given patient ID is equal to 0, meaning they want to see the average vital signs
        # for all patients.
        if patientId == 0:
            print("Vital Signs for All Patients:")
            # For loop that iterates through every key in the dictionary.
            for patient in patients:
                # For loop that iterates through every sublist in the list associated with the current key in the
                # dictionary.
                for visit in patients[patient]:
                    # Increments the number of visits by 1 to keep count of each visit.
                    num_visits += 1
                    # Adds the data from the visit to its corresponding sum variable. These variables keep track of
                    # the total of each statistic. The temperature is found in index position 1 in visit since the date
                    # is in the 0th position.
                    temp_sum += visit[1]
                    heart_sum += visit[2]
                    respiratory_sum += visit[3]
                    systolic_sum += visit[4]
                    diastolic_sum += visit[5]
                    oxygen_sum += visit[6]
        # This branch executes if the given patientId is not equal to 0.
        else:
            # Try statement which tries to access the value associated with the given key.

            try:
                # Creates a variable, patientVisits, that stores the value (all the visit information) associated with
                # the given key (patientId).
                patientVisits = patients[patientId]
                print('Vital Signs for Patient %d:' % patientId)

                # For loop that iterates through each sublist (visit) in the list of the patient's data.
                for visit in patientVisits:
                    # Increments the number of visits by 1. Keeps track of each visit.
                    num_visits += 1
                    # Adds the data from each of the patient's visits to their corresponding sum variable.
                    temp_sum += visit[1]
                    heart_sum += visit[2]
                    respiratory_sum += visit[3]
                    systolic_sum += visit[4]
                    diastolic_sum += visit[5]
                    oxygen_sum += visit[6]
            # Catches any key error that occurs when trying to access the value (list) associated with the key given
            # by the user. Key error occurs if the user provides a key that does not exist in the given dictionary.
            except KeyError:
                # Tells the user that the given key was invalid.
                print(f"No data found for patient with ID {patientId}.")
                # Since the input was invalid, validToPrint is set to false so that the function does not try to
                # compute the averages and print them.
                validToPrint = False

        # Executes if all the given information is valid and thus no errors occurred.
        if validToPrint:
            # Calculates and prints the average temperature, heart rate, respiratory rate, systolic blood pressure,
            # diastolic blood pressure, and oxygen saturation, to two decimal places. To calculate the average of a
            # statistic, the sum of all the data for that stat is divided by the number of visits counted. If the user
            # provided the ID of a single patient, num_visits will equal the total number of visits from that patient,
            # otherwise it will be equal to the total number of visits by all patients.
            print(" Average temperature:", "%.2f" % (temp_sum / num_visits), "C")
            print(" Average heart rate:", "%.2f" % (heart_sum / num_visits), "bpm")
            print(" Average respiratory rate:", "%.2f" % (respiratory_sum / num_visits), "bpm")
            print(" Average systolic blood pressure:", "%.2f" % (systolic_sum / num_visits), "mmHg")
            print(" Average diastolic blood pressure:", "%.2f" % (diastolic_sum / num_visits), "mmHg")
            print(" Average oxygen saturation:", "%.2f" % (oxygen_sum / num_visits), "%")


def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list. This function takes the user input as parameters. It checks the input
    and then puts it into a list that gets added to the patients dictionary. If the patient already exists in the
    dictionary, then the data gets appended to the list of existing visits for that patient. Otherwise, a key is created
    for that patient and then the corresponding data is added. Then, if successful, this text file is rewritten, now
    including the added patient data.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    # Boolean variable used to determine whether data is valid.
    valid = True

    # Try statement that attempts to add the patient data and write it to the file, and catches any unforeseen errors.
    try:
        # Try statement which tries to split the date string into a list using '-' as a delimiter. Splits twice since
        # there should be two '-' in the date.
        try:
            checkDate = date.split('-', 2)
        # Catches any error that occurs when trying to split the date. An error will occur if there is no '-' in the
        # date.
        except:
            # Tells the user that the given date is invalid.
            print("Invalid date format. Please enter date in the format ‘yyyy-mm-dd’.")
            # Sets valid to false since input is not valid.
            valid = False
        # If no error occurs, this branch executes. Continues to check if the date is valid.
        else:
            # Checks if the year contains non-numeric digits or is not 4 characters in length.
            if len(checkDate[0]) != 4 or checkDate[0].isdigit() == False:
                # If either of those conditions are true, tells the user that the date is invalid.
                print("Invalid date format. Please enter date in the format ‘yyyy-mm-dd’.")
                valid = False
            # Checks if the month contains non - numeric digits or is not 2 characters in length.
            elif len(checkDate[1]) != 2 or checkDate[1].isdigit() == False:
                # If either of those conditions are true, tells the user that the date is invalid.
                print("Invalid date format. Please enter date in the format ‘yyyy-mm-dd’.")
                valid = False
            # Checks if the day contains non - numeric digits or is not 2 characters in length.
            elif len(checkDate[2]) != 2 or checkDate[2].isdigit() == False:
                # If either of those conditions are true, tells the user that the date is invalid.
                print("Invalid date format. Please enter date in the format ‘yyyy-mm-dd’.")
                valid = False
            # If none of the previous branches executed, then this branch will execute. This branch will check if the
            # date given is reasonable, meaning that the year is any year after 1900, the given month is a number from
            # 1 to 12, and the day is a number between 1 and 31.
            else:
                # Checks if the given year is before 1900, which is invalid.
                if int(checkDate[0]) < 1900:
                    # Tells the user that the date is invalid.
                    print("Invalid date. Please enter a valid date.")
                    valid = False
                # Checks if the month is not in the range 1 - 12, which is invalid.
                elif int(checkDate[1]) < 1 or int(checkDate[1]) > 12:
                    # Tells the user that the date is invalid.
                    print("Invalid date. Please enter a valid date.")
                    valid = False
                # Checks if the day is not in the range 1-31, which is invalid.
                elif int(checkDate[2]) < 1 or int(checkDate[2]) > 31:
                    # Tells the user that the date is invalid.
                    print( "Invalid date. Please enter a valid date.")
                    valid = False
        # If none of the previous branches executed, then the date is valid. The function will now check all the other
        # values.
        if valid:
            # Checks if the temperature is not between 35 and 42, which is invalid.
            if temp < 35.0 or temp > 42.0:
                # Tells the user that the given temperature is not valid.
                print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
                valid = False
            # Checks if the heart rate is not between 30 and 180, which is invalid.
            elif hr < 30 or hr > 180:
                # Tells the user that the given heart rate is not valid.
                print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
                valid = False
            # Checks if the respiratory rate is not between 5 and 40, which is invalid.
            elif rr < 5 or rr > 40:
                # Tells the user that the given respiratory rate is not valid.
                print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
                valid = False
            # Checks if the systolic blood pressure is not between 70 and 200, which is invalid.
            elif sbp < 70 or sbp > 200:
                # Tells the user that the given systolic blood pressure is not valid.
                print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
                valid = False
            # Checks if the diastolic blood pressure is not between 40 and 120, which is invalid.
            elif dbp < 40 or dbp > 120:
                # Tells the user that the given diastolic blood pressure is not valid.
                print( "Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
                valid = False
            # Checks if the oxygen concentration is not between 70 and 100, which is invalid.
            elif spo2 < 70 or spo2 > 100:
                # Tells the user that the given oxygen concentration is not valid.
                print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
                valid = False

        # If all the data given is valid, then this branch will execute.
        if valid:
            # Creates a list variable with all the given data
            listToAppend = [date, temp, hr, rr, sbp, dbp, spo2]

            # If the given patientId is already in the given dictionary, this branch executes. It will append the list,
            # listToAppend to the list that exists containing that patient's visits.
            if patientId in patients:
                patients[patientId].append(listToAppend)
            # If the given patientId is not in the given dictionary, this branch executes. It will create a new key in
            # the dictionary with the value patientId and set it equal to an empty list (the list of the patient's
            # visits). It then appends listToAppend to this list.
            else:
                patients[patientId] = []
                patients[patientId].append(listToAppend)

            # Uses with command to open the given file as writeFile, write to it, and then close it when finished.
            with open(fileName, 'w') as writeFile:
                # For loop that iterates through each key in the dictionary.
                for patient in patients:
                    # For loop that loops through each sublist in the list value associated with the current key in the
                    # dictionary.
                    for visit in patients[patient]:
                        # Converts each piece of data within the sublist into a string, and writes it onto the same line
                        # of the file, separated by a comma. This corresponds to the information for one visit.
                        writeFile.write(str(patient))
                        writeFile.write(',')
                        writeFile.write(str(visit[0]))
                        writeFile.write(',')
                        writeFile.write(str(visit[1]))
                        writeFile.write(',')
                        writeFile.write(str(visit[2]))
                        writeFile.write(',')
                        writeFile.write(str(visit[3]))
                        writeFile.write(',')
                        writeFile.write(str(visit[4]))
                        writeFile.write(',')
                        writeFile.write(str(visit[5]))
                        writeFile.write(',')
                        writeFile.write(str(visit[6]))
                        # Uses \n to go to the next line of the file when printing the information for the next visit.
                        writeFile.write('\n')
            # At the end, tells the user that the data has been saved.
            print("Visit is saved successfully for Patient # %d" % patientId)
    # Catches any unprecedented errors that occur.
    except:
        print("An unexpected error occurred while adding new data.")


def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both. A month and year can be given, and the data corresponding data will be
    returned. Just a month cannot be given, this will return an empty list. Just a year can be given, and all the visits
    in that year will be returned. Also, if no month or year is given, all the visits will be returned. This function
    returns a list containing tuples. Each tuple consists of the patient ID, and a list containing the visit information
    such as date, temperature, etc.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    # Creates a list variable that will store all the information for the given year / month. The list will be a list
    # of tuples. Each tuple will contain the patient ID as an integer and a list containing the information regarding
    # the visit.
    visits = []

    # Boolean variable used when determining if the given year is valid.
    valid = True

    # If no year is given, but a month is given, function returns an empty list, as this is invalid.
    if year == None and month != None:
        return visits
    # If a year is given, but not a month, this branch executes. Displays visits for all months in the given year.
    elif year != None and month == None:
        # If the year is invalid (less than 1900), this branch will execute.
        if year < 1900:
            valid = False
        # If the year given is valid, this branch will execute.
        if valid:
            # Iterates through each key in the dictionary.
            for patient in patients:
                # Iterates through each sublist in the list value associated with the current key in the dictionary.
                for visit in patients[patient]:
                    # If the length of the date is 10 characters, this branch executes.
                    if len(visit[0]) == 10:
                        # Splits the date string into a list using '-' as the delimiter.
                        visitDate = visit[0].split('-')
                        # If the year in the visit is equal to the year given by the user, then this branch executes.
                        if year == int(visitDate[0]):
                            # Creates a tuple which stores the patientId, and the list of data regarding the visit.
                            visitInGivenDate = (patient, visit)
                            # Appends this tuple to the list of visits containing all information for the given year.
                            visits.append(visitInGivenDate)
    # This branch executes if a year and month are both given. Displays data for visits in that year and month.
    elif year != None and month != None:
        # If the given year is less than 1900, which is invalid, this branch executes.
        if year < 1900:
            valid = False
        # If the given month is less than 1 or greater than 12, the month is invalid, and this branch executes.
        if month < 1 or month > 12:
            valid = False
        # If the given year and month are valid, this branch executes.
        if valid:
            # Loops through each key in the dictionary.
            for patient in patients:
                # Loops through each sublist in the list value that corresponds to the current key in the dictionary.
                for visit in patients[patient]:
                    # If the length of the date is 10 characters, this branch executes.
                    if len(visit[0]) == 10:
                        # Splits the date using '-' as delimiter.
                        visitDate = visit[0].split('-')
                        # If the year in the current sublist is equal to the given year and the month in the current
                        # sublist is equal to the given month, then this branch executes.
                        if year == int(visitDate[0]) and month == int(visitDate[1]):
                            # Creates a tuple storing the patient ID and the visit information.
                            visitInGivenDate = (patient, visit)
                            # Appends the tuple to the list of visits.
                            visits.append(visitInGivenDate)
    # This branch executes if no year or month are given. Displays the visits for every month in every year.
    else:
        # Loops through each key in the dictionary.
        for patient in patients:
            # Loops through each sublist in the list value associated with the current key in the dictionary.
            for visit in patients[patient]:
                # If the length of the date string is equal to 10, this branch executes.
                if len(visit[0]) ==  10:
                    # Creates tuple with patient ID and list of the visit information.
                    visitInGivenDate = (patient,visit)
                    # Appends this tuple to the list of visits.
                    visits.append(visitInGivenDate)
    # Returns the list of visits.
    return visits


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs. This function looks at the vital signs of the
    patients (specifically, heart rate, systolic blood pressure, diastolic blood pressure, and oxygen saturation level),
    and determines if these values are abnormal. If any of these values are out of the normal ranges for a patient, then
    they are added to a list of patients who require follow-ups. This function will return the list of patients who
    require a follow-up visit.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits due to abnormal health stats.
    """
    # List variable which will store patient IDs for those that require follow-up visits.
    followup_patients = []

    # Iterates through each key in the dictionary.
    for patient in patients:
        # Iterates through each sublist in the list value associated with the current key in the dictionary.
        for visit in patients[patient]:
            # Boolean variable used to determine whether the patient requires a follow-up.
            followUpNeeded = False
            # If the heart rate (the value in index position 0 of the visit list) is greater than 100 or less than 60,
            # this branch executes.
            if visit[2] > 100 or visit[2] < 60:
                # A follow-up is required.
                followUpNeeded = True
            # If systolic is greater than 140, this branch executes.
            elif visit [4] > 140:
                # A follow-up is required.
                followUpNeeded = True
            # If diastolic is greater than 90, this branch executes.
            elif visit[5] > 90:
                # A follow-up is required.
                followUpNeeded = True
            # If oxygen saturation is less than 90, this branch executes.
            elif visit[6] < 90:
                # A follow-up is required.
                followUpNeeded = True

            # If followUpNeeded is True, this branch executes.
            if followUpNeeded:
                # If the patient is not already in the list of follow-up patients, they are added to it.
                if patient not in followup_patients:
                    followup_patients.append(patient)
    # Returns the list of patients who require follow-ups.
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient. This function uses the pop() method to remove all visits of a particular
    patient from the patients dictionary. It removes both the key and its associated list for the given patient. Then,
    the textfile is re-written, exluding the visit information for that patient. Since the data no longer exists in the
    dictionary, it will also not be written to the file.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """

    # Try statement that attempts to remove the given key (patientId) and its associated value from the dictionary.
    try:
        patients.pop(patientId)

        # This section of code rewrites the file now that the patient data has been removed from the dictionary. Uses
        # with to open the file for writing as writeFile, write to it, and then close it when finished.
        with open(filename, 'w') as writeFile:
            # Loops through each key in dictionary.
            for patient in patients:
                # Loops through each sublist in the list value associated with the current key in the dictionary.
                for visit in patients[patient]:
                    # Writes out each piece of data relating to the current visit on the same line, separated by commas.
                    # Writes the patient ID first, followed by the date, which is in the 0th position of the visit list,
                    # and so on. Converts each value to a string before writing it to the file.
                    writeFile.write(str(patient))
                    writeFile.write(',')
                    writeFile.write(str(visit[0]))
                    writeFile.write(',')
                    writeFile.write(str(visit[1]))
                    writeFile.write(',')
                    writeFile.write(str(visit[2]))
                    writeFile.write(',')
                    writeFile.write(str(visit[3]))
                    writeFile.write(',')
                    writeFile.write(str(visit[4]))
                    writeFile.write(',')
                    writeFile.write(str(visit[5]))
                    writeFile.write(',')
                    writeFile.write(str(visit[6]))
                    # At the end of the line, writes a newline character so that the data for the next visit appears
                    # on the next line of the file.
                    writeFile.write('\n')
    # Catches any key error that occurs when trying to remove a patient from the dictionary. Occurs if the given key
    # (patientId) does not exist in the dictionary.
    except KeyError:
        # Tells the user that the given patient ID is invalid.
        print( "No data found for patient with ID %d" % patientId)
    # If an error does not occur, this branch executes, telling the user that the patient's data has been removed.
    else:
        print("Data for patient %d has been deleted." % patientId)


def main():

    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()