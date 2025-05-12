# MindfulU

MindfulU is an e-learning site where users can view and subscribe to various programs and courses related to meditation.


### Description

This is an e-learning platform where users can subscribe to programs and enroll in courses. Upon enrollment, they receive hypothetical Zoom links and study materials via email. Users can also submit and view reviews for programs, courses, and navigate easily using a back-to-top arrow for a seamless learning experience. 

### Getting Started

1. Run the following commands:
```bash
python manage.py makemigrations meditate
python manage.py migrate
python manage.py runserver
```
2. Visit http://127.0.0.1:8000/ in your web browser to use the site.

### Specification

#### Index  
- The homepage features a carousel with three slides, along with two sections for **Programs** and **Courses**.  
- Clicking on either section redirects the user to the respective page.  

#### Programs  
- Displays a list of all available programs offered by **Meditate**.  
- Each program card includes an image, title, duration (in days), and the number of subscribers.  

#### Program Page  
- Clicking on a program takes the user to a detailed program page.  
- The signed-in user can **subscribe** or **unsubscribe** from the program.  
- Users can view all **program reviews** and submit a review using a form.  
- All actions are performed asynchronously.  

#### Courses  
- Displays a list of all available courses offered by **Meditate**.  
- Each course card includes an image, title, subtitle, duration, and the number of enrollees.  

#### Course Page  
- Clicking on a course takes the user to a detailed course page.  
- The signed-in user can **enroll** or **unenroll** from the course.  
- The page updates dynamically, preventing page reloads.  

#### Enrollments  
- Displays a list of all **programs** and **courses** the user has subscribed to or enrolled in.  
- Clicking on any item takes the user to its respective **Program Page** or **Course Page**.  

#### About  
- Provides information about the **Meditate** e-learning platform.

#### Additional Feature

- **Back to Top**: After scrolling **20px down**, a **back-to-top arrow** appears. Clicking it smoothly scrolls the user back to the top of the page.  

### About

This project was developed to demonstrate proficiency in Django web development, focusing on dynamic content generation, user authentication, and seamless user interactions. The platform is fully mobile-responsive, ensuring an optimal experience across all devices.

### Video Demo

You can view a video showcasing the project on [YouTube](https://www.youtube.com/watch?v=fi6bc3mwsyc).
