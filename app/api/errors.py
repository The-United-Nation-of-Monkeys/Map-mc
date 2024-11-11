from fastapi import HTTPException, status

def error_404(detail: str | dict | None = None):
    if detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
def error_401(detail: str | dict | None = None):
    if detail:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
def error_403(detail: str | dict | None = None):
    if detail:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=detail)
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)