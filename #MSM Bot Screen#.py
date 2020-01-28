import pyautogui
import time
import cx_Freeze
import sys


#         ***** Click Function *****

def ClickQuestIcon():
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen('QuestIcon.png', grayscale=True, confidence=.7))
        return True
    except:
        return False


def ClickProgress():
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen('ProgressIcon.png', grayscale=True, confidence=.7))
        return True
    except:
        return False


def ClickSkip():
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen('SkipIcon.png', grayscale=True, confidence=.7))
        return True
    except:
        return False


def ClickAccept():
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen('AcceptIcon.png', grayscale=True, confidence=.7))
        return True
    except:
        return False


def ClickComplete():
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen('CompleteIcon.png', grayscale=True, confidence=.7))
        return True
    except:
        return False


def ClickClaimReward():
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen('ClaimRewardIcon.png', grayscale=True, confidence=.7))
        return True
    except:
        return False

def ClickConfirm():
    try:
        pyautogui.click(pyautogui.locateCenterOnScreen('ConfirmIcon.png', grayscale=True, confidence=.7))
        return True
    except:
        return False


#         ***** Check Function *****

def CheckQuestIcon():
    if ClickQuestIcon():
        return True
    else:
        return False


def CheckConfirmIcon():
    if ClickConfirm():
        return True
    else:
        return False


def CheckProgress():
    if ClickProgress():
        return True
    else:
        return False


def CheckSkip():
    if ClickSkip():
        return True
    else:
        return False


def CheckAccept():
    if ClickAccept():
        return True
    else:
        return False


def CheckComplete():
    if ClickComplete():
        return True
    else:
        return False


def RunAgain():
    # While until the player stop walking or attacking mob's.
    counter = 0
    print('Start While #from agian#')
    while not CheckSkip() and not CheckComplete() and not CheckAccept() and not CheckConfirmIcon():
        counter += 1
    print('End While #from agian#', counter)

    time.sleep(3)

    # Skip Icon
    print('Start Skip Icon #from agian#')
    CheckSkip()
    time.sleep(3)
    print('End Skip Icon #from agian#')

def PlanA():
    if CheckConfirmIcon():
        time.sleep(3)
        # While until the player stop walking or attacking mob's.
        counter = 0
        print('Start While #from PlanA')
        while not CheckSkip() and not CheckComplete() and not CheckAccept():
            counter += 1
        print('End While #from PlanA', counter)
        time.sleep(3)
        # ***** check maybe split the code (Chek's..) to 3 if's.
        #first if : CheckSkip() and save the result.
        #second if : CheckComplete() and save the result.
        #thired if: CheckAccept() and save the result.





# def Other():
#     pyautogui.click(pyautogui.locateCenterOnScreen())


# Claim Reward not need to be here, always appear after Complete.


#         ***** Main Function *****

def Main():
    while True:
        # Quest Icon
        print('Start Quest Icon')
        CheckQuestIcon()
        time.sleep(3)
        print('End Quest Icon')

        time.sleep(3)

        # Progress Icon
        print('Start Progress Icon')
        CheckProgress()
        time.sleep(3)
        print('End Progress Icon')

        time.sleep(3)

        # Skip Icon
        print('Start Skip Icon')
        CheckSkip()
        time.sleep(3)
        print('End Skip Icon')

        time.sleep(3)

        # Confirm Icon       ---- fix when Confirm clicked - the next thing is broke.
        print('Start Skip Icon')
        CheckConfirmIcon()
        time.sleep(3)
        print('End Skip Icon')

        time.sleep(3)

        # Accept Icon
        print('Start Accept Icon')
        CheckAccept()
        time.sleep(3)
        print('End Accept Icon')

        time.sleep(3)

        # While until the player stop walking or attacking mob's.
        counter = 0
        print('Start While')
        while not CheckSkip() and not CheckComplete() and not CheckAccept():
            counter += 1
        print('End While ', counter)

        time.sleep(3)

        # Skip Icon
        print('Start Skip Icon')
        CheckSkip()
        time.sleep(3)
        print('End Skip Icon')

        time.sleep(3)
        if CheckAccept():
            RunAgain()

        time.sleep(3)

        # Confirm Icon
        print('Start Skip Icon')
        CheckConfirmIcon()
        time.sleep(3)
        print('End Skip Icon')

        time.sleep(3)

        # Complete Icon
        print('Start Complete Icon')
        CheckComplete()
        time.sleep(3)
        print('End Accept Icon')

        time.sleep(3)
        print('Start Claim Reward')
        ClickClaimReward()
        print('End Claim Reward')

        time.sleep(3)



Main()
