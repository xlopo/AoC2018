from __future__ import annotations
from dataclasses import dataclass


@dataclass()
class Marble:
    value: int
    clockwise: Marble = None
    counter_clockwise: Marble = None

    def __repr__(self):
        return f'Marble({self.value})'


@dataclass()
class Player:
    id: int
    marbles: list
    score: int = 0

    def add_marble(self, marble):
        self.marbles.append(marble)
        self.score += marble.value

    def __repr__(self):
        return f'Player({self.id}, marbles=..., {self.score})'


def place_marble(player: Player, current_marble: Marble, marble: Marble):
    left_marble = current_marble.clockwise

    right_marble = left_marble.clockwise

    marble.counter_clockwise = left_marble
    left_marble.clockwise = marble

    marble.clockwise = right_marble
    right_marble.counter_clockwise = marble


def print_tree(root, current_marble: Marble):
    marble = None
    while marble != root:
        if marble is None:
            marble = root
        if marble == current_marble:
            print(f'({marble.value:2})', end='')
        else:
            print(f'{marble.value:4}', end='')
        marble = marble.clockwise
    print()


def pop_marble(current_marble: Marble):
    marble = current_marble
    for x in range(7):
        marble = marble.counter_clockwise

    left_marble = marble.counter_clockwise
    right_marble = marble.clockwise

    left_marble.clockwise = right_marble
    right_marble.counter_clockwise = left_marble
    return marble


def play(num_players: int, num_marbles):
    players = [Player(i, []) for i in range(num_players)]

    value = 0
    root = Marble(value)
    root.counter_clockwise = root
    root.clockwise = root
    current_marble = root
    done = False
    while done is False:
        for player in players:
            # print_tree(root, current_marble)
            value += 1
            marble = Marble(value)
            if marble.value % 23 == 0:
                popped_marble = pop_marble(current_marble)
                player.add_marble(marble)
                player.add_marble(popped_marble)
                current_marble = popped_marble.clockwise
            else:
                place_marble(player, current_marble, marble)
                current_marble = marble
            if value == num_marbles:
                done = True
                break

    # print_tree(root, current_marble)
    highest_player = max(players, key=lambda x: x.score)
    print(highest_player)
    return highest_player


def main():
    assert play(num_players=10, num_marbles=25).score == 32
    assert play(num_players=10, num_marbles=1618).score == 8317
    assert play(num_players=13, num_marbles=7999).score == 146373
    assert play(num_players=17, num_marbles=1104).score == 2764
    assert play(num_players=21, num_marbles=6111).score == 54718
    assert play(num_players=30, num_marbles=5807).score == 37305

    # 424 players; last marble is worth 71482 points
    play(num_players=424, num_marbles=71482)



if __name__ == '__main__':
    main()
