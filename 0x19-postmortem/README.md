# Postmortem Report
## Oops! The 404 Page Not Found Incident

![N|Solid](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2N1dmVvNzhyc2J4bTZ0amNhNmNremV1MG5kNzB1N25kYzUyc3NlayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/H54feNXf6i4eAQubud/giphy.gif)

## Issue Summary
### Duration of Outage:
    Start Time: August 17, 2024, 14:00 UTC
    End Time: August 17, 2024, 15:30 UTC

## Impact:
For about 1.5 hours, most users (around 70%) who tried to visit our website, www.foobar.com, got a "404 Page Not Found" error. This meant that they couldn’t access the website at all. Additionally, about 10% of users found the website to be super slow during this time.

## Root Cause:
The issue was caused by a small mistake in the Nginx web server settings. During a routine update, the server was accidentally configured to look in the wrong place for the website files, which resulted in the 404 errors.

## Timeline
- **14:00 GMT** - Issue detected: Our monitoring system showed a big jump in 404 errors, so an engineer started investigating.
- **14:05 GMT** - Initial checks: We suspected the problem might be due to some new code that was deployed, so we started looking into that.
- **14:15 GMT** - Misleading path: We rolled back the new code to see if it would fix the problem, but the errors continued, which meant the code wasn’t the issue.
- **14:25 GMT** - Escalation: The problem was then handed over to the infrastructure team, who are in charge of the servers.
- **14:40 GMT** - Root cause found: The team discovered that the server’s configuration had been changed to point to the wrong directory.
- **14:50 GMT** - Fix applied: The correct directory path was set in the server’s settings, and everything was reloaded.
- **15:00 GMT** - Back to normal: The 404 errors disappeared, and the website started working as usual.
- **14:30 GMT** - Incident closed: We made sure everything was stable and then ended the incident.

## Root Cause and Resolution

### Root Cause:
The problem started because of a small mistake in the server’s configuration. During a regular update, the Nginx server was accidentally told to look for the website files in the wrong place. This caused the server to return a "404 Page Not Found" error to users trying to visit the site.

### Resolution:
Once we figured out that the server configuration was the issue, we changed it back to the correct settings and reloaded the server. This immediately fixed the problem, and the website became accessible again.

## Corrective and Preventative Measures

### What can be improved:
Double-check the server settings before making any changes in the future.
Improve our monitoring system to quickly catch configuration errors like this.
Provide more training on how to safely update server configurations.

### Tasks to prevent this in the future:
Update the Nginx server to make sure it checks for mistakes in configuration.
Add alerts in our monitoring system that specifically look for configuration issues.
Test server settings before they go live to catch mistakes early.
Schedule a training session to go over best practices for server updates.
