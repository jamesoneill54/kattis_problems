# Kattis problem link: https://open.kattis.com/problems/musicalnotation
import sys


def read_notes(played_notes):
    notes = {'G': ['G: '],
             'F': ['F: '],
             'E': ['E: '],
             'D': ['D: '],
             'C': ['C: '],
             'B': ['B: '],
             'A': ['A: '],
             'g': ['g: '],
             'f': ['f: '],
             'e': ['e: '],
             'd': ['d: '],
             'c': ['c: '],
             'b': ['b: '],
             'a': ['a: ']}

    for idx, note in enumerate(played_notes):
        for n in notes:
            if note[0] == n:
                if len(note) == 1:
                   notes[note].append('*')
                else:
                   notes[note[0]].append('*' * int(note[1]))
            if n in ['G', 'E', 'C', 'A', 'f', 'd', 'c', 'b']:
                if idx < (len(played_notes) - 1):
                    if note[0] == n:
                        notes[n].append(' ')
                    elif len(note) == 1:
                        notes[n].append('  ')
                    else:
                        notes[n].append(' ' * (int(note[1]) + 1))
                elif note[0] != n:
                    if len(note) == 1:
                        notes[n].append(' ')
                    else:
                        notes[n].append(' ' * int(note[1]))
            else:
                if idx < (len(played_notes) - 1):
                    if note[0] == n:
                        notes[n].append('-')
                    elif len(note) == 1:
                        notes[n].append('--')
                    else:
                        notes[n].append('-' * (int(note[1]) + 1))
                elif note[0] != n:
                    if len(note) == 1:
                        notes[n].append('-')
                    else:
                        notes[n].append('-' * int(note[1]))

    return notes


def main():
    line = sys.stdin.readlines()[1]
    out = read_notes(line.strip().split())
    for stave_line in ['G', 'F', 'E', 'D', 'C', 'B', 'A',
                       'g', 'f', 'e', 'd', 'c', 'b', 'a']:
        print(''.join(out[stave_line]))


if __name__ == "__main__":
    main()
