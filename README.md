# DAP Project

## Abstract
As stated by Arthur Conan Doyle "To revenge crime is important, but to prevent it is more so". The main objective of this study is to analyse crime and gain valuable insights from the same to curb them from taking place. To achieve the objectives, reported crime from three different regions were used to perform analysis. We used ETL methodology to prepare the datasets for analysis. The analysis of these datasets showed that even though crime rates were fluctuating in different regions, crimes classified as assault are on a rise. This ever-increasing rise of such crime can be potentially dangerous for the future and thus further research needs to be done on understanding the main reason of such assault.

## Steps to run the project

1. Setup the MongoDB on the local system by running the command: docker-compose up --build -d mongodb 
2. For this project, the postgres was installed on the local system. Database, Username and Password can be changed from 
config.py file. For this project, Database is 'postgres', Username is 'postgres' and Password is '1234'
3. Activate the virtual environment by using the command for windows: dapproject\Scripts\activate.bat and for MacOS: source dapproject/bin/activate
5. Install the required libraries from requirements.txt using the command: pip install -r requirements.txt
6. run the main.py file using the command: python main.py 
