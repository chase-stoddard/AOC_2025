from functools import lru_cache

def read_instructions():
    with open('input/day11.txt', "r") as f:
        reactor_dict = {}
        for line in f:
            line = line.strip()
            key, values = line.split(': ')
            reactor_dict[key] = values.split(' ')
        return reactor_dict
    


example = {'svr': ['aaa', 'bbb'], 'aaa': ['fft'], 'fft': ['ccc'], 'bbb': ['tty'],
            'tty': ['ccc'], 'ccc': ['ddd', 'eee'], 'ddd': ['hub'], 'hub': ['fff'],
              'eee': ['dac'], 'dac': ['fff'], 'fff': ['ggg', 'hhh'], 'ggg': ['out'], 'hhh': ['out']}

instructions = read_instructions()


def count_paths(reactor, start):
    @lru_cache(None)
    def dfs(node, has_fft, has_dac):
        if node == 'out':
            return 1 if (has_fft and has_dac) else 0

        new_has_fft = has_fft or (node == 'fft')
        new_has_dac = has_dac or (node == 'dac')

        total = 0
        for neighbor in reactor.get(node, []):
            total += dfs(neighbor, new_has_fft, new_has_dac)

        return total

    return dfs(start, False, False)

print(count_paths(instructions, 'svr'))