echo import subprocess > pipeline.py
echo import sys >> pipeline.py
echo def run(cmd): >> pipeline.py
echo     result = subprocess.run(cmd, shell=True) >> pipeline.py
echo     if result.returncode != 0: sys.exit(1) >> pipeline.py
echo. >> pipeline.py
echo print("Step 3: Fetching data...") >> pipeline.py
echo run("git pull origin main") >> pipeline.py
echo. >> pipeline.py
echo print("Step 4: Training model...") >> pipeline.py
echo run("python train.py") >> pipeline.py
echo. >> pipeline.py
echo print("Step 5: Building Docker...") >> pipeline.py
echo run("docker build -t ml-api .") >> pipeline.py
echo. >> pipeline.py
echo print("Step 6: Running container...") >> pipeline.py
echo run("docker stop ml-api 2>nul") >> pipeline.py
echo run("docker rm ml-api 2>nul") >> pipeline.py
echo run("docker run -d --name ml-api -p 8000:8000 ml-api") >> pipeline.py
echo. >> pipeline.py
echo print("Done! API at http://localhost:8000/metrics") >> pipeline.py