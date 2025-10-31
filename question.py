# question funtion
answer = {}

def q(name="dummy", question="", newline=False):
    if newline:
        newlinetemp = "\n"
    else:
        newlinetemp = ""
    answer = input(f"{question} {newlinetemp}")
    return answer

# usage:
# from question import q
# nameinput = q("nameinput", "What is your name?")
# print(nameinput)