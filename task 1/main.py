def hamming_distance(first_str, second_str):
  return sum(int(first_str[i] != second_str[i]) for i in range(len(first_str)))


assert(hamming_distance("abcde", "bcdef") == 5)
assert(hamming_distance("abcde", "abcde") == 0)
assert(hamming_distance("strong", "strung") == 1)
assert(hamming_distance("ABBA", "abba") == 4)