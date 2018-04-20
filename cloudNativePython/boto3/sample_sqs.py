# Amazon Simple Queue Service
# Amazon SQS moves data between distributed application components.
# SQS allows you to queue and then process messages.

import boto3
from logall import config_logging


def main():

    # Configuring and getting a logger object
    logger = config_logging()

    # Get the service resource
    sqs = boto3.resource('sqs')

    # Create the queue. This return an SQS.Queue instance
    queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

    # You can now access identifiers and attributes
    logger.info(queue.url)
    logger.info('Atribute DelaySeconds: %s',
                queue.attributes.get('DelaySeconds'))

    # Using an Existing Queue
    same_queue = sqs.get_queue_by_name(QueueName='test')

    if queue == same_queue:
        logger.info('Same queue!')

    # Print out each queue name, which is part of its ARN
    for queue in sqs.queues.all():
        logger.info(queue.url)

    # Create a new messages
    simple_response = queue.send_message(MessageBody='world')

    # You can also create messages with custom attributes
    attr_response = queue.send_message(MessageBody='boto3', MessageAttributes={
        'Author': {
            'StringValue': 'Daniel',
            'DataType': 'String'
        }
    })

    responses = [simple_response, attr_response]

    for response in responses:
        # The response is not a resource, but gives you a message ID and MD5
        # logger.info(response.get('MessageID'))
        logger.info(response.get('MD5OfMessageBody'))

    # Messages can also be sent in batches.
    batch_response = queue.send_messages(Entries=[
        {
            'Id': '100',
            'MessageBody': 'Hello, world!'
        },
        {
            'Id': '200',
            'MessageBody': 'Emanuel D R Sena',
            'MessageAttributes': {
                'Author': {
                    'StringValue': 'Emanuel',
                    'DataType': 'String'
                }
            }
        }
    ])

    logger.info(batch_response.get('Failed'))

    # Process messages by printing out body and optional author name
    for message in queue.receive_messages(MessageAttributeNames=['Author']):
        # Get the custom author message attribute if it was set
        author_text = ''
        if message.message_attributes is not None:
            author_name = message.mesesage_attributes.get(
                'Author').get('StringValue')
            if author_name:
                author_text = ' ({})'.format(author_name)

            # Print out the body and author (if set)
            logger.info('Hello, %s!%s', message.body, author_text)

            # Let queue know that the message is processed
            message.delete()


if __name__ == '__main__':
    main()
