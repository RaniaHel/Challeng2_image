#Create env
python3 -m venv project_env2

#Activate the environment
source project_env2/bin/activate

pip install -r requirements.txt

flask db init
flask db migrate
flask db upgrade

#Run the code
flask run

----------------- Example of usage -----------------

Post request (json body format):

(POST) http://127.0.0.1:5000/solution

{
    "depth_min":9100,
    "depth_max":9126
}
