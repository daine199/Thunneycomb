import threading
import asyncio
import requests
import time
import queue


class TimeRequest(object):

    def __init__(self, query_samples=None):
        super(TimeRequest, self).__init__()
        self.responses = queue.Queue()
        if query_samples is None:
            self.query_samples = ["http://127.0.0.1:8000/summerhere/delay_test"]
        else:
            self.query_samples = query_samples
        self.loop = asyncio.get_event_loop()
        self.task = []

    def requests_internal(self, query_sample):
        time_1 = time.time()
        res = requests.get(query_sample)
        time_res = time.time() - time_1
        res = {"status": res.status_code, "query": query_sample, "cost": time_res}
        self.responses.put(res)

    def thread_request(self, query_sample):
        self.task.append(threading.Thread(target=TimeRequest.requests_internal, args=(query_sample)))


    def run(self):
        for query in self.query_samples:
            self.thread_request(query)
        for req in self.task:
            req.start()
        for req in self.task:
            req.join()

if __name__ == "__main__":
    time_1 = time.time()
    samples = ["http://127.0.0.1:8000/summerhere/delay_test/2"] * 10

    test = TimeRequest(samples)
    test.run()
    time_final = time.time() - time_1

    while test.responses.qsize() > 0:
        print(test.responses.get())
    print("total takes {0}".format(time_final))
