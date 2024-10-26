from fastapi import HTTPException
from App.Models.PydanticModels import Permission, PermissionResponse, PermissionUpdate
from App.Controller import PermissionController
from .CommonRouter import permissionRouter
from fastapi import Depends

permission_controller = PermissionController()

@permissionRouter.post("/create_permission")
def create_permission(permission: Permission):
    new_permission = permission_controller.create_permission(permission)
    if new_permission:
        return new_permission
    raise HTTPException(status_code=400, detail="Permission already exists")

@permissionRouter.delete("/delete_permission/{permission_id}")
def delete_permission(permission_id: str):
    permission = permission_controller.delete_permission(permission_id)
    if permission:
        return permission
    raise HTTPException(status_code=404, detail="Permission not found")

@permissionRouter.get("/get_all_permissions")
def get_all_permissions():
    return permission_controller.get_all_permissions()