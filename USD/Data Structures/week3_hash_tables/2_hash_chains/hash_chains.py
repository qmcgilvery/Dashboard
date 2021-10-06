# python3


# count = 0
# with open("tests/07") as p:
#     for line in p:
#         count += 1
#
# f = open("tests/07")


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = dict.fromkeys(range(bucket_count))
        for i in range(len(self.elems)):
            self.elems[i] = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            if self.elems[query.ind]:
                print(*self.elems[query.ind])
            else:
                print('')
        else:
            ind = -1
            if hasattr(Query, 'ind'):
                ind = query.ind
            if query.type == 'find':
                s = self._hash_func(query.s)
                if query.s in self.elems[s]:
                    print("yes")
                else:
                    print("no")
            elif query.type == 'add':
                if ind == -1:
                    key = self._hash_func(query.s)
                    self.elems.setdefault(key, [])
                    if query.s not in self.elems[key]:
                        self.elems[key].insert(0, query.s)
            else:
                d = self._hash_func(query.s)
                if query.s in self.elems[d]:
                    self.elems[d].remove(query.s)


    def process_queries(self):
        # n = count - 1
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


# bucket_count = int(f.readline())
# process = QueryProcessor(bucket_count)
# process.process_queries()


# f.close()
if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

