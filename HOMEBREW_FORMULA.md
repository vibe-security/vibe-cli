# Homebrew Formula Instructions

To distribute `vibe-security` via Homebrew, after you have a binary release (macOS), create a formula like this:

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

- Replace `url` and `sha256` with the actual release asset and checksum.
- Submit to your own tap or to homebrew-core.
