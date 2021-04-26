from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import re


class MyWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.w = uic.loadUi("calculator.ui")
		self.setCentralWidget(self.w)
		self.w.pB_0.clicked.connect(self.onPushButton)
		self.w.pB_1.clicked.connect(self.onPushButton)
		self.w.pB_2.clicked.connect(self.onPushButton)
		self.w.pB_3.clicked.connect(self.onPushButton)
		self.w.pB_4.clicked.connect(self.onPushButton)
		self.w.pB_5.clicked.connect(self.onPushButton)
		self.w.pB_6.clicked.connect(self.onPushButton)
		self.w.pB_7.clicked.connect(self.onPushButton)
		self.w.pB_8.clicked.connect(self.onPushButton)
		self.w.pB_9.clicked.connect(self.onPushButton)
		self.w.pB_C.clicked.connect(self.clear) # C
		self.w.pB_subtract.clicked.connect(self.subtract) # -
		self.w.pB_add.clicked.connect(self.add) # +
		self.w.pB_total.clicked.connect(self.total_result) # =
		self.w.pB_multiply.clicked.connect(self.onPushButton) # *
		self.w.pB_division.clicked.connect(self.onPushButton) #/
		self.numbers = ''
		self.num1 = ''
		self.num2 = ''
		self.total = ''
		self.result = ''


	def a(self):
		self.result = re.findall(r'\d+', self.numbers)
		return self.result[0]
	def b(self):
		self.result = re.findall(r'\d+', self.numbers)
		if len(self.result) > 2:
			return self.result[1]
		else:
			pass
	
		

	def onPushButton(self):
		self.num = self.sender().text() 
		self.numbers = self.numbers + self.num
		#print(self.numbers)
		self.w.lineEdit.setText(self.numbers)
		self.symb = re.findall(r'[+,\-,*,/]', self.numbers)
		self.add = len(self.symb)
		#print(self.add)
		if self.add > 1:
			#result = re.findall(r'\W+', self.numbers)
			#print(result)
			self.total_result()
			self.num1 = self.total
			self.numbers = str(self.num1) + self.num
			print(self.num1)
			#print(self.numbers)
			#print(self.num)
			#self.numbers = self.numbers + result[1]
			self.w.lineEdit.setText(self.numbers)


	def subtract(self):
		self.num = self.sender().text() 
		self.numbers = self.numbers + self.num
		self.w.lineEdit.setText(self.numbers)
		if len(self.result) == 2:
			self.num1 = self.a()
			self.num2 = self.b()
			self.total = int(self.num1) - int(self.num2)
			return self.w.lineEdit.setText(str(self.total))
		else:
			pass
	def add(self):
		self.num = self.sender().text() 
		self.numbers = self.numbers + self.num
		self.w.lineEdit.setText(self.numbers)
		if self.b() is None:
			pass
		else:
			self.total =int(self.a()) + int(self.b())
			return self.w.lineEdit.setText(str(self.total)) 

	def multiply(self):
		self.num = self.sender().text() 
		self.numbers = self.numbers + self.num
		self.w.lineEdit.setText(self.numbers)
		if  self.b() is None:
			pass
		else:
			self.total = self.a() * self.b()
			return self.w.lineEdit.setText(str(self.total)) 
	def division(self):
		self.num = self.sender().text() 
		self.numbers = self.numbers + self.num
		self.w.lineEdit.setText(self.numbers)
		if  self.b() is None:
			pass
		else:
			self.total = self.a() / self.b()
			return self.w.lineEdit.setText(str(self.total)) 





	def total_result(self):
		self.result = re.findall(r'\d+', self.numbers)
		self.num1 = int(self.result[0])
		self.num2 = int(self.result[1])
		self.symb = re.findall(r'[+,\-,*,/]', self.numbers)
		if self.symb[0] == '+':
			self.add()
		if self.symb[0] == '-':
			self.subtract()
		if self.symb[0] == '*':
			self.total = self.num1 * self.num2
		if self.symb[0] == '/':
			self.total = self.num1 / self.num2
		self.numbers = str(self.total)
		return self.w.lineEdit.setText(str(self.total)) 
		#self.numbers = '+'

		

		


	def clear (self):
		self.numbers = ''
		self.w.lineEdit.clear()


	#def name (self):
	#	self.total = self.num1 + self.num2
		

app = QApplication([])
window = MyWindow()
#window = Window()
#form = Form()
#form.setupUi(window)
window.show()

app.exec()