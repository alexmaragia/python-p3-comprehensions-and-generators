#!/usr/bin/env python3

def return_evens(num_list):
    # Returns a list of even numbers from the input list
    return [n for n in num_list if n % 2 == 0]

def make_exclamation(sentence_list):
    # Returns a list of sentences with an exclamation mark added at the end
    return [sentence + '!' for sentence in sentence_list]
