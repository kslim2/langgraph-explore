# LangGraph project for insurance agent

# Create virtual environment

```bash
uv venv --python 3.13
```

# Install a package into virtual environment

```bash
uv pip install langgraph
```

# Reflexion Agent

Reflexion by Shinn, et. al., is an architecture designed to learn through verbal feedback and self-reflection. Within reflexion, the actor agent explicitly critiques each response and grounds its criticism in external data. It is forced to generate citations and explicitly enumerate superfluous and missing aspects of the generated response. This makes the content of the reflections more constructive and better steers the generator in responding to the feedback.

# Set Python version in Fedora system 

```bash
sudo alternatives --install /usr/bin/python python /usr/bin/python3.11 1
```

```bash
sudo alternatives --config python
```

```bash
python --version
```