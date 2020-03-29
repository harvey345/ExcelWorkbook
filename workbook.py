class ExcelWorkbook:
    def __init__(self,filename):
        from openpyxl import Workbook
        self.wb = Workbook()
        self.ws = self.wb.active
        self.filename=filename
    def write(self,block,data):
        self.ws[block]=data
        self.wb.save(self.filename)
        
    def append(self,data):
        self.ws.append(data)
        self.wb.save(self.filename)

    
    

    

    


