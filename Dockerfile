FROM python:3.13-slim

WORKDIR /app

RUN pip install uv

# Copy only dependency files first
COPY pyproject.toml uv.lock ./

# Install deps into system Python (NO venv)
RUN uv pip install --system .

# Copy the rest of the code
COPY . .

CMD ["bash"]
