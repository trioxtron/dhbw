class Question:
    def __init__(self, question, answer, options):
        self._question = question
        self._answer = answer
        self._options = options


    def get_question(self):
        """ Get the question """
        return self._question

    def check_answer(self, answer):
        """ Check if the answer is correct
        Parameters:
            answer (str): The answer to be checked
        Returns:
            bool: True if the answer is correct, False otherwise
            str: The correct answer
        """
        return self._options[int(answer) - 1] == self._answer, self._answer

    def get_options(self):
        """ Get the options """
        return self._options
