# Th AWS Cloud Resume Challenge requires one keeps a count of how many times
# one's resume has been viewed
# This terraform file creates a dynamo db table to hold the view count

provider "aws" {
  region  = "us-east-2"
  profile = "initial-aws-account"
}

resource "aws_dynamodb_table" "dt" {
  name         = "cloud-resume-challenge"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "totalCount"

  attribute {
    name = "totalCount"
    type = "N"
  }
  tags = {
    key   = "Project"
    value = "cloud-resume-challenge"
  }
}
