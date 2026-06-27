class ServiceRequest:
    def __init__(self, request_id, customer_name, appliance_type, issue_description):
        self.request_id = request_id
        self.customer_name = customer_name
        self.appliance_type = appliance_type
        self.issue_description = issue_description
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"""
ID: {self.request_id}
Customer: {self.customer_name}
Appliance: {self.appliance_type}
Issue: {self.issue_description}
Status: {self.status}
"""