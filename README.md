# Test-Blog
A News Webapp made using Django which lets you create articles, list, update and delete the articles. It is based on CRUD.
____

Here is the **Home** page of the blog. It shows the list of posts users has created.
![screen shot 2018-04-18 at 9 24 06 am](https://user-images.githubusercontent.com/25135893/38996202-52f4173e-4408-11e8-85ed-e5744955b8bf.png)

____

Here is the **login/ signup** screen of the website. We have added a security feature for during signup as well. During signup you will be sent a token on
your email-id from where you will have to enter the token to verify your email-id.
![screen shot 2018-04-18 at 9 24 31 am](https://user-images.githubusercontent.com/25135893/38996244-71e9dc1e-4408-11e8-88d5-e41ef215bec4.png)

![screen shot 2018-04-19 at 7 34 00 pm](https://user-images.githubusercontent.com/25135893/38996391-b9efadcc-4408-11e8-98ea-0b171792a35d.png)

____

You can **Create** new articles by clicking on the 'Create' link on home page.
**You can only create articles when you are logged in**
![screen shot 2018-04-18 at 9 24 54 am](https://user-images.githubusercontent.com/25135893/38996432-ceba9d48-4408-11e8-8981-daeff65e4c8f.png)

____

You can also **Edit/Update** or **Delete** posts by clicking on their respective links.
![screen shot 2018-04-18 at 9 25 24 am](https://user-images.githubusercontent.com/25135893/38996465-e484a240-4408-11e8-8b35-033f7d3327d2.png)

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
**This project uses python 3.6 and django 1.9**
