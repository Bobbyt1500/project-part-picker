1. Create virtual environment `python -m venv environment`
2. Activate virtual environment `./environment/Scripts/activate`
3. Install required modules `pip install -r requirements.txt`
4. Create .env file `echo > .env`
5. In the .env file set the following variables:
    * DB_USERNAME="example: username"
    * DB_PASSWORD="example: password"
    * DB_CLUSTER="example: cluster0"
6. Start the flask server with `python app.py`
