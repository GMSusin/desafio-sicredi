class Orders:
    def combine_orders(self, requests, n_max):
        requests.sort(reverse=True)  # Sort requests in descending order
        print(requests)
        num_trips = 0
        i = 0
        j = len(requests) - 1
        while i <= j:
            if requests[i] + requests[j] <= n_max:
                j -= 1          
            i += 1                             
            num_trips += 1
        return num_trips
    

orders = [70, 30, 10]
n_max = 100
expected_orders = 2

how_many = Orders().combine_orders(orders, n_max)
assert how_many == expected_orders