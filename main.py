import pygame
import random
import requests

pygame.init()
FrameX = 600
FrameY = 400
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)

WindowScreen = pygame.display.set_mode((FrameX, FrameY))
pygame.display.set_caption("Hangman")
WindowScreen.fill(White)
Clock = pygame.time.Clock()
FPS = 60
GuessingLetter = True
Attempt = 0
BestGuess = 0
GameActive = False
LoseScreen = False
WinScreen = False
Guesses = 0

Font = pygame.font.Font('Font/April.ttf', 36)
GameFont = pygame.font.Font('Font/April.ttf', 72)
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

def Initialize():
    global GuessingLetter, Attempt, BestGuess, GameActive, LoseScreen, Guesses, Guess, GuessedLetters, RandomWord, LetterGuessed
    GuessingLetter = True
    Attempt = 0
    BestGuess = 0
    GameActive = False
    LoseScreen = False
    Guesses = 0
    Guess = "_____"
    GuessedLetters = []
    RandomWord = ''
    LetterGuessed = ""

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
    WindowScreen.blit(Background, (0, 0))
    WindowScreen.blit(TitleScreen, (0, 0))
    EnterStart = Font.render(f"Press enter to start!", True, Black)
    EnterStartRect = EnterStart.get_rect(midtop = (FrameX / 2, 280))
    WindowScreen.blit(EnterStart, EnterStartRect)

def GameScreen():
    global LoseScreen, WinScreen, GameActive, Guesses
    
    WindowScreen.blit(Background, (0, 0))
    WindowScreen.blit(Try1, (0, 0))

    if Guesses <= 7:
        AttemptNumber = GameFont.render(str(Guesses), True, Black)
        AttemptNumberRect = AttemptNumber.get_rect(center=(500, 100))
        WindowScreen.blit(AttemptNumber, AttemptNumberRect)
    elif Guesses > 7:
        AttemptNumber = GameFont.render(str(Guesses), True, Red)
        AttemptNumberRect = AttemptNumber.get_rect(center=(500, 100))
        WindowScreen.blit(AttemptNumber, AttemptNumberRect)

    if Guesses < 11 and '_' not in Guess:
        WinScreen = True
        GameActive = False
    
    if Guesses > 9:
        GameActive = False
        LoseScreen = True
        WrongSound.play()

    if Guesses == 0:
        WindowScreen.blit(Try1, (0, 0))
    elif Guesses == 1:
        WindowScreen.blit(Try2, (0, 0))
    elif Guesses == 2:
        WindowScreen.blit(Try3, (0, 0))
    elif Guesses == 3:
        WindowScreen.blit(Try4, (0, 0))
    elif Guesses == 4:
        WindowScreen.blit(Try5, (0, 0))
    elif Guesses == 5:
        WindowScreen.blit(Try6, (0, 0))
    elif Guesses == 6:
        WindowScreen.blit(Try7, (0, 0))
    elif Guesses == 7:
        WindowScreen.blit(Try8, (0, 0))
    elif Guesses == 8:
        WindowScreen.blit(Try9, (0, 0))
    elif Guesses == 9:
        WindowScreen.blit(Try10, (0, 0))

def UpdateWord():
    print(Guess)
    WordGame = GameFont.render(Guess, True, Black)
    WordGameRect = WordGame.get_rect(center=(FrameX/2, 300))
    WindowScreen.blit(WordGame, WordGameRect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (pygame.KEYDOWN and event.type == pygame.K_ESCAPE):
            pygame.quit()
            print(GuessedLetters)
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if not GameActive and not LoseScreen and not WinScreen:
                Initialize()
                GameActive = True
                FindNewWord()

            elif not GameActive and (LoseScreen or WinScreen):
                Initialize()
                LoseScreen = False
                WinScreen = False
                GameActive = False

        if event.type == pygame.KEYDOWN and event.key != pygame.K_RETURN and GameActive:
            LetterGuessed = event.unicode.upper()
            CheckLetters(RandomWord, LetterGuessed)
            print(Guess)

        # if event.type == pygame.KEYDOWN:
        #    "Hello, World!"(print)

        if GameActive:
            if LetterGuessed not in GuessedLetters and LetterGuessed not in RandomWord:
                GuessedLetters.append(LetterGuessed)
                Guesses += 1

            GameScreen()
            UpdateWord()
        else:
            if LoseScreen:
                WindowScreen.blit(Background, (0, 0))
                WindowScreen.blit(Lose, (0, 0))
            elif WinScreen:
                WindowScreen.blit(Background, (0, 0))
                WindowScreen.blit(Win, (0, 0))
            else:
                StartScreen()

    pygame.display.update()
    Clock.tick(FPS)