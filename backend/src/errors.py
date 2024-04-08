from fastapi import HTTPException, status


def with_errors(*errors: HTTPException):
    d = {}
    for err in errors:
        if err.status_code in d:
            d[err.status_code]["description"] += f"\n\n{err.detail}"
        else:
            d[err.status_code] = {"description": err.detail}
    return d


def invalid_credentials():
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail="Invalid credentials")


def token_validation_failed():
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail="Failed token validation")


def unauthorized():
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail="Authorization check failed")


def token_expired():
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail="Token expired")


def access_denied():
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                         detail="Access denied")


def user_not_found():
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="User not found!")


def audio_not_found():
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="Audio not found!")


def user_create_error(message="Unable to create such user!"):
    return HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                         detail=message)


def fragment_unavailable():
    return HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                         detail="This fragment is not available now!")


def transcribation_unavailable():
    return HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                         detail="This transcribation is not available now!")


def not_implemented():
    return HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,
                         detail="Not yet implemented")


def transcribation_not_found():
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="Transcribation not found!")


def no_audio_available():
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="No fragments left available!")


def no_transcribations_available():
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="No transcribations left available!")


def no_tasks_available():
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="No task left available!")


def file_not_found():
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="File not found!")


def permissions_not_found():
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="Permissions not found!")


def task_is_not_available():
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                         detail="Task completion is not available due your permissions!")


def unable_to_upload_file():
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                         detail="Unable to upload file now!")


def project_not_found():
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="Project not found!")


def user_already_in_group():
    return HTTPException(status_code=status.HTTP_409_CONFLICT,
                         detail="User already is a member of this group!")


def user_in_group_not_found():
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="No such user in this group!")
