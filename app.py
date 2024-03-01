# imports necessary libraries
import tkinter as tk
import PIL.Image
import pandas as pd
import csv
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from datetime import date, datetime
from help.helpers import clear_widgets, add_background_image
from tkcalendar import DateEntry

# create the gui
root = tk.Tk()
root.title("Concert Buddy")
# size the gui
screen_width = 360
screen_height = 640
root.minsize(screen_width, screen_height)

# configure the gui
root.configure(background="#FADCD8")


def display_age():
    # displays the age of the user on the profile page in the place of the button to select the birthdate

    pp_age_button.destroy()

    pp_calculated_age_label = tk.Label(root,
                                       text=f"{age}",
                                       font="SegueUI 12",
                                       fg="#E16856",
                                       bg="#FADCD8"
                                       )
    pp_calculated_age_label.place(x=70, y=60)


def calculate_age():
    global age

    dob = calendar.get_date()

    current_date = date.today()

    age = int((current_date - dob).days / 365.25)


def create_calendar():
    # opens a new window where the user can select their birthdate

    global calendar

    # create and configure the new the gui window
    calendar_window = tk.Tk()
    calendar_window.title("Select your birthdate")
    screen_width = 60
    screen_height = 200
    calendar_window.minsize(screen_width, screen_height)
    calendar_window.configure(background="#FADCD8")

    # add a label with instructions
    dob_label = tk.Label(calendar_window,
                         text="Select your date of birth",
                         font="Impact 15",
                         fg="#E16856",
                         bg="#FADCD8"
                         )
    dob_label.pack(anchor="center", side="top", padx="5", pady="5")

    # add the calendar
    calendar = DateEntry(calendar_window,
                         width=10,
                         font="SegueUI 12",
                         select_mode="day")
    calendar.place(x=20, y=50)

    # create a button to confirm the selected birthdate
    age_calc_button = tk.Button(calendar_window,
                                text="confirm",
                                font="SegueUI 12",
                                fg="#E16856",
                                bg="#FBF5F5",
                                activebackground="#E16856",
                                activeforeground="#FBF5F5",
                                command=lambda: [calculate_age(), calendar_window.destroy(), display_age()]
                                )
    age_calc_button.place(x=20, y=90)

    calendar_window.mainloop()


def create_profile_page():
    global pp_age_button

    # clears the page and adds the navigational shortcuts at the bottom
    clear_widgets(root)
    icon_shortcuts()

    # add necessary labels, buttons, entry-boxes, dropdown menus of the page
    pp_name_label = tk.Label(root,
                             text=f"Hello {name.get()}",
                             font="Impact 15",
                             fg="#3C4B66",
                             bg="#FADCD8"
                             )
    pp_name_label.pack(anchor=tk.CENTER, side="top", padx="5", pady="20")

    pp_age_label = tk.Label(root,
                            text=f"Age:",
                            font="SegueUI 12",
                            fg="#E16856",
                            bg="#FADCD8"
                            )
    pp_age_label.place(x=30, y=60)

    pp_age_button = tk.Button(root,
                              text="Select your birthdate",
                              font="SegueUI 12",
                              fg="#E16856",
                              bg="#FBF5F5",
                              activebackground="#E16856",
                              activeforeground="#FBF5F5",
                              command=create_calendar
                              )
    pp_age_button.place(x=70, y=60)

    pp_gender_label = tk.Label(root,
                               text="Gender:",
                               font="SegueUI 12",
                               fg="#E16856",
                               bg="#FADCD8"
                               )
    pp_gender_label.place(x=30, y=100)

    # add a dropdown menu to select the gender
    # define the options of the dropdown menu
    gender_options = [
        "female",
        "male",
        "non-binary",
        "divers",
        "prefer not to say"
    ]

    # define datatype of menu text
    clicked_gender = StringVar()

    # choose initial menu text
    clicked_gender.set("select your gender")

    # create the dropdown menu
    dropdown_gender = OptionMenu(root, clicked_gender, *gender_options)
    dropdown_gender.configure(bg="#FBF5F5",
                              fg="#E16856",
                              activebackground="#E16856",
                              activeforeground="#FBF5F5",
                              font="SegueUI 12",
                              highlightthickness=0)
    dropdown_gender.place(x=100, y=100)

    pp_location_label = tk.Label(root,
                                 text="My location:",
                                 font="SegueUI 12",
                                 fg="#E16856",
                                 bg="#FADCD8"
                                 )
    pp_location_label.place(x=30, y=140)

    location_entry = tk.Entry(root,
                              font="SegueUI 12",
                              bg="#FBF5F5",
                              fg="#3C4B66",
                              width=20
                              )
    location_entry.place(x=130, y=140)

    pp_education_label = tk.Label(root,
                                  text="My education/work:",
                                  font="SegueUI 12",
                                  fg="#E16856",
                                  bg="#FADCD8"
                                  )
    pp_education_label.place(x=30, y=180)

    education_entry = tk.Entry(root,
                               font="SegueUI 12",
                               bg="#FBF5F5",
                               fg="#3C4B66",
                               width=15
                               )
    education_entry.place(x=170, y=180)

    pp_language_label = tk.Label(root,
                                 text="Languages:",
                                 font="SegueUI 12",
                                 fg="#E16856",
                                 bg="#FADCD8"
                                 )
    pp_language_label.place(x=30, y=220)

    language_entry = tk.Entry(root,
                              font="SegueUI 12",
                              bg="#FBF5F5",
                              fg="#3C4B66"
                              )
    language_entry.place(x=130, y=220)

    pp_music_button = tk.Button(root,
                                text="connect your spotify/apple music account",
                                font="SegueUI 12",
                                fg="#E16856",
                                bg="#FBF5F5",
                                activebackground="#E16856",
                                activeforeground="#FBF5F5"
                                )
    pp_music_button.place(x=30, y=260)

    pp_social_button = tk.Button(root,
                                 text="connect your social media accounts",
                                 font="SegueUI 12",
                                 fg="#E16856",
                                 bg="#FBF5F5",
                                 activebackground="#E16856",
                                 activeforeground="#FBF5F5"
                                 )

    pp_social_button.place(x=30, y=300)

    # create a dropdown menu for the prompts
    # add dropdown menu options
    options_prompts = [
        "Currently on repeat:",
        "My go-to karaoke song:",
        "Which song makes you happy?",
        "What songs played at your wedding?",
        "Which artists would you want to meet?",
        "What was your favorite concert you’ve been to?",
        "Is there one artist you really want to see live?",
        "What is your guilty pleasure song?"
    ]

    # change datatype of menu text
    clicked_prompts = StringVar()

    # display initial menu text
    clicked_prompts.set("add prompts about your music taste")

    # create the dropdown menu
    dropdown_prompts = OptionMenu(root, clicked_prompts, *options_prompts)
    dropdown_prompts.configure(bg="#FBF5F5",
                               fg="#E16856",
                               activebackground="#E16856",
                               activeforeground="#FBF5F5",
                               font="SegueUI 12",
                               highlightthickness=0)
    dropdown_prompts.place(x=30, y=340)

    prompt_entry = tk.Entry(root,
                            font="SegueUI 12",
                            bg="#FBF5F5",
                            fg="#3C4B66")
    prompt_entry.place(x=30, y=380)


def display_concerts():
    # add a definition to display the concerts of the user on the concert page as a table

    # open the csv file with the concert data
    file = open("data/concert_data.csv")
    csvreader = csv.reader(file)

    # define the headers
    header_list = ["artist", "location", "date"]
    # create a list for the rows of data
    concert_entries = [row for row in csvreader]

    # create the treeview
    trv = ttk.Treeview(root, selectmode="browse")
    trv.pack(pady="10")
    # number a rows shown in the table (before scrolling)
    trv["height"] = 5
    # display the column headers
    trv["show"] = "headings"
    # define column headers
    trv["columns"] = header_list

    # define headers and columns
    for i in header_list[:3]:
        trv.column(i, width=100, anchor="c")
        trv.heading(i, text=i)

    # insert the data rows into the treeview
    for dt in concert_entries[1:]:
        v = [r for r in dt]
        trv.insert("", "end", iid=v[0], values=v)


def save_concert():
    # definition to save the entered concert info of the user in a csv file

    # create a timestamp
    current_timestamp = datetime.now()

    # define what data should be saved in a dictionary
    concert_data = {
        "artist": artist.get(),
        "location": location.get(),
        "date": date_of_concert.get(),
        "category": dropdown_choice.get(),
        "created-at": current_timestamp
    }

    # converting the dictionary to a data frame
    concert_data_df = pd.DataFrame([concert_data])
    # write data to a csv file
    concert_data_df.to_csv("data/concert_data.csv", index=False, header=False, mode='a')

    create_concerts_page()


def create_add_concert_page():
    # definition to add a page where the user can add a concert to their profile

    global artist, location, date_of_concert, dropdown_choice

    clear_widgets(root)
    icon_shortcuts()

    # add necessary labels, buttons, entry-boxes, dropdown menus of the page
    hello_label = tk.Label(root,
                           text="Please enter the information for the concert",
                           font="LucidBright 12 bold",
                           bg="#E16856",
                           fg="#FBF5F5"
                           )
    hello_label.pack(anchor=tk.CENTER, padx="5", pady="20")

    artist_label = tk.Label(text="Please enter the name of the artist*",
                            font="SegueUI 12",
                            fg="#E16856",
                            bg="#FADCD8"
                            )
    artist_label.place(x=30, y=60)

    artist = tk.StringVar()
    artist_entry = tk.Entry(root,
                            textvariable=artist,
                            font="SegueUI 12",
                            bg="#FBF5F5",
                            fg="#3C4B66"
                            )
    artist_entry.place(x=30, y=90)

    location_label = tk.Label(text="Please enter the location of the concert*",
                              font="SegueUI 12",
                              fg="#E16856",
                              bg="#FADCD8"
                              )
    location_label.place(x=30, y=130)

    location = tk.StringVar()
    location_entry = tk.Entry(root,
                              textvariable=location,
                              font="SegueUI 12",
                              bg="#FBF5F5",
                              fg="#3C4B66"
                              )
    location_entry.place(x=30, y=160)

    date_of_concert_label = tk.Label(text="Please enter the date of the concert*",
                                     font="SegueUI 12",
                                     fg="#E16856",
                                     bg="#FADCD8"
                                     )
    date_of_concert_label.place(x=30, y=200)

    date_of_concert = DateEntry(root,
                                width=10,
                                font="SegueUI 12",
                                select_mode="day")
    date_of_concert.place(x=30, y=240)

    seating_label = tk.Label(text="You can also enter your seat/standing category",
                             font="SegueUI 12",
                             fg="#E16856",
                             bg="#FADCD8"
                             )
    seating_label.place(x=30, y=270)

    # create dropdown menu for the seating/standing categories
    options = [
        "Standing K1",
        "Standing K2",
        "Seating K1 R1",
        "Seating K1 R2",
        "Seating K2 R1",
        "Seating K2 R2",
        "(these are just sample categories in practise they would correspond with the actual categories of the concert)"
    ]

    dropdown_choice = tk.StringVar()

    dropdown_choice.set("select here")

    dropdown_seating = OptionMenu(root, dropdown_choice, *options)
    dropdown_seating.configure(bg="#FBF5F5",
                               fg="#E16856",
                               activebackground="#E16856",
                               activeforeground="#FBF5F5",
                               font="SegueUI 12",
                               highlightthickness=0)
    dropdown_seating.place(x=30, y=300)

    # button to save the entered concert information
    submit_concert_button = tk.Button(root,
                                      text="SAVE",
                                      font="SegueUI 12 bold",
                                      bg="#E16856",
                                      fg="#FBF5F5",
                                      activebackground="#E16856",
                                      activeforeground="#FBF5F5",
                                      command=save_concert
                                      )
    submit_concert_button.place(x=150, y=400)

    star_label = tk.Label(text="*the starred categories are necessary to fill out.",
                          font="SegueUI 10",
                          fg="#3C4B66",
                          bg="#FADCD8"
                          )
    star_label.pack(side=tk.BOTTOM, anchor=tk.CENTER)


def create_concerts_page():
    clear_widgets(root)
    icon_shortcuts()

    # add necessary labels, buttons, entry-boxes, dropdown menus of the page
    concerts_label = tk.Label(root,
                              text="Your Concerts:",
                              font="Impact 15",
                              fg="#3C4B66",
                              bg="#FADCD8"
                              )
    concerts_label.pack(anchor=tk.CENTER, side="top", padx="5", pady="20")

    add_concert_button = tk.Button(root,
                                   text="add concert",
                                   font="SegueUI 12",
                                   fg="#E16856",
                                   bg="#FBF5F5",
                                   activebackground="#E16856",
                                   activeforeground="#FBF5F5",
                                   command=create_add_concert_page
                                   )
    add_concert_button.pack(anchor=tk.CENTER)

    display_concerts()


def create_location_page():
    clear_widgets(root)
    add_background_image(root, "pictures/location_example.png")
    icon_shortcuts()

    hello_label = tk.Label(root,
                           text="Looking for concerts near you?",
                           font="Impact 15",
                           fg="#3C4B66",
                           bg="#FADCD8"
                           )
    hello_label.pack(anchor=tk.CENTER, side="top", padx="5", pady="10")

    filter_button = tk.Button(root,
                              text="Here you can filter the results",
                              font="SegueUI 12",
                              fg="#E16856",
                              bg="#FBF5F5",
                              activebackground="#E16856",
                              activeforeground="#FBF5F5"
                              )
    filter_button.place(x=33, y=75)


def create_find_buddy_page():
    clear_widgets(root)
    add_background_image(root, "pictures/buddy_example.png")
    icon_shortcuts()

    filter_button = tk.Button(root,
                              text="Filter",
                              font="SegueUI 12",
                              fg="#E16856",
                              bg="#FBF5F5",
                              activebackground="#E16856",
                              activeforeground="#FBF5F5"
                              )
    filter_button.pack(side=RIGHT, anchor="ne", padx="10", pady="10")


def create_sell_ticket_page():
    clear_widgets(root)
    icon_shortcuts()

    # add necessary labels, buttons, entry-boxes, dropdown menus of the page
    hello_label = tk.Label(root,
                           text=f"Which ticket do you want to sell?",
                           font="Impact 15",
                           fg="#3C4B66",
                           bg="#FADCD8"
                           )
    hello_label.pack(anchor=tk.CENTER, side="top", padx="5", pady="20")

    concert_label = tk.Label(root,
                             text="For which concert do you want to sell a ticket?",
                             font="SegueUI 12",
                             fg="#E16856",
                             bg="#FADCD8"
                             )
    concert_label.place(x=30, y=60)

    # create a dropdown menu with the concerts of the user as options
    file = open("data/concert_data.csv")
    csvreader = csv.reader(file)

    concert_options = [" - ".join(row[:4]) for row in csvreader]

    clicked_concert = StringVar()

    clicked_concert.set("select the concert")

    dropdown_concerts = OptionMenu(root, clicked_concert, *concert_options)
    dropdown_concerts.configure(bg="#FBF5F5",
                                fg="#E16856",
                                activebackground="#E16856",
                                activeforeground="#FBF5F5",
                                font="SegueUI 12",
                                highlightthickness=0)
    dropdown_concerts.place(x=30, y=100)

    number_label = tk.Label(root,
                            text=f"Enter the seat number or standing category:",
                            font="SegueUI 12",
                            fg="#E16856",
                            bg="#FADCD8"
                            )
    number_label.place(x=30, y=140)

    seat_entry = tk.Entry(root,
                          font="SegueUI 12",
                          bg="#FBF5F5",
                          fg="#3C4B66"
                          )
    seat_entry.place(x=30, y=180)

    original_price_label = tk.Label(root,
                                    text="Original Price:",
                                    font="SegueUI 12",
                                    fg="#E16856",
                                    bg="#FADCD8"
                                    )
    original_price_label.place(x=30, y=220)

    price_label = tk.Label(root,
                           text="*will be calculated*",
                           font="SegueUI 12",
                           bg="#FBF5F5",
                           fg="#3C4B66"
                           )
    price_label.place(x=150, y=220)

    reduction_label = tk.Label(root,
                               text="Do you want to sell it for less?",
                               font="SegueUI 12",
                               fg="#E16856",
                               bg="#FADCD8"
                               )
    reduction_label.place(x=30, y=260)

    reduction_options = [
        "No",
        "Yes. 10% less",
        "Yes. 20% less",
        "Yes. 30% less",
        "Yes. 40% less",
        "Yes. 50% less",
        "Yes. 60% less",
        "Yes. 70% less",
        "Yes. 80% less",
        "Yes. 90% less",
        "I want to give it away for free.",
    ]

    clicked_reduction = StringVar()

    clicked_reduction.set("select the concert")

    dropdown_reduction = OptionMenu(root, clicked_reduction, *reduction_options)
    dropdown_reduction.configure(bg="#FBF5F5",
                                 fg="#E16856",
                                 activebackground="#E16856",
                                 activeforeground="#FBF5F5",
                                 font="SegueUI 12",
                                 highlightthickness=0)
    dropdown_reduction.place(x=30, y=300)

    sell_button = tk.Button(root,
                            text="put up for sale",
                            font="SegueUI 12",
                            fg="#FBF5F5",
                            bg="#E16856",
                            activebackground="#FBF5F5",
                            activeforeground="#E16856"
                            )
    sell_button.place(x=120, y=380)

    back_button = tk.Button(root,
                            text="🔙",
                            font="arial 18",
                            fg="#E16856",
                            bg="#FBF5F5",
                            activebackground="#E16856",
                            activeforeground="#FBF5F5",
                            command=create_ticket_sale_page)
    back_button.pack(side=BOTTOM)


def create_ticket_sale_page():
    # definition to create a page where the user can sell or buy tickets of other users

    clear_widgets(root)
    icon_shortcuts()

    # add necessary labels, buttons, entry-boxes, dropdown menus of the page
    hello_label = tk.Label(root,
                           text="Welcome to our Ticket Sale",
                           font="Impact 15",
                           fg="#3C4B66",
                           bg="#FADCD8"
                           )
    hello_label.pack(anchor=tk.CENTER, side="top", padx="5", pady="20")

    sell_button = tk.Button(root,
                            text="I want to sell a ticket",
                            font="SegueUI 12 bold",
                            bg="#E16856",
                            fg="#FBF5F5",
                            activebackground="#E16856",
                            activeforeground="#FBF5F5",
                            padx="6",
                            pady="6",
                            command=create_sell_ticket_page
                            )
    sell_button.pack(anchor=tk.CENTER, side="top", padx="5", pady="10")

    buy_button = tk.Button(root,
                           text="I'm looking to buy a ticket",
                           font="SegueUI 12 bold",
                           bg="#E16856",
                           fg="#FBF5F5",
                           activebackground="#E16856",
                           activeforeground="#FBF5F5",
                           padx="6",
                           pady="6"
                           )
    buy_button.pack(anchor=tk.CENTER, side="top", padx="5", pady="10")


def send_user_message():
    user_message = entry_box.get()
    if user_message:
        text_box.insert(tk.END, f'\nMe: {user_message}')
        text_box.insert(tk.END, f'\nMark: Yes haha')

    # delete what was entered by the user
    entry_box.delete(0, tk.END)


def create_chat_page():
    # definition to create the page where the user can chat with matched users

    global entry_box, text_box

    clear_widgets(root)
    icon_shortcuts()

    chat_label = tk.Label(root,
                          text="Chats:",
                          font="Impact 15",
                          fg="#3C4B66",
                          bg="#FADCD8"
                          )
    chat_label.pack(anchor=tk.CENTER, side="top", padx="5", pady="20")

    # create the text box
    text_box = tk.Text(root,
                       bg="#F88776",
                       fg="#3C4B66",
                       font="SegueUI 12",
                       width=38
                       )
    text_box.pack(anchor=tk.CENTER)

    # add the first "message" of the user
    text_box.insert(tk.END, "Mark: Hi, I have the same go-to karaoke song.\nHow funny!")

    entry_frame = Frame(master=root,
                        bg="#FADCD8")
    entry_frame.pack(anchor=tk.CENTER, side=tk.LEFT, pady=10, padx=10)

    # create an entry box for user to enter a message
    entry_box = tk.Entry(master=entry_frame,
                         bg="#FBF5F5",
                         fg="#E16856",
                         font="SegueUI 12",
                         width=30
                         )
    entry_box.pack(side=tk.LEFT)

    send_button = tk.Button(master=entry_frame,
                            text="➡️",
                            font="SegueUI 12 bold",
                            bg="#E16856",
                            fg="#FBF5F5",
                            activebackground="#E16856",
                            activeforeground="#FBF5F5",
                            command=send_user_message
                            )
    send_button.pack(side=tk.LEFT, padx=5)


def enter_user_data():
    # definition to save the user data in a csv file

    # create a timestamp
    current_timestamp = datetime.now()

    # create dictionary that stores user data
    user_data = {
        "name": name.get(),
        "user_id": username.get(),
        "created-at": current_timestamp
    }

    # get the list of user ids
    user_ids = list(pd.read_csv("data/user_data.csv").user_id)

    # if the username exists in the csv file, print a warning
    if username.get() in user_ids:
        tk.messagebox.showwarning("WARNING", "Please select another username. This one is taken")
    # otherwise store the users data
    else:
        # converting the dictionary to a data frame
        user_data_df = pd.DataFrame([user_data])
        # write your data to a .csv file - since we want to append date we add mode = 'a'
        user_data_df.to_csv("data/user_data.csv", index=False, header=False, mode='a')


def create_sign_up_page():
    global name, username

    clear_widgets(root)

    # add necessary labels, buttons, entry-boxes, dropdown menus of the page
    welcome_label = tk.Label(root,
                             text="Welcome to ConcertBuddy!\nPlease sign up to find a buddy",
                             font="Impact 15",
                             fg="#3C4B66",
                             bg="#FADCD8"
                             )
    welcome_label.pack(anchor=tk.CENTER, side="top", padx="5", pady="20")

    name_label = tk.Label(root,
                          text="Please enter your name:",
                          font="SegueUI 13",
                          fg="#E16856",
                          bg="#FADCD8"
                          )
    name_label.place(x=30, y=100)

    name = tk.StringVar()
    name_entry = tk.Entry(root,
                          textvar=name,
                          width=18,
                          font="SegueUI 12",
                          bg="#FBF5F5",
                          fg="#3C4B66"
                          )
    name_entry.place(x=30, y=130)

    username_label = tk.Label(root,
                              text="Please create a username:",
                              font="SegueUI 13",
                              fg="#E16856",
                              bg="#FADCD8"
                              )
    username_label.place(x=30, y=200)

    username = tk.StringVar()
    username_entry = tk.Entry(root,
                              textvar=username,
                              width=18,
                              font="SegueUI 12",
                              bg="#FBF5F5",
                              fg="#3C4B66"
                              )
    username_entry.place(x=30, y=230)

    # button so the user can submit their information
    sign_up_button = tk.Button(root,
                               text="SIGN UP",
                               font="SegueUI 15 bold",
                               bg="#E16856",
                               fg="#FBF5F5",
                               activebackground="#FBF5F5",
                               activeforeground="#E16856",
                               command=lambda: [enter_user_data(), create_profile_page()]
                               )
    sign_up_button.place(x=40, y=300)

    back_button = tk.Button(root,
                            text="🔙",
                            font="arial 18",
                            fg="#E16856",
                            bg="#FBF5F5",
                            activebackground="#E16856",
                            activeforeground="#FBF5F5",
                            command=create_homepage)
    back_button.pack(side=BOTTOM)


def check_user():
    # definition to check if the user already exists in the database

    # read all the usernames in the username from the .csv file
    user_ids = list(pd.read_csv("data/user_data.csv").user_id)

    # check if username exists - then go onto next page
    if username.get() in user_ids:
        create_profile_page()
    # otherwise give a warning
    else:
        tk.messagebox.showwarning("WARNING", "User does not exist")


def create_log_in_page():
    global name, username

    clear_widgets(root)

    # add necessary labels, buttons, entry-boxes, dropdown menus of the page
    welcome_label = tk.Label(root,
                             text="Welcome back ConcertBuddy!\nPlease log in",
                             font="Impact 15",
                             fg="#3C4B66",
                             bg="#FADCD8"
                             )
    welcome_label.pack(anchor=tk.CENTER, side="top", padx="5", pady="20")

    name_label = tk.Label(root,
                          text="Name:",
                          font="SegueUI 13",
                          fg="#E16856",
                          bg="#FADCD8"
                          )
    name_label.place(x=30, y=100)

    name = tk.StringVar()
    name_entry = tk.Entry(root,
                          textvar=name,
                          width=18,
                          font="SegueUI 12",
                          bg="#FBF5F5",
                          fg="#3C4B66"
                          )
    name_entry.place(x=30, y=130)

    username_label = tk.Label(root,
                              text="Username:",
                              font="SegueUI 13",
                              fg="#E16856",
                              bg="#FADCD8"
                              )
    username_label.place(x=30, y=200)

    username = tk.StringVar()
    username_entry = tk.Entry(root,
                              textvar=username,
                              width=18,
                              font="SegueUI 12",
                              bg="#FBF5F5",
                              fg="#3C4B66"
                              )
    username_entry.place(x=30, y=230)

    # button so the user can submit their information
    log_in_button = tk.Button(root,
                              text="LOG IN",
                              font="SegueUI 15 bold",
                              bg="#E16856",
                              fg="#FBF5F5",
                              activebackground="#FBF5F5",
                              activeforeground="#E16856",
                              command=check_user
                              )
    log_in_button.place(x=40, y=300)

    back_button = tk.Button(root,
                            text="🔙",
                            font="arial 18",
                            fg="#E16856",
                            bg="#FBF5F5",
                            activebackground="#E16856",
                            activeforeground="#FBF5F5",
                            command=create_homepage)
    back_button.pack(side=BOTTOM)


def create_homepage():
    clear_widgets(root)

    # add necessary labels, buttons, entry-boxes, dropdown menus of the page
    welcome_label = tk.Label(root,
                             text="WELCOME TO CONCERTBUDDY",
                             font="Impact 20",
                             fg="#3C4B66",
                             bg="#FADCD8"
                             )
    welcome_label.pack(side="top", padx="5", pady="20")

    motto_label = tk.Label(root,
                           text="find friends for concerts",
                           font="SegueUI 12",
                           fg="#E16856",
                           bg="#FADCD8"
                           )
    motto_label.pack()

    # add two buttons for either signing up or logging in
    sign_up_button = tk.Button(root,
                               text="New here? Sign Up",
                               font="SegueUI 12 bold",
                               bg="#E16856",
                               fg="#FBF5F5",
                               activebackground="#FBF5F5",
                               activeforeground="#E16856",
                               padx="8",
                               pady="10",
                               command=create_sign_up_page
                               )
    sign_up_button.pack(side="top", padx="5", pady="40")

    log_in_button = tk.Button(root,
                              text="Welcome back? Log in",
                              font="SegueUI 12 bold",
                              bg="#E16856",
                              fg="#FBF5F5",
                              activebackground="#FBF5F5",
                              activeforeground="#E16856",
                              padx="8",
                              pady="10",
                              command=create_log_in_page
                              )
    log_in_button.pack(side="top", padx="5", pady="5")


def icon_shortcuts():
    # definition to display a row of buttons on the bottom of the page to navigate in between pages

    # add a frame for the buttons
    shortcut_frame = Frame(master=root)
    shortcut_frame.pack(side=tk.BOTTOM, fill="x")

    # create a button for each page that should be accessible through the shortcut navigation
    sc_profile_page = tk.Button(master=shortcut_frame,
                                text="👤",
                                font="arial 15",
                                fg="#FBF5F5",
                                bg="#E16856",
                                activebackground="#FBF5F5",
                                activeforeground="#E16856",
                                padx="12",
                                pady="12",
                                command=create_profile_page
                                )
    sc_profile_page.pack(side=tk.LEFT)

    sc_concerts_page = tk.Button(master=shortcut_frame,
                                 text="🎶",
                                 font="arial 15",
                                 fg="#FBF5F5",
                                 bg="#E16856",
                                 activebackground="#FBF5F5",
                                 activeforeground="#E16856",
                                 padx="12",
                                 pady="12",
                                 command=create_concerts_page
                                 )
    sc_concerts_page.pack(side=tk.LEFT)

    sc_location_page = tk.Button(master=shortcut_frame,
                                 text="📍",
                                 font="arial 15",
                                 fg="#FBF5F5",
                                 bg="#E16856",
                                 activebackground="#FBF5F5",
                                 activeforeground="#E16856",
                                 padx="12",
                                 pady="12",
                                 command=create_location_page
                                 )
    sc_location_page.pack(side=tk.LEFT)

    sc_find_buddy_page = tk.Button(master=shortcut_frame,
                                   text="👋",
                                   font="arial 15",
                                   fg="#FBF5F5",
                                   bg="#E16856",
                                   activebackground="#FBF5F5",
                                   activeforeground="#E16856",
                                   padx="12",
                                   pady="12",
                                   command=create_find_buddy_page
                                   )
    sc_find_buddy_page.pack(side=tk.LEFT)

    sc_chat_page = tk.Button(master=shortcut_frame,
                             text="💬",
                             font="arial 15",
                             fg="#FBF5F5",
                             bg="#E16856",
                             activebackground="#FBF5F5",
                             activeforeground="#E16856",
                             padx="12",
                             pady="12",
                             command=create_chat_page
                             )
    sc_chat_page.pack(side=tk.LEFT)

    sc_ticket_sale_page = tk.Button(master=shortcut_frame,
                                    text="🎫",
                                    font="arial 15",
                                    fg="#FBF5F5",
                                    bg="#E16856",
                                    activebackground="#FBF5F5",
                                    activeforeground="#E16856",
                                    padx="12",
                                    pady="12",
                                    command=create_ticket_sale_page
                                    )
    sc_ticket_sale_page.pack(side=tk.LEFT)


create_homepage()

root.mainloop()