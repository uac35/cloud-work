import requests
import os
import time

folders = ["YOUR_FOLDER_IDs"]
links   = ["YOUR_UPLOAD_URLs"]


for folder_id, upload_url in zip(folders, links):

# Replace with your API key
    api_key = "YOUR_UPLOAD_WEBSITE_API_KEY"
    drive_api_key = "YOUR_GOOGLE_CLOUD_GOOGLE_DRIVE_API_KEY"

# Get the list of files in the Google Drive folder
    url = f"https://www.googleapis.com/drive/v3/files?q='{folder_id}'+in+parents&fields=nextPageToken,files(id,name,mimeType,modifiedTime)&orderBy=modifiedTime&key={drive_api_key}"
    last_page = None

    while True:
        response = requests.get(url)
        data = response.json()
        if "nextPageToken" in data:
            url = url + "&pageToken=" + data["nextPageToken"]
        else:
            last_page = data
            break

# Get the latest file in the folder
    files = last_page["files"]
    files.reverse()

    i=0

    for file in files:
        latest_file = files[i]
# Iterate through each file in the folder
        file_id = latest_file["id"]
        file_name = latest_file["name"]
        file_mime_type = latest_file["mimeType"]

    # If the file is a Google Drive folder, skip it
        if file_mime_type == "application/vnd.google-apps.folder":
            print("This is a folder")
            i=i+1
            continue
        else:
            print('Image found') 
            break

    # Download the file
# Download the file
    file_url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&key={drive_api_key}"
    file_response = requests.get(file_url, stream=True)
    file_content = b""

# Read the file content in chunks
    for chunk in file_response.iter_content(chunk_size=8192):
        if chunk:
        
            file_content += chunk
        


    # Upload the file to the website
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Length": str(len(file_content))
    }

    files = {"file": (file_name  + ".png", file_content)}
    response = requests.post(upload_url, headers=headers, files=files)
    if response.status_code != 200:
        print(f"Failed to upload {file_name}: {response.text}")
    else:
        print(f"Succesful upload {file_name}: {response.text}")
    

