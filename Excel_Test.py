import xlrd
import xlwt
import xlutils.copy


workbook = xlrd.open_workbook('C:\\Users\DTJ\Desktop\工作簿1.xls')
####################################通过名称获取##################################
#sheets = workbook.sheet_names()
#worksheet = workbook.sheet_by_name(sheets[0])
####################################通过索引获取##################################
worksheet = workbook.sheets()[0]
rows = worksheet.nrows
cols = worksheet.ncols
A1 = worksheet.cell_value(0, 0)
C4 = worksheet.cell_value(3, 2)
A4 = A1 + C4
appendbook = xlutils.copy.copy(workbook)
appendsheet = appendbook.get_sheet(0)
appendsheet.write(3, 0, A4)
appendbook.save('C:\\Users\DTJ\Desktop\工作簿1.xls')