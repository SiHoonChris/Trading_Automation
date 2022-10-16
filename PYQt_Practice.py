# 키움증권 OpenAPI(KOA Studio) 활용을 위한 PyQt5 학습

# 학습자료1 (퀀트투자를 위한 키움증권 API (파이썬 버전))
# https://wikidocs.net/book/1173
# 학습자료2 (초보자를 위한 Python GUI 프로그래밍 - PyQt5)
# https://wikidocs.net/book/2944
# 학습자료3 (파이썬으로 배우는 알고리즘 트레이딩 (개정판-2쇄))
# https://wikidocs.net/4236
# 학습자료4 (키움 OpenAPI+ 파이썬 개발가이드)
# https://wikidocs.net/book/8107
# 참고자료 (키움 OpenAPI+ 개발가이드)
# https://download.kiwoom.com/web/openapi/kiwoom_openapi_plus_devguide_ver_1.1.pdf

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(300, 300, 300, 150)

        # 파이썬에서 키움증권의 클래스 사용하려면 'QAxWidget' 사용해 객체 생성해야 함
        # 키움증권 제공 클래스는 고유의 CLSID(16진수) 또는 ProgID(문자열) 가짐, 이를 'QAxWidget'의 생성자로 전달하면 인스턴스 생성
        # 당연히 ProgID 활용하는 것이 편리함 
        # 레지스트리 편집기 활용, 검색
        # > ProgID : KHOPENAPI.KHOpenAPICtrl.1
        # > CLSID : {A1574A0D-6BFA-4BD7-9020-DED88711818D}
        self.kiwoom=QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")

        btn1=QPushButton("LOG-IN", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)
    
        btn2=QPushButton("Check State", self)
        btn2.move(20, 70)
        btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        # CommConnect : OpenAPI가 제공하는 메서드(로그인 윈도우 실행)
        # CommConnect 메서드 이용하려면 kiwoom(객체) 사용하여 dynamicCall 메서드 호출
        # ( OCX방식에서의 호출 방식임 )
        ret = self.kiwoom.dynamicCall("CommConnect")

    def btn2_clicked(self):
        # GetConnectState : OpenAPI가 제공하는 메서드(서버 접속상태 확인)
        if self.kiwoom.dynamicCall("GetConnectState()")==0:
            self.statusBar().showMessage("Not connected")
        else:
            self.statusBar().showMessage("Connected")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()