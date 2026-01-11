# Troubleshooting Python App in cPanel

## Finding Logs When App Won't Start

### 1. Primary Log: Passenger Log

**Location:**
```
/home/YOUR_USERNAME/logs/passenger.log
```

**View in Terminal:**
```bash
# View last 50 lines
tail -50 ~/logs/passenger.log

# Watch real-time (press Ctrl+C to stop)
tail -f ~/logs/passenger.log

# View entire file
less ~/logs/passenger.log

# Search for specific errors
grep -i "error\|traceback\|exception" ~/logs/passenger.log
```

### 2. Apache Error Log

**Location:**
```
/home/YOUR_USERNAME/logs/error_log
```

**View in Terminal:**
```bash
tail -100 ~/logs/error_log
grep -i python ~/logs/error_log
```

### 3. Application-Specific Logs

Check the log path you specified in "Setup Python App" interface (if any).

---

## Common Issues and Solutions

### Issue 1: "ModuleNotFoundError: No module named 'flask'"

**Cause:** Dependencies not installed in virtual environment

**Solution:**
```bash
# 1. Go to cPanel → Setup Python App
# 2. Copy the command shown (looks like below)
source /home/logicalv/virtualenv/repositories/HostingTest/3.11/bin/activate && cd /home/logicalv/repositories/HostingTest

# 3. Run it in Terminal, then install dependencies
pip install -r requirements.txt

# 4. Verify installation
pip list | grep -i flask

# 5. Restart app in cPanel interface
```

### Issue 2: "ImportError: cannot import name 'app'"

**Cause:** Wrong entry point name or app.py not found

**Check:**
1. Verify `app.py` exists in Application Root directory
2. Verify Application Entry Point is exactly: `app` (lowercase)
3. Check that app.py contains: `app = Flask(__name__)`

**Solution:**
```bash
# Verify file exists
ls -la /home/logicalv/repositories/HostingTest/app.py

# Check the content
cat /home/logicalv/repositories/HostingTest/app.py | grep "app = Flask"
```

### Issue 3: "SyntaxError" or Python Version Mismatch

**Cause:** Code written for different Python version

**Solution:**
1. In Setup Python App, change Python version to 3.9 or 3.11
2. Reinstall dependencies for new version
3. Restart app

### Issue 4: File Permission Errors

**Cause:** Incorrect file permissions

**Solution:**
```bash
# Set correct permissions
cd /home/logicalv/repositories/HostingTest
chmod 644 app.py
chmod 644 requirements.txt
chmod 755 .
```

### Issue 5: App Shows White/Blank Page or "Application Error"

**Check Passenger Log:**
```bash
tail -50 ~/logs/passenger.log
```

Look for:
- Python exceptions
- Import errors
- Syntax errors

### Issue 6: "502 Bad Gateway" or "503 Service Unavailable"

**Causes:**
- App taking too long to start
- Python process crashing
- Wrong Application Root path

**Solution:**
```bash
# 1. Check passenger log for crashes
tail -100 ~/logs/passenger.log

# 2. Verify Application Root in Setup Python App
#    Should match where your app.py is located

# 3. Test app locally first (if possible)
python app.py
```

---

## Step-by-Step Debugging Process

### Step 1: Check Passenger Log
```bash
tail -50 ~/logs/passenger.log
```

**What to look for:**
- `Traceback` - Shows Python errors
- `ModuleNotFoundError` - Missing dependencies
- `SyntaxError` - Code syntax issues
- `ImportError` - Can't import your app

### Step 2: Verify Application Setup

In cPanel → Setup Python App, verify:
- [ ] **Application Root**: `/home/logicalv/repositories/HostingTest`
- [ ] **Application Startup File**: `app.py`
- [ ] **Application Entry Point**: `app`
- [ ] **Python Version**: 3.9 or higher

### Step 3: Check Files Exist
```bash
cd /home/logicalv/repositories/HostingTest
ls -la

# You should see:
# app.py
# requirements.txt
```

### Step 4: Verify Dependencies Installed
```bash
# Activate virtual environment (copy command from Setup Python App)
source /home/logicalv/virtualenv/repositories/HostingTest/3.11/bin/activate

# Check installed packages
pip list

# Should see Flask and Werkzeug
```

### Step 5: Test Python Syntax
```bash
# Activate virtual environment first
python -m py_compile app.py

# If no output = success
# If error = syntax problem in app.py
```

### Step 6: Check Application Status

In Setup Python App interface:
- Status indicator (should be green/running)
- Any error messages at top of page

### Step 7: Restart Application

After fixing issues:
1. Go to Setup Python App
2. Click the **Restart** button (circular arrow icon)
3. Wait 10-15 seconds
4. Try accessing your URL again
5. Check logs again if still failing

---

## Useful Commands for Debugging

```bash
# View last 100 lines of passenger log
tail -100 ~/logs/passenger.log

# Search for recent errors
grep -i "error" ~/logs/passenger.log | tail -20

# Check if app.py has syntax errors
python -m py_compile ~/repositories/HostingTest/app.py

# List all Python packages in virtual env
source ~/virtualenv/repositories/HostingTest/3.11/bin/activate
pip list

# Check Python version being used
python --version

# View file permissions
ls -la ~/repositories/HostingTest/

# Test if Flask is importable
python -c "from flask import Flask; print('Flask OK')"
```

---

## Getting More Detailed Logs

Add logging to your `app.py`:

```python
import os
import logging
from flask import Flask

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('/home/logicalv/logs/flask_app.log'),
        logging.StreamHandler()
    ]
)

app = Flask(__name__)
app.logger.info("Flask app starting...")

@app.route('/')
def hello_world():
    app.logger.info("Hello world route accessed")
    name = os.environ.get('NAME', 'World')
    env_var = os.environ.get('CUSTOM_MESSAGE', 'No CUSTOM_MESSAGE environment variable set')
    
    return f'''
    <h1>Hello, {name}!</h1>
    <h2>Environment Variable:</h2>
    <p><strong>CUSTOM_MESSAGE:</strong> {env_var}</p>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
```

Then check:
```bash
tail -f ~/logs/flask_app.log
```

---

## Still Not Working?

1. **Delete and recreate the app:**
   - Delete in Setup Python App
   - Remove all files from Application Root
   - Create fresh app
   - Upload files again
   - Install dependencies
   - Restart

2. **Contact hosting support** with:
   - Last 50 lines of passenger.log
   - Your Application Root path
   - Python version you're using
   - Content of your app.py

3. **Test with minimal app:**

Create a super simple test:

```python
# test.py
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"<h1>Python App Works!</h1>"]
```

If this works, the issue is with your Flask code.

---

## Quick Checklist

- [ ] Passenger log shows no errors
- [ ] app.py exists in Application Root
- [ ] Application Entry Point is `app`
- [ ] Flask is installed in virtual environment
- [ ] File permissions are correct (644 for files)
- [ ] Python version is 3.9+
- [ ] Application has been restarted
- [ ] No typos in Application Startup File name
- [ ] Virtual environment path matches Application Root

---

## Most Common Solution

90% of the time, the issue is missing dependencies:

```bash
# Copy the activate command from Setup Python App interface
source /home/logicalv/virtualenv/repositories/HostingTest/3.11/bin/activate && cd /home/logicalv/repositories/HostingTest

# Install dependencies
pip install -r requirements.txt

# Verify
pip list | grep Flask

# Go back to Setup Python App and click Restart
```

