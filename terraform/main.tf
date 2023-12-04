terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.28.0"
    }
  }
}

# Configure the AWS provider
provider "aws" {
  region     = "us-east-1"
}

variable "REPOSITORY_URI" {
  type = string
}

resource "aws_lightsail_container_service" "notebook_application" {
  name = "notebook_app"
  power = "nano"
  scale = 1

  private_registry_access {
    ecr_image_puller_role {
      is_active = true
    }
  }


  tags = {
    version = "1.0.0"
  }
}

resource "aws_lightsail_container_service_deployment_version" "notebook_app_deployment" {
  container {
    container_name = "notebook_application"

    image = "${var.REPOSITORY_URI}:latest"
    
  }

  public_endpoint {
    container_name = "notebook_application"

    health_check {
      healthy_threshold   = 2
      unhealthy_threshold = 2
      timeout_seconds     = 2
      interval_seconds    = 5
      path                = "/"
      success_codes       = "200-499"
    }
  }

  service_name = aws_lightsail_container_service.notebook_application.name
}
