s3-sync
-------

This action syncs local directory with s3-compatible remote.

Usage
-------

```yaml
steps:
- uses: recsysio/actions/s3-sync@master
  with:
    local_dir: dist
    s3_dir: tmp
  env:
    ACL: public-read
    BUCKET: ${{ secrets.S3_BUCKET }}
    ENDPOINT: ${{ secrets.S3_ENDPOINT }}
    ACCESS_KEY: ${{ secrets.S3_ACCESS_KEY }}
    ACCESS_SECRET: ${{ secrets.S3_ACCESS_SECRET }}
```
