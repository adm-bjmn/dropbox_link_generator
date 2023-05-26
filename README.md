# dropbox_link_generator



<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Quick Guide</a>
    </li>
    <li>
      <a href="#contact">Contact</a>
    </li>
  </ol>
</details>
    
## About The Project

Dropbox Link Generator is a terminal app that allows a user to upload a file to thier dropbox account and get a direcrt url link to the uploaded file from within the command line.
The app uses the Dropbox API to connect to a users Dropbox account after being authorized using an access token.
The User is requested to state the name of the file they wish to upload followed by the folder within the dropbox that they wish to save the file to.
The app the attemps to upload the file and upon success will provide the user with a URL link to the file that can be shared with others.

<p align="right">(<a href="#top">back to top</a>)</p>


## Getting Started

1. Right click the 'dropbox_link_generator.py' file in this repository and click Download Linked File.
Save the file to the desired location.
</br>

2. Open the file in an IDE and find the variable for root directory at the top of the code. Change this variable to your prefered destination.
![RootDir](media/rootdir.jpg?raw=true "Root Directory")
You can copy a file path on macOS from the bottom of the finder window.
![path](media/path.jpg?raw=true "path")
</br>

3. Go to www.Dropbox.com/developers/apps and create a new app and allow all read and write permissions. In your new apps settings you will be able to generate an access token to allow the app permission to access your Dropbox.
![token](media/token.jpg?raw=true "token")
</br>

4. Open a terminal and navigate to the folder where you have saved dropbox_link_generator.py - Start the app by running the command ~  python3 dropbox_link_generator.py 
</br>

5. Copy and paste your Dropbox token when prompted.
![token_paste](media/token_paste.jpg?raw=true "token_paste") 
</br>

7. Copy and paste the name of the file to be uploaded
![file](media/file.jpg?raw=true "file")
</br>

7. State the name of the dropbox folder where the file is to be saved. 
![folder](media/folder.jpg?raw=true "folder")
</br>

8. The app will upload the file and provide a direct link to share with others. The app will close after completion.
(Any errors will be shown in the command line and the program will be terminated.)
![complete](media/complete.jpg?raw=true "complete")
</br>


## Contact

Adm Benjamin Bastow - adm.bjmn@gmail.com

GitHub: [https://github.com/adm-bjmn](https://github.com/adm-bjmn)

LinkedIn: [Adam Benjamin](https://www.linkedin.com/in/adam-benjamin-81273a251/)

<p align="right">(<a href="#top">back to top</a>)</p>
