#####################################
############ Modules ################
#####################################

module "tf-aws-network" {
  source          = "git@github.com:owen-eternal/tf-aws-network-mod.git"
  db_server_port  = null
  database        = var.database
  environment     = terraform.workspace
  ipaddr          = var.ipaddr
  project_name    = "Tekken7C"
  subnet_cdir     = var.network[terraform.workspace].subnets
  vpc_cdir        = var.network[terraform.workspace].vid
  web_server_port = null
}