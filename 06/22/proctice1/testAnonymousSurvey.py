import unittest
from AnonymousSurvey import AnoymousSurvey

class AnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "what language did you first learn to speak?"
        self.my_survey = AnoymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']

    def test_store_single_response(self):
        #测试单个答案会被妥善的存储
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_response(self):
        #测试三个答案会被妥善的存储
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

    # def test_store_single_response(self):
    #     question = "what language did you first learn to speak ?"
    #     my_survey = AnoymousSurvey(question)
    #     responses = ['English','Spanish','Mandarin']
    #     for res in responses:
    #         my_survey.store_response(res)
    #     for res in responses:
    #         self.assertIn(res,my_survey.responses)

    if __name__ == '__main__':
        unittest.main()

