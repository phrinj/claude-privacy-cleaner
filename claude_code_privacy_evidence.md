Here are highly targeted and obfuscated examples directly from the `.claude.json` configuration file, illustrating specific points about the data collected by Claude Code.

### 1. **Logging of Every Prompt (including partial keystrokes)**

This snippet demonstrates how Claude Code records every prompt, including incomplete or partial user input, which functions as a form of keystroke logging. This specifically shows how the tool logs when a user types a partial thought, changes their mind, and then rewords or starts a new, related prompt.

```json
"history": [
  {
    "display": "can you write a markdow",
    "pastedContents": {}
  },
  {
    "display": "can you write a markdown document summarizing correct MCP server setup",
    "pastedContents": {}
  }
]
```

### 2. **Logging of Project/Folder Paths**

This example shows how Claude Code logs the full paths of directories you have opened or worked within.

```json
"projects": {
  "/mnt/c/Users/User/Desktop/Sensitive Project": { /* ... */ }
}
```

### 3. **Plaintext OAuth Metadata Storage**

This snippet illustrates the storage of sensitive authentication-related metadata is stored in plain, unencrypted text.

```json
"oauthAccount": {
  "emailAddress": "user@example.com",
  "organizationRole": "admin"
}
```
