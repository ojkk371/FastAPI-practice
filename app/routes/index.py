from datetime import datetime
from fastapi import APIRouter
from starlette.responses import Response

router = APIRouter()


@router.get("/")
async def index():
    """
    `ELB status check API`\n
    :return:
    """
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')}")
