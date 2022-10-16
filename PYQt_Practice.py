# 키움증권 OpenAPI(KOA Studio) 활용을 위한 PyQt5 학습

# 학습자료1 (퀀트투자를 위한 키움증권 API (파이썬 버전))
# https://wikidocs.net/book/1173
# 학습자료2 (초보자를 위한 Python GUI 프로그래밍 - PyQt5)
# https://wikidocs.net/book/2944
# 학습자료3 (파이썬으로 배우는 알고리즘 트레이딩 (개정판-2쇄))
# 로그인할 때 에러 발생 원인 확인 후, [3) 기본 정보 요청하기]부터 시작
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

        self.kiwoom=QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        self.text_edit.setEnabled(False) # 읽기/쓰기 모드

        # 로그인 성공 시, OnEventConnect 이벤트 발생
        # 이를 활용해 GetConnectState 쓰지 않고 로그인 성공 여부 확인
        # 이벤트(로그인) 이벤트 처리 메서드 연결
        self.kiwoom.OnEventConnect.connect(self.event_connect)

    # 이벤트 처리 메서드
    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()