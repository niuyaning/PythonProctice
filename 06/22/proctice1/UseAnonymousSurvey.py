from AnonymousSurvey import AnoymousSurvey

question = "what language did you first learn to speak"
my_survey = AnoymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit")
while True:
    response = input("Language:")
    if response == 'q':
        print("结束")
        break
    my_survey.store_response(response)

print("===========调查结果================")
my_survey.show_result()
