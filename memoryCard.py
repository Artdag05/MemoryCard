from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import randint, shuffle 
 
class Question():
    ''' contains a question, a correct answer and three incorrect ones'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
 
questions_list = [] 
questions_list.append(
        Question('State language of Brazil', 'Portuguese', 'English', 'Spanish', 'Brazilian'))
questions_list.append(
        Question('What color is on the flag of Ukraine?', 'Green', 'Red', 'Yellow', 'White'))
questions_list.append(
        Question('National dish of Italy', 'Pizza', 'Sushi', 'Hot dog', 'Borscht'))
 
app = QApplication([])
 
btn_OK = QPushButton('Answer') # answer button
lb_Question = QLabel('The hardest question in the world!') # answer text
 
RadioGroupBox = QGroupBox("Answer options") # on-screen group for radio buttons with responses
 
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')
 
RadioGroup = QButtonGroup() # this is for grouping radio buttons to control their behavior
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # vertical will be inside the horizontal
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # two answers in the first column
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # two answers in the second column
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # put the columns on the same line
 
RadioGroupBox.setLayout(layout_ans1) # ready "panel" with answer options 
 
AnsGroupBox = QGroupBox("Test results")
lb_Result = QLabel('are you right or not?') # it says "correct" or "incorrect""
lb_Correct = QLabel('the answer will be here!') # the text of the correct answer will be written here
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() # question
layout_line2 = QHBoxLayout() # answer options or test result
layout_line3 = QHBoxLayout() # "Answer" button
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() # hide the panel with the answer, first the panel of questions should be visible
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # button should be big
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spaces between content
def show_result():
    ''' show response panel '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next quiestion')
 
def show_question():
    ''' show question bar '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')
    RadioGroup.setExclusive(False) # removed the restrictions so that you can reset the radio button selection
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # brought back restrictions, now only one radio button can be selected
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Question):
    ''' the function writes the values ​​of the question and answers to the corresponding widgets,
    the answer options are distributed randomly.'''
    shuffle(answers) # shuffled the list of buttons, now some unpredictable button is in the first place of the list
    answers[0].setText(q.right_answer) # Fill in the first element of the list with the correct answer, the rest with incorrect ones.
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # question
    lb_Correct.setText(q.right_answer) # answer
    show_question() # show question bar
 
def show_correct(res):
    ''' show result - set the passed text to the inscription "result" and show the desired panel '''
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    ''' if some answer option is selected, then you need to check and show the answer panel'''
    if answers[0].isChecked():
        # correct answer!
        show_correct("That's it!")
        window.score += 1
        print('Statistics\n-Total questions: ', window.total, '\n-Correct answers: ', window.score)
        print('Rating: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # wrong answer!
            show_correct('Wrong!')
            print('Rating: ', (window.score/window.total*100), '%')
    
 
def next_question():
    ''' asks a random question from a list '''
    window.total += 1
    print('Statistics\n-Total questions: ', window.total, '\n-Correct answers: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question] # took the question
    ask(q) # asked
 
def click_OK():
    ''' whether to show another question or check the answer to this question '''
    if btn_OK.text() == 'Answer':
        check_answer() # check the answer
    else:
        next_question() # next question
 
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
 
btn_OK.clicked.connect(click_OK) # by clicking on the button, select what exactly happens
 
window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()
 
