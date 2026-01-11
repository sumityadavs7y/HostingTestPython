# Fix: Double Path Issue in cPanel Python App

## Problem Identified

Your error log shows:
```
File not found [/home/logicalv/home/logicalv/repositories/HostingTest/403.shtml]
```

Notice `/home/logicalv` appears **twice** - this means the Application Root is configured incorrectly.

## Root Cause

cPanel automatically prepends `/home/USERNAME/` to your Application Root path.

**What's happening:**
- You entered: `/home/logicalv/repositories/HostingTest`
- cPanel adds prefix: `/home/logicalv/` + `/home/logicalv/repositories/HostingTest`
- Result: `/home/logicalv/home/logicalv/repositories/HostingTest` ❌

## Solution

### Step 1: Edit Your Python App Configuration

1. Log into cPanel
2. Go to **Setup Python App**
3. Click on your application name (to edit it)
4. Find the **Application Root** field

### Step 2: Fix the Application Root Path

**Change FROM:**
```
/home/logicalv/repositories/HostingTest
```

**Change TO (option 1 - relative path):**
```
repositories/HostingTest
```

**OR TO (option 2 - absolute from home):**
```
/repositories/HostingTest
```

### Step 3: Verify Other Settings

While you're here, make sure these are correct:

- **Application Startup File:** `app.py`
- **Application Entry Point:** `app`
- **Python Version:** 3.9 or higher

### Step 4: Save and Restart

1. Click **Update** button
2. Click **Restart** button (circular arrow icon)
3. Wait 10-15 seconds

### Step 5: Test Your Application

Visit your application URL:
```
https://test.logicalvalley.in
```

You should now see your Flask app!

---

## Verification

After the change, cPanel will use:
```
/home/logicalv/ + repositories/HostingTest = /home/logicalv/repositories/HostingTest ✅
```

This is the correct path where your files are located.

---

## If Still Not Working

### Check the corrected logs:

```bash
tail -20 /home/logicalv/logs/error_log
```

### Verify files are in the correct location:

```bash
ls -la /home/logicalv/repositories/HostingTest/
# Should show:
# app.py
# requirements.txt
```

### Make sure dependencies are installed:

```bash
# Activate virtual environment (use command from Setup Python App)
source /home/logicalv/virtualenv/repositories/HostingTest/3.11/bin/activate

# Install dependencies
pip install -r requirements.txt

# Restart the app in cPanel
```

---

## Common Application Root Configurations

For your username `logicalv`, here are correct formats:

| If files are in: | Application Root should be: |
|------------------|----------------------------|
| `/home/logicalv/repositories/HostingTest/` | `repositories/HostingTest` |
| `/home/logicalv/public_html/myapp/` | `public_html/myapp` |
| `/home/logicalv/myflaskapp/` | `myflaskapp` |

**Rule:** Use path **relative to your home directory** without leading `/home/username/`

---

## Alternative: Use cPanel File Picker

Instead of typing the path:

1. In Setup Python App, look for a **folder icon** 📁 next to Application Root
2. Click it to browse directories
3. Navigate to and select: `repositories/HostingTest`
4. This will automatically use the correct format

---

## Expected Result

After fixing, you should see:

```
Hello, World!

Environment Variable:
CUSTOM_MESSAGE: No CUSTOM_MESSAGE environment variable set
```

At your application URL!

---

## Quick Reference

**Correct Configuration:**
- **Application Root:** `repositories/HostingTest`
- **Application Startup File:** `app.py`
- **Application Entry Point:** `app`

This should fix your issue! 🎉

