# python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = [cur_query.name, cur_query.number]
            # if cur_query.number in contacts.values():
            #     contacts["name"] = cur_query.name
            # else:  # otherwise, just add it
            #     contacts[cur_query.number] = [cur_query.name, cur_query.number]
        elif cur_query.type == 'del':
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        else:
            response = 'not found'
            if cur_query.number in contacts:
                response = contacts[cur_query.number][0]
            result.append(response)
    return result


# count = 0
# with open("input.txt") as f:
#     for line in f:
#         count += 1
# with open("input.txt") as f:
#     write_responses(process_queries([Query(f.readline().split()) for i in range(count)]))


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

