# 키움증권 OpenAPI(KOA Studio) 활용을 위한 PyQt5 학습

# 학습자료1 (퀀트투자를 위한 키움증권 API (파이썬 버전))
# https://wikidocs.net/book/1173
# 학습자료2 (초보자를 위한 Python GUI 프로그래밍 - PyQt5)
# https://wikidocs.net/book/2944
# 학습자료3 (파이썬으로 배우는 알고리즘 트레이딩 (개정판-2쇄))
# [12. 키움증권 API의 3) 기초 API 익히기] 부터 다시 학습 시작할 것!
# https://wikidocs.net/4236


import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# 화면에 출력될 객체
class MyWindow(QMainWindow):  # MyWindow클래스가 QMainWindow클래스를 상속
                              # 다른 위젯에 포함되지 않은 최상위 위젯을 window라고 함
                              # 윈도우를 생성하기 위한 클래스로 QMainWindow나 QDialog 사용
    def __init__(self):
        super().__init__()
        self.setWindowTitle("윈도우~~~")       # 윈도우의 제목 설정
        self.setGeometry(300, 300, 300, 400) # 윈도우의 위치 및 크기 조절

        btn1=QPushButton("Click(버튼)", self)   # 윈도우 안의 버튼 생성
        btn1.move(20, 20)                    # 버튼의 출력 위치
        btn1.clicked.connect(self.btn1_clicked)
    
    def btn1_clicked(self): # 이벤트 처리 메서드
        QMessageBox.about(self, "message(창)", "clicked(눌림)")
        # 이벤트 : 사용자가 버튼 클릭
        # 이벤트 처리 : "message"라는 제목의 새 팝업창, "cliked" 출력(이벤트에 대한 새로운 이벤트 발생)

# 이벤트 루프
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 객체(app) 생성
    window = MyWindow()           # 객체(window) 생성
    window.show()                 # window 화면에 출력
    app.exec_()                   # app 종료(execute)

# label = QLabel("Hello PyQt")
# label.show()