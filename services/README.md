# services

Three services that talk through the `orders` SNS topic (`infra/queues.tf`):

- `checkout` (Python) saves orders and publishes `order.placed`
- `fulfillment` (Python) reads `order.placed` and creates a shipment in the warehouse system
- `notifications` (TypeScript) reads `order.placed` and emails the receipt

Each service is deployed on its own pipeline.
