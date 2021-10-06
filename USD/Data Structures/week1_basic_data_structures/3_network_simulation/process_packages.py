# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        start = request[0]
        if not self.finish_time:
            self.finish_time.append(request[1])
            return Response(False, start)
        if start + self.size > self.finish_time[-1]:
            self.finish_time.append(request[1])
            return Response(False, sum(self.finish_time[:-1]))
        return Response(False, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    f = open("tests/18", "r")
    buffer_size, n_requests = map(int, f.readline().split())
    # buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, f.readline().split())
        # arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


main()
# if __name__ == "__main__":
#     main()

# Input_file = open("tests/03", "r")
# for n in Input_file:
#     main()


# print __name__
