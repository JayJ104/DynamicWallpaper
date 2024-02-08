# DynamicWallpaper
GDSC Explorer Cohort Project - Team Eve

## Tools used:
Frontend - React Native
Backend  - Python, Flask

## SETUP
## Frontend
### 1. Node.js
Download the Node.js installer for your OS from https://nodejs.org/en/download/current

Run the installer and follow the installation wizard. Open a terminal on VSCode and type node --version to verify your node installation. Type npm --v to verify your npm installation.

    Troubleshooting: 
    a. If you get an error saying that node or npm is not recognized as a command, try restarting VSCode to see if the issue fixes itself. (If you had VSCode opened while installing Node, this should fix it)

    b. If the problem persists, search for Environment variables in your Start menu. Click on Edit your Environment variables. Click on Environment Variables in the new window that opens up.

    c. Find the variable Path and click on Edit.

    d. Check for C:\Program Files\nodejs\ in the list of paths that appear. If it's not there, click on New and add it to the list.

    e. Restart VSCode and it should ideally work now.


### 2. Eslint Extension
Go to the Extensions tab on VSCode and install ESLint.

Once it is installed, open your Command Palette by pressing ```Ctrl + SHift + P``` or ```Command + Shift + P``` and search for **Preferences: Open Workspace Settings (JSON)**. Open the file and add this code into the file:

```
{"editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
},
"eslint.validate": ["javascript"]
}
```

## Python Virtual Environment
Run these commands on the terminal:

```
cd scripts
python -m venv venv
```

Activate the environment on Windows:

```
.\venv\Scripts\activate
```

or on Mac/Linux:

```
source venv/bin/activate
```

You should see **(venv)** at the beginning of the file path in your terminal

Installing dependencies in the scripts folder:
```
pip install -r requirements.txt
```

## Getting Started=
### Frontend Emulator:

```
cd frontend
npm install     # installs dependencies
npm run web     # starts app emulator
```

Open http://localhost:3000 with your browser to see the result.

**Learn More**
React Native Documentation: https://reactnative.dev/docs/getting-started 

### Backend Server
coming soon...