from App.Models import PermissionModel

class PermissionController:
    def create_permission(self, permission_data):
        new_permission = PermissionModel(
            name=permission_data.name,
            features=permission_data.features
        )
        permission_id = PermissionModel.create_permission(new_permission)
        return permission_id

    def delete_permission(self, permission_id):
        # Deleta uma permissão pelo ID e retorna um booleano indicando sucesso
        deleted = PermissionModel.delete_permission(permission_id)
        return deleted

    def get_all_permissions(self):
        permissions = PermissionModel.get_all_permissions()
        return [permission for permission in permissions]