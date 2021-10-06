#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = {}
    count = 0
    for pattern in patterns:
        current_node = 0
        for i in range(len(pattern)):
            current_symbol = pattern[i]
            if current_node in tree and current_symbol in tree[current_node]:
                current_node = tree[current_node][current_symbol]
            else:
                count += 1
                new_node = {current_symbol: count}
                if not current_node in tree:
                    tree[current_node] = {}
                    tree[current_node].update(new_node)
                else:
                    tree[current_node].update(new_node)
                current_node = list(new_node.values())[-1]
    return tree

#
# if __name__ == '__main__':
#     # f = open("./sample_tests/sample3")
#     # patterns = f.read().split()[1:]
#     patterns = sys.stdin.read().split()[1:]
#     tree = build_trie(patterns)
#     for node in tree:
#         for c in tree[node]:
#             print("{}->{}:{}".format(node, tree[node][c], c))

print(len('TCTGGGCCTAACCAACGGAGCCCGAGAACCAGTGGCGATTAACACTAAGATCTTCGAAACTTCCAAGTGAGCTATTTACTTGTCAAGCCTCCTGCTGGTTCGGTCCCGAGCTACTAAAAAATTGGGAGGCACACCGCGTAAGTGGATGTTTAGAGTCGACGGAGCCCCCTAAAACATATCTAATCACGTAGACCGTACACTCTATCCAGGTCCCCATACTGCAACCACAAGTAGTTCGCGGCTCGTGCTTGTTATCCGGAGCAACAATAACTTGTCATATGAATCTTCCATCCTGGTCCTCTGGAGCGTGATTGTCCAGCGCTACGGAGAACGGCGGCCACGAATAGAATTATCTCCCTGTTCCCCTTCCTAATTATTCACCCTTGTTCAAAAAAAAAGTGCATCCTACGTTACGGCTGCATATTACTTTCACCGCTAGCTTTTTAGGGCCGACAGAGTCTTAATTCTCTATGATATGGTCGTGTTGGGCGTTGGTAGGGTGAGATTTACTAGTCGAAGCTGGATCTTTTGATTATAAAGGAGCCCCTAAGGTGGCATAAGGTTTTGCAGGCATCGGTAATGATACAAGTTGACAAAATTCATCGTACCTCACGACGCTAGGTATCGCTTGCCTTAAAAATGAAAGCTCTCGATGTTACCTCCCTGAGCGGAATTTATGTTCAGAAATTGGCATGTACCATACGCAATGCCCCCATGAGGTGAGAGCGAGGTTGCCCGACTAGTATGTCACGGGGAGCTCCGATTGTAAATATTATAAGGCGTATGGGCAAGGCGCCACGATCTATCCTGACTGATCTTAATCCTACAGTATATATCTTGGATGCATAATAAATAGACCTCTGGAGGTCTCTGTCCACTGTGTGGCTCTATCCAACGCTACTTCATAGCTGACATCGTCCGCCGACGACGCAGTTTAAACGCACTGGTCCGAAGCGCACCGAGTGAATTTGGTTATCCGCTGGTTTGGAATAAATTAATAGAGTCGTTCGTGCAGTTATGCTCGGACCTCCAAGAGTAAAATCCCACACAGCGATACCATTGTCAGTTTCTCACCGGAACAGGTCTGAAGTTCCGGGGCCGCCGTCGACTTACCGGTCATTTGGAATTCCGTTGATCAAGGACGCGAAGTATTTCGCCAGACGCCCTAATGTATGTTTTCGATCCTATTATCCCAGTCGGACGTAACGTAGGACCCGTTAAGTACCCGAAACTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'))