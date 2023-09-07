####### VPC-Tier Module Variables ########
variable "database" {}
variable "ipaddr" {}

variable "network" {
  description = "Object with a list of CIDR block ranges for VPC networks."
  type        = map(any)
  default = {
    "staging" = {
      "vid" = "10.0.0.0/16"
      "subnets" = {
        "web" = ["10.0.0.0/18", "10.0.64.0/18"]
        "db"  = []
      }
    }
    "production" = {
      "vid" = "172.0.0.0/16"
      "subnets" = {
        "web" = ["172.0.0.0/18", "172.0.64.0/18"]
        "db"  = []
      }
    }
  }
}