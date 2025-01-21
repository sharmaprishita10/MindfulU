
# Meditate

Meditate is an e-learning site where users can view and subscribe to various programs and courses related to meditation.


### Description

This is an e-learning site where users can subscribe to various programs after which a hypothetical zoom link is mailed. Users can enroll themselves in various courses whose study material is hypothetically mailed.
The users can give their reviews on a specific program and can view all reviews. Users can also view programs and courses they are enrolled in. Using a back-to-top arrow, users can go to the top of the page after scrolling down.

Name of the Django project is capstone and name of the app is meditate.


### Getting Started

1. Run python manage.py makemigrations meditate to make migrations for the meditate app.
2. Run python manage.py migrate to apply migrations to your database.


### Understanding

In meditate/urls.py, there are three basic routes, /login route for login, /logout for logout and /register for registering a new user.
In meditate/views.py, the views that are associated with each of these routes are  
the login_view view renders a login form when a user tries to GET the page. 
When a user submits the form using the POST request method, the user is authenticated, logged in, and redirected to the index page. 
The logout_view view logs the user out and redirects them to the index page. 
Finally, the register route displays a registration form to the user, and creates a new user when the form is submitted. 

There are three **API** routes:
- /subscribe/<int:prog_id> : A GET request to this route returns the number of subscribers of a particular program and a PUT request adds or removes the signed in user to the program as they subscribe or unsubscribe to the program respectively.
- /enroll/<int:course_id> : A GET request to this route returns the number of enrollers of a particular course and a PUT request adds or removes the signed in user to the course as they enroll or unenroll from the course respectively.
- /comments/<int:prog_id> : A GET request to this route returns all the comments of a particular program in reverse chronological order as an array of JavaScript objects using serialize() and a POST request creates a new comment object for the particular program by the signed in user.

Run python manage.py runserver to start up the Django web server, and visit the website in your browser. Click “Register” and register for an account. You should see that you are now “Signed in as” your user account, and the links at the top of the page have changed.Take a look at meditate/templates/meditate/layout.html for the HTML layout of this application. Notice that several parts of the template are wrapped in a check for if user.is_authenticated, so that different content can be rendered depending on whether the user is signed in or not. 
Then the index view associated with the default index route, renders a template 'meditate/index.html'. The template shows a carousel 
with three slides. Then /programs route requests programs view which renders 'meditate/programs.html' that displays all the available programs for users to subscribe. The page also shows the number of subscribers.

The /program/<int:prog_id> requests the program view that renders 'meditate/program.html' template that displays details of a particular program. If the user
is signed in, they can subscribe/unsubscribe to a program. They can also give their reviews in the program reviews section that has a form and displays all the reviews.
The /courses route requests the courses view that renders 'meditate/courses.html' template that displays all the available courses that the users can enroll in. Similar to programs view,
this also displays the number of enrollers. The /course/<int:course_id> route requests the course view that displays course details and its duration. 
If the user is signed in, they can enroll/unenroll in a course. The /enrollments route requests the enrollments view that renders 'meditate/enrollments.html' template that
displays the programs the user has subscribed and the courses user has enrolled in. The /about route requests the about view that renders 'meditate/about.html' template that just 
gives a brief about the site 'Meditate'. The site also has a footer that gives contact details to the user.


### Specification

- **Index** : The user can see a carousel of three slides with indicators and two divs for programs and courses. Clicking on any of the div takes the user to the respective page.

- **Programs** : This page displays a list of all the programs Meditate offers. Each div for program displays an image, program title, program days and the number of subscribers.

- **Program Page** : Clicking on any of the program takes the user to a page specific to the program that displays its details and the signed in user is able to subscribe or unsubscribe 
to the program. The page also displays all the program reviews and gives a form to the signed in user to add a comment. All of this is happening through fetch.

- **Courses** : This page displays a list of all the courses Meditate offers. Each div for course displays an image, courses title, subtitle, duration and the number of enrollers.

- **Course Page** : Clicking on any of the course takes the user to a page specific to the course that displays its details and the signed in user is able to enroll or unenroll to  a course.
All of this is because of fetch i.e. the page does not reload.

- **Enrollments** : This page displays a list of all the programs and courses that the user has subscribed or enrolled in. Clicking on any of these takes the user to a page specific to the
program or course.

- **About** : This page displays information about the e-learning site Mediate.

- **Back to top** : After scrolling 20px down through the window, the user is able to go back to the top of the page by clicking a back to top arrow implemented through JavaScript.


### Capstone requirements

- **Distinctiveness and complexity** : This project is distinct as it is not similar to any of the previous projects. In CS50W, we have made projects on search engine, encyclopedia, e-commerce, email client,
social network. But this project is an e-learning site that allows users to subscibe to various programs and enroll in courses. The zoom links or course material is hypothetically emailed to the user. 
The project is complex as it has a carousel with three slides implemented with BootStrap JavaScript and a back to top feature that allows the user to go back to the top of the page which is implemented through JavaScript and onscroll event listener in particular.

- **Django and JavaScript** : This project has four models - User, Program, Course and Comment.
User model extends AbstractUser class. Program and Course models store information about the programs and courses respectively. Comment model stores information about all the comments made by users on the programs, i.e. user, program, comment and the comment date.
The project utilizes internal JavaScript.
- **Mobile-responsive** : This project is responsive to the device width as it uses viewport, BootStrap's column model and flexbox features.
