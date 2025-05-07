# .deb Packaging Instructions

To distribute a .deb package for `vibe-security`:

## 1. Build the binary (see GitHub Actions workflow)

## 2. Use `fpm` to create a .deb package

Install fpm:
```sh
sudo gem install --no-document fpm
```

Package the binary:
```sh
fpm -s dir -t deb -n vibe-security -v 0.1.1 --prefix /usr/local/bin dist/vibe-security-linux
```

This will create a `vibe-security_0.1.1_amd64.deb` file.

## 3. Distribute
- Upload the .deb to GitHub Releases or your own APT repo.
- Users can install with:
  ```sh
  sudo dpkg -i vibe-security_0.1.1_amd64.deb
  ```
