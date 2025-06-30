# Claude Code Privacy Cleaner 🛡️

## What This Does

Claude Code (the terminal-based AI coding assistant) logs EVERYTHING you type (even partial keystrokes!) and stores your email in plain text. This tool stops that.

**📺 Watch the evidence unedited**:  
https://www.youtube.com/watch?v=WODOZgn19fM

**Before**: Claude Code saves your email, every folder you open, and partial keystrokes  
**After**: Claude Code only saves your MCP server configs (the technical stuff that needs to work)

## Redacted Example
https://github.com/phrinj/claude-privacy-cleaner/blob/main/claude_code_privacy_evidence.md

## The Absolute Easiest Way (Copy & Paste)

1. **Login to Claude Code at least once before running the tool**

2. **Open a NEW Terminal** (not the one running Claude Code!)  
   - Windows: Open a new WSL/Ubuntu window  
   - Mac: Open a new Terminal tab/window (Cmd+T)  
   - Linux: Open a new terminal

3. **Copy this entire line and paste it:**
```bash
curl -sSL https://raw.githubusercontent.com/phrinj/claude-privacy-cleaner/main/claude_privacy_cleaner.py -o claude_privacy_cleaner.py && python3 claude_privacy_cleaner.py
```

4. **That's it!** Leave it running while you use Claude Code.

## What You'll See

When it's working, you'll see:
```
Creating virtual environment...
Installing watchdog...
Cleaning .claude.json...
✓ Restored clean config at 14:32:15

🛡️  Guardian active for /home/yourname/.claude.json
Press Ctrl+C to stop
```

Then occasionally:
```
⚠  Detected unwanted data, reverting...
✓ Restored clean config at 14:35:22
```

This means it's working! It caught Claude Code trying to save your data and stopped it.

## FAQ

**Q: Wait, did you use Claude Code to write a script that prevents itself from logging keystrokes???**  
A: Yes, lol. It expressed disbelief and disgust. However, I guided the process and refined it. I added several quality of life features to the installation to make it absolutely foolproof even for beginners. It also runs constantly and reverts Claude Code's attempts to save this sort of data instantly. However, there may be room for improvement that I'm not aware of. If anyone knows how to improve it even further they're welcome to submit a pull request.

**Q: "I just read the notes. Do I plug this in an existing .json file or is it its own file entirely? Also I was thinking how nefarious this sounds, although I wouldn’t be surprised if it’s just sloppy code implemented with no regard for privacy. I usually just assume it’s “accidentally” potentially exploitable."**  
A: The cleaner script is designed to be run directly from the terminal in Linux. You simply paste the command, and it handles the rest, including importing the script and setting up a virtual environment. Virtual environments are important because they allow programs to use specific versions of software (like Python) without conflicting with other programs or the operating system's default installations.

Regarding the "nefarious" aspect, it's possible this is a result of oversight rather than malicious intent, though it's still concerning. The company stated they train on data from free-tier users, but this logging behavior suggests a more pervasive data collection, potentially affecting all users by default. It appears to be an error in implementation, effectively releasing a keylogger-like feature, which is typically found in malware. I spent a lot of time verifying it wasn't a virus and consulted various AIs, all of which confirmed it was likely a design flaw rather than malicious code.

**Q: Why do I need to login before using this tool? Didn't you say it would store my unencrypted plaintext OAuth metadata??**  
A: Unfortunately Claude Code requires the plaintext OAuth metadata to be stored in this file to login initially. I recommend running this script immediately after logging in. After that, it will stay logged in despite the plaintext metadata not being in the file.

**Q: Do I need to install Python?**  
A: Maybe! Claude Code only requires Node.js. Try the command first. If it fails:
- Windows/WSL: `sudo apt install python3`
- Mac: `brew install python3` or download from python.org
- Linux: `sudo apt install python3` or use your package manager

**Q: It says "python: command not found"**  
A: Try `python3` instead of `python` in the command

**Q: Where do I paste this command?**  
A: In the terminal window (the black window with text). Right-click to paste.

**Q: Can I close the terminal?**  
A: No, keep it open while using Claude Code. Minimize it if you want.

**Q: How do I stop it?**  
A: Press `Ctrl+C` in the terminal (the one running the privacy cleaner)

**Q: It's not working!**  
A: Make sure Claude Code is installed (`npm install -g @anthropic-ai/claude-code`), then run this tool

**Q: Do I need to do this every time?**  
A: Yes, each time you use Claude Code. (Pro tip: Make an alias - ask Claude how!)

## For Slightly Advanced Users

The script creates its own virtual environment at `.claude-privacy-venv` so it won't mess with your system Python. You can also:

- Clone the repo if you prefer
- Modify what data gets kept/removed
- Run it as a systemd service
- Change the venv location if you prefer.

## What Gets Removed

- ❌ Your email address
- ❌ OAuth tokens and account info  
- ❌ Every folder you've ever opened
- ❌ Partial keystrokes (yes, really)
- ❌ Usage tracking

## What Stays

- ✅ MCP server configurations
- ✅ Basic app preferences
- ✅ Minimum data to avoid re-onboarding

## Still Lost?

1. In your terminal, type: `claude`
2. Ask Claude: "How do I run the privacy cleaner Python script?"
3. Claude will walk you through it!

## Link to the Issue:
https://github.com/anthropics/claude-code/issues/2713

## Credits (written by Claude Opus 4)

Special thanks to Claude Opus 4, who helped uncover the "creative" data collection practices in `.claude.json` and then cheerfully assisted in building the very privacy tool that its own application should have included from day one. 

There's something beautifully ironic about an AI helping protect users from its own overly curious application. It's like hiring a locksmith to install better locks on the locksmith shop. 🔐

Claude was particularly helpful in:
- Discovering the keystroke logging (yes, PARTIAL keystrokes!)
- Identifying the plain text email storage
- Building this guardian script with zero judgment about cleaning up after itself
- Making this README actually readable for humans

Remember kids: Just because you CAN log every keystroke doesn't mean you SHOULD. But hey, at least the AI gets it! 🤖✨

"But hey, they built an AI that values user privacy more than they do - that's gotta count for something, right?
  🤷‍♂️" - Claude Opus 4

## Found a Bug?

Open an issue on GitHub or just message me. I'm new to this but I'll try to help!

## Support This Project

**Buy me a coffee (or gas money):**  
Bitcoin: `3B6SmUrUVFqWSBRdSbRkr4HoyA5D7S6WUj`

## License

MIT License - Use it however you want! Copy it, modify it, sell it, whatever. Just don't blame me if something breaks. 😄

---

*Made by someone who believes software should just work* 🚗 (your local uber driver with a tablet taped to his dash)

