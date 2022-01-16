from enum import unique
import os
import csv
import pathlib

voter_path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'Resources','election_data.csv')

with open(voter_path) as path_copy:
    reader = csv.reader(path_copy, delimiter = ",")
    header = next(path_copy)

    voter_list = []
    county_list = []
    candidate_list = []

    for row in reader:
        voter_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])

total_votes = len(voter_list)


all_candidates = []
for name in candidate_list:
    if name not in all_candidates:
        all_candidates.append(name)

#print(all_candidates)

candidate_votes = {
    all_candidates[0] : 0,
    all_candidates[1] : 0,
    all_candidates[2] : 0,
    all_candidates[3] : 0
}
#print(candidate_votes)

for name in candidate_list:
    candidate_votes[name] += 1

#print(candidate_votes)

candidate_percentage = {
    all_candidates[0] : round((candidate_votes[all_candidates[0]]/total_votes)*100,0),
    all_candidates[1] : round((candidate_votes[all_candidates[1]]/total_votes)*100,0),
    all_candidates[2] : round((candidate_votes[all_candidates[2]]/total_votes)*100,0),
    all_candidates[3] : round((candidate_votes[all_candidates[3]]/total_votes)*100,0)
}

#print(candidate_percentage)
winner = ""
winner_percent = 0

for name in all_candidates:
    if candidate_percentage[name] > winner_percent:
        winner = name
        winner_percent = candidate_percentage[name]

#print(winner)

output_path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'analysis', 'analysis.txt')

output_line_1 = "Total Votes: " + str(total_votes)
output_line_2 = "Khan:" + " " + str(candidate_percentage[all_candidates[0]]) + "% (" + str(candidate_votes[all_candidates[0]]) +")"
output_line_3 = "Correy:" + " " + str(candidate_percentage[all_candidates[1]]) + "% (" + str(candidate_votes[all_candidates[1]]) +")"
output_line_4 = "Li:" + " " + str(candidate_percentage[all_candidates[2]]) + "% (" + str(candidate_votes[all_candidates[2]]) +")"
output_line_5 = "O'Tooley:" + " " + str(candidate_percentage[all_candidates[3]]) + "% (" + str(candidate_votes[all_candidates[3]]) +")"

#print(output_line_1, output_line_2, output_line_3, output_line_4, output_line_5)

final_output = [
    "Election Results", 
    "-------------------------", 
    output_line_1,
    "-------------------------",
    output_line_2, output_line_3, output_line_4, output_line_5,
    "-------------------------",
    "Winner:" + " " + winner,
    "-------------------------"
]

#print(final_output)

with open(output_path, 'w') as output_copy:

    for line in final_output:
        output_copy.write(line)
        output_copy.write("\n")

for line in final_output:
    print(line)