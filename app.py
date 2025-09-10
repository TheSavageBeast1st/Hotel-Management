import mysql.connector as sq


def display_welcome_message():
    print("ONLINE HOTEL BOOKING\n********************\n")
    print("Welcome to Baratie Hotel! The Best Coastal Resort in Town!")


def check_in():
    print("\nWhat inquiry do you have?")
    print("1. Suites and Pricing")
    print("2. Check Availability of Hotel Room")
    print("3. Entertainment Facilities")
    print("4. What's Nearby")
    print("5. Cancel Booking")
    print("6. View Amenities")
    print("7. Leave")
    
    try:
        n = int(input(">>> "))
        return n
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
        return check_in()


def suites_and_pricing():
    
    print("Captain:\nDesigned for the discerning traveler who appreciates both style and comfort, the Captain Suite is the perfect balance of elegance and functionality. With a spacious layout, the suite features a king-size bed with premium linens, a separate seating area with plush armchairs, and a work desk. The decor reflects nautical themes with subtle hints of maritime adventure, combining deep blues and warm woods. A well-appointed bathroom with a soaking tub and separate shower ensures ultimate relaxation. Whether you're preparing for a long journey or winding down after a day of exploration, the Captain Suite offers a serene, welcoming environment.\n\nComes with: \n> Two Beds \n> One Bathroom \n> Television Connection with 120 + Channels \n> Air Conditioning \n> Complementary Coffee, Tea and Breakfast \n> Balcony View \n> Access to in-house Gym \n> Mini Fridge (Non-Complementary)\n")
    
    print("Vice Admiral:\nElevating your stay to new heights, the Vice Admiral Suite is designed for guests who desire a greater sense of opulence and space. Larger than the Captain Suite, this suite offers a private lounge area with a full bar, perfect for entertaining guests or unwinding after a busy day. The bedroom boasts a luxurious king-size bed and a designer walk-in closet, while the en-suite bathroom features a soaking tub with a view, a rainfall shower, and dual vanities. The suite’s refined decor blends classic nautical motifs with contemporary luxury, creating an ambiance of sophistication and grandeur. With panoramic views of the ocean or cityscape, the Vice Admiral Suite is your personal haven of indulgence.\n\nComes with: \n> Three Beds \n> Two Bathrooms \n> Smart Television Connection with 120 + Channels and 10 + OTT Subscriptions \n> Air Conditioning \n> Complementary Coffee, Tea, Breakfast and Dinner \n> Balcony View \n> Access to in-house Gym, Bar and Swimming Pool \n> Mini Fridge (Non-Complementary)\n")
    
    print("Fleet Admiral:\nThe pinnacle of luxury at Baratie Hotel, the Fleet Admiral Suite offers an extraordinary experience for guests seeking the ultimate in comfort and grandeur. This expansive suite features a master bedroom with a California king bed, complete with 800-thread-count Egyptian cotton sheets, a private spa area, and a dedicated dining room. A separate study or library offers a peaceful retreat, while the living area is perfect for entertaining with an elegant bar, a baby grand piano, and floor-to-ceiling windows that provide breathtaking, unobstructed views of the horizon. The bathroom is a sanctuary of indulgence, with a double jacuzzi, a steam shower, and a sauna, along with high-end toiletries. Personalized service is at your fingertips, ensuring every detail of your stay is beyond expectation.\n\nComes with: \n> Four Beds \n> Two Bathrooms \n> Smart Television Connection with 120 + Channels and 10 + OTT Subscriptions \n> Air Conditioning \n> Complementary Coffee, Tea, Breakfast, Lunch and Dinner \n> Balcony View \n> Private Jacuzzi \n> Access to in-house Gym, Bar, Swimming Pool, Tennis Court and Basketball Court \n> Access to Special VIP Lounge \n> Mini Fridge (Non-Complementary)\n")

    

    print("\nPricing:")
    print("Captain\tRs.6800/Night")
    print("Vice Admiral\t\tRs.9000/Night")
    print("Fleet Admiral\t\tRs.13000/Night")

    print("Each suite at Baratie Hotel reflects the dedication to luxury and attention to detail, ensuring a memorable stay regardless of which level you choose. Whether you're a seasoned traveler or simply seeking a special escape, we offer the perfect suite for every need and desire.")


def show_entertainment_facilities():
    print("Baratie Hotel Offers Many Entertainment Facilities to It's Visitors!\n")

    entertainment_areas = [("Spa & Wellness Center", "Indulge in rejuvenating treatments like massages, facials, body scrubs, and therapeutic rituals at the resort's world-class spa."),("Gourmet Dining Experiences", "Savor local and international cuisine at the resort's fine dining restaurants, casual eateries, or beachfront seafood grills."),("Water Sports & Activities", "Explore a wide variety of water activities, from snorkeling in crystal-clear waters to diving excursions, sailing lessons, or even surfing."),("Fitness Center & Outdoor Activities", "Stay active with access to a fully-equipped gym, fitness classes (yoga, pilates, spinning), and outdoor adventures such as ."),("Tennis Courts & Sports Complex", "Enjoy a friendly match on the resort's premium tennis courts or try other activities like pickleball, or basketball.")]
    
    for name, description in entertainment_areas:
        print(f"{name}\n{description}\n")


def show_nearby_places():
    places = ["Marine Ford Stadium", "Longest Pier on Earth at Pearl Harbour", "City Park and Botanical Gardens", "Museum of Local Art & Culture", "Ocean View Lookout", "Scuba diving, Surfing, Fishing and More at Wano Beach", "Aquarium & Marine Life Exhibit", "Thriller Bark Theme Park"]
    
    print("\nSome of the Appealing Nearby Destinations to Visit:")
    for i, place in enumerate(places, 1):
        print(f"{i}. {place}")

def view_amenities():
    print("Welcome to the perfect blend of luxury, relaxation, and adventure at our stunning coastal hotel. Imagine waking up to the soothing sound of the waves and stepping into paradise with a wide array of world-class amenities designed to make your stay unforgettable. Unwind with direct access to pristine sandy shores, Crystal Clear Infinity Pool where the water meets the sky, Rejuvenating Spa & Wellness Seaside Dining, beach volleyball games and movie nights on the sand to lively music and fire pit gatherings, there's no shortage of entertainment. Your Dream Coastal Escape Awaits! Book now and let the ocean breeze be your guide!")

def room_booking():
    mycon=sq.connect(host="localhost",user="root",passwd="12345",database="baratiehotel")
    cur=mycon.cursor()
    s="select Room_No,Suite,Status from Baratie_Booking where Status='VACANT'"
    cur.execute(s)
    data=cur.fetchall()
    for row in data:
        print(row)
    s="select Suite, Cost_Per_Night from suite_pricing"
    cur.execute(s)
    c=cur.fetchall()
    
    
    while True:
        stat = 0
        a=""
        suite=input("Enter the suite you wish to stay in: ")
        for i in c:
            if suite == i[0]:
                cost = i[1]
        
        st = ['captain', 'vice admiral', 'fleet admiral']
        
        if suite.lower() not in st:
            print("The entered suite is not a valid suite")
            continue
        
        try:
            room=int(input("Enter number of the room you wish to stay in: "))
        
        except ValueError: 
            print("Please enter a valid option")
            continue
        
        if room >125 or room<101:
            print("Room does not exist")
            print("Please try again")
            continue
        for row in data:
            if row[2] == 'BOOKED':
                print("Room is already booked")
                print("Please try again")
                continue
        for row in data:
            if suite==row[1] and room==row[0]:
                print("Room available")
                break
        else:
            print("Room not available or chosen Suite does not match with room number")
            y=input("Do you wish to try again?y/n: ")
            if y=="n" or y=="N":
                break
            else:
                a="ok"
        if a=="ok":
            continue
        c=input("Do you wish to confirm?y/n: ")
        if c=="y" or c=="Y":
            stat += 1
            pass
        else:
            continue
        name=input("Enter your booking name: ")
        email=input("Enter your booking email: " )
        days=int(input("Enter number of days you wish to stay?: "))
        print("The Total cost comes to: ", cost * days, "Rs")
        c=input("Do you wish to confirm?y/n: ")
        if c=="y" or c=="Y":
            break
        else:
            continue
    if stat == 1:
        s="update Baratie_Booking set Status='BOOKED',Booking_Name='{0}',Booking_Email='{1}', No_Of_Days = {2} where (Room_No={3})".format(name,email,days,room)
        cur.execute(s)
        mycon.commit()
        s="select*from Baratie_Booking where Room_No='{0}'".format(room)
        cur.execute(s)
        p = cur.fetchall()
        total_cost = days * cost
        
        s = "update cost SET Total_Cost = {0} where Room_No = {1}".format(total_cost, room)
        
        cur.execute(s)
        mycon.commit()
        
        mycon.close()
        print("Thank you for booking with Baratie Hotel, We hope you enjoy your stay!")


def cancel():
    mycon=sq.connect(host="localhost",user="root",passwd="12345",database="baratiehotel")
    cur=mycon.cursor()
    s="select Room_No,Suite,Status, Booking_Email, Booking_Name from Baratie_Booking"
    cur.execute(s)
    data=cur.fetchall()

    
    while True:
        stat = 0
        try:
            no = int(input("Enter the Number of the Room that you wish to cancel booking for: "))
        except ValueError: 
            print("Please enter a valid option")
            continue

        if no >125 or no<101:
            print("Room does not exist")
            print("Please try again")
            continue
        else:
            for i in data:
                if i[0] == no and i[2] == 'BOOKED':
                    stat +=1
                    pass
                    
            if stat == 1:
                pass
            else:
                print("The selected room is vacant")
                y=input("Do you wish to try again?y/n: ")
                if y=="n" or y=="N":
                    break
                else:
                    continue

    
        suite = input("Enter the Suite of the Room that you wish to cancel booking for: ")
    
        st = ['Captain', 'Vice Admiral', 'Fleet admiral']
            
        if suite not in st:
            print("The entered suite is not a valid suite")
            y=input("Do you wish to try again?y/n")
            if y=="n" or y=="N":
                break
            else:
                continue
                
        email = input("Enter the Email that was used to book the room: ")
        
        
        for row in data: 
            if row[1] == suite and row[3] == email:
                try:
                    s = "update Baratie_Booking set Status = 'VACANT', Booking_Name = '-', Booking_Email = '-', No_Of_Days = NULL where Room_No = {0}".format(no)
                    cur.execute(s)
                    mycon.commit()
    
                    s = "update cost set Total_Cost = NULL, No_Of_Days = NULL where Room_No = {0}".format(no)
                    
                    cur.execute(s)
                    mycon.commit()
    
                    print("The booking has been successfully cancelled. Have a great day!")
                    break
                except sq.Error as e:
                    print(f"An error occurred while updating the database: {e}")
                    break
        else:
            print("Mismatch in the booking details. Please try again.")
            continue
        
        break
    
        
        
    
    


def main():
    display_welcome_message()
    
    while True:
        choice = check_in()
        
        if choice == 1:
            suites_and_pricing()
        elif choice == 2:
            room_booking()
        elif choice == 3:
            show_entertainment_facilities()
        elif choice == 4:
            show_nearby_places()
        elif choice == 5:
            cancel()
        elif choice == 6:
            view_amenities()
        elif choice == 7:
            print("\nThank you for using the Baratie Hotel Booking Page. Have a great day!")
            break
        else:
            print("\nInvalid choice. Please choose a number between 1 and 7.")


if __name__ == "__main__":
    main()
    
