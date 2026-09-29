#step 1 : use official lightweight python operating system template 
FROM python:3.11-alpine

# Step 2: Establish a secure runtime directory inside the container
WORKDIR /app

# Step 3: Copy your local application script into that internal workspace
COPY app.py .

# Step 4: The master execution string triggered when the container starts
CMD ["python", "app.py"]
