# rh_coding_class
Content for the Redemption Hill Coding Class

1. create github account
2. create ssh key: `ssh-keygen -t ed25519 -C "your email"`
3. start ssh-agen: `eval "$(ssh-agent -s)"`
4. add content to `~/.ssh/config`
```
Host github.com
  AddKeysToAgent yes
  IdentityFile ~/.ssh/id_ed25519
```
5. add to keychain: `ssh-add --apple-use-keychain ~/.ssh/id_ed25519`
6. add public key to github.com `cat ~/.ssh/id_ed25519.pub| pbcopy`
7. add key to ssh-agent `ssh-add ~/.ssh/id_ed25519`
8. optional, set origin `git remote set-origin git@github.com:...`

### Thanks for visiting!
