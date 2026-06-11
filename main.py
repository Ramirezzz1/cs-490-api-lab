from fastapi import FastAPI
from teams import (
    breeze,
    claude_scholars,
    instructor,
    merge_survivors,
    team_dragons,
    team101,
    the_shrimps,
)

app = FastAPI(title="Bridge of Death API")


@app.get("/")
def root():
    return {"message": "Bridge of Death API", "docs": "/docs"}


app.include_router(breeze.router, prefix="/breeze", tags=["breeze"])
app.include_router(
    claude_scholars.router, prefix="/claude-scholars", tags=["claude-scholars"]
)
app.include_router(instructor.router, prefix="/instructor", tags=["instructor"])
app.include_router(
    merge_survivors.router, prefix="/merge-survivors", tags=["merge-survivors"]
)
app.include_router(team_dragons.router, prefix="/team-dragons", tags=["team-dragons"])
app.include_router(team101.router, prefix="/team101", tags=["team101"])
app.include_router(the_shrimps.router, prefix="/the-shrimps", tags=["the-shrimps"])
