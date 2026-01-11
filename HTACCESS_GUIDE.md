# .htaccess Configuration Guide for Flask on cPanel

## File Description

**`.htaccess`** - Production-ready configuration for your Flask application at `/home/logicalv/repositories/HostingTestPython`

## How to Use

### Option 1: Using cPanel Setup Python App (Recommended)

If you configured your app using **"Setup Python App"** in cPanel:

1. **You may NOT need a .htaccess file** - cPanel creates it automatically
2. If you want to customize, upload `.htaccess` to your application root
3. Adjust the paths to match your setup

### Option 2: Manual Configuration

If you want full control without using Setup Python App:

1. Choose the appropriate `.htaccess` file
2. Rename/copy it to `.htaccess` (no prefix)
3. Upload to your application root directory
4. Customize the paths

---

## For Your Current Setup

### Step 1: Upload to Server

Upload `.htaccess` to:
```
/home/logicalv/repositories/HostingTestPython/
```

**In cPanel File Manager:**
1. Navigate to `/home/logicalv/repositories/HostingTestPython/`
2. Upload `.htaccess`

**Via Terminal:**
```bash
# If uploading from local machine via SCP/FTP
cd /home/logicalv/repositories/HostingTestPython/
# Upload the .htaccess file
```

### Step 2: Verify Files Are Present

Your directory should contain:
```
/home/logicalv/repositories/HostingTestPython/
├── .htaccess
├── app.py
└── requirements.txt
```

Check with:
```bash
ls -la /home/logicalv/repositories/HostingTestPython/
```

### Step 3: Test Your Application

Visit your application URL after uploading

---

## Important Notes

### When Using "Setup Python App" in cPanel:

✅ **cPanel automatically manages Passenger configuration**
- It creates/updates `.htaccess` automatically
- It sets the correct Python path
- It manages the virtual environment

❌ **Manual .htaccess may conflict**
- Your manual settings might be overwritten
- Use Setup Python App settings instead of .htaccess when possible

### When to Use Manual .htaccess:

Use a manual `.htaccess` file when you need to:
- Set custom environment variables
- Configure URL rewrites
- Add security headers
- Enable HTTPS redirects
- Fine-tune Passenger settings

---

## Customization Examples

### Set Environment Variables

Add these lines to your `.htaccess`:

```apache
SetEnv NAME "John Doe"
SetEnv CUSTOM_MESSAGE "Welcome to my Flask app!"
SetEnv DATABASE_URL "mysql://user:pass@localhost/dbname"
```

Then access them in `app.py`:
```python
import os
name = os.environ.get('NAME')  # Returns "John Doe"
```

### Force HTTPS

Uncomment these lines in `.htaccess`:

```apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

### Enable Debug Mode (Development Only)

Change this line:
```apache
PassengerAppEnv production
```

To:
```apache
PassengerAppEnv development
```

And:
```apache
PassengerFriendlyErrorPages on
```

⚠️ **Never use debug mode in production!**

---

## Troubleshooting

### .htaccess Not Working

**Check:**
1. File is named exactly `.htaccess` (starts with a dot)
2. File is in the application root directory
3. File permissions are correct (644)
4. No syntax errors in the file

**Set correct permissions:**
```bash
chmod 644 /home/logicalv/newapp.logicalvalley.in/.htaccess
```

### Application Still Not Starting

**Possible reasons:**
1. **Passenger not enabled** - Check if `PassengerEnabled On` is present
2. **Wrong paths** - Verify `PassengerAppRoot` matches your actual directory
3. **Missing dependencies** - Install Flask in virtual environment
4. **Python version mismatch** - Check `PassengerPython` path

**Debug steps:**
```bash
# 1. Check .htaccess exists
ls -la /home/logicalv/newapp.logicalvalley.in/.htaccess

# 2. View .htaccess contents
cat /home/logicalv/newapp.logicalvalley.in/.htaccess

# 3. Check error logs
tail -50 /home/logicalv/logs/error_log

# 4. Verify app.py exists
ls -la /home/logicalv/newapp.logicalvalley.in/app.py
```

### 500 Internal Server Error

**Common causes:**
- Syntax error in `.htaccess`
- Wrong `PassengerAppRoot` path
- Python app has errors
- Missing dependencies

**Check Apache error log:**
```bash
tail -50 /home/logicalv/logs/error_log
```

### Environment Variables Not Working

Make sure:
1. `SetEnv` directives are in `.htaccess`
2. Variables are accessed correctly in Python: `os.environ.get('VAR_NAME')`
3. Application has been restarted after changes

---

## Restarting Your Application

### Method 1: Via cPanel

1. Go to **Setup Python App**
2. Click **Restart** button

### Method 2: Via .htaccess Trick

Create a `tmp/restart.txt` file:

```bash
mkdir -p /home/logicalv/newapp.logicalvalley.in/tmp
touch /home/logicalv/newapp.logicalvalley.in/tmp/restart.txt
```

Passenger will detect this and restart the app automatically.

To restart again:
```bash
touch /home/logicalv/newapp.logicalvalley.in/tmp/restart.txt
```

---

## Quick Reference

### Your Configuration:

**Application Root:** `/home/logicalv/repositories/HostingTestPython`  
**Startup File:** `app.py`  
**Entry Point:** `app`  
**.htaccess Location:** `/home/logicalv/repositories/HostingTestPython/.htaccess`

### Essential Files:
```
/home/logicalv/repositories/HostingTestPython/
├── .htaccess          ← Passenger configuration
├── app.py             ← Your Flask application
├── requirements.txt   ← Python dependencies
└── tmp/
    └── restart.txt    ← Touch to restart app
```

### Useful Commands:
```bash
# View .htaccess
cat /home/logicalv/repositories/HostingTestPython/.htaccess

# Edit .htaccess (in cPanel File Manager or via editor)
nano /home/logicalv/repositories/HostingTestPython/.htaccess

# Check permissions
ls -la /home/logicalv/repositories/HostingTestPython/.htaccess

# Restart application
mkdir -p /home/logicalv/repositories/HostingTestPython/tmp
touch /home/logicalv/repositories/HostingTestPython/tmp/restart.txt
```

---

## Best Practices

1. ✅ Use **Setup Python App** in cPanel for initial configuration
2. ✅ Only add manual `.htaccess` for custom features
3. ✅ Keep `.htaccess` backed up
4. ✅ Test changes in development first
5. ✅ Use `PassengerAppEnv production` in production
6. ✅ Disable `PassengerFriendlyErrorPages` in production
7. ✅ Protect sensitive files (`.env`, `requirements.txt`)
8. ✅ Enable HTTPS for production sites

---

## Need Help?

1. **Check logs:** `tail -50 /home/logicalv/logs/error_log`
2. **Verify paths:** Make sure all paths in `.htaccess` match your setup
3. **Test syntax:** Use an online .htaccess validator
4. **Contact support:** Provide your `.htaccess` content and error logs

---

Your `.htaccess` files are ready to use! 🚀

