import csv
import logging

results={}

# import election raw data file (source.txt)
def read_lines():
    source ='source.txt'
    with open(source) as lines:
        for line in lines:
            key, code_and_votes = line.strip().split(',', maxsplit=1)
            results[key] = code_and_votes

# strip and reorder code and vote in dict
def strip_and_reorder():
    for key in results:
        code_and_votes = results[key].split(',')
        votes = code_and_votes[::2]
        votes = [i.strip() for i in votes]
        code = code_and_votes[1::2]
        code = [i.strip() for i in code]
        d2 = zip(code, votes)
        results[key] = dict(d2)   

# formatted party names and sort alphabetically
def format_code():
    for key in results:        
        results[key] = {
        k.replace('C', 'Conservative Party').replace('LD', 'Liberal Democrats').replace('UKIP', 'UKIP').replace('G', 'Green Party').replace('Ind', 'Independent').replace('SNP', 'SNP'): int(v) for k, v in results[key].items()
    }
        results[key] = {'Labour Party' if k == 'L' else k: v for k, v in results[key].items()}
        if 'Conservative Party' not in results[key].keys():
            results[key]['Conservative Party'] = 0
        if 'Liberal Democrats' not in results[key].keys():
            results[key]['Liberal Democrats'] = 0
        if 'UKIP' not in results[key].keys():
            results[key]['UKIP'] = 0
        if 'Green Party' not in results[key].keys():
            results[key]['Green Party'] = 0
        if 'Independent' not in results[key].keys():
            results[key]['Independent'] = 0
        if 'SNP' not in results[key].keys():
            results[key]['SNP'] = 0
        if 'Labour Party' not in results[key].keys():
            results[key]['Labour Party'] = 0
        results[key] = dict(sorted(results[key].items()))

            

# change vote counts to percentage
def format_percent():
    for key in results:
        s = sum(results[key].values())
        pct_results = {k: round(v / s, 4) for k, v in results[key].items()} 
        results[key] = pct_results


# create election result file (results.csv) with columns
def write_data_to_file():
    file = 'results.csv'
    with open(file, 'w', newline="") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['Constituency', 'Conservative Party', 'Green Party', 'Independent', 'Labour Party', 'Liberal Democrats', 'SNP', 'UKIP'])
        for key in results:
            writer.writerow([key] + [results[key]['Conservative Party']]+ [results[key]['Green Party']]+ [results[key]['Independent']]+ [results[key]['Labour Party']]+ [results[key]['Liberal Democrats']]+ [results[key]['SNP']]+ [results[key]['UKIP']])


read_lines()
strip_and_reorder()
format_code()
format_percent()
write_data_to_file()