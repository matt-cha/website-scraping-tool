import gspread

sa = gspread.service_account()
sh = sa.open('website scraping')

wks = sh.worksheet('Sheet1')


wks.update(values=[['aaaaa']], range_name='A2')
wks.delete_rows(2)
# print(wks.acell('A2').value)
# wks.update('F2', '=UPPPER(E2)', raw=False)