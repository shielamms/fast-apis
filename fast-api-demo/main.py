from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

from models import User, SchoolLocation, StudentProfile

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@app.get('/ping')
async def root(token: str = Depends(oauth2_scheme)):
    return {'response': 200, 'message': 'pong!'}

@app.post('/users/')
async def add_user(user: User):
    return {'user': user, 'response': 200}

@app.post('/recommend-by-location/')
async def recommend_by_location(location: SchoolLocation):
    location_dict = location.dict()
    if ('country' in location_dict
        and 'country_subdivision' not in location_dict
        and 'locality' not in location_dict):
        return {'level': 'country', 'data': location_dict}
    elif 'country_subdivision' in location_dict:
        return {'level': 'country_subdivision', 'data': location_dict}
    else:
        return {'level': 'locality', 'data': location_dict}

@app.post('/recommend-by-student-profile/')
async def recommend_by_student_profile(profile: StudentProfile):
    profile_dict = profile.dict()
    return {'profile_dict': profile_dict}
