# Nexus AI Agents

Nexus AI Agents are a central hub for answering all business finance data related to banking, sales, finance and company's finance related queries.

## Project Structure

```
.
├── Dockerfile
├── requirements.txt
├── server.py
├── NexusAI-BankAgent/
│   ├── agent.py
│   ├── bank_custom_functions.py
│   ├── custom_agents.py
│   ├── __init__.py
│   └── thirdpartytool.py
├── NexusAI-CompanyinfoAgent/
│   ├── agent.py
│   ├── company_custom_function.py
│   ├── custom_agents.py
│   ├── __init__.py
│   └── thirdpartytool.py
├── NexusAI-FinanceAgent/
│   ├── agent.py
│   ├── custom_agents.py
│   ├── finance_custom_function.py
│   ├── __init__.py
│   └── thirdpartytool.py
├── NexusAI-SalesAgent/
│   ├── agent.py
│   ├── custom_agents.py
│   ├── __init__.py
│   ├── sales_custom_functions.py
│   └── thirdpartytool.py
└── Parallel-NexusAIAgent/
    ├── agent.py
    ├── bank_custom_function.py
    ├── company_custom_function.py
    ├── custom_agents.py
    ├── finance_custom_function.py
    ├── __init__.py
    ├── sales_custom_function.py
    └── thirdpartytool.py
```

## Execution Steps

To run this project, you need to have Docker installed.

1.  **Build the Docker image:**
    ```bash
    docker build -t nexus-ai-agents .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 8080:8080 -e API_NINJAS_KEY="YOUR_API_KEY" nexus-ai-agents
    ```
    *Replace `YOUR_API_KEY` with your actual API key from API-Ninjas.*

## Agent Descriptions

### NexusAI-BankAgent
This agent provides banking related information. It can:
- Fetch bank information from a Bank Identification Number (BIN).
- Find SWIFT codes for banks.
- Get central bank interest rates for 22 countries.
- Get current and historical LIBOR rates.

### NexusAI-CompanyinfoAgent
This agent provides information about companies. It can:
- Get real-time market capitalization data for companies.
- Search millions of SEC filings.
- Get comprehensive earnings report data for public US companies.
- Get information about companies in the S&P 500 index.

### NexusAI-FinanceAgent
This agent provides financial information. It can:
- Calculate mortgage and other home financing payment information.
- Get information about over 100 stock markets around the world.
- Get real-time and historical stock market prices.
- Get detailed information about mutual funds.
- Get exchange rates for global currencies.

### NexusAI-SalesAgent
This agent provides sales related information. It can:
- Get real-time commodity prices.
- Get current and historical Value Added Tax (VAT) rates for all countries in the European Union.
- Calculate sales tax for any purchase amount in the United States.

### Parallel-NexusAIAgent
This agent acts as a supervisor, running the other four agents in parallel and then synthesizing their results into a single, clear response for the user.
