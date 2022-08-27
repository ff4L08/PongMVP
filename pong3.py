from pygame import*
from random import*

WIN_WIDTH = 1000
WIN_HEIGHT = 400
window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption('Pong')
square = 'whitesquare.png'
rectangle = 'whiterect.png'


class GameSprite(sprite.Sprite):
    # class constructor
    def __init__(self, imageFile, position, size, speed):
        #Call for the class (Sprite) constructor:
        super().__init__()
    
        #every sprite must store the image property
        self.image = image.load(imageFile)
        self.image = transform.scale(self.image, size)

        #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = Rect(position,size)

        self.speed = Vector2(speed)
    # method drawing the character on the window
    def draw(self, surface):
        surface.blit(self.image, (self.rect.topleft))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed.y
        if keys[K_DOWN]:
            self.rect.y += self.speed.y

        if self.rect.top < 30:
            self.rect.top = 30
        if self.rect.bottom > WIN_HEIGHT-30:
            self.rect.bottom = WIN_HEIGHT-30

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LSHIFT]:
            self.rect.y -= self.speed.y
        if keys[K_LCTRL]:
            self.rect.y += self.speed.y

        if self.rect.top < 30:
            self.rect.top = 30
        if self.rect.bottom > WIN_HEIGHT-30:
            self.rect.bottom = WIN_HEIGHT-30

class Ball(GameSprite):
    def update(self):
        self.rect.topleft += self.speed
        if self.rect.bottom > WIN_HEIGHT or self.rect.top < 0:
            self.speed.y *= -1

class TextSprite(sprite.Sprite):
    def __init__(self, text, color, pos, font_size):
        self.font = font.Font(None, font_size)
        self.color = color
        self.pos = pos
        self.update_text(text)
        self.rect = self.image.get_rect()
    def update_text(self, new_text):
        self.image = self.font.render(new_text,True, self.color)
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

font.init()      

paddle1 = Player1(imageFile = 'whiterect.png', position = (WIN_WIDTH-50, WIN_HEIGHT/2), size = (30, 70), speed = (0,10))
paddle2 = Player2(imageFile = 'whiterect.png', position = (20, WIN_HEIGHT/2), size = (30, 70), speed = (0,10))
squareBall = Ball(imageFile = 'whitesquare.png', position = (WIN_WIDTH/2, WIN_HEIGHT/2), size = (30, 30), speed = (-5,5))

LeftWin = TextSprite(text = 'Left Win!!', color = 'Blue' , pos = (0, 0), font_size = 200)
LeftWin.rect.center = (WIN_WIDTH/2, WIN_HEIGHT/2)
RightWin = TextSprite(text = 'Right Win!!', color = 'Blue' , pos = (0, 0), font_size = 200)
RightWin.rect.center = (WIN_WIDTH/2, WIN_HEIGHT/2)

finish = False
clock = time.Clock()
run = True

while run:
    for ev in event.get():
        if ev.type == QUIT:
            run = False
    if not finish:
        window.fill('black')

        paddle1.update()
        paddle2.update()
        squareBall.update()
        
        if sprite.collide_rect(squareBall, paddle1):
            change = randint(-110,-90)/100
            squareBall.speed.x *= change
            squareBall.rect.right = paddle1.rect.left
        
        if sprite.collide_rect(squareBall, paddle2):
            change = randint(-110,-90)/100
            squareBall.speed.x *= change
            squareBall.rect.left= paddle2.rect.right


        if squareBall.rect.left > WIN_WIDTH:
            # RIGHT WINS 
            print('right wins')
            finish = True

        elif squareBall.rect.right < 0:
            # LEFT WINS
            print('Left wins') 
            finish = True

        paddle1.draw(window)
        paddle2.draw(window)
        squareBall.draw(window)
    else:
        if squareBall.rect.left > WIN_WIDTH:
            RightWin.draw(window)
        else:
            LeftWin.draw(window)

    display.update()
    
    clock.tick(60)
