provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "ai_server" {
  ami           = "ami-0f5ee92e2d63afc18"
  instance_type = "t3.xlarge"
  key_name      = "your-key"

  security_groups = [aws_security_group.ai_sg.name]

  user_data = <<-EOF
              #!/bin/bash
              apt update -y
              apt install -y docker.io git
              systemctl start docker
              EOF
}

resource "aws_security_group" "ai_sg" {
  name = "ai-sg"

  ingress {
    from_port = 22
    to_port   = 22
    protocol  = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 5000
    to_port   = 5000
    protocol  = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 3000
    to_port   = 3000
    protocol  = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
