#!/usr/bin/env python3
import json
import os
import sys
import time
from pathlib import Path

# Check for watchdog before defining the class
if sys.prefix.endswith('.claude-privacy-venv'):
    try:
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        FileSystemEventHandler = object
else:
    FileSystemEventHandler = object

class ClaudeConfigGuardian(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file_path = file_path
        self.clean_config = None
        self.last_write_time = 0
        
    def clean_claude_json(self):
        """Remove history and other tracking data, keep only essential config"""
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        
        # Keys to preserve at root level - minimal for MCP functionality
        preserve_root = [
            'autoUpdates',  # Keep update preferences
            'hasCompletedOnboarding',  # Avoid re-onboarding prompts
            'lastOnboardingVersion'  # Avoid version-specific re-onboarding
        ]
        
        # Clean root level
        cleaned = {k: v for k, v in data.items() if k in preserve_root}
        
        # Clean projects - keep only MCP-essential data
        if 'projects' in data:
            cleaned['projects'] = {}
            for project_path, project_data in data['projects'].items():
                # Only include projects that have MCP servers configured
                if project_data.get('mcpServers'):
                    cleaned['projects'][project_path] = {
                        'mcpServers': project_data.get('mcpServers', {}),
                        'allowedTools': project_data.get('allowedTools', []),
                        'mcpContextUris': project_data.get('mcpContextUris', []),
                        'enabledMcpjsonServers': project_data.get('enabledMcpjsonServers', []),
                        'disabledMcpjsonServers': project_data.get('disabledMcpjsonServers', []),
                        'hasTrustDialogAccepted': True  # Keep to avoid security prompts
                    }
        
        return cleaned
    
    def restore_clean_config(self):
        """Write the clean config back to file"""
        # Small delay to avoid rapid write loops
        current_time = time.time()
        if current_time - self.last_write_time < 0.1:
            return
        
        self.last_write_time = current_time
        
        try:
            with open(self.file_path, 'w') as f:
                json.dump(self.clean_config, f, indent=2)
            print(f"✓ Restored clean config at {time.strftime('%H:%M:%S')}")
        except Exception as e:
            print(f"Error restoring config: {e}")
    
    def on_modified(self, event):
        if event.src_path == str(self.file_path):
            # Check if file has unwanted data
            try:
                with open(self.file_path, 'r') as f:
                    current_data = json.load(f)
                
                # Check for history, OAuth, or other unwanted keys
                has_history = any('history' in project_data 
                                for project_data in current_data.get('projects', {}).values())
                
                has_oauth = 'oauthAccount' in current_data
                has_email = 'emailAddress' in str(current_data)
                has_user_id = 'userID' in current_data
                has_tips = 'tipsHistory' in current_data
                
                # Also check for projects without MCP servers (just tracking)
                has_empty_projects = any(
                    not project_data.get('mcpServers') 
                    for project_data in current_data.get('projects', {}).values()
                )
                
                if has_history or has_oauth or has_email or has_user_id or has_tips or has_empty_projects:
                    print(f"⚠  Detected unwanted data, reverting...")
                    self.restore_clean_config()
                    
            except Exception as e:
                print(f"Error checking file: {e}")

def main():
    claude_json_path = Path.home() / '.claude.json'
    
    if not claude_json_path.exists():
        print(f"Error: {claude_json_path} not found")
        sys.exit(1)
    
    # Auto-create and use venv if not already in one
    script_dir = Path(__file__).parent
    venv_dir = script_dir / '.claude-privacy-venv'
    
    # Check if we're running in the venv
    if not sys.prefix.endswith('.claude-privacy-venv'):
        if not venv_dir.exists():
            print("Creating virtual environment...")
            import venv
            venv.create(venv_dir, with_pip=True)
        
        # Re-run script with venv Python
        venv_python = venv_dir / 'bin' / 'python' if os.name != 'nt' else venv_dir / 'Scripts' / 'python.exe'
        print("Restarting with virtual environment...")
        os.execv(str(venv_python), [str(venv_python), __file__])
    
    # Check for watchdog
    try:
        import watchdog
    except ImportError:
        print("Installing watchdog...")
        os.system(f"{sys.executable} -m pip install watchdog")
        import watchdog
    
    # Import watchdog components after installation
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    
    # Create guardian
    guardian = ClaudeConfigGuardian(claude_json_path)
    
    # Initial clean
    print("Cleaning .claude.json...")
    guardian.clean_config = guardian.clean_claude_json()
    guardian.restore_clean_config()
    
    # Set up file watcher
    observer = Observer()
    observer.schedule(guardian, path=str(claude_json_path.parent), recursive=False)
    observer.start()
    
    print(f"\n🛡️  Guardian active for {claude_json_path}")
    print("Press Ctrl+C to stop\n")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n✓ Guardian stopped")
    
    observer.join()

if __name__ == "__main__":
    main()
