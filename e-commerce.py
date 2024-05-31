from deco_time import time_logger
import time

@time_logger("payment_time")
def pay():
    time.sleep(1.5)
    print("결제가 완료되었습니다.")

pay()

# uvicorn main:app --reload : 실행코드 