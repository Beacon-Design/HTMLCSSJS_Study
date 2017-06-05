# Google App Engine Installation



## Google App Engine SDK for Python



**Install Google App Engine**

Make sure you are downloading Python 2 rather than Python 3, as this is what Google App Engine uses!

**Changes to Google App Engine**

The Google App Engine system (now part of Google Cloud) has changed a lot since this course was created. You will need to create an app with a new, unique name using [**the Developer Console**](https://console.developers.google.com/) before you can deploy it. For more information, take a look at these guides written by Udacity mentor Steven Wooding: [**(Windows)**](https://drive.google.com/file/d/0Byu3UemwRffDbjd0SkdvajhIRW8/view), [**(Mac and Linux)**](https://drive.google.com/file/d/0Byu3UemwRffDc21qd3duLW9LMm8/view)

**Running Google App Engine on Mac OS**

Unfortunately Google no longer supports the GoogleAppengineLauncher program that Steve demonstrates in this video. You follow use the instructions below for Linux, or you can download the deprecated GoogleAppengineLauncher installer from the "Supporting Materials" list below. *Warning:* Use the GoogleAppengineLauncher program at your own peril! As Google no longer supports the tool it may stop working in the future. The **gcloud** command-line program is the currently supported tool.



## To install the original App Engine SDK on Mac OS X:

1. In the Finder, click **Go > Applications** to open the Applications folder.

2. Double click the `GoogleAppEngineLauncher-1.9.54.dmg` file that you downloaded to open it, then drag the**GoogleAppEngineLauncher** icon over to the Applications folder.

3. Double-click **GoogleAppEngineLauncher** in the Application folder.

4. When prompted to *Make command symlinks*, click **OK**. The symlinks allow you to run important SDK command-line tools in any terminal window.

   > **Important:** The GoogleAppEngineLauncher is a convenient UI-based tool for running and deploying App Engine apps, but it *does not* provide all the features you'll need. You can use the equivalent `gcloud`command-line tool, for many of the tasks that you'll want to perform.

5. Notice that the installation process above unpacks the contents of the App Engine SDK at the location:

   ```
   /usr/local/google_appengine
   ```

6. The App Engine SDK requires Python 2.7, which is installed by default on Mac OS X 10.6 (Snow Leopard) or later. Verify your Mac's Python installation using the following command:

   ```
   /usr/bin/env python -V
   ```

   If the output looks like `Python 2.7.[NUMBER]` then you already have the correct Python version installed. Otherwise you can download and install Python 2.7 from the [Python web site](https://www.python.org/download/releases/2.7.4).







## Run Google App Engine

1. File > New Application > Application ID : hellojohn
2. Run "hellojohn"
3. edit the  main.py of "hellojohn"











