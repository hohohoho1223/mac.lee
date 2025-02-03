from typing_extensions import Self
import time
import threading

class Menu: #메뉴판
    @staticmethod
    def menu_list_main() :
        menu_list_main = {
            '1. 치즈 햄버거 - 5000원':5000 ,
            '2. 불고기 햄버거 - 7000원':7000,
            '3. 쉬림프 햄버거 - 7000원':7000,
            '4. 빅 햄버거 - 8500원':8500
        }
        for i in menu_list_main:
            print(i) # 메인 메뉴판 공개
    @staticmethod
    def menu_list_side() :
        menu_list_side = {
            '1. 감자튀김 - 2500원':2500,
            '2. 해쉬 브라운 - 2500원':2500,
            '3. 너겟 - 3000원':3000
        }
        for i in menu_list_side:
            print(i) # 사이드 메뉴판 공개
    @staticmethod
    def menu_list_drink() :
        menu_list_drink = {
            '1. 콜라 - 2500원':2500,
            '2. 사이다 - 2500원':2500,
            '3. 환타 - 2500원':2500
        }
        for i in menu_list_drink:
            print(i) # 음료 메뉴판 공개

class Bucket: # 메뉴 장바구니
    def __init__(self):
        self.items = [] #장바구니 리스트

    def add_item(self,item):
        self.items.append(item) #장바구니 리스트에 추가

    # def remove_item(self,item):
    #     self.items.remove(item) #장바구니 리스트에서 제거

#사용자 입력
class User:
    def __init__(self):
        self.name = "" #인스턴스 변수 초기값 설정

    def user_info(self): #일반 메서드
        print("-----------------------------------------------")
        while True :
            print("이름을 입력하십시오.")
            self.name = input() # 사용자 이름 입력
            print(self.name + "님이 맞습니까? Y/N")
            user_name_check = input()
            if user_name_check == 'Y' :
                # print("랜덤으로 지급액이 산정되며")
                # print("해당 지급액으로 주문이 가능합니다!^^")
                Order(self.name).start() # 주문 시작
                break
            elif user_name_check == 'N' :
                print("이름을 다시 입력하십시오.")
                continue
            else :
                print("잘못 입력하셨습니다.")
                continue

#주문
class Order:
    def __init__(self, user_name):
        self.total_amount = 0 #주문 금액
        self.bucket = Bucket() #장바구니(클래스)로부터 객체 생성
        self.name = user_name #사용자 이름

    def start(self): #주문 시작
        print("-------------------Welcome---------------------")
        print("안녕하세요" " "+ self.name + "님!")
        while True :
            print("주문을 하시겠습니까? Y/N")
            order_select = input()
            if order_select == 'Y' :
                print("주문을 시작합니다.")
                self.menu_list_main_function() # 주문 함수 호출
                break
            elif order_select == 'N' :
                print("주문을 취소합니다.")
                print("초기화면으로 돌아갑니다.")
                return #함수종료
            else :
                print("잘못 입력하셨습니다.")
                continue

    def menu_list_main_function(self) : # 주문 함수
        print("--------------------MENU(Main)--------------------")
        Menu.menu_list_main()
        print("--------------------------------------------------")
        while True :
            print("메인 메뉴 번호를 입력하십시오.")
            try:
                main_select_number = int(input()) #메인 메뉴 선택
                if main_select_number in range(1,5) :
                    self.menu_list_main_select_process(main_select_number)
                    break
                else :
                    print("잘못 입력하셨습니다.")
                    continue
            except ValueError:
                print("잘못 입력하셨습니다. 숫자로 입력하세요!")
                continue
            # else :
            #     print("메뉴판에 없는 메뉴입니다.")
            #     continue

    def menu_list_main_select_process(self,main_select_number) :

        main_price = {1: 5000, 2:7000, 3:7000, 4:8500}
        main_name = {1: '치즈햄버거', 2: '불고기햄버거', 3: '쉬림프햄버거', 4: '빅햄버거'}

        self.total_amount += main_price[main_select_number] #총 결제 금액에 메뉴 가격 추가
        self.bucket.add_item(main_name[main_select_number])
        print(main_name[main_select_number] + "가 선택되었습니다.")
        print("주문 품목:" + ",".join(self.bucket.items))
        print("총 금액 : " + str(self.total_amount) + "원")
        self.menu_list_side_function() #사이드 메뉴 함수 호출

    ################################

    def menu_list_side_function(self) : #사이드 주문 여부 확인
        print("사이드 메뉴를 선택하시겠습니까? Y/N")
        menu_list_side_select = input()
        if menu_list_side_select == 'Y' :
            print("사이드 메뉴판 입니다.")
            print("--------------------MENU(Side)--------------------")
            Menu.menu_list_side()
            print("--------------------------------------------------")
            while True :
                print("사이드메뉴 번호를 선택하십시오.")
                menu_list_side_number = int(input())
                try:
                    if menu_list_side_number in [1,2,3] :
                        self.menu_list_side_select_process(menu_list_side_number)
                        break
                    else :
                        print("잘못 입력하셨습니다.")
                        continue
                except ValueError:
                    print("잘못 입력하셨습니다. 숫자로 입력하세요!")
                    continue
            # else :
            #     print("메뉴판에 없는 메뉴입니다.")
            #     continue
                 
        elif menu_list_side_select == 'N' :
            print("사이드 메뉴를 선택하지 않으셨습니다.")
            self.menu_list_drink_function() #음료 함수 호출
        else :
            print("잘못 입력하셨습니다.")
            self.menu_list_side_function()#돌아가기

    def menu_list_side_select_process(self,menu_list_side_number) :
        side_price = {1: 2500, 2: 2500, 3: 3000}
        side_name = {1: "감자튀김", 2: "해쉬 브라운", 3: "너겟"}
        self.total_amount += side_price[menu_list_side_number] #총 결제 금액에 메뉴 가격 추가
        self.bucket.add_item(side_name[menu_list_side_number])
        print(side_name[menu_list_side_number] + "가 선택되었습니다.")
        print("주문 품목:" + ",".join(self.bucket.items))
        print("총 금액 : " + str(self.total_amount) + "원")
        self.menu_list_drink_function() #음료 함수 호출
                
    ################################

    def menu_list_drink_function(self): #음료 주문
        print("음료를 선택하시겠습니까? Y/N")
        menu_list_drink_select = input()
        if menu_list_drink_select == 'Y' : # 예 선택
            print("음료 메뉴판 입니다.")
            print("--------------------MENU(Drink)--------------------")
            Menu.menu_list_drink()
            print("---------------------------------------------------")
            while True :
                print("음료를 선택하십시오.")
                drink_select_number = int(input())
                try:
                    if drink_select_number in [1,2,3]:
                        self.menu_list_drink_select_process(drink_select_number)
                        break
                    else :
                        print("잘못 입력하셨습니다.")
                        continue
                except ValueError:
                    print("잘못 입력하셨습니다. 숫자로 입력하세요!")
                    continue
        elif menu_list_drink_select == 'N' : # 아니오 선택
            print("음료를 선택하지 않으셨습니다.")
            Pay(self.total_amount, self.bucket.items).pay()  # 결제 호출
        else :
            print("잘못 입력하셨습니다.")
            self.menu_list_drink_function()#다시호출

    def menu_list_drink_select_process(self,drink_select_number):
        drink_price = {1: 2500, 2: 2500, 3: 2500}
        drink_name = {1: "콜라", 2: "사이다", 3: "환타"}
        
        self.total_amount += drink_price[drink_select_number]  # 총 결제 금액에 메뉴 가격 추가
        self.bucket.add_item(drink_name[drink_select_number])
        print(drink_name[drink_select_number] + "가 선택되었습니다.")
        print("주문 품목: " + ",".join(self.bucket.items))
        print("총 금액: " + str(self.total_amount) + "원")
        Pay(self.total_amount, self.bucket.items).pay()  # 결제 호출
#결제
class Pay :
    def __init__(self, total_amount, bucket_items):
        self.total_amount = total_amount
        self.bucket_items = bucket_items
    def pay(self): #결제 모듈
        global total_amount # 전역 변수 호출(값이 수정되므로 global 키워드 사용)
        global menu_bucket_list # 전역 변수 호출(값이 수정되므로 global 키워드 사용)
        print("--------------------BILL--------------------")
        print("주문 품목:" + str(self.bucket_items))
        print("총 주문 금액:" + str(self.total_amount))
        print("--------------------------------------------")
        while True :
            print("결제를 하시겠습니까? Y/N")
            pay_select = input()
            if pay_select == 'Y':  # 예 선택
                self.select_payment_method()
                break
            elif pay_select == 'N':  # 아니오 선택
                self.cancel_payment()
                break
            else:
                print("잘못 입력하셨습니다.")
                continue

    def select_payment_method(self):  # 결제 방법 선택
        print("결제를 시작합니다.")
        print("결제 방식을 입력해주십시오.")
        print("cash or card")
        while True:
            pay_method = input()
            if pay_method == 'cash':
                PayCash(self.total_amount).pay_method_cash()  # 현금 결제 함수 호출
                break
            elif pay_method == 'card':
                PayCard(self.total_amount).pay_method_card()  # 카드 결제 함수 호출
                break
            else:
                print("잘못 입력하셨습니다.")
                continue

    def cancel_payment(self):
        print("결제를 취소하시겠습니까?")
        print("현재 저장된 데이터는 사라집니다 Y/N")
        while True:
            pay_select_cancel = input()
            if pay_select_cancel == 'N':
                self.pay()  # 결제 메서드 다시 호출
            elif pay_select_cancel == 'Y':
                print("초기 화면으로 돌아갑니다.")
                return  # 초기 화면으로 돌아가기
            else:
                print("잘못 입력하셨습니다.")
                continue


# 현금 결제
class PayCash:
    def __init__(self, total_amount):
        self.total_amount = total_amount

    def pay_method_cash(self):
        print("현금 결제를 시작합니다.")
        print("--------------------PAY(Cash)--------------------")
        print("총 결제 금액은 " + str(self.total_amount) + "원 입니다.")
        while True:
            print("투입할 금액을 입력해주십시오.")
            try:
                total_amount_input = int(input())  # 현금 금액 입력
                break
            except ValueError:
                print("잘못 입력하셨습니다.")
                continue

        # 금액이 부족한 경우
        while total_amount_input < self.total_amount:
            print("######################")
            print("금액이 부족합니다.")
            print("필요한 금액: " + str(self.total_amount - total_amount_input) + "원")
            print("금액을 더 입력해주십시오.")
            print("######################")
            try:
                amount_input = int(input())  # 추가 금액 입력
                total_amount_input += amount_input
            except ValueError:
                print("잘못 입력하셨습니다.")
                continue

        # 결제가 완료된 경우
        print("잔돈은 " + str(total_amount_input - self.total_amount) + "원 입니다.")
        print("결제가 완료되었습니다.")
        print("--------------------------------------------")
        print("현금 영수증을 출력하시겠습니까? Y/N")
        while True:
            if input() == 'Y':
                Receipt.receipt_cash()  # 현금 영수증 함수 호출
                break
            elif input() == 'N':
                print("결제가 완료되었습니다. 감사합니다.")
                return  # 종료
            else:
                print("잘못 입력하셨습니다.")
                continue


# 카드 결제
class PayCard:
    def __init__(self, total_amount):
        self.total_amount = total_amount

    def pay_method_card(self):
        print("카드 결제를 시작합니다.")
        print("--------------------PAY(Card)--------------------")
        print("총 결제 금액은 " + str(self.total_amount) + "원 입니다.")
        print("-------------------------------------------------")
        def loading():
            print("카드 결제중입니다",end="")
            for _ in range(5): #5초 동안 결제 로딩 구현
                    time.sleep(1)
                    print(".",end="") #점을 찍어서 로딩 중임을 보여줌
        
            print("결제가 완료되었습니다.")
        # 로딩 스레드 시작
        loading_thread = threading.Thread(target=loading)
        loading_thread.start()
        loading_thread.join()  # 로딩이 끝날 때까지 기다림
        
        Receipt.receipt_card()  # 영수증 함수 호출

# 영수증
class Receipt:
    @staticmethod
    def receipt_card():  # 카드 결제
        print("영수증을 출력하시겠습니까? Y/N")
        receipt_response = input()
        while True:
            if receipt_response == 'Y':
                print("영수증 출력이 되었습니다.")
                print("결제를 종료합니다.")
                print("감사합니다.")
                break
            elif receipt_response == 'N':
                print("영수증을 출력하지 않습니다.")
                print("결제가 완료되었습니다. 감사합니다.")
                break  # 종료
            else:
                print("잘못 입력하셨습니다.")
                continue

    @staticmethod
    def receipt_cash():  # 현금 결제
        print("현금영수증 번호를 입력해주세요.")
        while True:
            try:
                receipt_cash_number = int(input())
                if receipt_cash_number > 0:
                    print(str(receipt_cash_number) + " 입력 되었습니다.")
                    print("--------------------------------------------")
                    print("현금영수증이 발행되었습니다.")
                    print("감사합니다.")
                    break
                else:
                    print("잘못 입력하셨습니다.")
                    continue
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해주세요!")
                continue

# 프로그램 시작
user = User()
user.user_info()  # 사용자 입력 메서드 실행
