resource "aws_sns_topic" "orders" {
  name = "orders"
}

resource "aws_sqs_queue" "fulfillment" {
  name           = "fulfillment"
  redrive_policy = jsonencode({ deadLetterTargetArn = aws_sqs_queue.fulfillment_dlq.arn, maxReceiveCount = 5 })
}

resource "aws_sqs_queue" "fulfillment_dlq" {
  name = "fulfillment-dlq"
}

resource "aws_sqs_queue" "notifications" {
  name           = "notifications"
  redrive_policy = jsonencode({ deadLetterTargetArn = aws_sqs_queue.notifications_dlq.arn, maxReceiveCount = 5 })
}

resource "aws_sqs_queue" "notifications_dlq" {
  name = "notifications-dlq"
}

resource "aws_sns_topic_subscription" "fulfillment_orders" {
  topic_arn            = aws_sns_topic.orders.arn
  protocol             = "sqs"
  endpoint             = aws_sqs_queue.fulfillment.arn
  raw_message_delivery = true
}

resource "aws_sns_topic_subscription" "notifications_orders" {
  topic_arn            = aws_sns_topic.orders.arn
  protocol             = "sqs"
  endpoint             = aws_sqs_queue.notifications.arn
  raw_message_delivery = true
}
