# Test-Blog
A News Webapp made using Django which lets you create articles, list, update and delete the articles. It is based on CRUD.
____

Here is the **Home** page of the blog. It shows the list of posts users has created.
![screenshot from 2017-09-26 23 46 53](https://user-images.githubusercontent.com/25135893/31447129-ddaa844c-aebe-11e7-839e-6822b33208d5.png)

____

Here is the **login/ signup** screen of the website. We have added a security feature for during signup as well. During signup you will be sent a token on
your email-id from where you will have to enter the token to verify your email-id.

____

You can **Create** new articles by clicking on the 'Create' link on home page.
**You can only create articles when you are logged in**
![screenshot from 2017-09-26 23 44 08](https://user-images.githubusercontent.com/25135893/31447235-210e6780-aebf-11e7-8720-e17110d3e52a.png)

____

You can also **Edit/Update** or **Delete** posts by clicking on their respective links.
![screenshot from 2017-09-26 23 43 49](https://user-images.githubusercontent.com/25135893/31447355-65459ec8-aebf-11e7-8e4b-0908485d9f14.png)

____

Now to run this app on your pc, you can clone this repository or download it from above.
Then navigate to the folder that you have downloaded and type in your terminal
```
pip install -r requirements.txt
```
Then run the django server using
```
python manage.py runserver
```
