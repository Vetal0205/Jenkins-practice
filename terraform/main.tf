terraform {
  required_version = ">=0.13.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS provider
provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "notebook_app" {
  name        = "notebook_app"
  description = "security group"
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

 ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags= {
    Name = "notebook_app"
  }
}

resource "aws_instance" "app_instance" {
  ami           = "ami-0fc5d935ebf8bc3bc"
  instance_type = "t2.micro"
  security_groups= ["notebook_app"]
  tags = {
    Name = "app_instance"
  }
}

output "instance_public_ip" {
  value     = aws_instance.app_instance.public_ip
  sensitive = true
}
