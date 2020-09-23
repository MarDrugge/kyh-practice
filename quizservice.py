import requests

ENDPOINT = 'https://mqif4s7obg.execute-api.eu-central-1.amazonaws.com/olofs_lambda'


class QuizzWebServiceAPI(object):

    def __init__(self):
        self.url = ENDPOINT

    def get_all_questions(self):
        r = requests.get(self.url)
        ls = r.json()['questions']
        return ls

    def add_question(self, prompt, answer, alternatives):
        data = {
            'prompt': prompt,
            'rightAnswer': answer,
            'wrongAnswers': alternatives
        }
        r = requests.post(url=self.url, json=data)
        return True if r.status_code == 200 else False


def main():
    quiz = QuizzWebServiceAPI()
    quiz_ls = quiz.get_all_questions()

    print(f'Det finn {len(quiz_ls)} i Quiz-Databasen')
    inp = input(f'Gör ett val:\n1. Lägg till Fråga.\n2. Avsluta programmet\n')
    if inp == "1":
        prompt = input("Fråga: ")
        answer = input("Svar: ")
        alternatives = input("Alternativ: ").split(",")
        quiz.add_question(prompt=prompt, answer=answer, alternatives=alternatives)
    if inp == 2:
        return



if __name__ == '__main__':
    main()