from pygame import*
game=True
up1 = K_w
up2 = K_s
down1 = K_UP
down2 = K_DOWN
FPS=60


timer =time.Clock()

window= display.set_mode((700,500))
display.set_caption('Пин Понг')

background= transform.scale(image.load('Space.jpg'),(700,500))

class GameSprite(sprite.Sprite):
   def __init__(self,player_image,player_x,player_y,player_speed):
      super().__init__()
      self.image = transform.scale(image.load(player_image),(10,80))
      self.speed = player_speed
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
   def reset(self):
      window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
   def __init__(self,player_image,player_x,player_y,player_speed,UP,down):
      super().__init__(player_image,player_x,player_y,player_speed)
      self.down=down
      self.up=UP
   def update(self):
      keys_pressed = key.get_pressed()
      if keys_pressed[K_LEFT] and self.rect.y < 10:
         self.rect.x -= self.speed       
      if keys_pressed[K_RIGHT] and self.rect.y > -470:
         self.rect.x += self.speed

p1=Player('rocket.png',50,250,10,up1,down1)
p2=Player('rocket.png',600,250,10,up2,down2)

while game:
   for e in event.get():
      if e.type == QUIT:
         game = False
   window.blit(background,(0, 0))
   p1.update()
   p2.update()
   p1.reset()
   p2.reset()
   display.update()
   timer.tick(FPS)
