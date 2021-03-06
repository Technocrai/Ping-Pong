from pygame import*
game=True
up1 = K_w
up2 = K_UP
down1 = K_s
down2 = K_DOWN
FPS=60
font.init()
font1= font.Font(None,15)
LOSE1= font.Font(None,30).render("Player 1 lose", True,(180,0,0))
LOSE2= font.Font(None,30).render("Player 2 lose", True,(180,0,0))
timer =time.Clock()

window= display.set_mode((700,500))
display.set_caption('Пин Понг')

background= transform.scale(image.load('Space.jpg'),(700,500))

class GameSprite(sprite.Sprite):
   def __init__(self,player_image,player_x,player_y,player_speed,w,h):
      super().__init__()
      self.image = transform.scale(image.load(player_image),(w,h))
      self.speed = player_speed
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
   def reset(self):
      window.blit(self.image,(self.rect.x, self.rect.y))

class Ball(GameSprite):
   def __init__(self,player_image,player_x,player_y,player_speed,w,h,speedx,speedy):
      super().__init__(player_image,player_x,player_y,player_speed,w,h)
      self.speedx = speedx
      self.speedy = speedy
   def update(self):
      self.rect.x += self.speedx
      self.rect.y += self.speedy
      if ball.rect.y > 450 or ball.rect.y < 0:
         self.speedy *= -1
      if ball.rect.x > 1510 or ball.rect.x < -1400:
         self.rect.x=330
         self.rect.y=250
         self.speedy *= -1
         self.speedx *= -1
      if ball.rect.x > 690:
         window.blit(LOSE2, (200,200))
      if ball.rect.x < -10:
         window.blit(LOSE1, (200,200))
      if sprite.collide_rect(p1,self):
         self.speedx *= -1
      if sprite.collide_rect(p2,self):
         self.speedx *= -1



class Player(GameSprite):
   def __init__(self,player_image,player_x,player_y,player_speed,w,h,up,down):
      super().__init__(player_image,player_x,player_y,player_speed,w,h)
      self.down=down
      self.up=up
   def update(self):
      keys_pressed = key.get_pressed()
      if keys_pressed[self.up] and self.rect.y > 10:
         self.rect.y -= self.speed       
      if keys_pressed[self.down] and self.rect.y < 470:
         self.rect.y += self.speed

p1=Player('rocket.png',50,230,10,10,20,up1,down1)
p2=Player('rocket.png',600,230,10,10,20,up2,down2)
ball=Ball('Ball.png',330,250,3,40,40,3,3)

while game:
   for e in event.get():
      if e.type == QUIT:
         game = False

   if ball.rect.x > 690:
      window.blit(LOSE2, (200,200))

   if ball.rect.x < -10:
      window.blit(LOSE1, (200,200))
   window.blit(background,(0, 0))
   p1.update()
   p2.update()
   ball.update()
   ball.reset()
   p1.reset()
   p2.reset()
   display.update()
   timer.tick(FPS)
