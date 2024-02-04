# E-Business Event Management System

# Event database (dictionary)
events = {}
#{event_id:{'name': event_name, 'speaker': speaker_name, 'date': date, 'capacity': capacity, 'attendees': set()}}
# Customer database (dictionary)
customers = {}
#{customer_id:{'name': name, 'loyalty_points': 0, 'booking_history': [],'feed_back':{}}}
#应该有no， name， loyalty point，booking list

# Function to add new customer to the database 1
def add_customer(customer_id, name):
    customers[customer_id] = {'name': name, 'loyalty_points': 0, 'booking_history': []}
    print(f"Customer {name} added to the database.")

# Function to remove customer from the database 2
def remove_customer(customer_id):
    if customer_id in customers:
        del customers[customer_id]
        print(f"Customer {customer_id} removed from the database.")
    else:
        print("Customer not found.")


# Function to create or modify an event 3
def create_event(event_id, event_name, speaker_name, date, capacity):
    events[event_id] = {'name': event_name, 'speaker': speaker_name, 'date': date, 'capacity': capacity, 'attendees': set()}#为什么用set
    print(f"Event '{event_name}' created or modified.")

#update 后期添加update功能-Add update function in the later stage
# Function to update an existing event 4
def update_event(event_id, event_name, speaker_name, date, capacity):
    if event_id in events:
        events[event_id]['name'] = event_name
        events[event_id]['speaker'] = speaker_name
        events[event_id]['date'] = date
        events[event_id]['capacity'] = capacity
        print(f"Event '{event_name}' updated.")
    else:
        print("Event not found. Cannot update.")

# Function to update an existing customers 5
def update_customer(customer_id, customer_name):
    if customer_id in customers:
        customers[customer_id]['name'] = customer_name
        print(f"Customer '{customer_name}' updated.")
    else:
        print("Customer not found. Cannot update.")
   
# Function to register for an event 6
#event 与 customer 都要同步-"Both event and customer need to be synchronized"(straight translation)
def register_for_event(event_id, customer_id):
    if event_id in events and customer_id in customers:#确定都是正确的值-"Ensure that all values are correct"
        event = events[event_id]
        if len(event['attendees']) < event['capacity']:#增加一个判断，判断用户是否已经注册-"Add a judgment to determine if the user has already registered"
            event['attendees'].add(customer_id)#把客户id加入event的名单之中-"Add customer ID to the event list"
            print(f"Registration successful for event '{event['name']}'")
            customers[customer_id]['loyalty_points'] += 1  # Increment loyalty points#成功注册加分，直接写入字典中，即使一开始没有创建值（默认是0）-"Successful registration bonus points, written directly into the dictionary, even if no value was created at the beginning (default is 0)"
            #customers[customer_id]['booking_history'].append(event_id) #客户的bookinghistory同步增加-"The customer's booking history has increased at the same time"  easy one
            booking = {'event_id': event_id, 'event_name': event_name, 'speaker': speaker_name, 'date': date}#订单信息也是使用字典来存储，产品信息的值由列表存储-"#booking information is also stored using a dictionary, and the values of product information are stored in a list"
            customers[customer_id]['booking_history'].append(booking)#订单历史用列表存储，列表存储字典-"booking history is stored in a list, which stores a dictionary"
        else:
            print(f"Event '{event['name']}' is at full capacity. Registration not allowed.")
    else:
        print("Invalid event ID or customer ID.")

# Function to display customer details and booking history 7 #could display feedback in the future
def display_customer_details(customer_id):
    if customer_id in customers:
        customer_info = customers[customer_id]
        print(f"Name: {customer_info['name']}")
        print(f"loyalty points: {customer_info['loyalty_points']}")
        #print("Order History:")
        #for order in customer_info['order_history']:
        #    print(f"  Order ID: {order['order_id']}, Total Cost: ${order['total_cost']}")
        #    for product in order['products']:
        #        print(f"    Product: {product['name']}, Quantity: {product['quantity']}")
        for booking in customer_info['booking_history']:
            print(f"  Event ID: {booking['event_id']}, Event Name: {booking['event_name']}, Speaker: {booking['speaker']}, Date:{booking['date']}")
           
    else:
        print("Customer not found.")

# Function to display events details 8
def display_event_details(event_id):
    if event_id in events:
        event = events[event_id]
        print(f"Event Details for '{event['name']}':")
        print(f"Event ID: {event_id}")
        print(f"Speaker: {event['speaker']}")
        print(f"Date: {event['date']}")
        print(f"Capacity: {event['capacity']}")
        print(f"Current Attendees: {len(event['attendees'])}")
    else:
        print("Event not found.")        

# Function to display total loyalty points for each customer 9
def display_loyalty_points():
    print("Loyalty Points:")
    for customer_id, customer_info in customers.items():
        print(f"{customer_info['name']} - Loyalty Points: {customer_info['loyalty_points']}")#直接读取

# Function to generate a report on event attendance and participant feedback 10
def generate_report(event_id):
    if event_id in events:
        event = events[event_id]
        print(f"Report for Event '{event['name']}':")
        print(f"Date: {event['date']}")
        print(f"Speaker: {event['speaker']}")
        print(f"Capacity: {event['capacity']}")
        print(f"Total Attendees: {len(event['attendees'])}")
        print("Attendees:")
        for attendee_id in event['attendees']:
            print(f"  {customers[attendee_id]['name']}")#通过存在set里的客户id读取customer库中的信息获取参加会议的名字-"#Retrieve the names of attendees from the customer library by reading the customer ID stored in the set"
    else:
        print("Event not found.")

# Function to collect participant feedback 11
def collect_feedback(event_id, customer_id, feedback):
    if event_id in events and customer_id in customers:
        event_name = events[event_id]['name']
        customers[customer_id]['feedback'] = {'event_id': event_id, 'event_name': event_name, 'feedback_text': feedback}
        print(f"Feedback collected for event '{event_name}'.")
    else:
        print("Invalid event ID or customer ID.")

# Main User Interface Loop
while True:
    print("\nE-Business Event Management System")
    print("1. Add New Customer")
    print("2. Remove Customer")
    print("3. Create/Modify Event")
    print("4. Update An Existing Event")
    print("5. Update An Existing Customers")
    print("6. Register for Event")
    print("7. Display Customer Details and Booking History")
    print("8. Display events details")
    print("9. Display Loyalty Points")
    print("10. Generate Event Report")
    print("11. Collect Participant Feedback")
    print("0. Exit")

    choice = input("Enter your choice (0-11): ")

    if choice == '1':
        customer_id = input("Enter customer ID: ")
        name = input("Enter customer name: ")
        add_customer(customer_id, name)
    
    if choice == '2':
        customer_id = input("Enter customer ID: ")
        remove_customer(customer_id)

    
    if choice == '3':
        event_id = input("Enter event ID: ")
        event_name = input("Enter event name: ")
        speaker_name = input("Enter speaker name: ")
        date = input("Enter event date: ")
        capacity = int(input("Enter event capacity: "))
        create_event(event_id, event_name, speaker_name, date, capacity)
    
    elif choice == '4':
        event_id = input("Enter event ID to update: ")
        event_name = input("Enter new event name: ")
        speaker_name = input("Enter new speaker name: ")
        date = input("Enter new event date: ")
        capacity = int(input("Enter new event capacity: "))
        update_event(event_id, event_name, speaker_name, date, capacity)
    
    if choice == '5':
        customer_id = input("Enter customer ID: ")
        customer_name = input("Enter customer name: ")
        update_customer(customer_id, customer_name)

    elif choice == '6':
        event_id = input("Enter event ID: ")
        customer_id = input("Enter customer ID: ")
        register_for_event(event_id, customer_id)
    
    elif choice == '7':
        customer_id = input("Enter customer ID: ")
        display_customer_details(customer_id)
    
    elif choice == '8':
        event_id = input("Enter event ID: ")
        display_event_details(event_id)
    

    elif choice == '9':
        display_loyalty_points()

    elif choice == '10':
        event_id = input("Enter event ID: ")
        generate_report(event_id)

    elif choice == '11':
        event_id = input("Enter event ID: ")
        customer_id = input("Enter customer ID: ")
        feedback = input("Enter participant feedback: ")
        collect_feedback(event_id, customer_id, feedback)

    elif choice == '0':
        print("Exiting E-Business Event Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 0 and 5.")