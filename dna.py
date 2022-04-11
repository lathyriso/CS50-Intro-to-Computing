import csv
import sys
import re

# Main()
def main():
    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py CSVFILE TEXTFILE")
    # Creating file name variable
    fileName = sys.argv[2]
    fileName2 = sys.argv[1]
    
    # List to be used for slicing the dna sequence of Suspect
    dna_string = None
   
    with open(fileName, "r") as file:
        for line in file:
            dna_string = line
    
    # List of dictionnaries for CSV FIle
    database_seq = []
    
    with open(fileName2) as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            database_seq.append(line)
    
    # Call Functions
    indiv_string = suspect_sequence(dna_string)
    print(compare_seq(database_seq, indiv_string))
   
        
    
# Other Functions Here

def compare_seq(database_dict, indiv_dict):
    # Comparison
    values = ["AGATC", "TTTTTTCT", "AATG", "TCTAG", "GATA", "TATC", "GAAA", "TCTG"]
    
    # Temporary dictionaries to compare
    temp_dict = None
    name = ""
    for diction in database_dict:
        #print(diction)
        temp_dict = diction
        #print(temp_dict)
        for word in values:
            temp_dict[word] = int(temp_dict[word])
        res = all(temp_dict.get(key) == indiv_dict.get(key) for key in values)    
        if res == True:
            name = f'The name of suspect is: {temp_dict["name"]}'
            break
        else:
            name = "No Match Found"
    return name       

def suspect_sequence(suspect_dna):
    # List to be used for slicing the dna sequence
    values = ["AGATC", "TTTTTTCT", "AATG", "TCTAG", "GATA", "TATC", "GAAA", "TCTG"]
    
    # Dictionnary to count occurence of sequence
    id_string = {
        "AGATC": 0,
        "TTTTTTCT" : 0, 
        "AATG" : 0, 
        "TCTAG" : 0, 
        "GATA" : 0, 
        "TATC" : 0, 
        "GAAA" : 0, 
        "TCTG" : 0
    }
    
    # Loop to creat every instance of variation in the DNA
    num_seq = 0
    for word in values:
        for index in range(len(suspect_dna)):
            new_str = suspect_dna[index:index+len(word)]
            if new_str == word:
                count = 0
                test_str = ""
                for val in range(index, len(suspect_dna), len(word)):
                    test_str = suspect_dna[val:val+len(word)]
                    if test_str == word:
                        count += 1
                    else:
                        count = 0
                        break
                    if count > num_seq:
                        num_seq = count
        id_string[word] = num_seq
        num_seq = 0

    
    # Retrun Number of Occurence in suspect DNA
    return(id_string)
    
    
main()