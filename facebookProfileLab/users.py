## In the user_class.py file, you'll code out your user class.
## Here, you can write tests to see if your user class is functioning correctly.

## This line of code is important. It's how your users.py program loads in your definition of the user class.
## Uncomment the line below for your program to run at all.
# import user_class


## If the line below runs without error, you're able to make an instance of a user class.
## As you can see, this user has a name, an email, a password, and an age.
## Uncomment this initializer and see if it runs without error.
# jolson615 = user_class.User("Jeff", "jolson615@gmail.com", "password1", 28)

## If your first user was created successfully, the one below probably won't be.
## What would you need to change for Sarah to have an account?
# sarah773 = user_class.User("Sarah", "sarah.owen14@gmail.com", "mangotrain")

## Next, lets set a user's mood.
# jolson615.mood = "Happy"

## Now let's write a method called status_update that prints an update about a user's mood.
## For example, if we called this method on jolson615, it should print "I'm feeling Happy today."
# jolson615.status_update()

## let's finally write a method to try to change a user's password. It will take two arguments - the old password, and the new one.
## If the old password matches, it should change the password and print a success message.
# jolson615.change_password("password1", "moosedogredpine")

## If the old password doesn't match, it should print an error message.
# sarah773.change_password("mango", "mygreatnewpassword")
