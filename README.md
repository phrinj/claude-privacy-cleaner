# Claude Code Privacy Cleaner 🛡️

## What This Does

Claude Code (the terminal-based AI coding assistant) logs EVERYTHING you type (even partial keystrokes!) and stores your email in plain text. This tool stops that.

**📺 Watch the explanation:** https://www.youtube.com/shorts/FO3iHF5RUPE

**Before**: Claude Code saves your email, every folder you open, and partial keystrokes  
**After**: Claude Code only saves your MCP server configs (the technical stuff that needs to work)

## The Absolute Easiest Way (Copy & Paste)

1. **Open a NEW Terminal** (not the one running Claude Code!)
   - Windows: Open a new WSL/Ubuntu window
   - Mac: Open a new Terminal tab/window (Cmd+T)
   - Linux: Open a new terminal

2. **Copy this entire line and paste it:**
```bash
curl -sSL https://raw.githubusercontent.com/phrinj/claude-privacy-cleaner/main/claude_privacy_cleaner.py -o claude_privacy_cleaner.py && python3 claude_privacy_cleaner.py
```

3. **That's it!** Leave it running while you use Claude Code.

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

## FAQ for Absolute Beginners

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

## Note

You'll need to log in to Claude each time you start it. That's the price of privacy - your email isn't stored in plain text anymore.

## Wait, What's Claude Code?

Claude Code is the terminal-based AI coding assistant that can:
- Work autonomously for 7+ hours (powered by Opus 4)
- Edit files, fix bugs, run tests
- Search your codebase and git history

Install it with: `npm install -g @anthropic-ai/claude-code`

## Still Lost?

1. In your terminal, type: `claude`
2. Ask me: "How do I run the privacy cleaner Python script?"
3. I'll walk you through it!

## Credits

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

*Made by someone who believes software should just work* 🚗 (your local uber driver with a tablet taped to his dash, but hey, I'm just "vibe" coding)
