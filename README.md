# Vibe Security CLI

A fast, user-friendly command-line tool to run comprehensive security scans (Semgrep, SQLMap, Trivy) on your codebase. Perfect for local development and CI/CD pipelines.

## Features

📚 **Full documentation:** [Vibe Security Suite Docs – CLI](https://github.com/vibe-security/vibe-security-suite/blob/main/docs-site/docs/cli.md)

- One-command install
- Code, dependency, and container scanning
- Friendly, emoji-rich output

## Installation (All Platforms)

You can install Vibe Security CLI on any platform using the prebuilt binaries from the [GitHub Releases page](https://github.com/vibe-security/vibe-cli/releases).

### Linux/macOS (tar.gz)
```sh
# Download the latest release (replace version as needed)
wget https://github.com/vibe-security/vibe-cli/releases/download/v1.0.0/vibe-security-1.0.0-linux.tar.gz
# or for macOS:
wget https://github.com/vibe-security/vibe-cli/releases/download/v1.0.0/vibe-security-1.0.0-macos.tar.gz

# Extract the binary
# For Linux:
tar -xzf vibe-security-1.0.0-linux.tar.gz
# For macOS:
tar -xzf vibe-security-1.0.0-macos.tar.gz

# Move to a directory in your PATH
sudo mv vibe-security /usr/local/bin/

# Test the CLI
vibe-security --help
```

### Windows (zip)
1. Download the latest `zip` from the [releases page](https://github.com/vibe-security/vibe-cli/releases).
2. Extract it using Windows Explorer or PowerShell:
   ```powershell
   Expand-Archive -Path .\vibe-security-1.0.0-windows.zip -DestinationPath .
   ```
3. Optionally add the extracted folder to your PATH, or run the `.exe` directly:
   ```powershell
   .\vibe-security.exe --help
   ```

---

For advanced users, you may also use Homebrew, Scoop, or a .deb package (see docs in this repo), but the above approach works on all platforms with no extra tools required.

## Usage
```sh
vibe-security scan
```

## License
MIT
