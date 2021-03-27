import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0 # total of votes cast
candidates = [] # list of candidates that received votes
candidate_votes = [] # list of the number of votes for each candidate

Khan_votes = ""
Khan_percent = 0
OTooley_votes = ""
OTooley_percent = ""
Correy_votes = ""
Correy_percent = ""
Li_votes = ""
Li_percent = ""


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)
    for row in csvreader:
        
        total_votes += 1
        
        if row[2] not in candidates:
            
            candidates.append(row[2])
            
            index = candidates.index(row[2])
           
            candidate_votes.append(1) 
        else:
           
            index = candidates.index(row[2])

            candidate_votes[index] += 1
        
    print(total_votes)  
    # 3521001 
    print(candidates) 
        # ['Khan', 'Correy', 'Li', "O'Tooley"]
    print(candidate_votes) 
    # [2218231, 704200, 492940, 105630]
    
  
    Khan_votes = candidate_votes[0]
    Correy_votes = candidate_votes[1]
    Li_votes = candidate_votes[2]
    OTooley_votes = candidate_votes[3]

    print(Khan_votes)
    print(Correy_votes)
    print(Li_votes)
    print(OTooley_votes)
    
    Khan_percent = (Khan_votes / total_votes) * 100
    Correy_percent = (Correy_votes / total_votes) * 100
    Li_percent = (Li_votes / total_votes) * 100
    OTooley_percent = (OTooley_votes / total_votes) * 100
       
    print(Khan_percent)
    print(Correy_percent)
    print(Li_percent)
    print(OTooley_percent)

    
      


   
            

        





# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.