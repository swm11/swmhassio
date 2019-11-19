# Notes on Hassio configuration

## ssh access

ssh daemon enabled via Hassio interface and a pubic key registered via the ssh config on the web interface.  To access, ssh configuration is required to provide the right key.  Access as user 'root' and use IPv4, vis:

```
ssh -4 -v root@hassio.local
```


