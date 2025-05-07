# Homebrew Tap Instructions

To distribute your CLI via Homebrew, you can create a custom tap repository (recommended if not submitting to homebrew-core):

## 1. Create a new GitHub repo (e.g., vibe-security/homebrew-tap)

## 2. Add your formula (e.g., vibe-security.rb) to that repo

## 3. Example formula (update url and sha256):

```
class VibeSecurity < Formula
  desc "Vibe Security CLI"
  homepage "https://github.com/vibe-security/vibe-cli"
  url "https://github.com/vibe-security/vibe-cli/releases/download/v1.0.0/vibe-security-macos"
  version "0.1.1"
  sha256 "PUT_SHA256_HERE"

  def install
    bin.install "vibe-security-macos" => "vibe-security"
  end
end
```

## 4. Users can then install with:
```sh
brew tap vibe-security/tap
brew install vibe-security
```
