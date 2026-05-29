import random
import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
import sys
from pgzero.loaders import sounds


def correct_location(sprite):
    if sprite.x > WIDTH + sprite.width // 2:
        sprite.x = -sprite.width // 2
    if sprite.x < -sprite.width // 2:
        sprite.x = WIDTH + sprite.width // 2
    if sprite.y > HEIGHT + sprite.height // 2:
        sprite.y = -sprite.height // 2
    if sprite.y < -sprite.height // 2:
        sprite.y = HEIGHT + sprite.height // 2

def random_location(sprite):
    sprite.x = random.randint(sprite.width//2,WIDTH-sprite.width//2 )
    sprite.y = random.randint(sprite.height//2,HEIGHT-sprite.height//2)


def on_key_down():
    global status
    if keyboard.space:
        status = "play"
    if keyboard.q and keyboard.e and keyboard.w:
        luigi.score += 1000


def draw():
    if status == "home":
        mod.screen.blit("home", (0, 0))
    elif status == "play":
        mod.screen.blit("background",(0, 0))
        mario.draw()
        luigi.draw()
        coin.draw()
        enemy.draw()
        mod.screen.draw.text(f"Mario Score: {mario.score}", (10,10), fontsize=30, color="red" )
        mod.screen.draw.text(f"Luigi Score: {luigi.score}", (1100,10), fontsize=30, color="green" )
    elif status == "mario_win":
        mod.screen.blit("mario_win",(0, 0))
    elif status == "luigi_win":
        mod.screen.blit("luigi_win",(0, 0))



def update():
    global status
    if status == "play":
        # Mario section
        if keyboard.right:
            mario.x += 5
            mario.image = "mario_right"
        if keyboard.left:
            mario.x -= 5
            mario.image = "mario_left"
        if keyboard.up:
            mario.y -= 5
        if keyboard.down:
            mario.y += 5
        if mario.colliderect(coin):
            mario.score += 10
            random_location(coin)
            sounds.jiring.play()
        if mario.score >= 100:
            status = "mario_win"
        correct_location(mario)



        # Luigi section
        if keyboard.s:
            luigi.x += 5
            luigi.image = "luigi_right"
        if keyboard.a:
            luigi.x -= 5
            luigi.image = "luigi_left"
        if keyboard.w:
            luigi.y -= 5
        if keyboard.z:
            luigi.y += 5
        if luigi.colliderect(coin):
            luigi.score += 10
            random_location(coin)
            sounds.jiring.play()
        if luigi.score >= 100:
            status = "luigi_win"
        correct_location(luigi)

        # enemy section
        enemy.x += 2
        enemy.y += 2
        correct_location(enemy)
        if enemy.colliderect(mario):

            sounds.lose.play()

        if enemy.colliderect(luigi):
            luigi.score = 0
            sounds.lose.play()
            random_location(luigi)


WIDTH = 1280
HEIGHT = 720


mod = sys.modules["__main__"]

status = "home"

mario = Actor('mario_right')
random_location(mario)
mario.score = 0

luigi = Actor('luigi_right')
random_location(luigi)
luigi.score = 0

coin = Actor('coin')
random_location(coin)

enemy = Actor('enemy_right')
random_location(enemy)


pgzrun.go()

