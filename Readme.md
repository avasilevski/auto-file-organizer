📁 Auto File Organizer
Automatically sort files in your Downloads folder into categorized subfolders based on file type (e.g., PDFs, images, videos, etc.).

🧩 File Organizer Workflow
	1.	main.py
	•	Starts the application and initializes a file watcher on the target directory (WORK_PATH)
	•	Uses WatcherHandler to bind the on_created event to a handler
	•	Keeps the process alive until interrupted (Ctrl+C)
	2.	watcher.py
	•	Implements Handler class that reacts to new file creation
	•	When triggered, it calls organize() from organizer.py
	3.	organizer.py
	•	organize() handles file classification and movement:
	•	Uses get_category() to classify based on extension
	•	Creates the destination folder under WORK_PATH
	•	Moves the file
	•	Calls log_move() from logger.py to record the action
	4.	logger.py
	•	Runs a C++ subprocess to log messages
	•	The C++ main.out:
	•	Creates the log directory (../logs)
	•	Appends timestamped logs to log.txt

▶️ How to Run
./run.sh

📦 Dependencies
	•	watchdog
	•	python-dotenv