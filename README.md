AirLabs MCP Server
==================

A specialized Model Context Protocol (MCP) server that connects AI assistants (like Poke, Claude, etc.) to real-time global flight data via [AirLabs](https://airlabs.co/).

Features
--------

### ✈️ Flight Data Tools

*   **airlabs\_get\_flight\_status**: Real-time tracking of specific flights (e.g., "KL601").
    
*   **airlabs\_get\_schedules**: Find flight schedules between airports (e.g., "AMS" to "SFO").
    
*   **airlabs\_get\_airport\_delays**: Check for delays at specific airports.
    
*   **airlabs\_search\_airports**: Look up IATA codes by city name (e.g., "London" -> LHR, LGW).
    
*   **airlabs\_get\_nearby\_airports**: Find airports near a specific location.
    

Setup & Running Locally
-----------------------

1.  git clone \[https://github.com/gsa87/airlabs-mcp-server.git\](https://github.com/gsa87/airlabs-mcp-server.git)cd airlabs-mcp-server
    
2.  pip install -r requirements.txt
    
3.  Create a .env file or export your API key:export AIRLABS\_API\_KEY="your\_airlabs\_key"
    
4.  python src/server.py
    

Deployment on Render
--------------------

1.  Fork this repository.
    
2.  Create a new **Web Service** on Render.
    
3.  Connect your GitHub repo.
    
4.  Add the following **Environment Variable** in the Render dashboard:
    
    *   AIRLABS\_API\_KEY
        
5.  Deploy!
    

API Key
-------

Get a free API key from [AirLabs.co](https://airlabs.co/).

License
-------

MIT
