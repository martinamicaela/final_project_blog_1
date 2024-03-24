<h1>Decor Statement</h1>

<h2>Introduction</h2>

This is a full-stack framework project built using Django, Python, HTML and CSS. My goal is to create a functioning and responsive website, that allows the admin user to post, and users can create an account and leave a review on the existing posts.

## User Experience Design

 target audience:

Young and middle age adults, mostly couples and women, who are planning on buying a house or renovating their homes. 

This website intends to inspire and give fresh ideas to users. It also wants to become a mean of entertainment bringing new decor trends and useful tips.

- The target audience will expect: 

   -intuitive navigation.  

   -An informative website, with information that is easy-to-find & concise.

   -Ability to review and rate posts.

   -Ability to make a user account in order to interact with the site content





## Landing page for first time users

The landing page allows users to see a display with all the upcommimg events ordered in chronologically way, being the closest one, the first appearing on the top of the page.

Besides, right at the top the users can see the logo of the page in bright blue with a navbar under it that contains the main sections of the site: Home, Register and Login. Alonside with the navbar, on the opposte side of the page the user can find the footer with the names of the developers who worked together on this project. 

<strong>Landing page for first time users</strong>

addd 

<img src="imge urls goes here" alt="home page landing page first time">

<strong>Home page across multiple devices</strong>


<img src="image url goes here" alt="Options page across different devices">

<br>

## Home page (Site Logo)

The first element that the user sees when visiting site, is the logo: Campfire Campus in big, bright blue font. 

- User experience in the Logo section: 

  - The selection of size, colour and type of font, 
 helps the user to identify quickly the name of the site.

  - The name of the site "Campfire Campus" indicates clearly that this is a website related with the academic world. In addition, the name indicates that it is a place for socialising and students are welcomed. 
  
  - Thanks to the Logo the user would feel comfortable and with a positive attitude even before checking the rest of the page. 

 <strong>Home page Logo section</strong>

<img src="./ReadmeFiles/ReadmeImages/logo.png" alt="Home page Logo section">  



## Home page (Events) 

The Home page focuses mainly on the display of the events, as we mentioned before the events appeared ordered in time. Each event is enclosed in a black square to differentiate it from the rest of events. The main features that can be highlighted are:

- The name of the event is as well a clickable button for the user. 

- Under the event name, the user can see the location, the date, and the creator of the event each one with a descriptive icon.  

- On the top right corner, the user can see the number of available spots and the number of participants attending with icon next to it. 

- Finally, on the bottom right corner there is a clickable button for those students who want to register.

- User experience in the events section: 

  - The selection of size, colour and type of font, 
 helps the user to identify quickly the name of the event and the button for registering.
 
  - The icons give important visual information about the event (location, date, author, number of participants) and help the user to navigate through the information provided.

  -The colour animation on the attending icon gives 
  
   - The clickable button is easy  to identify, as it stands alone on the right corner, besides it gives straight and intuitive access to the new user who wants to register for an upcoming event.

<strong>Home page Events section</strong>

<img src="imge urls goes here" alt="Home page Events section">


## Home page (Navbar and foooter) 

Apart from the events, section the Home page also provides the user with a useful navbar and a informative footer. The navbar is divided into three main areas of interest; Home, Register and Login and the footer proportionate information of interest about the developers that collaborated on this project. The main features that can be highlithed are:

- The clickable sections in both, the navbar and the footer 

- The colour animation when the user hovers over the clickable parts.

- The change in the cursor icon when the user hovers over the clickable parts.

- User experience in the navbar and footer section: 

  - The selection of size, colour and type of font, 
 helps the user to identify quickly the different sections that can be found on the navbar.

  - The colour transition animation in the navbar and the footer, as well as the change in the cursor icon, both give clear indications about the clickable property of the elements in these sections. Besides, they produce an eye-catching effect on the user when these elements are hoovered over, creating the need for clicking and a sense of mystery.

  - The Git hub cat icon in the footer,  gives important visual information about the names, as it makes explicit their contribution as developers in the project. 
  

<strong>Home page Events section</strong>

<img src="./ReadmeFiles/ReadmeImages/navbar.png" alt="Home page Navbar section">

<br>

<img src="./ReadmeFiles/ReadmeImages/footer.png" alt="Home page Footer section">




## Authentication

### Registration

We have a registration page built using the default django user registration form, we have a custom view to display messages back to the user to feedback when the form is incorrect but as the default view isn't very customizable it displays mid-form. A fully bespoke solution would be needed next project

<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/registration.png">
</div>

### login

We have a simple frictionless login page so users can log in quickly, it will feedback to the user if there are errors. a future feature would be password recovery via email

<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/login.png">
</div>

## Design Choices

### Fonts 

IntroRust was chosen as a more interesting font that would give character to the page. It was sourced from [here](https://www.fontspring.com/fonts/fontfabric/intro-rust-free?utm_source=fontsquirrel.com&utm_medium=download_link&utm_campaign=intro-rust#firstfreeproduct)

We selected the font style Poppins 'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap'. It's is sans serif, so very clear and easy to read. it's popularity on the web gives it instant recognition as well'


We selected more plain and simple design with professional colours but a big, vibrant pop of pink as an accent. We derived our colours from [coolors](https://coolors.co/012765-d30cd5-003fa5-010100-f8fff4)

<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/coolors.png">
</div>

### Wire Frames

<strong>The wireframes were constructed using Balsamiq in a group call to get feedback on all design choices. This was so front-end and back-end could be aligned even from the early stages to think of any pitfalls that could occur<br></strong>

You can view the wireframes [here](./ReadmeFiles/Wireframes/CampusCampfire.pdf)

<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/wireframe.png">
</div>

### Database

We tried to plan out our models before had to avoid having to do migrations mid-project. we tried to work out the field types, one-to-many, PK or FK etc. 

Here is an image of our ERD:
<div align="center">
  <img src="./ReadmeFiles/ReadmeImages/ERD.png">
</div>

## User Stories, features and bugs

<table>
  <tr>
    <th>User Story</th>
    <th>Features</th>
    <th>Bugs / Issues - tested across viewports of all devices using Google Dev Tools</th>
  </tr>
   <tr>
    <td>As a site user, I can view a paginated list of posts so that I can select which post I want to view.</td>
    <td>Given more than one post in the database, these multiple posts are listed.</td>
    <td>None detected.</td>
   
    
  </tr>
  <tr>
    <td>As a Site User, I can click on a post so that I can read the full text.</td>
    <td>When a blog post title is clicked on a detailed view of the post is seen.</td>
    <td>None detected.</td>
  
  </tr>
   <tr>
    <td>As a Site User / Admin I can view reviews on an individual post so that I can read the conversation</td>
    <td>Given one or more user reviews the admin can view them.
    <br>Then a site user can click on the review thread to read the conversation.</td>
    <td>None detected.</td>
  <tr>
    <td>As a Site User I can register an account so that I can review on a post.</td>
    <td>Given an email a user can register an account.<br>Then the user can log in.When the user is logged in they can review. </td>
    <td>None detected.</td>
  </tr>
  <tr>
    <td>As a Site User I can leave reviews on a post so that I can be involved in the conversation</td>
    <td>When a user review is approved Then a user can reply  Given more than one review then there is a conversation thread</td>
    <td>None detected.</td>
    
  </tr>
  <tr>
    <td>As a Site User I can modify or delete my review on a post so that I can be involved in the conversation</td>
    <td>Given a logged in user, they can modify their review Given a logged in user, they can delete their review</td>
    <td>None detected</td>
    
  </tr>
  <tr>
    <td>As a Site Admin I can create, read, update and delete posts so that I can manage my blog content</td>
    <td>Given a logged in admin, they can create a blog post Given a logged in admin, they can read a blog post
    Given a logged in admin, they can update a blog post
    Given a logged in admin, they can delete a blog post</td>
    <td>None detected</td>
    
  </tr>
  <tr>
    <td>As a Site Admin I can create draft posts so that I can finish writing the content later</td>
    <td>Given a logged in user, they can save a draft blog post
    Then they can finish the content at a later time</td>
    <td>None detected</td>
    
  </tr>
  <tr>
    <td>As a Site Admin I can approve or disapprove reviews so that I can filter out objectionable reviews</td>
    <td>Given a logged in user, they can approve a review
     Given a logged in user, they can disapprove a review</td>
    <td>None detected</td>
    
  </tr>
  <tr>
    <td>As an Admin I can suggest to the user where to buy the product my post is focused on so that I can give them relevant information.</td>
    <td>The user can see the name of the product
     The user can see the price of the product</td>
    <td>None detected</td>
    
  </tr>
   <tr>
    <td>As a user, I can see the store and access the product through the blog site so I don't need to look for the product online.</td>
    <td>The user can see the name of the store where they can buy the product
    The name of the store can give them a link to the actual product</td>
    <td>None detected</td>
    
  </tr>
  <tr>
    <td>As an Admin I can add new decor styles to my database so that my posts can be categorised</td>
    <td>Given a logged in Admin, I can generate new decor styles in the database
    Given a logged in Admin, I can link the decor style generated to a specific post
    Given a logged in Admin, I can organise my posts using the decor style section in the admin panel</td>
    <td>None detected</td>
    
  </tr>
  <tr>
    <td>As a user, I want the site to be visually appealing.</td>
    <td> Select complementary colour scheme. <br>
    Different elements/features delineated.</td>
    <td>None detected</td>
    
  </tr>
  </table>

<br>


## Fixed Bugs / Issues
<br>
<table>
  <tr>
    <th>Bug/Issue</th>
    <th>Image</th>
    <th>Resolution</th>
  </tr>
  <tr>
  <td>"Delete button" it was not behaving as expected</td>
    <td>The project needed the static files to be updated "python3 manage.py collectstatic"</td>
  </tr>
  </table>

## Unfixed Bugs / Issues
<table>
  <tr>
    <th>Bug/Issue</th>
    <th>Image</th>
    <th>Resolution</th>
  </tr>
  <tr>
  <td>On smaller devices the "footer" does not extend completely</td>
    <td><img src="readmephotos/phonebug.png" alt="Image showing the footer on smaller devices"></td>
    
  <td>Unfortunately I ran out of time to fix this. I would in future sprints change to a fully responsive footer across all the devices, it works well on the rest of devices such as larger phones and tablets.</td>
  </tr>
</table>


### Validator Testing 

For HTML validation https://validator.w3.org/

For CSS validation  https://jigsaw.w3.org/css-validator/



## Deployment

Site successfully deployed on [heroku](https://blogdecor1-242e1f9b3655.herokuapp.com/)

## Credits 

[Coolors](https://coolors.co/012765-d30cd5-003fa5-010100-f8fff4) was used for colour pallette

[Bootstrap](https://getbootstrap.com/)

[fontawesome](https://fontawesome.com/)

[Code Institute](https://codeinstitute.net/ie/) - 'I think therefore I blog' project helped me with recipe details page and pagination

[Django documentation](https://docs.djangoproject.com/en/4.0/topics/pagination/) - also helped me with pagination and other problems


## Media 
All images were taken from [Pixabay](https://pixabay.com/)

### Content 

For validation in HTML https://validator.w3.org/

For validation in CSS https://jigsaw.w3.org/css-validator/

Wireframes produced using [Balsamiq](https://balsamiq.com/)

### Acknowledgements

Thanks to my mentor Spencer for his help on how to upload images and his guidance for the models design. 

Thanks to my colleague Tom for his help, debugging my site on the very last moment when two brains think better than one.



