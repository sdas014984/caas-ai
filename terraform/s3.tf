resource "aws_s3_bucket" "tenant_docs" {
  bucket = "ccaas-multitenant-docs"
}

resource "aws_s3_bucket_public_access_block" "block" {
  bucket = aws_s3_bucket.tenant_docs.id

  block_public_acls   = true
  block_public_policy = true
}
