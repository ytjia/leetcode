#!/usr/bin/env bash
#
# Write a bash script to calculate the frequency of each word in a text file words.txt.
# https://leetcode.com/problems/word-frequency/description/


# Read from the file words.txt and output the word frequency list to stdout.
# Globals:
#   None
# Arguments:
#   None
# Returns:
#   None
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{ print $2, $1 }'
