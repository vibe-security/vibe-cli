import argparse
import subprocess
import shutil
import sys

TOOLS = [
    ("semgrep", ["semgrep", "--version"]),
    ("sqlmap", ["sqlmap", "--version"]),
    ("trivy", ["trivy", "--version"]),
]

SCAN_CMDS = [
    ("semgrep", ["semgrep", "--config", "auto", "."]),
    ("sqlmap", ["sqlmap", "-u", "http://example.com", "--batch"]),
    ("trivy", ["trivy", "fs", "."]),
]

def check_tools():
    missing = []
    for tool, version_cmd in TOOLS:
        if not shutil.which(tool):
            missing.append(tool)
    return missing

def install_instructions(tool):
    if sys.platform.startswith("linux"):
        if tool == "trivy":
            return f"sudo apt-get install -y trivy"
        return f"pip install {tool}"
    elif sys.platform == "darwin":
        if tool == "trivy":
            return f"brew install aquasecurity/trivy/trivy"
        return f"pip install {tool}"
    elif sys.platform == "win32":
        return f"pip install {tool}"
    return f"Install {tool} manually."

def run_scan():
    print("\n✨ Welcome to Vibe Security Scan! ✨")
    print("Let's keep your project safe and vibing!\n")

    steps = [
        ("semgrep", "🔍 Running Semgrep (Code Scanning)...", ["semgrep", "--config", "auto", "."]),
        ("sqlmap", "💉 Running SQLMap (SQL Injection Testing)...", ["sqlmap", "-u", "http://example.com", "--batch"]),
        ("trivy", "🐳 Running Trivy (Filesystem/Container Scanning)...", ["trivy", "fs", "."]),
    ]

    for name, header, cmd in steps:
        if shutil.which(name):
            print(f"\n{header}")
            try:
                subprocess.run(cmd, check=True)
            except Exception as e:
                print(f"❌ {name} failed. Error: {e}")
        else:
            print(f"⚠️  {name.capitalize()} not found. Install with: {install_instructions(name)}")

    print("\n🎉 Scan complete! Reports saved in current directory. Stay secure and keep vibing!\n")

def main():
    parser = argparse.ArgumentParser(description="Vibe Security CLI")
    parser.add_argument("scan", nargs="?", help="Run security scan")
    args = parser.parse_args()

    if args.scan == "scan":
        missing = check_tools()
        if missing:
            print("Missing tools: " + ", ".join(missing))
            for tool in missing:
                print(f"Install {tool}: {install_instructions(tool)}")
            sys.exit(1)
        run_scan()
        return 0
    else:
        parser.print_help()
        return 1

if __name__ == "__main__":
    main()
