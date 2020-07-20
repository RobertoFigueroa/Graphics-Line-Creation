from render import Render

my_bmp_file = Render()

my_bmp_file.glInit()

my_bmp_file.glCreateWindow(500,500)

my_bmp_file.glViewport(125, 125, 250, 250)

my_bmp_file.glClearColor(0,0,1)

my_bmp_file.glVertex_coord(0,0)

my_bmp_file.glLine(-1,-1,-1,1)
my_bmp_file.glLine(-1,1,1,1)
my_bmp_file.glLine(1,1,1,-1)
my_bmp_file.glLine(1,-1,-1,-1)
# my_bmp_file.glLine(0,0,-1,-1)
# my_bmp_file.glLine(0,0,1,1)
my_bmp_file.glLine(0,0,-1,0.5)
my_bmp_file.glLine(0,0,1,-1)



my_bmp_file.glFinish('lab2')