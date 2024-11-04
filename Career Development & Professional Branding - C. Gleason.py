import csv
import random

#Reading the input file and returning data.
def read_input_file(input_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)#Creates CSV reader.
        data = list(reader)#Reads CSV and turns them into lists.
    return data

#Function to extract column headers and data from the input file.
def extract_headers_and_data(data):
    headers = data[0] #Takes first row and assigns it to headers.
    data = data[1:] #Removes headers from the data.
    return headers, data

#Function to count distinct values and keywords in each column.
def count_distinct_values(data):
    distinct_values = {} #Dictionary for distinct values and keywords.
    headers = data[0] #Assigns headers.
    for i in range(len(headers)):
        distinct_values[headers[i]] = list(set(row[i] for row in data[1:]))#Calculates the values for the currect column.
    return distinct_values

#Generating random keywords for each column.
def generate_random_data(headers, data, num_records):
    random_data = {} #Empty dictionary for randomly generated data.
    #Generating random data for each column.
    for header in headers:
        index = data[0].index(header)#Finds index of the column in first row of data.
        random_data[header] = [random.choice([row[index] for row in data[1:]]) for _ in range(num_records)]#Generates random data for the current column
    return random_data

#Writing generated data to a new CSV file
def write_to_csv(headers, generated_data, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file) #Creates CSV writer.
        writer.writerow(headers) #Writes headers to new CSV.
        for i in range(len(generated_data[headers[0]])):
            row = [generated_data[column][i] if column in generated_data else '' for column in headers]#Checks if there is corresponding data in generated_data.
            writer.writerow(row) #Writes the generated row.

#Main function.
def main(input_file, output_file):

    #Reads input file.
    data = read_input_file(input_file)

    #Extracts the headers and data from input file.
    headers, _ = extract_headers_and_data(data)
    
    #Prompts user for number of records they want and ensures positive integer.
    while True:
        try:
            num_records = int(input("How many records would you like? "))
            if num_records > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")
    
    #Generates random data for each column.
    generated_data = generate_random_data(headers, data, num_records)
    
    #Generates data to the new CSV file.
    write_to_csv(headers, generated_data, output_file)

#Assigns input and output files to a variable and ensures running.
if __name__ == "__main__":
    input_file = "Fictional_Customers.csv"
    output_file = "Generated_Customers.csv"
    main(input_file, output_file)

