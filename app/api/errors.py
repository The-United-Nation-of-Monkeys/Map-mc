from fastapi import HTTPException, status

def error_404(detail):
    if detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)