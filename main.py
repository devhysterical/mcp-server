from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional, Any
import uvicorn
from datetime import datetime

# Khởi tạo FastAPI app
app = FastAPI(
    title="MCP Server",
    description="Model Context Protocol Server for LLM interactions",
    version="1.0.0",
)


# Định nghĩa các model dữ liệu
class ToolRequest(BaseModel):
    tool_name: str
    parameters: Dict[str, Any]
    context: Optional[Dict[str, Any]] = None


class ToolResponse(BaseModel):
    success: bool
    result: Any
    error: Optional[str] = None
    timestamp: datetime = datetime.now()


# Danh sách các công cụ được hỗ trợ
SUPPORTED_TOOLS = {
    "calculator": "Performs basic mathematical calculations",
    "weather": "Gets weather information for a location",
    "search": "Performs web search queries",
}


@app.get("/")
async def root():
    """Root endpoint returning server information"""
    return {
        "name": "MCP Server",
        "version": "1.0.0",
        "status": "running",
        "supported_tools": SUPPORTED_TOOLS,
    }


@app.post("/execute", response_model=ToolResponse)
async def execute_tool(request: ToolRequest):
    """Execute a tool with given parameters"""
    if request.tool_name not in SUPPORTED_TOOLS:
        raise HTTPException(
            status_code=400, detail=f"Tool '{request.tool_name}' not supported"
        )

    try:
        # Xử lý yêu cầu dựa trên tool_name
        result = await process_tool_request(request)
        return ToolResponse(success=True, result=result)
    except Exception as e:
        return ToolResponse(success=False, result=None, error=str(e))


async def process_tool_request(request: ToolRequest) -> Any:
    """Process tool requests based on tool name"""
    if request.tool_name == "calculator":
        return await handle_calculator(request.parameters)
    elif request.tool_name == "weather":
        return await handle_weather(request.parameters)
    elif request.tool_name == "search":
        return await handle_search(request.parameters)
    else:
        raise ValueError(f"Unknown tool: {request.tool_name}")


async def handle_calculator(parameters: Dict[str, Any]) -> Any:
    """Handle calculator tool requests"""
    operation = parameters.get("operation")
    numbers = parameters.get("numbers", [])

    if not operation or not numbers:
        raise ValueError("Missing operation or numbers")

    if operation == "add":
        return sum(numbers)
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
        return result
    else:
        raise ValueError(f"Unsupported operation: {operation}")


async def handle_weather(parameters: Dict[str, Any]) -> Any:
    """Handle weather tool requests"""
    location = parameters.get("location")
    if not location:
        raise ValueError("Location is required")

    # TODO: Implement actual weather API integration
    return {"location": location, "temperature": "25°C", "condition": "Sunny"}


async def handle_search(parameters: Dict[str, Any]) -> Any:
    """Handle search tool requests"""
    query = parameters.get("query")
    if not query:
        raise ValueError("Search query is required")

    # TODO: Implement actual search functionality
    return {
        "query": query,
        "results": [
            {"title": "Sample Result 1", "url": "http://example.com/1"},
            {"title": "Sample Result 2", "url": "http://example.com/2"},
        ],
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
