#!/usr/bin/env python
from pyglet.gl import glClear,GLfloat as GLF,glColor3fv,glVertex2f,glBegin,glEnd
from pyglet.clock import set_fps_limit as a,tick
a(60)
from pyglet.window import Window as W
from os import listdir as LvL
LvL=iter(sorted(LvL for LvL in LvL(".") if LvL.endswith(".txt"))).next
W=W(style="borderless",vsync=1)
GLF=((GLF*3)(.8,.8,.8),(GLF*3)(.9,.3,.3)),((GLF*3)(1.,1.,not W.maximize()),)*2
W.event("on_mouse_motion")(lambda x,y,z1,z2,g=globals().__setitem__:(g("Mx",x-Wi>>5),g("My",Hi-y>>5)))
W.event("on_mouse_press")(lambda*x:globals().__setitem__("Li",-len(Lv)))
def makeLv(a):
	global Lv,Li,Wi,Hi,Wil,Hil
	Li=0
	Lv=[Lv.split("\n") for Lv in open(a).read().rstrip("\n").split("\n\n")]
	Wil=max(max(len(Lv) for Lv in Lv) for Lv in Lv)
	Hil=max(len(Lv) for Lv in Lv)
	Lv=[[[b not in " ." for b in a]+[False]*(Wil-len(a)) for a in Lv]+[[True]*Wil]*(Hil-len(Lv)) for Lv in Lv]
	Wi=W.width-(Wil<<5)>>1
	Hi=W.height+(Hil+2<<5)>>1
Ld=not not makeLv(LvL())
while 1:
	glClear(16384)
	Li=W.flip()
	li=60
	while not W.has_exit:
		li-=not W.dispatch_events()
		if not li:
			li=60
			Li=-(Li is glClear(16384)) or (Li!=-len(Lv) and Li+(Li>=0 or -1))
			if Li==len(Lv):break
			glColor3fv(GLF[Li>=0][Li==Ld])
			glBegin(2)
			glVertex2f(Wi,Hi)
			glVertex2f(Wi+(Wil<<5),Hi)
			glVertex2f(Wi+(Wil<<5),Hi-(Hil<<5))
			glVertex2f(Wi,Hi-(Hil<<5))
			glEnd()
			glBegin(7)
			for b,x in enumerate(Lv[Li]):
				b<<=5
				for a,x in enumerate(x):
					if x:
						a<<=5
						glVertex2f(Wi+a,Hi-b-32)
						glVertex2f(Wi+a+32,Hi-b-32)
						glVertex2f(Wi+a+32,Hi-b)
						glVertex2f(Wi+a,Hi-b)
			glEnd()
			W.flip()
		if Li is not tick() and Li>=0 and (not(0<=My<Hil and 0<=Mx<Wil) or Lv[Li][My][Mx]):break
	else:break
	Ld=not not makeLv(LvL()) if Li==len(Lv) else Li-len(Lv)
W.close()
