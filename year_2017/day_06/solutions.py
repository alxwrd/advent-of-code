import os

with open(os.path.dirname(__file__) + "/input", "r") as f_:
    PUZZLE_INPUT = f_.read()


class MemoryBanks(object):

    def __init__(self, banks):
        self.banks = [int(bank) for bank in banks.split()]
        self.seen_layout = [hash(tuple(self.banks))]
        self.operations = 0
        self.complete = False


    def cycle(self):
        index = self.banks.index(max(self.banks))
        amount = self.banks[index]
        self.banks[index] = 0
        while amount:
            index += 1
            self.banks[index % len(self.banks)] += 1
            amount -= 1


    def redistibute(self):
        while not self.complete:
            self.cycle()
            self.operations += 1
            if hash(tuple(self.banks)) in self.seen_layout:
                self.complete = True
            self.seen_layout.append(hash(tuple(self.banks)))


    def loop_size(self):
        if not self.complete:
            #Just a joke because of 'MemoryBanks'.
            raise MemoryError("Can't determine loop size before resdistribution")

        last_seen = self.seen_layout[-1]
        return len(self.seen_layout)-1 - self.seen_layout.index(last_seen)
