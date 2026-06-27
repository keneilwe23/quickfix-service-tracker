from service_request import ServiceRequest

class RequestManager:
    def __init__(self):
        self.requests = []
        self.next_id = 1

    def add_request(self, name, appliance, issue):
        request = ServiceRequest(self.next_id, name, appliance, issue)
        self.requests.append(request)
        self.next_id += 1

    def view_requests(self):
        if not self.requests:
            print("No service requests found.")
        for r in self.requests:
            print(r)

    def update_request(self, request_id, status):
        for r in self.requests:
            if r.request_id == request_id:
                r.update_status(status)
                return True
        return False