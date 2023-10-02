import datetime
import requests
PIXELAend = "https://pixe.la/v1/users"

def new_user():

    userParam = {
        'token': TOKEN,
        'username': USER_NAME,
        'agreeTermsOfService' : 'yes',
        'notMinor':'yes'
    }
    response = requests.post(url="https://pixe.la/v1/users", json=userParam)
    print(response.text)



def add_graph():
    HEADER = {
        "X-USER-TOKEN": TOKEN
    }
    graphEndpoint = f'{PIXELAend}/{USER_NAME}/graphs'
    graph_params = {
        'id': GRAPH_ID,
        'name': "Walking",
        'unit': "Km",
        'type': "float",
        'color': "sora"
    }

    response = requests.post(url=graphEndpoint, json=graph_params, headers=HEADER)
    print(response.text)

def add_new_pixel():
    HEADER = {
        "X-USER-TOKEN": TOKEN
    }
    TODAY = datetime.date.today().strftime("%Y%m%d")
    print(f"Data will be added for today --> {TODAY}")

    NEW_PIXEL_ADD_END = f"{PIXELAend}/{USER_NAME}/graphs/{GRAPH_ID}"
    PARAM_PIXEL = {
        "date": f"{TODAY}",
        "quantity": f"{QUANTITY}"
    }
    response = requests.post(url=NEW_PIXEL_ADD_END,json=PARAM_PIXEL,headers=HEADER)
    print(response.text)



def modify_data():
    HEADER = {
        "X-USER-TOKEN": TOKEN
    }

    UPDATE_END = f"{PIXELAend}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"
    UPDATE_PARAMS = {
        "quantity": f"{NEW_DATA}"
    }
    response = requests.put(url=UPDATE_END,json=UPDATE_PARAMS,headers=HEADER)
    print(response.text)


def delete_data():
    HEADER = {
        "X-USER-TOKEN": TOKEN
    }

    DELETE_ENDPOINT = f"{PIXELAend}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE_TO_DELETE}"
    response = requests.delete(url=DELETE_ENDPOINT, headers=HEADER)
    print(response.text)

def show_again():
    options = input("Options? <y/n>")
    if options.lower() == 'y':
        show = True


show = True
TOKEN = input("Generate a unique token <8-164 charcters>")
USER_NAME = input("Generate a unique user name <starts with a-z>")
new_user()

while show:
    user_choice = input("Choose \n2.New Graph \n3.New Entry \n4.Modify Entry \n5.Delete Entry \n <1/2/3/4/5>:")

    if user_choice =='2':
        GRAPH_ID = input("Name the graph")
        add_graph()
        show_again()
    if user_choice =='3':
        QUANTITY = input('Enter how much you walked.')
        add_new_pixel()
        show_again()
    if user_choice =='4':
        DATE = input("enter date to be modified <yyyymmdd>")  # day wished to be updated
        NEW_DATA = input("New data to be put?")
        modify_data()
        show_again()
    if user_choice =='4':
        DATE_TO_DELETE = input("enter date where data to be deleted <yyyymmdd>")
        delete_data()
        show_again()


