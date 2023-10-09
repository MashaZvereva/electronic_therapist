class Therapist:
    def __init__(self):
        self.questions = []
        self.diagnoses = {}

    def add_question(self, question):
        self.questions.append(question)

    def add_diagnosis(self, name, description):
        self.diagnoses[name] = description

    def diagnose(self, answers):
        for question in self.questions:
            if question not in answers:
                return "Не все вопросы были отвечены."

        score = 0
        for answer in answers.values():
            score += answer

        if score < 3:
            return self.diagnoses.get("low", "Диагноз неизвестен")
        elif score < 7:
            return self.diagnoses.get("medium", "Диагноз неизвестен")
        else:
            return self.diagnoses.get("high", "Диагноз неизвестен")

import unittest

class TestTherapist(unittest.TestCase):
    def setUp(self):
        self.therapist = Therapist()
        self.therapist.add_question("Q1")
        self.therapist.add_question("Q2")
        self.therapist.add_diagnosis("low", "Низкий риск")
        self.therapist.add_diagnosis("medium", "Средний риск")
        self.therapist.add_diagnosis("high", "Высокий риск")

    # Your test methods go here

if __name__ == '__main__':
    unittest.main()