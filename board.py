from tkinter import *
import time
import json

# There needs to be at least 2 different files read.
# this is only because it makes it easier to manually enter
# and read the topics and questions if they're spread over two
# different text files instead of shoved into one big file
def questions(file):    
    with open(file) as f:
        data = json.load(f)
    return data

class Board:
    # initalize a new window each time board is called
    def __init__(self, game_name, background_color):
        # these variables are just here to configure the window for the game each time
        # a new object is created
        self.window = Tk()
        self.window.title(game_name)
        self.window.configure(bg=background_color)
        self.window.attributes('-fullscreen', True)

        # these are the variables that will be used to manipulate the topics
        # buttons, and point totals and teams
        self.topics = []
        self.buttons = []
        self.list_of_teams = []
        self.point_amount = 200
        self.point_increase_amount = 200

        # variables to store the points for each team
        self.team_plus_min = []
        self.team1_points = 0
        self.team2_points = 0
        self.team3_points = 0
        #self.round_two = False

    def display_questions(self, question, question_index, question_amount):
        # I'm sure there is a better way to do this, but the easiest way I found to create a separate window for now
        # is to just create a new Tk() object entirely. I should probably have put the Tk() object in its own class
        # with customizable window options for whenever I need to call it.
        y_pad = 80
        x_pad = 30
        sign = "+"
        question_window = Tk()
        question_window.configure(bg="blue")
        question_window.attributes('-fullscreen', True)

        # displaying the question in the new window so that it takes up the top half of the screen.
        # the button is then disabled as soon as the button is pressed.
        question_label = Label(question_window, text=question, font=("Arial", 30), bg="blue", fg="white", pady=150, padx=100)
        question_label.grid(row=0, column=0,columnspan=6,rowspan=2, sticky="nsew")
        self.buttons[question_index].config(state='disabled')

        # these buttons will determine who gets the points and whether they are being
        # added or subtracted to that player's score

        # when trying to use a for loop to create all the buttons, for some reason the amount of points
        # given to the player is not working properly. Not sure why this is the case so I will just
        # create each button individually for now
        #for i in range(2,4):
         #   for j in range(0,3):
          #      if i == 3:
           #         sign = "-"
            #        question_amount *= -1
             #   Button(question_window, text=f"Team {j+1}: {sign}", font=("arial", 20), bg="blue", fg="white", padx=x_pad, pady=y_pad, command=lambda c=j+1, a=question_amount:self.award_points(c, a)).grid(row=i, column=j,columnspan=1,rowspan=1, sticky='nsew')
                    
        Button(question_window, text=f"Team {1}: +", font=("arial", 20), bg="blue", fg="white", padx=x_pad, pady=y_pad, command=lambda:self.award_points(1, question_amount)).grid(row=2, column=0,columnspan=1,rowspan=1, sticky='nsew')
        Button(question_window, text=f"Team {1}: -", font=("arial", 20), bg="blue", fg="white", padx=x_pad, pady=y_pad, command=lambda:self.award_points(1, question_amount*-1)).grid(row=3, column=0,columnspan=1,rowspan=1, sticky='nsew')
        
        Button(question_window, text=f"Team {2}: +", font=("arial", 20), bg="blue", fg="white", padx=x_pad, pady=y_pad, command=lambda:self.award_points(2, question_amount)).grid(row=2, column=1,columnspan=1,rowspan=1, sticky='nsew')
        Button(question_window, text=f"Team {2}: -", font=("arial", 20), bg="blue", fg="white", padx=x_pad, pady=y_pad, command=lambda:self.award_points(2, question_amount*-1)).grid(row=3, column=1,columnspan=1,rowspan=1, sticky='nsew')
        
        Button(question_window, text=f"Team {3}: +", font=("arial", 20), bg="blue", fg="white", padx=x_pad, pady=y_pad, command=lambda:self.award_points(3, question_amount)).grid(row=2, column=2,columnspan=1,rowspan=1, sticky='nsew')
        Button(question_window, text=f"Team {3}: -", font=("arial", 20), bg="blue", fg="white", padx=x_pad, pady=y_pad, command=lambda:self.award_points(3, question_amount*-1)).grid(row=3, column=2,columnspan=1,rowspan=1, sticky='nsew')

        # I'm not sure why, but every time I try to add the buttons to a list so I can access them later, it throws an error after I
        # use the quit button. I have tried changing each value, and the only reason I can think this is happening is because since
        # the buttons are all created at the same time and appended to the list, it causes it to destroy the Tk() object for
        # all the buttons at the same time making it complain that the object was destroyed.

        #for j in range(0,3):
         #   self.team_plus_min.append(Button(frame, text=f"Team {j+1}: +", font=("arial", 20), bg="blue", fg="white", padx=30, pady=30))
          #  self.team_plus_min[j].grid(row=1, column=j+1, sticky='nsew')
                        
        # give a way to exit the question window
        exit_button = Button(question_window, text="Exit Question", font=("Arial", 20), bg="blue", fg="white", pady=50, padx=30, command=question_window.destroy)
        exit_button.grid(row=3, column=3, columnspan=2, sticky='nsew')

    def final_round(self):
        # creating a new window so it doesn't interfere with any other objects
        final_round = Tk()
        final_round.configure(bg="blue")
        final_round.attributes('-fullscreen', True)
        x_pad = 80
        y_pad = 30

        # this just grabs the final question out of the text file so it can be displayed
        question = questions("final_round.txt")

        # This will display the question for the fallout round
        final_question = Label(final_round, text=f"{question['final']}", font=("Arial", 30), bg="blue", fg="white", pady=150, padx=100)
        final_question.grid(row=0,column=0, columnspan=5, sticky='nsew')

        # This should be refactored later on at some point so a point value can be typed in
        # in the meantime, all the user has to do is click the button and it will either add or subtract 100 points for each click
        Button(final_round, text=f"Team {1}: +", font=("arial", 20), bg="blue", fg="white", padx=x_pad, pady=y_pad, command=lambda:self.award_points(1, 100)).grid(row=2, column=0,columnspan=1,rowspan=1, sticky='nsew')
        Button(final_round, text=f"Team {1}: -", font=("arial", 20), bg="blue", fg="white", padx=x_pad, pady=y_pad, command=lambda:self.award_points(1, -100)).grid(row=3, column=0,columnspan=1,rowspan=1, sticky='nsew')
        
        Button(final_round, text=f"Team {2}: +", font=("arial", 20), bg="blue", fg="white", padx=x_pad, pady=y_pad, command=lambda:self.award_points(2, 100)).grid(row=2, column=1,columnspan=1,rowspan=1, sticky='nsew')
        Button(final_round, text=f"Team {2}: -", font=("arial", 20), bg="blue", fg="white", padx=x_pad, pady=y_pad, command=lambda:self.award_points(2, -100)).grid(row=3, column=1,columnspan=1,rowspan=1, sticky='nsew')
        
        Button(final_round, text=f"Team {3}: +", font=("arial", 20), bg="blue", fg="white", padx=x_pad, pady=y_pad, command=lambda:self.award_points(3, 100)).grid(row=2, column=2,columnspan=1,rowspan=1, sticky='nsew')
        Button(final_round, text=f"Team {3}: -", font=("arial", 20), bg="blue", fg="white", padx=x_pad, pady=y_pad, command=lambda:self.award_points(3, -100)).grid(row=3, column=2,columnspan=1,rowspan=1, sticky='nsew')

        # this is just the button to exit out of the window
        exit_button = Button(final_round, text="Bye Bye!", font=("Arial", 20), bg="blue", fg="white", pady=50, padx=30, command=final_round.destroy)
        exit_button.grid(row=3, column=3, columnspan=2, sticky='nsew')
        
    # this is just a function to configure the amount of points each team has by taking
    # the press of a button from the display_questions method and adding/subtracting it from the team score variables
    def award_points(self, team_id, point_amount):
        if team_id == 1:
            self.team1_points += point_amount
            self.list_of_teams[0].config(text=f"Team {team_id}: {self.team1_points}")
        elif team_id == 2:
            self.team2_points += point_amount
            self.list_of_teams[1].config(text=f"Team {team_id}: {self.team2_points}")
        elif team_id == 3:
            self.team3_points += point_amount
            self.list_of_teams[2].config(text=f"Team {team_id}: {self.team3_points}")        

    # this is simply a function that creates a list of buttons displaying the team score on the main window
    def create_teams(self):
        for i in range(0,3):
            self.list_of_teams.append(Button(self.window, text=f"Team {i+1}: {self.team1_points}", font=("Arial",15), bg="blue", fg="white", padx=70, pady=35))
            self.list_of_teams[i].grid(row=6, column=3+i, sticky='nsew')
    
    # create a list of topic labels
    def create_topics(self, data):
        # these labels cannot be altered once they are appended to the list.
        # I'm not sure of the exact reason why, but once the label gets appended.
        # it creates an object called .!label which throws an error when you
        # try to use destroy on the label.
        for i in range(0,6):
            self.topics.append(Label(self.window, text=data['topics'][i],padx=20, pady=30, font=("Arial", 17), bg="blue", fg="white"))
            self.topics[i].grid(row=0, column=i, columnspan=1, sticky="nsew")

    def button_points_display(self, text_file):
        point_values = questions(text_file)
        # each button counter is necessary for the proper indexing of the buttons
        # the button count is to make sure the proper index is found for each button in the list so it can be modified later
        # the row and column counter are necessary to correctly place each button on the window
        button_count = 0
        row_count = 1
        column_count = 0

        # this will create 30 different buttons that will be used for accessing the questions
        for i in range(0,5):
            for j in range(0,6):
                # the variables a,b,c are used for the lambda function as placeholders so that
                # the correct index is called instead of the last index referenced
                self.buttons.append(Button(self.window, text=str(self.point_amount), padx=79, pady=34, font=("Arial", 25), bg="blue", fg="white", command=lambda a=self.point_amount, b=j, c=button_count: self.display_questions(point_values[str(a)][b], c, a)))
                self.buttons[button_count].grid(row=row_count, column=column_count,columnspan=1, sticky="nsew")
                # make sure to update how many buttons are in the list and what column the window is at
                button_count += 1
                column_count += 1
            # make sure to update the location of the row 
            row_count += 1
            print()
            # use this to not only access each topic value, but also to display how many points are possible
            self.point_amount += self.point_increase_amount
            # reset the column counter so it isn't just a long list of columns
            if column_count == 6:
                column_count = 0

    def refresh(self, data, choose_round):
        ''' config is an easier way of changing what text is on the labels. By doing it like this
            I'm able to change the values using a completely different text file. It also does not create
            a new window, but will instead keep the same window intact. '''
        count = 0

        # updates the point values for each category to reflect whether
        # the game is in round 1 or round 2
        # is mainly going to be used to allow people to go back after the game
        # to let them see what the old questions were and how much they were worth
        if choose_round == 1:
            self.point_amount = 200
            self.point_increase_amount = 200
        else:
            self.point_amount = 400
            self.point_increase_amount = 400

        # loop through all the buttons and configure the text to reflect
        # the values depending on what round it is
        for i in range(0,5):
            for j in range(0,6):
                # going through each index changing the text of the buttons
                # this is also used to change the text of the labels created in display_questions()
                self.buttons[count].config(text=str(self.point_amount), command=lambda a=self.point_amount, b=j, c=count: self.display_questions(data[str(a)][b], c, a))
                # turning the buttons back on after disabling them when a question was clicked on
                self.buttons[count].config(state='normal')
                count += 1
            
            self.point_amount += self.point_increase_amount
        
        for c, i in enumerate(self.topics):
            i.config(text=data['topics'][c])
            # I have to manually stop enumerate from going out of bounds on the index value
            # never mind... I just commented out these lines and it's now working as it should
            #if c == 5:
             #   break

    def quit_game(self):
        self.window.destroy()
        # I tried to use these methods to erase the text on the labels but I could not
        # stop the second set of labels from printing before erasing the previous values. 
        #self.window.destroy()
        #self.__init__()
        
    
    
# just create the board object and display the questions and the points
name = Board("Cybersecurity Trivia", "blue")
name.create_topics(questions("round1.txt"))
name.button_points_display("round1.txt")

# this button will switch the game back to round 1
round_button1 = Button(name.window, text="Fallout", padx=70, pady=35, font=("Arial", 15),bg="blue", fg="white", command=name.final_round)
round_button1.grid(row=6,column=1, sticky='nsew')

# this will switch the game to round 2
# the text files should be named round1.txt, and round2.txt to make them easier to find
round_button2 = Button(name.window, text="Round 2", padx=70, pady=35, font=("Arial", 15),bg="blue", fg="white", command=lambda: name.refresh(questions("round2.txt"), 0))
round_button2.grid(row=6,column=2, sticky='nsew')

# this is the quit game button so that the window can be exited without pressing f4
quit_game_button = Button(name.window, text="Quit Game", padx=70, pady=35, font=("Arial", 15), bg="blue", fg="white", command=name.quit_game)
quit_game_button.grid(row=6, column=0, sticky='nsew')
name.create_teams()

name.window.mainloop()
