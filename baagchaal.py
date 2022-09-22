import pygame


class Game:
	def __init__(self):
		print("initializing")
		pygame.init()
		self.running=True
		self.which_checkers_turn=False # True:Tiger, False:Goat
		self.count_moves=0 # 40 for goats to move
		self.goat_is_static=True # goats can't move
		self.temp_pos=None
		self.boarder_color=False # True:RED, False:BLUE
	
		self.white=(255,255,255,255)
		self.black=(0,0,0,0)
		self.red=(255,20,50)
		self.blue=(0,0,255)

		self.xaxis=1200
		self.yaxis=1200
		self.x=self.xaxis//6
		self.y=self.yaxis//6
		self.radius=self.xaxis/30
		self.border=((0,0),(self.xaxis,self.y//4))
		self.border2=((0,self.yaxis-(self.y//4)),((self.xaxis,self.yaxis-(self.y//4))))
		self.goat_victim=None
		self.goat_death_count=0

		pygame.display.set_caption("Baag Chaal")
		self.positions()
		self.free_pos=[self.p_a,self.p_c,self.p_e,self.p_g,self.p_i,self.p_k,self.p_m,self.p_o,self.p_q,self.p_s,self.p_u,self.p_w,self.p_y]
		self.board(self.white)
		self.playing()
		pygame.quit()

	def positions(self):# all positions in alphabet
		self.p_a=[self.x,self.y]
		self.p_b=[self.x*2,self.y]
		self.p_c=[self.x*3,self.y]
		self.p_d=[self.x*4,self.y]
		self.p_e=[self.x*5,self.y]

		self.p_f=[self.x,self.y*2]
		self.p_g=[self.x*2,self.y*2]
		self.p_h=[self.x*3,self.y*2]
		self.p_i=[self.x*4,self.y*2]
		self.p_j=[self.x*5,self.y*2]

		self.p_k = [self.x,self.y*3]
		self.p_l=[self.x*2,self.y*3]
		self.p_m=[self.x*3,self.y*3]
		self.p_n=[self.x*4,self.y*3]
		self.p_o=[self.x*5,self.y*3]

		self.p_p=[self.x,self.y*4]
		self.p_q=[self.x*2,self.y*4]
		self.p_r=[self.x*3,self.y*4]
		self.p_s=[self.x*4,self.y*4]
		self.p_t=[self.x*5,self.y*4]

		self.p_u=[self.x,self.y*5]
		self.p_v=[self.x*2,self.y*5]
		self.p_w=[self.x*3,self.y*5]
		self.p_x=[self.x*4,self.y*5]
		self.p_y=[self.x*5,self.y*5]

	def which_clicked(self,pos):# shows which area's been clicked
		
		if ((pos[0] <= self.p_a[0] +self.radius) and (pos[1] <= self.p_a[1]+self.radius))  and ((pos[0] >= self.p_a[0] - self.radius) and (pos[1]>=self.p_a[1]-self.radius)):
			return self.p_a
		if ((pos[0] <= self.p_b[0] +self.radius) and (pos[1] <= self.p_b[1]+self.radius))  and ((pos[0] >= self.p_b[0] - self.radius) and (pos[1]>=self.p_b[1]-self.radius)):
			return self.p_b
		if ((pos[0] <= self.p_c[0] +self.radius) and (pos[1] <= self.p_c[1]+self.radius))  and ((pos[0] >= self.p_c[0] - self.radius) and (pos[1]>=self.p_c[1]-self.radius)):
			return self.p_c 
		if ((pos[0] <= self.p_d[0] +self.radius) and (pos[1] <= self.p_d[1]+self.radius))  and ((pos[0] >= self.p_d[0] - self.radius) and (pos[1]>=self.p_d[1]-self.radius)):
			return self.p_d
		if ((pos[0] <= self.p_e[0] +self.radius) and (pos[1] <= self.p_e[1]+self.radius))  and ((pos[0] >= self.p_e[0] - self.radius) and (pos[1]>=self.p_e[1]-self.radius)):
			return self.p_e
		if ((pos[0] <= self.p_f[0] +self.radius) and (pos[1] <= self.p_f[1]+self.radius))  and ((pos[0] >= self.p_f[0] - self.radius) and (pos[1]>=self.p_f[1]-self.radius)):
			return self.p_f
		if ((pos[0] <= self.p_g[0] +self.radius) and (pos[1] <= self.p_g[1]+self.radius))  and ((pos[0] >= self.p_g[0] - self.radius) and (pos[1]>=self.p_g[1]-self.radius)):
			return self.p_g
		if ((pos[0] <= self.p_h[0] +self.radius) and (pos[1] <= self.p_h[1]+self.radius))  and ((pos[0] >= self.p_h[0] - self.radius) and (pos[1]>=self.p_h[1]-self.radius)):
			return self.p_h
		if ((pos[0] <= self.p_i[0] +self.radius) and (pos[1] <= self.p_i[1]+self.radius))  and ((pos[0] >= self.p_i[0] - self.radius) and (pos[1]>=self.p_i[1]-self.radius)):
			return self.p_i
		if ((pos[0] <= self.p_j[0] +self.radius) and (pos[1] <= self.p_j[1]+self.radius))  and ((pos[0] >= self.p_j[0] - self.radius) and (pos[1]>=self.p_j[1]-self.radius)):
			return self.p_j
		if ((pos[0] <= self.p_k[0] +self.radius) and (pos[1] <= self.p_k[1]+self.radius))  and ((pos[0] >= self.p_k[0] - self.radius) and (pos[1]>=self.p_k[1]-self.radius)):
			return self.p_k
		if ((pos[0] <= self.p_l[0] +self.radius) and (pos[1] <= self.p_l[1]+self.radius))  and ((pos[0] >= self.p_l[0] - self.radius) and (pos[1]>=self.p_l[1]-self.radius)):
			return self.p_l
		if ((pos[0] <= self.p_m[0] +self.radius) and (pos[1] <= self.p_m[1]+self.radius))  and ((pos[0] >= self.p_m[0] - self.radius) and (pos[1]>=self.p_m[1]-self.radius)):
			return self.p_m
		if ((pos[0] <= self.p_n[0] +self.radius) and (pos[1] <= self.p_n[1]+self.radius))  and ((pos[0] >= self.p_n[0] - self.radius) and (pos[1]>=self.p_n[1]-self.radius)):
			return self.p_n
		if ((pos[0] <= self.p_o[0] +self.radius) and (pos[1] <= self.p_o[1]+self.radius))  and ((pos[0] >= self.p_o[0] - self.radius) and (pos[1]>=self.p_o[1]-self.radius)):
			return self.p_o
		if ((pos[0] <= self.p_p[0] +self.radius) and (pos[1] <= self.p_p[1]+self.radius))  and ((pos[0] >= self.p_p[0] - self.radius) and (pos[1]>=self.p_p[1]-self.radius)):
			return self.p_p
		if ((pos[0] <= self.p_q[0] +self.radius) and (pos[1] <= self.p_q[1]+self.radius))  and ((pos[0] >= self.p_q[0] - self.radius) and (pos[1]>=self.p_q[1]-self.radius)):
			return self.p_q
		if ((pos[0] <= self.p_r[0] +self.radius) and (pos[1] <= self.p_r[1]+self.radius))  and ((pos[0] >= self.p_r[0] - self.radius) and (pos[1]>=self.p_r[1]-self.radius)):
			return self.p_r
		if ((pos[0] <= self.p_s[0] +self.radius) and (pos[1] <= self.p_s[1]+self.radius))  and ((pos[0] >= self.p_s[0] - self.radius) and (pos[1]>=self.p_s[1]-self.radius)):
			return self.p_s
		if ((pos[0] <= self.p_t[0] +self.radius) and (pos[1] <= self.p_t[1]+self.radius))  and ((pos[0] >= self.p_t[0] - self.radius) and (pos[1]>=self.p_t[1]-self.radius)):
			return self.p_t
		if ((pos[0] <= self.p_u[0] +self.radius) and (pos[1] <= self.p_u[1]+self.radius))  and ((pos[0] >= self.p_u[0] - self.radius) and (pos[1]>=self.p_u[1]-self.radius)):
			return self.p_u
		if ((pos[0] <= self.p_v[0] +self.radius) and (pos[1] <= self.p_v[1]+self.radius))  and ((pos[0] >= self.p_v[0] - self.radius) and (pos[1]>=self.p_v[1]-self.radius)):
			return self.p_v
		if ((pos[0] <= self.p_w[0] +self.radius) and (pos[1] <= self.p_w[1]+self.radius))  and ((pos[0] >= self.p_w[0] - self.radius) and (pos[1]>=self.p_w[1]-self.radius)):
			return self.p_w
		if ((pos[0] <= self.p_x[0] +self.radius) and (pos[1] <= self.p_x[1]+self.radius))  and ((pos[0] >= self.p_x[0] - self.radius) and (pos[1]>=self.p_x[1]-self.radius)):
			return self.p_x
		if ((pos[0] <= self.p_y[0] +self.radius) and (pos[1] <= self.p_y[1]+self.radius))  and ((pos[0] >= self.p_y[0] - self.radius) and (pos[1]>=self.p_y[1]-self.radius)):
			return self.p_y

	def init_pos(self):# initial positions of tigers
		self.tiger_pos=[self.p_a,self.p_e, self.p_u, self.p_y]
		self.goat_pos=[]
		for t in self.tiger_pos:
			self.draw_tiger(t)
		pygame.display.flip()

	def store_pos(self,_whose,_prev,_new):# saves changes in positions
		if _whose=="tiger":
			self.draw_blank(_prev)
			self.draw_tiger(_new)
			self.tiger_pos.pop(self.tiger_pos.index(_prev))
			self.tiger_pos.append(_new)
		elif _whose=="goat":
			self.draw_blank(_prev)
			self.draw_goat(_new)
			self.goat_pos.pop(self.goat_pos.index(_prev))
			self.goat_pos.append(_new)
		self.temp_pos=None # also called _prev

	def board(self,_color):# creates board
		self.screen=pygame.display.set_mode(size=(self.xaxis,self.yaxis))
		self.screen.fill(self.black)
		pygame.draw.line(self.screen,_color,(self.x,self.y),(self.xaxis-self.x,self.yaxis-self.y),4)
		pygame.draw.line(self.screen,_color,(self.x,self.y),(self.xaxis-self.x,self.y),4)
		pygame.draw.line(self.screen,_color,(self.x,self.y),(self.x,self.yaxis-self.y),4)
		pygame.draw.line(self.screen,_color,(self.xaxis-self.x,self.y),(self.x,self.yaxis-self.y),4)
		pygame.draw.line(self.screen,_color,(self.xaxis-self.x,self.y),(self.xaxis-self.x,self.yaxis-self.y),4)
		pygame.draw.line(self.screen,_color,(self.x,self.yaxis-self.y),(self.xaxis-self.x,self.yaxis-self.y),4)
		pygame.draw.line(self.screen,_color,(self.xaxis/2,self.y),(self.xaxis/2,self.yaxis-self.y),4)
		pygame.draw.line(self.screen,_color,(self.x,self.yaxis/2),(self.xaxis-self.x,self.yaxis/2),4)

		pygame.draw.line(self.screen,_color,(self.x*2,self.y),(self.x*2,self.yaxis-self.y),2)
		pygame.draw.line(self.screen,_color,(self.x*4,self.y),(self.x*4,self.yaxis-self.y),2)
		pygame.draw.line(self.screen,_color,(self.x,self.y*2),(self.xaxis-self.x,self.y*2),2)
		pygame.draw.line(self.screen,_color,(self.x,self.y*4),(self.xaxis-self.x,self.y*4),2)

		pygame.draw.line(self.screen,_color,(self.x*3,self.y),(self.x,self.y*3),2)
		pygame.draw.line(self.screen,_color,(self.x*3,self.y*5),(self.x,self.y*3),2)
		pygame.draw.line(self.screen,_color,(self.x*3,self.y*5),(self.x*5,self.y*3),2)
		pygame.draw.line(self.screen,_color,(self.x*3,self.y),(self.x*5,self.y*3),2)
		
		pygame.draw.rect(self.screen,self.blue,self.border)
		pygame.draw.rect(self.screen,self.blue,self.border2)

		# draws blank holes on board
		
		for _where in [self.p_a,self.p_b,self.p_c,self.p_d,self.p_e,self.p_f,self.p_g,self.p_h,self.p_i,self.p_j,self.p_k,self.p_l,self.p_m,self.p_n,self.p_o,self.p_p,self.p_q,self.p_r,self.p_s,self.p_t,self.p_u,self.p_v,self.p_w,self.p_x,self.p_y]:
			self.draw_blank(_where)

		pygame.display.flip()
		if _color ==self.white:
			self.init_pos()
		else:
			self.final_screen()
			pygame.display.update()

	def turns(self,pos):# manage turns
		_where=self.which_clicked(pos)
		if _where == None:
			print(f"invalid")
			return
		if not self.move_is_valid(_where):
			return
		if _where in self.tiger_pos and self.temp_pos==None:
			print(f"Area occupied by tiger")
			if self.which_checkers_turn:
				self.temp_pos=_where
			return
		if _where in self.goat_pos:
			print(f"Area occupied by goat")
			if not self.which_checkers_turn and not self.goat_is_static:
				self.temp_pos=_where
			return

		if self.which_checkers_turn:# tiger's turn
			if self.temp_pos==None:
				print(f"tiger not selected")
				return

			if not self.no_line_rule(self.temp_pos,_where):
				print(f"No line rule")
				return

			if not self.game_rules(self.temp_pos,_where):
				print(f"Too far")
				if self.tiger_eats(self.temp_pos,_where):
					self.goat_attacked()
					self.store_pos("tiger",self.temp_pos,_where)
					self.which_checkers_turn=False
					return
				else:
					return

			self.which_checkers_turn=False
			self.store_pos("tiger",self.temp_pos,_where)

		elif not self.which_checkers_turn and self.goat_is_static:# goat is still in placement
			self.which_checkers_turn=True
			self.draw_goat(_where)
			self.goat_pos.append(_where)
		elif not self.which_checkers_turn and not self.goat_is_static and self.temp_pos!=None:# after all goats have been placed
			if not self.game_rules(self.temp_pos,_where):
				print(f"too far")
				return
			if not self.no_line_rule(self.temp_pos,_where):
				return
			self.which_checkers_turn=True
			self.store_pos("goat",self.temp_pos,_where)
		else:
			print(f"BAD OUTCOME")

		self.count_moves+=1
		if self.count_moves>=40:
			self.goat_is_static=False

	def draw_tiger(self,_center):# draws tiger
		pygame.draw.circle(self.screen, self.red, _center, self.radius)
		pygame.draw.rect(self.screen,self.blue,self.border)
		pygame.draw.rect(self.screen,self.blue,self.border2)

	def draw_goat(self,_center):# draws goat
		pygame.draw.circle(self.screen, self.blue, _center, self.radius)
		pygame.draw.rect(self.screen,self.red,self.border)
		pygame.draw.rect(self.screen,self.red,self.border2)
	
	def draw_blank(self,_center):# removes a piece
		pygame.draw.circle(self.screen,self.black,_center,self.radius)

	def move_is_valid(self,_where):# checks the validity of the  move
		if _where in self.goat_pos and self.goat_is_static:
			print(f"move not valid, Goat can't be moved")
			return False
		if self.temp_pos!=None and _where in self.tiger_pos:
			print(f'move not valid, changing selected tiger')
			self.temp_pos=_where
			return False
		return True

	def no_line_rule(self,_prev,_new):# stops pieces without lines
		if not _prev in self.free_pos:
			print(f"restricted position")
			_diff=[_prev[0]-_new[0],_prev[1]-_new[1]]
			if _diff[0]<0:# changes negative to positive int
				_diff[0]=int(str(_diff[0])[1:])
			if _diff[1]<0:
				_diff[1]=int(str(_diff[1])[1:])

			if _diff[0]==0 and _diff[1]!=0:
				return True
			elif _diff[1]==0 and _diff[0]!=0:
				return True
			else:
				return False
		else:
			print(f"Free position")
			return True

	def game_rules(self,_prev,_new):# the rules of the game
		_diff=[_prev[0]-_new[0],_prev[1]-_new[1]]
		
		print(f"_prev={_prev}\n_new={_new}")

		if _diff[0]<0:# changes negative to positive int
			_diff[0]=int(str(_diff[0])[1:])
		if _diff[1]<0:
			_diff[1]=int(str(_diff[1])[1:])
		
		print(f"_diff{_diff}")

		if _diff[0]>self.x or _diff[1]>self.y:
			return False
		else:
			return True
		
	def tiger_eats(self,_prev,_new):
		_diff=[_prev[0]-_new[0],_prev[1]-_new[1]]
		if _diff[0]<0:# changes negative to positive int
			_diff[0]=int(str(_diff[0])[1:])
		if _diff[1]<0:
			_diff[1]=int(str(_diff[1])[1:])
		
		if _diff[0]>self.x*2 or _diff[1]>self.y*2:
			print("Tiger stetching out it's paws")
			return False


		mid_point=[(_prev[0]+_new[0])//2,(_prev[1]+_new[1])//2]
		if mid_point in self.goat_pos:
			print("TIGER ATTACK!!")
			self.goat_victim=mid_point
			return True
		else:
			print("False Alarm, Tiger got nothing")
			return False

	def goat_attacked(self):
		print("Goat corpse taken care of")
		self.goat_pos.pop(self.goat_pos.index(self.goat_victim))
		self.draw_blank(self.goat_victim)
		self.goat_victim=None
		self.goat_death_count+=1

	def goat_wins(self):
		return

	def final_screen(self):
		for _goats in self.goat_pos:
			self.draw_goat(_goats)
		for _tigers in self.tiger_pos:
			self.draw_tiger(_tigers)
		pygame.draw.rect(self.screen,self.red,self.border)
		pygame.draw.rect(self.screen,self.red,self.border2)

	def game_is_over(self):
		if (not self.goat_is_static and len(self.goat_pos)<=15) or self.goat_death_count>=5 :
			print(f"tiger has won")
			pygame.time.delay(700)
			# textsurface = pygame.font.SysFont('Ariel', 40, True).render('TIGER WINS', False, self.white)
			# self.screen.fill(self.black)
			# self.screen.blit(textsurface, (self.p_l, self.p_n))
			self.board(self.red)
			return True
		return False

	def playing(self):# actual game running
		wait_before_quit=False
		while self.running:
			for event in pygame.event.get():
				pygame.display.update()
				if event.type==pygame.QUIT:
					self.running=False
					return
				if event.type==pygame.MOUSEBUTTONUP and wait_before_quit:
					self.running=False
					return
				if event.type==pygame.MOUSEBUTTONUP:
					pos=pygame.mouse.get_pos()
					self.turns(pos)
					if self.game_is_over():
						wait_before_quit=True
						
if __name__=="__main__":
	Game()