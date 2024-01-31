from numpy import random as rand

cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')
cValue=(2,3,4,5,6,7,8,9,10,11,12,13,14)

def check_straight(card1, card2, card3):
    card1Name = cards.index(card1)
    card2Name = cards.index(card2)
    card3Name = cards.index(card3)
    card1Value = cValue[card1Name]
    card2Value = cValue[card2Name]
    card3Value = cValue[card3Name]
    cardOrder=[card1Value,card2Value,card3Value]
    cardOrder.sort()
    if cardOrder[1] == (cardOrder[0] + 1) and cardOrder[2] == (cardOrder[1] + 1):
        return cardOrder[2]
    else:
        return 0

def check_3ofa_kind(card1, card2, card3):
    card1Name = cards.index(card1)
    card2Name = cards.index(card2)
    card3Name = cards.index(card3)
    card1Value = cValue[card1Name]
    card2Value = cValue[card2Name]
    card3Value = cValue[card3Name]
    if card1Value==card2Value and card3Value==card1Value:
        return card1Value
    else:
        return 0

def check_royal_flush(card1, card2, card3):
    if check_straight(card1,card2,card3)==14:
        return 14
    else:
        return 0

def play_cards(left1, left2, left3, right1, right2, right3):
    leftScore=0
    rightScore=0
    if check_royal_flush(left1, left2, left3)!=0:
        leftScore=check_royal_flush(left1, left2, left3)
    elif check_straight(left1, left2, left3) != 0:
        leftScore=check_straight(left1, left2, left3)
    elif check_3ofa_kind(left1, left2, left3) != 0:
        leftScore=check_3ofa_kind(left1, left2, left3)

    if check_royal_flush(right1, right2, right3) != 0:
        rightScore=check_royal_flush(right1, right2, right3)
    elif check_straight(right1, right2, right3) != 0:
        rightScore=check_straight(right1, right2,right3)
    elif check_3ofa_kind(right1, right2, right3) != 0:
        rightScore=check_3ofa_kind(right1, right2, right3)

    if leftScore > rightScore:
        return -1
    elif leftScore < rightScore:
        return 1
    elif leftScore == rightScore:
        return 0


play_cards('S2','S3','S3', 'SQ','SK','SA')

