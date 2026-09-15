import pygame
import random
import requests

pygame.init()
FrameX = 600
FrameY = 400
White = (255, 255, 255)
Black = (0, 0, 0)

WindowScreen = pygame.display.set_mode((FrameX, FrameY))
pygame.display.set_caption("Hangman")
WindowScreen.fill(White)
Clock = pygame.time.Clock()
FPS = 60
GuessingLetter = True
Attempt = 0
BestGuess = 0
GameActive = False

Font = pygame.font.Font('Font/April.ttf', 36)
TitleScreen = pygame.image.load('Image/Hangman.png').convert_alpha()
Win = pygame.image.load('Image/Win.png').convert_alpha()
Lose = pygame.image.load('Image/Lose.png').convert_alpha()
Background = pygame.image.load('Image/Background.png').convert()
Try1 = pygame.image.load('Image/try1.png').convert_alpha()
Try2 = pygame.image.load('Image/try2.png').convert_alpha()
Try3 = pygame.image.load('Image/try3.png').convert_alpha()
Try4 = pygame.image.load('Image/try4.png').convert_alpha()
Try5 = pygame.image.load('Image/try5.png').convert_alpha()
Try6 = pygame.image.load('Image/try6.png').convert_alpha()
Try7 = pygame.image.load('Image/try7.png').convert_alpha()
Try8 = pygame.image.load('Image/try8.png').convert_alpha()
Try9 = pygame.image.load('Image/try9.png').convert_alpha()
Try10 = pygame.image.load('Image/try10.png').convert_alpha()

CorrectSound = pygame.mixer.Sound('SFX/Correct.wav')
WrongSound = pygame.mixer.Sound('SFX/Wrong.wav')

WordList = "https://api.frontendexpert.io/api/fe/wordle-words"
response = requests.get(WordList)
WordList = response.json()
GuessedLetters = []
Guess = "_____"
LetterGuessed = ""
RandomWord = ''

def FindNewWord():
    global RandomWord
    if GameActive:
        RandomWord = WordList[random.randint(0, len(WordList) - 1)]

def CheckLetters(RandomWord, LetterGuessed):
    if GuessingLetter:
        for i in range(len(RandomWord)):
            if LetterGuessed == RandomWord[i] and LetterGuessed not in GuessedLetters:
                ShowLetters(i, LetterGuessed)

def ReplaceAtIndex(original, index, replacement):
    return original[:index] + replacement + original[index+1:]
                    
def ShowLetters(LetterIndex, LetterGuessed):
    global Guess
    Guess = ReplaceAtIndex(Guess, LetterIndex, LetterGuessed)
    
def StartScreen():
    WindowScreen.blit(TitleScreen, (0, 0))
    EnterStart = Font.render(f"Press enter to start!", True, Black)
    EnterStartRect = EnterStart.get_rect(midtop = (FrameX / 2, 280))
    WindowScreen.blit(EnterStart, EnterStartRect)

def GameScreen():

    global RandomWord
    
    WindowScreen.blit(Background, (0, 0))
    WindowScreen.blit(Try1, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (pygame.KEYDOWN and event.type == pygame.K_ESCAPE):
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            GameActive = True
        if event.type == pygame.KEYDOWN and event.key != pygame.K_RETURN and GameActive:
            LetterGuessed = event.unicode.upper()
            CheckLetters(RandomWord, LetterGuessed)
            print(Guess)
            GuessedLetters.append(LetterGuessed)

    if GameActive:
        GameScreen()
    else:
        StartScreen()

    pygame.display.update()
    Clock.tick(FPS)