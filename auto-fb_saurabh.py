import random
import time
import requests
from bs4 import BeautifulSoup
import re
import json
import secrets
import os

BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
INFO = '[i]'
SUCCESS = '[✓]'
FAILURE = '[✗]'
DIVIDER = '-' * 50
SUCCESS = "✅"
FAILURE = "❌"
INFO = "ℹ️"
WARNING = "⚠️"
LOADING = "⏳"
EMAIL = "📧"
PHONE = "📞"
LOCK = "🔒"
USER = "👤"
COOKIE = "🍪"
OTP = "🔢"
HEART = "❤️"
STAR = "⭐"
ARROW = "➡️"
DIVIDER = "═" * 50
os.system('clear')
print(f"""{BLUE}   ___                                     
 .'   `.                                   
/  .-.  \  __   _   .---.  .---.  _ .--.   
| |   | | [  | | | / /__\\/ /__\\[ `.-. |  
\  `-'  \_ | \_/ |,| \__.,| \__., | | | |  
 `.___.\__|'.__.'_/ '.__.' '.__.'[___||__] """)
print(DIVIDER)
print(f"{INFO}    Author: Alia Queen{RESET}")
print(f"{INFO}    Tool For: Auto Create FB{RESET}")
print(DIVIDER)

def generate_name(country, gender):
    names = {
        "Pakistan": {
            "male": [
                "Ahmed", "Ali", "Bilal", "Danish", "Fahad", "Hassan", "Imran", "Junaid", "Kamran", "Usman",
                "Abdullah", "Adnan", "Akbar", "Arsalan", "Asim", "Asif", "Azhar", "Baber", "Basit", "Faisal",
                "Farhan", "Hamza", "Haroon", "Ibrahim", "Irfan", "Javed", "Kashif", "Majid", "Mohsin", "Nadeem",
                "Naeem", "Nasir", "Noman", "Omar", "Qasim", "Raheel", "Rashid", "Rehan", "Saad", "Sabir",
                "Saeed", "Saleem", "Salman", "Samir", "Shahid", "Shakeel", "Shamim", "Sharjeel", "Tahir", "Talha",
                "Tariq", "Umar", "Waqar", "Waqas", "Yasir", "Younis", "Zafar", "Zahid", "Zeeshan", "Zubair",
                "Adeel", "Afzal", "Aftab", "Aitzaz", "Amir", "Anwar", "Asad", "Ashraf", "Atif", "Ayaz"
            ],
            "female": [
                "Ayesha", "Fatima", "Zainab", "Sana", "Hina", "Sadia", "Rabia", "Saima", "Nazia", "Farah",
                "Aisha", "Alia", "Amna", "Anam", "Anila", "Anum", "Asma", "Bushra", "Durdana", "Fariha",
                "Fauzia", "Ghazala", "Hafsa", "Hira", "Humaira", "Iram", "Ishrat", "Javeria", "Kainat", "Khadija",
                "Kulsoom", "Lubna", "Madiha", "Maham", "Mahwish", "Mariam", "Mehwish", "Mishal", "Momina", "Muniba",
                "Nadia", "Naghma", "Najma", "Nargis", "Nasreen", "Nida", "Nimra", "Noreen", "Nosheen", "Palwasha",
                "Quratulain", "Rafia", "Rida", "Rukhsar", "Saba", "Sadia", "Sahar", "Samina", "Sara", "Shabana",
                "Shazia", "Sobia", "Sonia", "Sumaira", "Tahira", "Tamanna", "Tayyaba", "Uzma", "Yasmeen", "Zara"
            ],
            "last": [
                "Khan", "Malik", "Butt", "Chaudhry", "Sheikh", "Qureshi", "Ahmed", "Ali", "Raza", "Hussain",
                "Abbasi", "Afridi", "Arain", "Awan", "Baig", "Bajwa", "Baloch", "Bhatti", "Chaudhry", "Cheema",
                "Daultana", "Dhariwal", "Farooqi", "Gillani", "Gondal", "Gujjar", "Hashmi", "Jatt", "Jutt", "Kamboh",
                "Kayani", "Khakwani", "Khar", "Lodhi", "Mahmood", "Makhdoom", "Malik", "Mian", "Mirza", "Naghma",
                "Naqvi", "Niazi", "Pasha", "Peerzada", "Qazi", "Qazilbash", "Rahim", "Randhawa", "Sahotra", "Satti",
                "Shah", "Shami", "Sharif", "Sial", "Siddiqui", "Soomro", "Sulehria", "Syed", "Tareen", "Tiwana",
                "Toor", "Turk", "Wattoo", "Yousaf", "Yousuf", "Zafar", "Zardari", "Zia", "Zuberi", "Zulfiqar"
            ]
        },
        "USA": {
            "male": [
                "James", "John", "Robert", "Michael", "David", "William", "Richard", "Joseph", "Thomas", "Charles",
                "Christopher", "Daniel", "Matthew", "Anthony", "Donald", "Mark", "Paul", "Steven", "Andrew", "Kenneth",
                "Joshua", "Kevin", "Brian", "George", "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan",
                "Jacob", "Gary", "Nicholas", "Eric", "Stephen", "Jonathan", "Larry", "Justin", "Scott", "Brandon",
                "Benjamin", "Samuel", "Frank", "Gregory", "Raymond", "Alexander", "Patrick", "Jack", "Dennis", "Jerry",
                "Tyler", "Aaron", "Jose", "Henry", "Douglas", "Adam", "Peter", "Nathan", "Zachary", "Walter",
                "Kyle", "Harold", "Carl", "Jeremy", "Keith", "Roger", "Gerald", "Ethan", "Arthur", "Terry",
                "Christian", "Sean", "Lawrence", "Austin", "Joe", "Noah", "Jesse", "Albert", "Bryan", "Billy"
            ],
            "female": [
                "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen",
                "Nancy", "Lisa", "Margaret", "Betty", "Sandra", "Ashley", "Dorothy", "Kimberly", "Emily", "Donna",
                "Michelle", "Carol", "Amanda", "Melissa", "Deborah", "Stephanie", "Rebecca", "Laura", "Sharon", "Cynthia",
                "Kathleen", "Amy", "Shirley", "Angela", "Helen", "Anna", "Brenda", "Pamela", "Nicole", "Samantha",
                "Katherine", "Emma", "Ruth", "Christine", "Catherine", "Debra", "Rachel", "Carolyn", "Janet", "Virginia",
                "Maria", "Heather", "Diane", "Julie", "Joyce", "Victoria", "Kelly", "Christina", "Lauren", "Joan",
                "Evelyn", "Olivia", "Judith", "Megan", "Cheryl", "Martha", "Andrea", "Frances", "Hannah", "Jacqueline",
                "Ann", "Gloria", "Jean", "Kathryn", "Alice", "Teresa", "Sara", "Janice", "Doris", "Madison"
            ],
            "last": [
                "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
                "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
                "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
                "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
                "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
                "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
                "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
                "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson"
            ]
        },
        "UK": {
            "male": [
                "Oliver", "George", "Harry", "Jack", "Jacob", "Charlie", "Thomas", "James", "William", "Leo",
                "Alfie", "Henry", "Joshua", "Freddie", "Archie", "Ethan", "Joseph", "Samuel", "Daniel", "Logan",
                "Edward", "Lucas", "Max", "Isaac", "Mason", "Theo", "Mohammed", "Alexander", "Benjamin", "Dylan",
                "Harrison", "Adam", "Zachary", "Teddy", "Riley", "Arthur", "Toby", "Jude", "Louie", "Nathan",
                "Ryan", "Lewis", "Matthew", "Harvey", "Luke", "Harley", "Reuben", "Michael", "Blake", "David",
                "Stanley", "Elijah", "Callum", "Kayden", "Gabriel", "Leon", "Oscar", "Jaxon", "Roman", "Elliot",
                "Finley", "Caleb", "Sebastian", "Connor", "Jayden", "Aaron", "Asher", "Dominic", "Kai", "Luca",
                "Andrew", "Theodore", "Louis", "Ezra", "Hudson", "Aiden", "Rory", "Reggie", "Jesse", "Felix"
            ],
            "female": [
                "Amelia", "Olivia", "Isla", "Emily", "Poppy", "Ava", "Isabella", "Jessica", "Lily", "Sophia",
                "Mia", "Evie", "Ruby", "Ella", "Scarlett", "Grace", "Freya", "Chloe", "Isabelle", "Daisy",
                "Phoebe", "Florence", "Alice", "Charlotte", "Sienna", "Matilda", "Evelyn", "Eva", "Millie", "Sofia",
                "Lucy", "Elsie", "Imogen", "Layla", "Rosie", "Maya", "Esme", "Elizabeth", "Lola", "Willow",
                "Ivy", "Erin", "Holly", "Emilia", "Molly", "Ellie", "Jasmine", "Eliza", "Abigail", "Georgia",
                "Maisie", "Eleanor", "Hannah", "Harriet", "Amber", "Bella", "Thea", "Annabelle", "Emma", "Amelie",
                "Harper", "Gracie", "Rose", "Summer", "Martha", "Violet", "Penelope", "Anna", "Nancy", "Zara",
                "Maria", "Darcie", "Maryam", "Clara", "Aisha", "Darcy", "Hollie", "Robyn", "Julia", "Lottie"
            ],
            "last": [
                "Smith", "Jones", "Taylor", "Brown", "Williams", "Wilson", "Johnson", "Davies", "Robinson", "Wright",
                "Thompson", "Evans", "Walker", "White", "Roberts", "Green", "Hall", "Wood", "Jackson", "Clarke",
                "Harris", "Clark", "Turner", "Martin", "Hill", "Scott", "Cooper", "Morris", "King", "Ward",
                "Moore", "Watson", "Baker", "Harrison", "Young", "Allen", "Anderson", "Mitchell", "Lee", "Parker",
                "James", "Bell", "Davis", "Bennett", "Phillips", "Richardson", "Shaw", "Cook", "Murphy", "Price",
                "Simpson", "Carter", "Bailey", "Collins", "Adams", "Wilkinson", "Foster", "Khan", "Patel", "Russell",
                "Hughes", "Griffiths", "Owen", "Marshall", "Ellis", "Fisher", "Reynolds", "Stevens", "Murray", "Gibson",
                "Gordon", "Dixon", "Mason", "Palmer", "Webb", "Holmes", "Rogers", "Stewart", "Reid", "Atkinson"
            ]
        },
        "India": {
            "male": [
                "Rajesh", "Amit", "Vikram", "Sanjay", "Anil", "Rahul", "Suresh", "Ravi", "Arun", "Naveen",
                "Abhishek", "Aditya", "Akshay", "Alok", "Amar", "Anand", "Ankur", "Ashok", "Bharat", "Deepak",
                "Dinesh", "Gaurav", "Girish", "Gopal", "Harsh", "Hemant", "Ishaan", "Jatin", "Jayant", "Karan",
                "Kunal", "Lalit", "Manish", "Mayank", "Mohan", "Nikhil", "Nitin", "Pankaj", "Piyush", "Prakash",
                "Prashant", "Prem", "Rajan", "Rajiv", "Rakesh", "Ramesh", "Rishabh", "Rohit", "Sachin", "Sameer",
                "Sandeep", "Satish", "Shivam", "Sohan", "Subhash", "Suman", "Sunil", "Sushant", "Tarun", "Uday",
                "Umesh", "Vaibhav", "Varun", "Vedant", "Vijay", "Vinay", "Vinod", "Vishal", "Yash", "Yogesh",
                "Adarsh", "Akash", "Aman", "Anshul", "Arjun", "Ashish", "Atul", "Brijesh", "Chandan", "Dheeraj"
            ],
            "female": [
                "Priya", "Neha", "Anjali", "Pooja", "Divya", "Shreya", "Kavita", "Sunita", "Rekha", "Meena",
                "Aarti", "Aditi", "Aishwarya", "Alka", "Amrita", "Ananya", "Ankita", "Archana", "Arpita", "Asha",
                "Bhavna", "Charu", "Deepa", "Dipika", "Gayatri", "Geeta", "Hema", "Isha", "Jaya", "Jyoti",
                "Kajal", "Kalpana", "Kanika", "Kiran", "Kriti", "Lata", "Madhu", "Manju", "Meera", "Monika",
                "Naina", "Namrata", "Nandini", "Nidhi", "Nisha", "Pallavi", "Parul", "Poonam", "Preeti", "Radha",
                "Rashmi", "Ritu", "Roshni", "Sakshi", "Saloni", "Sangeeta", "Sarika", "Seema", "Shilpa", "Shivani",
                "Shweta", "Simran", "Smita", "Sonal", "Sonam", "Sonia", "Suman", "Swati", "Tanvi", "Tanya",
                "Trisha", "Usha", "Vandana", "Vidya", "Vineeta", "Yamini", "Zoya", "Aarohi", "Anamika", "Bhoomi"
            ],
            "last": [
                "Patel", "Sharma", "Singh", "Kumar", "Gupta", "Verma", "Reddy", "Mehta", "Choudhary", "Malhotra",
                "Agarwal", "Arora", "Bansal", "Bhatia", "Chauhan", "Dubey", "Garg", "Goswami", "Iyer", "Jain",
                "Joshi", "Kapoor", "Khanna", "Kulkarni", "Mishra", "Naidu", "Pandey", "Pillai", "Rao", "Saxena",
                "Seth", "Shah", "Shukla", "Sinha", "Srivastava", "Tiwari", "Trivedi", "Varma", "Venkatesh", "Yadav",
                "Acharya", "Bakshi", "Chatterjee", "Desai", "Dwivedi", "Ganguly", "Grover", "Hegde", "Jha", "Khatri",
                "Kohli", "Luthra", "Mahajan", "Menon", "Nair", "Oberoi", "Puri", "Rana", "Sarin", "Sawant",
                "Sengupta", "Shetty", "Sood", "Tandon", "Thakur", "Upadhyay", "Vohra", "Walia", "Zaveri", "Aggarwal",
                "Bhardwaj", "Chakraborty", "Dutta", "Gandhi", "Hussain", "Kaur", "Mittal", "Nagpal", "Prasad", "Rastogi"
            ]
        }
    }
    
    if country not in names:
        country = "USA"
    
    gender_key = "male" if gender == 1 else "female"
    first = random.choice(names[country][gender_key])
    last = random.choice(names[country]["last"])
    return first, last

def get_random_tablet_ua():
    android_versions = [
        ("5.0", "LRX21Q"), ("5.0.1", "LRX22C"), ("5.0.2", "LRX22G"), ("5.1", "LMY47D"), ("5.1.1", "LMY48B"),
        ("6.0", "MRA58K"), ("6.0.1", "MMB29K"), ("7.0", "NRD90M"), ("7.1", "NMF26F"), ("7.1.1", "NMF26X"),
        ("8.0", "OPR1.170623.032"), ("8.1", "OPM1.171019.011"), ("9", "PPR1.180610.011"), ("10", "QP1A.190711.020"),
        ("11", "RP1A.201005.001"), ("12", "SP1A.210812.016"), ("13", "TP1A.220624.021"), ("14", "UP1A.231005.007"),
        ("15", "AP1A.240405.002")
    ]    
    tablet_models = [
        ("Samsung", "SM-T580", "gta2xlte"), ("Samsung", "SM-T590", "gtanotexl"), ("Samsung", "SM-T720", "gts7l"),
        ("Samsung", "SM-T510", "gta3xl"), ("Samsung", "SM-T290", "gtowifi"), ("Samsung", "SM-P610", "ltahifi"),
        ("Lenovo", "TB-X606F", "X606F"), ("Lenovo", "TB-8505F", "TB-8505F"), ("Lenovo", "TB-J606F", "TB-J606F"),
        ("Huawei", "AGS2-W09", "hwags2"), ("Huawei", "BAH3-W09", "hwbah3"), ("Huawei", "KOB2-W09", "hwkob2"),
        ("Amazon", "KFSUWI", "full_amazon"), ("Amazon", "KFARWI", "full_amazon"), ("Amazon", "KFGIWI", "full_amazon"),
        ("Xiaomi", "21051182G", "nabu"), ("Xiaomi", "22081283G", "diting"), ("Xiaomi", "23043RP34G", "marble"),
        ("Realme", "RMP2103", "RMX2103"), ("Realme", "RMP2104", "RMX2104"), ("Realme", "RMP2205", "RMX2205"),
        ("Oppo", "CPH2207", "OP4F2F"), ("Oppo", "CPH2305", "OP4F3F"), ("Oppo", "CPH2411", "OP4F4F"),
        ("Vivo", "PA2353", "PD2153"), ("Vivo", "PA2373", "PD2173"), ("Vivo", "PA2393", "PD2193"),
        ("OnePlus", "OP5000L1", "OnePlus5000"), ("OnePlus", "OP5100L1", "OnePlus5100"), ("OnePlus", "OP5200L1", "OnePlus5200"),
        ("Nokia", "TA-1398", "NokiaTablet"), ("Nokia", "TA-1399", "NokiaTablet"), ("Nokia", "TA-1400", "NokiaTablet"),
        ("Sony", "XQ-BT52", "SonyTablet"), ("Sony", "XQ-BT72", "SonyTablet"), ("Sony", "XQ-BT92", "SonyTablet"),
        ("Asus", "ASUS_X00ID", "ASUS_X00ID"), ("Asus", "ASUS_X01AD", "ASUS_X01AD"), ("Asus", "ASUS_X02BD", "ASUS_X02BD"),
        ("Acer", "A3-A40", "acer_a3a40"), ("Acer", "B3-A30", "acer_b3a30"), ("Acer", "B3-A40", "acer_b3a40"),
        ("Alcatel", "9024S", "Alcatel_9024S"), ("Alcatel", "9025S", "Alcatel_9025S"), ("Alcatel", "9026S", "Alcatel_9026S"),
        ("TCL", "9027S", "TCL_9027S"), ("TCL", "9028S", "TCL_9028S"), ("TCL", "9029S", "TCL_9029S"),
        ("LG", "LM-T600", "lm-t600"), ("LG", "LM-T605", "lm-t605"), ("LG", "LM-T610", "lm-t610"),
        ("ZTE", "ZTE K92", "P731F20"), ("ZTE", "ZTE K93", "P731F30"), ("ZTE", "ZTE K94", "P731F40"),
        ("BlackBerry", "BBG100-1", "bbg100"), ("BlackBerry", "BBG100-2", "bbg100"), ("BlackBerry", "BBG100-3", "bbg100"),
        ("Google", "Pixel C", "dragon"), ("Google", "Pixel Tablet", "tangorpro"), ("Google", "Pixel Tablet Pro", "tangorplus"),
        ("Microsoft", "Surface Duo", "SurfaceDuo"), ("Microsoft", "Surface Duo 2", "SurfaceDuo2"), ("Microsoft", "Surface Duo 3", "SurfaceDuo3"),
        ("HTC", "HTC 2Q7A100", "htc_2q7a100"), ("HTC", "HTC 2Q7A200", "htc_2q7a200"), ("HTC", "HTC 2Q7A300", "htc_2q7a300"),
        ("Motorola", "XT2115-2", "moto_g_tab"), ("Motorola", "XT2125-2", "moto_g_tab_plus"), ("Motorola", "XT2135-2", "moto_g_tab_max"),
        ("Tecno", "TECNO Pova", "TECNO_Pova"), ("Tecno", "TECNO Camon", "TECNO_Camon"), ("Tecno", "TECNO Spark", "TECNO_Spark"),
        ("Infinix", "Infinix X", "Infinix_X"), ("Infinix", "Infinix Y", "Infinix_Y"), ("Infinix", "Infinix Z", "Infinix_Z")
    ]
    manufacturer, model, device = random.choice(tablet_models)
    android_version, build_version = random.choice(android_versions)
    chrome_version = f"{random.randint(70,120)}.0.{random.randint(1000,9999)}.{random.randint(1,200)}"
    ua_templates = [
        f"[FB_IAB/FB4A;FBAV/488.0.0.78.79;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/488.0.0.78.79;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/502.0.0.66.79;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/493.0.0.72.158;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/495.0.0.45.201;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/522.0.0.52.96;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/519.0.0.44.92;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/520.0.0.44.99;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/520.0.0.44.99;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/519.0.0.44.92;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/518.0.0.63.86;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/515.1.0.62.90;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/514.0.0.65.72;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/510.0.0.72.41;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/510.0.0.72.41;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/510.0.0.72.41;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/510.0.0.72.41;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/510.0.0.72.41;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/510.0.0.72.41;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/513.1.0.66.92;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/507.0.0.66.49;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/514.0.0.65.72;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/512.0.0.64.75;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/511.0.0.73.36;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/508.0.0.74.47;IABMV/1;]",
        f"[FB_IAB/FB4A;FBAV/507.0.0.66.49;IABMV/1;]"
    ]
    
    # Select and format a random template
    user_agent = random.choice(ua_templates)
    return (
        f"Mozilla/5.0 (Linux; Android {android_version}; {model} Build/{build_version}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 "
    )

def extract_values(response_text):
    """Extract all required values from the response text."""
    soup = BeautifulSoup(response_text, 'html.parser')
    
    # Extract hidden form fields
    hidden_inputs = soup.find_all('input', type='hidden')
    form_data = {}
    for input_field in hidden_inputs:
        name = input_field.get('name')
        value = input_field.get('value', '')
        form_data[name] = value
    
    # Extract other required values using regex
    values = {
        'haste_session': re.search(r'"haste_session":"([^"]+)"', response_text),
        'hsi': re.search(r'"hsi":"([^"]+)"', response_text),
        'spin_r': re.search(r'"__spin_r":(\d+)', response_text),
        'spin_t': re.search(r'"__spin_t":(\d+)', response_text),
        'spin_b': re.search(r'"__spin_b":"([^"]+)"', response_text),
        'spin_y': re.search(r'"spin_y":(\d+)', response_text),
        'lsd_token': re.search(r'LSD",\[\],{"token":"([^"]+)"', response_text),
        'jazoest': re.search(r'jazoest=(\d+)', response_text),
        'reg_instance': re.search(r'"reg_instance":"([^"]+)"', response_text),
        'captcha_persist_data': re.search(r'"captcha_persist_data":"([^"]+)"', response_text),
        'ri': re.search(r'"ri":"([^"]+)"', response_text)
    }
    
    extracted = {}
    for key, match in values.items():
        extracted[key] = match.group(1) if match else ""
    extracted.update(form_data)    
    return extracted


def register_account(firstname, lastname, reg_contact, password, gender, country, contact_type):
    max_retries = 3
    retry_delay = 10
    
    for attempt in range(max_retries):
        try:
            session = requests.Session()
            time.sleep(3)    
            ua = get_random_tablet_ua()
            
            headers_get = {
                'authority': 'web.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ua,
            }
            
            try:
                # Add timeout and retry for initial requests
                response = session.get('https://web.facebook.com/', headers=headers_get, timeout=30)
                response = session.get('https://web.facebook.com/r.php?entry_point=login', headers=headers_get, timeout=30)
            except requests.exceptions.RequestException as e:
                print(f"{RED}{FAILURE} Connection error (attempt {attempt+1}), retrying in {retry_delay} seconds...{RESET}")
                time.sleep(retry_delay)
                continue
                
            extracted = extract_values(response.text)
            
            bd = str(random.randint(1, 28))
            bm = str(random.randint(1, 12))
            by = str(random.randint(1988, 2000))
            print(f"{BLUE}{INFO}    DOB: {GREEN}{bd}/{bm}/{by}{RESET}")
            time.sleep(3)
            
            data = {
            'jazoest': extracted.get('jazoest', ''),
            'lsd': extracted.get('lsd', ''),
            'reg_instance': extracted.get('reg_instance', ''),
            'ri': extracted.get('ri', ''),
            'firstname': firstname,
            'lastname': lastname,
            'reg_email__': reg_contact,
            'reg_email_confirmation__': reg_contact,
            'reg_passwd__': f'#PWD_BROWSER:0:{int(time.time())}:{password}',
            'sex': str(gender),
            'birthday_day': bd,
            'birthday_month': bm,
            'birthday_year': by,
            'birthday_age': '',
            'did_use_age': 'false',
            'preferred_pronoun': '',
            'custom_gender': '',
            'referrer': '',
            'asked_to_login': '0',
            'use_custom_gender': '',
            'terms': 'on',
            'ns': '0',
            'action_dialog_shown': '',
            'invid': '',
            'a': '',
            'oi': '',
            'locale': 'en_US',
            'app_bundle': '',
            'app_data': '',
            'reg_data': '',
            'app_id': '',
            'fbpage_id': '',
            'reg_oid': '',
            'openid_token': '',
            'uo_ip': '',
            'guid': '',
            'key': '',
            're': '',
            'mid': '',
            'fid': '',
            'reg_dropoff_id': '',
            'reg_dropoff_code': '',
            'ignore': 'captcha|reg_email_confirmation__',
            'captcha_persist_data': extracted.get('captcha_persist_data', ''),
            'captcha_response': '',
            '__user': '0',
            '__a': '1',
            '__req': '1',
            '__hs': extracted.get('haste_session', ''),
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': extracted.get('spin_r', ''),
            '__s': f'{secrets.token_hex(3)}:{secrets.token_hex(3)}:{secrets.token_hex(3)}',
            '__hsi': extracted.get('hsi', ''),
            '__csr': '',
            '__spin_r': extracted.get('spin_r', ''),
            '__spin_b': extracted.get('spin_b', 'trunk'),
            '__spin_t': extracted.get('spin_t', '')
        }

            headers_post = {
            'x-asbd-id': '359341',
            'sec-ch-ua-platform': '"Linux"',
            'x-fb-lsd': extracted.get('lsd', ''),
            'user-agent': ua,
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'content-type': 'application/x-www-form-urlencoded',
            'sec-ch-ua-mobile': '?0',
            'accept': '*/*',
            'origin': 'https://www.facebook.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors', 
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.facebook.com/r.php?entry_point=login',
            'priority': 'u=1, i'
        }

            print(f"{BLUE}{INFO}   SUBMITTING REGISTRATION FORM (Attempt {attempt+1}){RESET}")
            
            try:
                response = session.post(
                    'https://www.facebook.com/ajax/register.php',
                    headers=headers_post,
                    data=data,
                    timeout=30
                )
                
                if "for (;;);" in response.text:
                    json_data = json.loads(response.text.replace("for (;;);", ""))
                    if json_data.get("payload", {}).get("registration_succeeded"):
                        # Direct success (rare)
                        cookies = session.cookies.get_dict()
                        if 'c_user' in cookies:
                            uid = cookies['c_user']
                            cookie_str = ";".join([f"{k}={v}" for k,v in cookies.items() if v])
                            print(f"{BLUE}{INFO}    UID: {GREEN}{uid}{RESET}")
                            print(f"{BLUE}{INFO}    Password: {GREEN}{password}{RESET}")
                            print(f"{BLUE}{INFO}    {GREEN}Cookies 🍪: {RESET}{cookie_str}{RESET}")
                            save_line = f"{uid}|{password}|{cookie_str}|{reg_contact}\n"
                            file_path = "/sdcard/ali_novery.txt"
                            try:
                                with open(file_path, "a", encoding="utf-8") as file:
                                    file.write(save_line)
                                return "OK"
                            except IOError as e:
                                print(f"{RED}{FAILURE} Failed to save account details: {e}{RESET}")
                                return "OK"
                
                # Assume OTP needed
                contact_emoji = PHONE if contact_type == "phone" else EMAIL
                print(f"{BLUE}{contact_emoji} OTP sent to {contact_type}: {reg_contact}. Please check your {contact_type}.{RESET}")
                otp = input(f"{BLUE}{INFO} Enter OTP: {RESET}")
                
                # Prepare confirmation data
                confirmation_data = {
                    'lsd': data['lsd'],
                    'jazoest': data['jazoest'],
                    '__user': '0',
                    '__a': '1',
                    '__req': '2',  # Increment req
                    '__hs': data['__hs'],
                    'dpr': '1',
                    '__ccg': 'EXCELLENT',
                    '__rev': data['__rev'],
                    '__s': data['__s'],
                    '__hsi': data['__hsi'],
                    '__csr': '',
                    '__spin_r': data['__spin_r'],
                    '__spin_b': data['__spin_b'],
                    '__spin_t': data['__spin_t'],
                    'confirmation_code': otp,
                    # Add other fields if needed
                    'reg_instance': data['reg_instance'],
                    'ri': data['ri']
                }
                
                # Post to confirmation endpoint
                response2 = session.post(
                    'https://www.facebook.com/ajax/account/confirmation/',
                    headers=headers_post,
                    data=confirmation_data,
                    timeout=30
                )
                
                # Check for success
                if "for (;;);" in response2.text:
                    json_data2 = json.loads(response2.text.replace("for (;;);", ""))
                    if not json_data2.get("error") and ("success" in str(json_data2).lower() or "confirmed" in str(json_data2).lower()):
                        # Get final cookies by visiting home
                        session.get('https://www.facebook.com/', headers=headers_get, timeout=30)
                        cookies = session.cookies.get_dict()
                        if 'c_user' in cookies:
                            uid = cookies['c_user']
                            cookie_str = ";".join([f"{k}={v}" for k,v in cookies.items() if v])
                            print(f"{BLUE}{INFO}    UID: {GREEN}{uid}{RESET}")
                            print(f"{BLUE}{INFO}    Password: {GREEN}{password}{RESET}")
                            print(f"{BLUE}{INFO}    {GREEN}Cookies 🍪: {RESET}{cookie_str}{RESET}")
                            save_line = f"{uid}|{password}|{cookie_str}|{reg_contact}\n"
                            file_path = "/sdcard/ali_novery.txt"
                            try:
                                with open(file_path, "a", encoding="utf-8") as file:
                                    file.write(save_line)
                                return "OK"
                            except IOError as e:
                                print(f"{RED}{FAILURE} Failed to save account details: {e}{RESET}")
                                return "OK"
                    else:
                        print(f"{RED}{FAILURE} OTP verification failed (Attempt {attempt+1}){RESET}")
                        time.sleep(retry_delay)
                        continue
                else:
                    print(f"{RED}{FAILURE} Unexpected response in OTP verification (Attempt {attempt+1}){RESET}")
                    time.sleep(retry_delay)
                    continue
                
            except requests.exceptions.RequestException as e:
                print(f"{RED}{FAILURE} Request failed (attempt {attempt+1}): {e}{RESET}")
                time.sleep(retry_delay)
                continue
                
        except Exception as e:
            print(f"{RED}{FAILURE} Unexpected error (attempt {attempt+1}): {e}{RESET}")
            time.sleep(retry_delay)
            continue
    
    print(f"{RED}{FAILURE} Max retries reached. Giving up.{RESET}")
    return "CP"


def main():
print(f"{BLUE}{INFO}    Facebook Account Creator{RESET}")
    print(f"{DIVIDER}{RESET}")
    
    num_accounts = int(input(f"{BLUE}{INFO}    How many accounts do you want to create? {RESET}"))
    
    print(f"{BLUE}{INFO}    1. Male{RESET}")
    print(f"{BLUE}{INFO}    2. Female{RESET}")
    gender = int(input(f"{BLUE}{INFO}    Select gender (1/2): {RESET}"))
    
    print(f"{BLUE}{INFO}    1. Pakistan{RESET}")
    print(f"{BLUE}{INFO}    2. USA{RESET}")
    print(f"{BLUE}{INFO}    3. UK{RESET}")
    print(f"{BLUE}{INFO}    4. India{RESET}")
    country_choice = int(input(f"{BLUE}{INFO}    Select country (1-4): {RESET}"))
    
    countries = {1: "Pakistan", 2: "USA", 3: "UK", 4: "India"}
    country = countries.get(country_choice, "Pakistan")
    
    password = input(f"{BLUE}{INFO}    Enter password for all accounts: {RESET}")
    
    print(f"{BLUE}{INFO}    1. Use Phone for registration{RESET}")
    print(f"{BLUE}{INFO}    2. Use Email for registration{RESET}")
    contact_choice = int(input(f"{BLUE}{INFO}    Select contact type (1/2): {RESET}"))
    
    if contact_choice == 1:
        contact_type = "phone"
        contact_label = PHONE + " Phone"
    else:
        contact_type = "email"
        contact_label = EMAIL + " Email"
    
    ok = 0
    cp = 0
    
    print(f"{DIVIDER}{RESET}")
    for i in range(num_accounts):
        firstname, lastname = generate_name(country, gender)
        
        reg_contact = input(f"{BLUE}{INFO}    Enter {contact_label} for account {i+1}: {RESET}".strip())
        
        # Optional other contact
        other_type = "email" if contact_type == "phone" else "phone"
        other_label = EMAIL + " Email" if other_type == "email" else PHONE + " Phone"
        other_contact = input(f"{BLUE}{INFO}    Enter {other_label} (optional, add manually later): {RESET}".strip()) or None
        
        print(f"{BLUE}{INFO}    Creating account {i+1}/{num_accounts}{RESET}")
        time.sleep(3)
        print(f"{BLUE}{INFO}    Name: {GREEN}{firstname} {lastname}{RESET}")
        time.sleep(3)
        print(f"{BLUE}{INFO}    {contact_label}: {GREEN}{reg_contact}{RESET}")
        if other_contact:
            print(f"{BLUE}{INFO}    {other_label}: {GREEN}{other_contact}{RESET}")
        
        result = register_account(firstname, lastname, reg_contact, password, gender, country, contact_type)
        
        if result == "OK":
            ok += 1
            print(f"{GREEN}{SUCCESS} Account created successfully{RESET}")
            if other_contact:
                print(f"{WARNING} Remember to add the {other_type} ({other_contact}) manually after logging in.{RESET}")
        else:
            cp += 1
            print(f"{RED}{FAILURE} Account creation failed{RESET}")
        
        print(f"{BLUE}{INFO}    Status: {GREEN}OK={ok}{RESET} {RED}CP={cp}{RESET}")
        print(f"{DIVIDER}{RESET}")
        time.sleep(3)

if __name__ == "__main__":
    main()