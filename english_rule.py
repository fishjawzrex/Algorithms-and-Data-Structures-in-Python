class EnglishRuler:
  def __init__(self, inches, ticks):
    self.inches  = inches
    self.ticks = ticks
  def draw_line(self,ticks,label):
    line = '-'*ticks
    if label:
      line += label
    print(line)

  def draw_interval(self,center_line):
    if center_line:
      self.draw_interval(center_line-1)
      self.draw_line(center_line-1,None)
      self.draw_interval(center_line-1)

  def draw_ruler(self):
    self.draw_line(self.ticks, '0')
    for i in range(1,self.inches+1):
      self.draw_interval(self.ticks)
      self.draw_line(self.ticks,str(i))

w = EnglishRuler(4,5)
w.draw_ruler()