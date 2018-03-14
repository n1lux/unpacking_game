import os
from collections import namedtuple
from termcolor import colored


def build_questions():
    Question = namedtuple('Question', ('qid', 'question', 'response', 'represent')) 
    all_questions, qid = [], 0

    with open('data.2.csv', 'r') as fd:
        for i, line in enumerate(fd.readlines()):
            if '#' in line:
                q, r, _repr = line.split('#')
                question = Question(
			qid = qid ,
                        question=q.strip(), 
                        response=r.strip(), 
                        represent=_repr.strip()
                )
                all_questions.append(question)
                qid += 1


    return all_questions            


def is_help_key(key):
    return '?' == key


def show_response(q):
    print(colored(q.represent, 'yellow'))
    c = input()


def show_wrong_message():
    print(colored("Wrong!!! One more time!!!", 'red'))
    return


def show_correct_response(q):
    print(colored(f"Nice!!!! -> {q.represent}", 'green'))


def show_question(q):
    print("[{}] {}".format(q.qid, q.question))


def main():
    for q in build_questions():
        show_question(q)
        inp = input('Resposta:  ')
        if is_help_key(inp):
            show_response(q)
            continue
        while True: 
            if inp != q.response:
                show_wrong_message()
                show_question(q)
                inp =  input('Resposta:  ')
                if is_help_key(inp):
                    show_response(q)
                    break
            else:
                show_correct_response(q)
                break;


if __name__ == "__main__":
    main()

