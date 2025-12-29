from fastapi import APIRouter, Depends, HTTPException
from jose import jwt
from fastapi.security import HTTPBearer
from ..config import settings

router = APIRouter()
security = HTTPBearer()

def require_admin(token: str = Depends(security)):
    payload = jwt.decode(token.credentials, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
    if not payload.get("is_admin"):
        raise HTTPException(status_code=403, detail="Admins only")
    return True

@router.get("/admin/dashboard")
def admin_dashboard(_: bool = Depends(require_admin)):
    return {"message": "Welcome Admin"}
