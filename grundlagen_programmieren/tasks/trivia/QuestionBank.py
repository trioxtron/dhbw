import random 

class QuestionBank:
    def __init__(self):
        self._questions = []
        self._read_questions = []
        

    def add_question(self, question):
        """ Add a question to the question bank
        Parameters:
            question (Question): The question to be added to the question
        """
        self._questions.append(question)

    def randomize_questions(self):
        """ Randomize the order of the questions in the question bank """
        random.shuffle(self._questions)

    def get_new_question(self):
        """ Get a new question from the question bank
        Returns:
            Question: The new question
        """
        # If there are no more questions, return None
        if len(self._questions) == 0:
            return None

        # Get the last question in the list and remove it from the list before returning
        question = self._questions[-1]
        self._read_questions.append(question)
        self._questions.pop()
        return question
