from openpyxl import Workbook
wb = Workbook()   # 새 워크북 생성
ws = wb.active # 현재 활성화된 sheet를 가지고 온다.

ws.title = "NadoSheet" # sheet 이름 변경
wb.save("sample.xlsx") # sample.xlsx에 저장
wb.close() # 파일 닫기
