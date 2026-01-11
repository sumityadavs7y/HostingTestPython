# cPanel Deployment Guide

This guide explains how to deploy your Flask application on cPanel hosting.

## Configuration Values for cPanel

When setting up your Python application in cPanel's "Setup Python App" interface:

| Setting | Value | Description |
|---------|-------|-------------|
| **Application Startup File** | `app.py` | The filename containing your Flask app |
| **Application Entry Point** | `app` | The Flask application object name |
| **Python Version** | 3.9 or higher | Recommended version |
| **Application Root** | `repositories/HostingTestPython` | Where you upload your files (relative path) |

## Step-by-Step Deployment

### 1. Upload Files to cPanel
Upload these files to your application directory:
- `app.py`
- `requirements.txt`

### 2. Access cPanel Python App Setup
1. Log into cPanel
2. Find "Setup Python App" (usually under Software section)
3. Click "Create Application"

### 3. Configure Your Application

Fill in the form with these values:

**Python Version:** Select 3.9 or higher

**Application Root:** 
```
repositories/HostingTestPython
```
(use relative path from home directory)

**Application URL:** 
- Select your domain or subdomain

**Application Startup File:**
```
app.py
```

**Application Entry Point:**
```
app
```

**Passenger Log File** (optional):
```
/home/yourusername/logs/passenger.log
```

### 4. Set Environment Variables

In the cPanel Python App interface, scroll down to "Environment Variables" section and add:

| Variable Name | Value | Description |
|--------------|-------|-------------|
| `NAME` | `World` | Name to display in greeting |
| `CUSTOM_MESSAGE` | `Hello from cPanel!` | Custom message to display |

Click "Add" for each variable.

### 5. Install Dependencies

After creating the app, cPanel will show a command to enter in the virtual environment. It looks like:

```bash
source /home/username/virtualenv/your-app-folder/3.9/bin/activate && cd /home/username/your-app-folder
```

Copy and run this in cPanel Terminal, then install dependencies:

```bash
pip install -r requirements.txt
```

### 6. Start/Restart the Application

Back in the Python App interface:
- Click the "Restart" button (circular arrow icon)
- Your app should now be live!

## Accessing Your Application

Your Flask app will be available at the URL you configured:
- `https://yourdomain.com` (if root domain)
- `https://yourdomain.com/myapp` (if subdirectory)
- `https://subdomain.yourdomain.com` (if subdomain)

## Troubleshooting

### Check Passenger Logs
If the app doesn't work, check the passenger log file:
```bash
tail -f /home/yourusername/logs/passenger.log
```

### Common Issues

1. **500 Internal Server Error**
   - Check that `app.py` is in the Application Root directory
   - Verify the entry point is exactly `app` (case-sensitive)
   - Check passenger logs for Python errors

2. **Module Not Found Errors**
   - Ensure you ran `pip install -r requirements.txt` in the virtual environment
   - Restart the application after installing dependencies

3. **Application Won't Start**
   - Verify Python version compatibility
   - Check that all paths are correct
   - Make sure `app.py` has no syntax errors

### Testing Locally First

Before deploying, test locally:
```bash
python app.py
```
Visit `http://localhost:5000` to verify it works.

## Updating Your Application

1. Upload modified files via cPanel File Manager or FTP
2. If you changed `requirements.txt`, reinstall:
   ```bash
   source /home/username/virtualenv/your-app-folder/3.9/bin/activate
   pip install -r requirements.txt
   ```
3. Click "Restart" in the Python App interface

## Important Notes

- **Debug Mode**: The app automatically disables debug mode in production (Passenger handles this)
- **Port Configuration**: Not needed for cPanel - Passenger manages ports
- **Host Binding**: `0.0.0.0` in the code is fine - Passenger controls the actual binding
- **File Permissions**: Ensure `app.py` has read permissions (644)

## Quick Reference

**Application Startup File:** `app.py`  
**Application Entry Point:** `app`  

That's it! Your Flask application should now be running on cPanel.

