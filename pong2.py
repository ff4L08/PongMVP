from pygame import*

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

class Enemy(GameSprite):
    def update(self):
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y
        if self.rect.top > WIN_HEIGHT:
            
            self.rect.x = randint(0, WIN_WIDTH-(self.rect.width))

paddle1 = Player1(imageFile = 'whiterect.png', position = (WIN_WIDTH-50, WIN_HEIGHT/2), size = (30, 70), speed = (0,10))
paddle2 = Player2(imageFile = 'whiterect.png', position = (50, WIN_HEIGHT/2), size = (30, 70), speed = (0,10))

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

        paddle1.draw(window)
        paddle2.draw(window)


        display.update()
    
    clock.tick(60)