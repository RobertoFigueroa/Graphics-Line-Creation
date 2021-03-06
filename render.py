from data_types_module import dword, word, char
from utils import color

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
RED = color(255, 0, 0)


class Render(object):

	#constructor
	def __init__(self):
		self.framebuffer = []
		self.curr_color = WHITE

	def glCreateWindow(self, width, height):
		#width and height for the framebuffer
		self.width = width
		self.height = height

	def glInit(self):
		self.curr_color = BLACK

	def glViewport(self, x, y, width, height):
		self.viewportX = x
		self.viewportY = y
		self.viewportWidth = width
		self.viewportHeight = height

	def glClear(self):
		self.framebuffer = [[BLACK for x in range(
		    self.width)] for y in range(self.height)]

	def glClearColor(self, r, g, b):
		clearColor = color(
				round(r * 255),
				round(g * 255),
				round(b * 255)
			)

		self.framebuffer = [[clearColor for x in range(
		    self.width)] for y in range(self.height)]

	def glVertex(self, x, y):
		#las funciones fueron obtenidas de https://www.khronos.org/registry/OpenGL-Refpages/es2.0/xhtml/glViewport.xml
		X = round((x+1) * (self.viewportWidth/2) + self.viewportX)
		Y = round((y+1) * (self.viewportHeight/2) + self.viewportY)
		self.point(X, Y)
		

	def glVertex_coord(self, x, y):
		self.framebuffer[y][x] = self.curr_color

	def glColor(self, r, g, b):
		self.curr_color = color(round(r * 255), round(g * 255), round(b * 255))

	def point(self, x, y):
		self.framebuffer[x][y] = self.curr_color

	def glFinish(self, filename):
		archivo = open(filename, 'wb')

		# File header 14 bytes
		archivo.write(char("B"))
		archivo.write(char("M"))
		archivo.write(dword(14+40+self.width*self.height))
		archivo.write(dword(0))
		archivo.write(dword(14+40))

		#Image Header 40 bytes
		archivo.write(dword(40))
		archivo.write(dword(self.width))
		archivo.write(dword(self.height))
		archivo.write(word(1))
		archivo.write(word(24))
		archivo.write(dword(0))
		archivo.write(dword(self.width * self.height * 3))
		archivo.write(dword(0))
		archivo.write(dword(0))
		archivo.write(dword(0))
		archivo.write(dword(0))

		#Pixeles, 3 bytes cada uno

		for x in range(self.height):
			for y in range(self.width):
				archivo.write(self.framebuffer[x][y])

		#Close file
		archivo.close()

	#class implementation
	def glLine(self, x0, y0, x1, y1):
		x0 = round(( x0 + 1) * (self.viewportWidth  / 2 ) + self.viewportX)
		x1 = round(( x1 + 1) * (self.viewportWidth  / 2 ) + self.viewportX)
		y0 = round(( y0 + 1) * (self.viewportHeight / 2 ) + self.viewportY)
		y1 = round(( y1 + 1) * (self.viewportHeight / 2 ) + self.viewportY)

		dx = abs(x1 - x0)
		dy = abs(y1 - y0)

		steep = dy > dx

		if steep:
			x0, y0 = y0, x0
			x1, y1 = y1, x1

		if x0 > x1:
			x0, x1 = x1, x0
			y0, y1 = y1, y0

		dx = abs(x1 - x0)
		dy = abs(y1 - y0)

		offset = 0
		limit = 0.5

		m = dy/dx
		y = y0

		for x in range(x0, x1 + 1):
			if steep:
				self.glVertex_coord(y, x)
			else:
				self.glVertex_coord(x, y)

			offset += m
			if offset >= limit:
				y += 1 if y0 < y1 else -1
				limit += 1

	#Homework implementation
	#Reference: http://www.dgp.toronto.edu/~karan/courses/csc418/lectures/BRESENHAM.HTML
	# def glLine(self, x0, y0, x1, y1):
	# 	x0 = round(( x0 + 1) * (self.viewportWidth  / 2 ) + self.viewportX)
	# 	x1 = round(( x1 + 1) * (self.viewportWidth  / 2 ) + self.viewportX)
	# 	y0 = round(( y0 + 1) * (self.viewportHeight / 2 ) + self.viewportY)
	# 	y1 = round(( y1 + 1) * (self.viewportHeight / 2 ) + self.viewportY)


	# 	dy = abs(y1 - y0)
	# 	dx = abs(x1 - x0)
		
	# 	steep = dy > dx

	# 	if steep:
	# 		x0, y0 = y0, x0
	# 		x1, y1 = y1, x1
		
	# 	if x0 > x1:
	# 		x0, x1 = x1, x0
	# 		y0, y1 = y1, y0
		
	# 	dy = abs(y1 - y0)
	# 	dx = abs(x1 - x0)
		

	# 	y = y0
	# 	offset = 2 *dy - dx

	# 	incre = 2* dy
	# 	decre = 2 * (dy - dx)

	# 	for x in range(x0, x1 + 1):
	# 		offset += 2*dy
	# 		if steep:
	# 			self.glVertex_coord(x, y)
	# 		else:
	# 			self.glVertex_coord(y, x)
	# 		if offset > 0 :
	# 			y += 1
	# 			offset += decre
	# 		else:
	# 			offset += incre
			

		




