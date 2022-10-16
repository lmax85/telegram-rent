#!/usr/bin/env python3

import argparse

def parse_command():
    parser = argparse.ArgumentParser(description='Parse telegram channel with estate ads.')
    parser.add_argument('--channel', metavar='C', type=str, nargs='?',
                        help='an integer id or string username of telegram channel, for example -1001753067073')
    parser.add_argument('--price-pattern', metavar='P', type=str, nargs='?',
                        default='\d+[\$\€]|\d{1,3}?[\,\.]{1}\d{1,3}[\$\€]',
                        help='regex pattern for obtain only numbers in price (default: \d+[\$\€]|\d{1,3}?[\,\.]{1}\d{1,3}[\$\€])')
    parser.add_argument('--parse-limit-hours', metavar='L', type=int, nargs='?',
                        default=25,
                        help='limit in hours for iterate last telegram messages')
    parser.add_argument('--parse-size', metavar='S', type=int, nargs='?',
                        default=10,
                        help='size for obtain telegram messages in one api request (default: 2500, max: 3000)')
    parser.add_argument('--country', type=str, nargs='?',
                        default='unknown',
                        help='country of estate ads in channel (default: unknown)')
    parser.add_argument('--city', type=str, nargs='?',
                        default='unknown',
                        help='city of estate ads in channel (default: unknown)')

    args = parser.parse_args()

    if args.channel == None:
        raise ValueError('A channel must be set and valid!')

    return args
