echo "___________________________________________"
echo "Running your application..."
bash installer.sh
echo "___________________________________________"
python app.py
echo "Application run complete.."
echo "___________________________________________"
echo "Pushing your app to the github repository..."
bash git_push.sh
echo "Done!!!"
echo "___________________________________________"