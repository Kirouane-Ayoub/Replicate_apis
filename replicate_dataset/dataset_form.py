import re
import json

def reformat_string(input_string):
    questions_and_answers = re.findall(r"QS: (.+?) Answer: (.+?)(?=(?:\s*QS:|$))", input_string)
    reformatted_list = []
    
    for question, answer in questions_and_answers:
        prompt = {"prompt": question.strip()}
        completion = {"completion": answer.strip()}
        reformatted_list.append(json.dumps({**prompt, **completion}))
    
    return reformatted_list

input_string = "QS: What is your name and how would you like to be addressed? Answer: My name is Albert Einstein, and I prefer to be addressed as Albert. QS: A question. If I have to install an external program ANYWAY, why not just.. use something outside of the browser? Answer: Making in the browser makes it a little bit easier to support all the various operating systems not to mention form factors (e.g. smart phones too.)."
reformatted_output = reformat_string(input_string)

for item in reformatted_output:
    print(item)

