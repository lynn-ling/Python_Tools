'''
需求：
创建3份不同的测试试卷
为每份试卷创建10个多重选择题，次序随机
为每个问题提供一个正确答案和3个随机错误答案，次序随机
将测试试卷写到3个文本文件中
将答案写到3个文本文件中
'''


import random

capitals = {'Alabama': 'Montgomery' , 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 
 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta'}

#创建3份试卷
for quizNum in range(3):
    quizFile = open('capitalsquiz%s.txt' % (quizNum+1),'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum+1),'w')

    quizFile.write('Name:\n\nDate:\n\n')
    quizFile.write((' '*20)+'State Capitals Quiz (Form %s)' % (quizNum+1))
    quizFile.write('\n\n')

    #创建州名的随机列表
    states = list(capitals.keys())
    random.shuffle(states)
    
    #创建10个问题
    for questionNum in range(10):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        #random.sample(参数1，参数2),参数1：希望选择的列表，参数2：希望选择的值的个数
        wrongAnswers = random.sample(wrongAnswers,3)
        #将correctAnswer用[]框起来将它变成列表形式就可以和前面的列表形式的wronganswers相加组成一个新的列表
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #每道题的问题
        quizFile.write('%s.What is the capital of %s?\n' % (questionNum+1,states[questionNum]))

        #将正确+错误的4个答案进行随机排列
        for i in range(4):
            #'ABCD'[i]将字符串'ABCD'看成是一个数组，它在循环的每次迭代中将分别求值为'A','B'，'C'，'D'
            quizFile.write(' %s. %s\n' % ('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')

        answerKeyFile.write('%s. %s\n' % (questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()



























