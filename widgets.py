import pygame
from PyCliche import core

class Component:

	def __init__(self, pos, dimensions, parent):
		self.pos = pos
		self.dimensions = dimensions
		self.parent = parent
		self.parent_x_positions = [0]
		self.parent_y_positions = [0]
		
class Widget(Component, core.Shape):
	
	def __init__(self, pos, dimensions, parent=None):
		Component.__init__(self, pos, dimensions, parent)
		core.Shape.__init__(self, pos, self.dimensions)
		
class RectWidget(Widget):
	
	def __init__(self, pos, dimensions, parent=None):
		Component.__init__(self, pos, dimensions, parent)
		core.Shape.__init__(self, pos, self.dimensions)
		self.color = (0, 0, 0, 0)
		self.rect = None
		
	def draw(self, surface):
		self.rect.draw(surface)
		
	def set_color(self, rgba):
		self.color = rgba
		self.rect = core.Rectangle(self.color, self.pos, self.dimensions)

def rpc(p, l=[]):
	if p.parent:
		rpc(p.parent)
	else:
		l.append(p)
	return l

class Panel(RectWidget):
	
	def __init__(self, grid=None, parent=None, position_in_grid=None, pos=None):
		if pos:
			self.pos = pos
		else:
			self.pos = (0, 0)
		self.grid = grid
		self.dimensions = (
			self.grid.grid_size[0] * self.grid.cell_size[0], 
			self.grid.grid_size[1] * self.grid.cell_size[1]
		)
		self.x_positions = [x for x in range(0, self.dimensions[0], self.grid.cell_size[0])]
		self.y_positions = [x for x in range(0, self.dimensions[1], self.grid.cell_size[1])]
		if (parent and position_in_grid):
			self.parent = parent
			self.position_in_grid = position_in_grid
			parents = rpc(parent)
			lastParent = parents[len(parents)-1]
			self.x_positions = [x for x in range(0, lastParent.dimensions[0], lastParent.grid.cell_size[0])]
			self.y_positions = [x for x in range(0, lastParent.dimensions[1], lastParent.grid.cell_size[1])]
			self.dimensions = [
				lastParent.grid.cell_size[0], 
				lastParent.grid.cell_size[1]
			]
			self.pos = (
				self.x_positions[self.position_in_grid[0]] + lastParent.pos[0],
				self.y_positions[self.position_in_grid[1]] + lastParent.pos[1]
			)
		else:
			self.position_in_grid = (0, 0)
		RectWidget.__init__(self, self.pos, self.dimensions)
		self.rect = core.Rectangle(self.color, self.pos, self.dimensions)
		
	def draw(self, surface):
		self.rect.draw(surface)
		
class Button(RectWidget):

	def __init__(self, text, parent, position_in_grid):
		self.text = text
		self.parent = parent
		self.position_in_grid = position_in_grid
		self.dimensions = [
			self.parent.grid.cell_size[0], 
			self.parent.grid.cell_size[1]
		]
		self.x_positions = [x for x in range(0, self.parent.dimensions[0], self.dimensions[0])]
		self.y_positions = [x for x in range(0, self.parent.dimensions[1], self.dimensions[1])]
		self.pos = [
			self.x_positions[self.position_in_grid[0]] + self.parent.pos[0],
			self.y_positions[self.position_in_grid[1]] + self.parent.pos[1]
		]
		RectWidget.__init__(self, self.pos, self.dimensions, self.parent)
		self.rect = core.Rectangle(self.color, self.pos, self.dimensions)

	def on_click(self, event, function, *args):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if self.rect.R.collidepoint(event.pos):
					function(*args) if args else function()