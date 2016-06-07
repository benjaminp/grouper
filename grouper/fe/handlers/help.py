from grouper.constants import PERMISSION_AUDITOR, PERMISSION_CREATE, PERMISSION_GRANT, TAG_EDIT
from grouper.fe.settings import settings
from grouper.fe.util import GrouperHandler
from grouper.models.permission import Permission


class Help(GrouperHandler):
    def get(self):
        permissions = (
            self.session.query(Permission)
            .order_by(Permission.name)
        )
        d = {permission.name: permission for permission in permissions}

        self.render("help.html",
                    how_to_get_help=settings.how_to_get_help,
                    site_docs=settings.site_docs,
                    grant_perm=d[PERMISSION_GRANT],
                    create_perm=d[PERMISSION_CREATE],
                    audit_perm=d[PERMISSION_AUDITOR],
                    tag_edit=d[TAG_EDIT])
