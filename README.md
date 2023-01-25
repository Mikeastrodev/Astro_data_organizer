# ASTRO_DATA_ORGANIZER

ASIAIR Data Organizer
The script  purpose is to sort and organize image files taken from a telescope using a specific naming convention. The script is built using Python and PyQt5 library, which is used for the GUI.

The file structure in order to work should look like this out of ASIAIR:

Light/Dark/Bias_Target_ExposureTime_Bin_CameraModel_Filter_Gain_Date_Sequence.fit

The script begins by defining the main class "MyApp" and initializing the UI elements such as buttons, labels, and checkboxes. The "Select Folder" button allows the user to select the folder containing the image files, the "Organize" button triggers the sorting process, and the checkboxes allow the user to specify the criteria for sorting the files (by filter, target, or exposure time).

Once the "Organize" button is pressed, the script starts by iterating over all files in the selected folder. It then checks the file extension to determine if it's an image file (in this case, only .jpg files are deleted) or a .fit file, which is the file type used for the telescope images.

If the file is a .fit file, the script splits the file name by underscores to extract the target name, exposure time, and filter name. These values are then used to create subfolders within the selected folder, following the criteria specified by the user in the checkboxes. The script then moves the .fit file to the appropriate subfolder.

Finally, the script displays a message box with a message of completion.

In summary, "ASIAIR Data Organizer" is a script that simplifies the process of sorting and organizing image files taken from a telescope, by providing an easy-to-use GUI and allowing the user to specify the sorting criteria. It is useful for astronomers and astrophotographers who want to keep their image files organized in a systematic manner.

The file structure in order to work should look like this out of ASIAIR:

Light/Dark/Bias_Target_ExposureTime_Bin_CameraModel_Filter_Gain_Date_Sequence.fit

Setup File here: https://drive.google.com/file/d/1K47yDAmO_nqUJYQn9NhrPZbGULDL0DoO/
