#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    last_rom = 0
    for ch in roman_string:
        curr_rom = rom_n.get(ch, 0)
        if curr_rom > last_rom:
            num += curr_rom - 2 * last_rom
        else:
            num += curr_rom
        last_rom = curr_rom
    return num
