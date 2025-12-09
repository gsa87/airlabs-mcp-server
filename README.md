# AirLabs MCP Server

A specialized Model Context Protocol (MCP) server that connects AI assistants (like Poke, Claude, etc.) to real-time global flight data via [AirLabs](https://airlabs.co/).

## Features

### ✈️ Flight Data Tools

* **`airlabs_get_flight_status`**: Real-time tracking of specific flights (e.g., "KL601").

* **`airlabs_get_schedules`**: Find flight schedules between airports (e.g., "AMS" to "SFO").

* **`airlabs_get_airport_delays`**: Check for delays at specific airports.

* **`airlabs_search_airports`**: Look up IATA codes by city name (e.g., "London" -> LHR, LGW).

* **`airlabs_get_nearby_airports`**: Find airports near a specific location.

## Setup & Running Locally

1. **Clone the repo**

   ```bash
   git clone [https://github.com/gsa87/airlabs-mcp-server.git](https://github.com/gsa87/airlabs-mcp-server.git)
   cd airlabs-mcp-server
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   Copy the example environment file and add your API key:

   ```bash
   cp .env.example .env
   ```
   Open `.env` and paste your key:
   ```text
   AIRLABS_API_KEY=your_actual_api_key_here
   ```

4. **Run the Server**

   ```bash
   python src/server.py
   ```

## Deployment on Render

1. Fork this repository.

2. Create a new **Web Service** on Render.

3. Connect your GitHub repo.

4. Add the following **Environment Variable** in the Render dashboard:

   * `AIRLABS_API_KEY`

5. Deploy!

## API Key

Get a free API key from [AirLabs.co](https://airlabs.co/).

## License

MIT