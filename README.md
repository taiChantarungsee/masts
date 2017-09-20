# masts

If you don't have Django installed, install from requirements.txt:

``` pip install -r requirements.txt ```

Apply migrations. Then if you want to see how the database script works, in the command line execute:

``` ./manage.py flush ``` 

Then execute the script:

```./manage.py shell < import_csv_data.py ```
