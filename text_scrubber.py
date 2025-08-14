import re

FILE_TO_READ = './apostrophe_sample.txt'
def print_tally(tokens_map):
    # sort by count
    alpha_map = dict(sorted(tokens_map.items(), key=lambda x: (x[1], x[0]), reverse=False ))
    descending_map = dict(sorted(alpha_map.items(), key=lambda kv: kv[1], reverse=True))
    # print tallies
    for k in descending_map:
        print("{}    {}".format(k, descending_map[k]))

def validate_and_count_tokens(tokens):
    TOKEN_COUNTS = {}
    # checks for only alpha or token-medial straight apostrophe
    regex_pattern = "[A-Za-z](?:[A-Za-z']*[A-Za-z])?"
    for token in tokens:
        if re.fullmatch(regex_pattern, token):
            lower_token = token.lower()
            if lower_token in TOKEN_COUNTS:
                TOKEN_COUNTS[lower_token] +=1
            else:
                TOKEN_COUNTS[lower_token] = 1
    return TOKEN_COUNTS

def get_tokens():
    with open(FILE_TO_READ) as file:
        return  file.read().split()
            
def main():
    # run through all files in the corpora from the top folder structure
    tokens = get_tokens()
    tokens_map =validate_and_count_tokens(tokens)
    print_tally(tokens_map)

main()