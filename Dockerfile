# Use the official AWS Lambda Python base image
FROM public.ecr.aws/lambda/python:3.9

# Set working directory
WORKDIR /app

# Copy application files
COPY my_app/ /app/

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Command to run the application
CMD ["app.lambda_handler.lambda_handler"]
