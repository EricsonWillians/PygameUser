import pygame
import math

class Shape:
	
	def __init__(self, pos, dimensions):
		self.pos = pos
		self.dimensions = dimensions
		self.x = pos[0]
		self.y = pos[1]
		self.w = dimensions[0]
		self.h = dimensions[1]
		
	def center(self, window_dimensions):
		self.x = (window_dimensions[0] / 2) - (self.w / 2)
		self.y = (window_dimensions[1] / 2) - (self.h / 2)
		
class Rectangle(Shape):
	
	def __init__(self, color, pos, dimensions):
		Shape.__init__(self, pos, dimensions)
		self.color = color
		
	def draw(self, surface):
		pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
		
class Ellipse(Shape):
	
	def __init__(self, color, pos, dimensions):
		Shape.__init__(self, pos, dimensions)
		self.color = color
		
	def draw(self, surface):
		pygame.draw.ellipse(surface, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
		
class SysFont(Shape):
	
	def __init__(self, color, pos, dimensions, font_name="monospace", bold=False, italic=False):
		Shape.__init__(self, pos, dimensions)
		self.color = color
		self.font_name = font_name
		self.bold = bold
		self.italic = italic
		self.font = pygame.font.SysFont(font_name, 32, bold, italic)

	def draw_text(self, surface, text):
		surface.blit(self.font.render(text, 1, self.color, (self.w, self.h)), (self.x, self.y))

if __name__ == "__main__":	

	pass
