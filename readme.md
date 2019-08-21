## Demo and playground project for  web crwling with Scrapy

Following this tutorial:  
https://www.youtube.com/playlist?list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t

The crawler has three pipelines:
* Print items to console
* Save items to SQLite database
* Save items to MySQL database

Create Anaconda environment with the environment.yml: **conda env create -f environment.yml**

```conda env export > environment.yml´´´
```´´´


## Issues

* I had following error message while using mysql connector mysql-connector-python: "ModuleNotFoundError: No module named 'mysql'". Maybe it was caused by using mysql-connector-python version 2.0.4. The error was gone after setting up to version 8.0.16