output "load_balancer_ip" {
  value = aws_lb.development.dns_name
}