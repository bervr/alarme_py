# pip install rdm6300

#
# reader = rdm6300.Reader('/dev/ttyS0')
# print("Please insert an RFID card")
# while True:
#     card = reader.read()
#     if card:
#         print(f"[{card.value}] read card {card}")

import rdm6300

class Reader(rdm6300.BaseReader):
    def card_inserted(self, card):
        print(f"card inserted {card}")

    def card_removed(self, card):
        print(f"card removed {card}")

    def invalid_card(self, card):
        print(f"invalid card {card}")


r = Reader('/dev/ttyS0')
r.start()
