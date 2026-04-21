output "ec2_public_ip" {
  description = "Public IP of the AI EC2 instance"
  value       = aws_instance.ai_server.public_ip
}

output "ec2_public_dns" {
  description = "Public DNS of the AI EC2 instance"
  value       = aws_instance.ai_server.public_dns
}

output "ssh_command" {
  description = "SSH command to connect to EC2"
  value       = "ssh -i your-key.pem ubuntu@${aws_instance.ai_server.public_ip}"
}

output "app_url" {
  description = "FastAPI endpoint"
  value       = "http://${aws_instance.ai_server.public_ip}:5000"
}

output "swagger_url" {
  description = "Swagger UI for API testing"
  value       = "http://${aws_instance.ai_server.public_ip}:5000/docs"
}

output "s3_bucket_name" {
  description = "S3 bucket for tenant documents"
  value       = aws_s3_bucket.tenant_docs.bucket
}