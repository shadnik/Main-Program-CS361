class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class Playlist:
    def __init__(self, name, mood):
        self.name = name
        self.mood = mood
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f'Song "{song}" added to playlist.')

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f'Song "{song}" removed from playlist.')
        else:
            print(f'Song "{song}" not found in playlist.')

    def view_playlist(self):
        if not self.songs:
            print("Playlist is currently empty.")
        else:
            print("Current Playlist:")
            for i, song in enumerate(self.songs, 1):
                print(f"{i}. {song}")


def register_user():
    print("\nUser Registration")
    print("Sign up for free! Enter your details below.")
    print("Note: Your email will only be used as your username. No emails will be sent or information shared.")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email Address: ")
    password = input("Enter Password: ")
    confirm_password = input("Confirm Password: ")

    while password != confirm_password:
        print("Passwords do not match. Please try again.")
        password = input("Enter Password: ")
        confirm_password = input("Confirm Password: ")

    print("Registration successful!")
    return User(first_name, last_name, email, password)


def login_user(registered_user):
    print("\nLogin Page")
    print("If you've forgotten your password, please contact support to reset it.")
    email = input("Enter Email Address: ")
    password = input("Enter Password: ")

    if email != registered_user.email or password != registered_user.password:
        print("Invalid credentials. Please try again.")
        return None

    print("Login successful!")
    return registered_user


def create_playlist_workflow():
    print("\nCreate Playlist Workflow")
    print("Would you like a short explanation of how to use the playlist feature? (Y/N)")
    explanation = input("Enter your choice: ")
    if explanation.lower() == 'y':
        print(
            "To create a playlist, you can add songs, view the current list, or remove songs. You can also exit the "
            "workflow at any time.")
    playlist_name = input("Enter Playlist Name: ")
    mood = input("Assign a Mood to the Playlist: ")
    playlist = Playlist(playlist_name, mood)

    while True:
        action = input("\nOptions: [1] Add Song, [2] View Playlist, [3] Remove Song, [4] Exit Workflow\nChoose an "
                       "option: ")

        if action == "1":
            song = input("Enter Song Name to Add: ")
            playlist.add_song(song)
        elif action == "2":
            playlist.view_playlist()
        elif action == "3":
            song = input("Enter Song Name to Remove: ")
            confirm = input(f'Are you sure you want to remove "{song}"? (Y/N): ')
            if confirm.lower() == 'y':
                playlist.remove_song(song)
        elif action == "4":
            confirm_exit = input("Are you sure you want to finalize the playlist and exit? (Y/N): ")
            if confirm_exit.lower() == 'y':
                print("Exiting Playlist Workflow.")
                break
        else:
            print("Invalid option. Please try again.")


def main():
    print("Welcome to the Jamify!")
    print("New Feature: Playlist creation is now available!")

    user = register_user()
    logged_in_user = None

    while not logged_in_user:
        logged_in_user = login_user(user)

    while True:
        action = input("\nMain Menu: [1] Create Playlist, [2] Exit\nChoose an option: ")

        if action == "1":
            create_playlist_workflow()
        elif action == "2":
            print("Thank you for using the Jamify. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
