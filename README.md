# Vibe Security CLI

A fast, user-friendly command-line tool to run comprehensive security scans (Semgrep, SQLMap, Trivy) on your codebase. Perfect for local development and CI/CD pipelines.

## Features
- One-command install
- Code, dependency, and container scanning
- Friendly, emoji-rich output

## Native Installation

### Linux (Debian/Ubuntu)
Download the latest `.deb` from [Releases](https://github.com/vibe-security/vibe-cli/releases) and install:
```sh
sudo dpkg -i vibe-security_VERSION_amd64.deb
```

### macOS (Homebrew)
```sh
brew tap vibe-security/tap
brew install vibe-security
```

### Windows
Download the `.exe` from [Releases](https://github.com/vibe-security/vibe-cli/releases) and run it, or use [Scoop](https://scoop.sh/):
```sh
scoop bucket add vibe-security https://github.com/vibe-security/scoop-bucket.git
scoop install vibe-security
```

### Universal (Python/pipx)
```sh
pipx install vibe-security
```

## Usage
```sh
vibe-security scan
```

## License
MIT
