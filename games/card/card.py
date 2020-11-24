class Card:
    def __init__(self,value,suit):
        self.value = value # 1 זה אס (הכי גבוה) ואז כרגיל 2-13 (11-נסיך, 12-מלכה, 13-מלך)
        self.suit = suit #הצורה של הקלף. יהלום (diamond) הכי חזק 1, אחריו תלתן (spade) 2, לב (heart) 3, והכי חלש עלה. (club) 4

#     def what_higher(self,card,card2):
#         if card.value > card2
#
# class DeckOfCards:
