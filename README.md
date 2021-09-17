# Clinical_Decision_System
CDS built using Flask and Svelte

### Instruction of use
1. clone the git repo
2. open cmd / bash / shell
3. cd into frontend/CDS folder
4. now run ```npm install```
5. after run ```npm run build```
6. copy the dist folder generated and paste it to backend folder
7. now cd into backend folder
8. run ```pip install -r requirement.txt```
9. in the code folder, run train.py to create required model and json files
10. edit server.py 18 line - add a random string at the place of "KEY"
11. if you want to run debug mode, add debug=True in the brackets in server.py last line
12. run ```python server.py```, open localhost:5000 or similar in browser
13. Enjoy!!! 

### Instruction of website
1. create a user by going to login
2. the login to go to dashboard
3. use the AI sypmtoms checker
