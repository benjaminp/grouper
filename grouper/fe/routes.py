from grouper.constants import (
        NAME_VALIDATION,
        NAME2_VALIDATION,
        PERMISSION_VALIDATION,
        USERNAME_VALIDATION,
        )
from grouper.fe.handlers.audits_complete import AuditsComplete
from grouper.fe.handlers.audits_create import AuditsCreate
from grouper.fe.handlers.audits_view import AuditsView
from grouper.fe.handlers.group_add import GroupAdd
from grouper.fe.handlers.group_disable import GroupDisable
from grouper.fe.handlers.group_edit import GroupEdit
from grouper.fe.handlers.group_edit_member import GroupEditMember
from grouper.fe.handlers.group_enable import GroupEnable
from grouper.fe.handlers.group_join import GroupJoin
from grouper.fe.handlers.group_leave import GroupLeave
from grouper.fe.handlers.group_permission_request import GroupPermissionRequest
from grouper.fe.handlers.group_remove import GroupRemove
from grouper.fe.handlers.group_request_update import GroupRequestUpdate
from grouper.fe.handlers.group_requests import GroupRequests
from grouper.fe.handlers.group_view import GroupView
from grouper.fe.handlers.groups_view import GroupsView
from grouper.fe.handlers.help import Help
from grouper.fe.handlers.index import Index
from grouper.fe.handlers.not_found import NotFound
from grouper.fe.handlers.perf_profile import PerfProfile
from grouper.fe.handlers.permission_disable_auditing import PermissionDisableAuditing
from grouper.fe.handlers.permission_enable_auditing import PermissionEnableAuditing
from grouper.fe.handlers.permission_view import PermissionView
from grouper.fe.handlers.permissions_create import PermissionsCreate
from grouper.fe.handlers.permissions_grant import PermissionsGrant
from grouper.fe.handlers.permissions_request_update import PermissionsRequestUpdate
from grouper.fe.handlers.permissions_requests import PermissionsRequests
from grouper.fe.handlers.permissions_revoke import PermissionsRevoke
from grouper.fe.handlers.permissions_view import PermissionsView
from grouper.fe.handlers.public_key_add import PublicKeyAdd
from grouper.fe.handlers.public_key_delete import PublicKeyDelete
from grouper.fe.handlers.search import Search
from grouper.fe.handlers.stats import Stats
from grouper.fe.handlers.user_disable import UserDisable
from grouper.fe.handlers.user_enable import UserEnable
from grouper.fe.handlers.user_requests import UserRequests
from grouper.fe.handlers.user_token_add import UserTokenAdd
from grouper.fe.handlers.user_token_disable import UserTokenDisable
from grouper.fe.handlers.user_view import UserView
from grouper.fe.handlers.users_public_key import UsersPublicKey
from grouper.fe.handlers.users_user_tokens import UsersUserTokens
from grouper.fe.handlers.users_view import UsersView


HANDLERS = [
    (r"/", Index),
    (r"/audits", AuditsView),
    (r"/audits/(?P<audit_id>[0-9]+)/complete", AuditsComplete),
    (r"/audits/create", AuditsCreate),
    (r"/groups", GroupsView),
    (r"/permissions/create", PermissionsCreate),
    (r"/permissions/requests", PermissionsRequests),
    (r"/permissions/requests/(?P<request_id>[0-9]+)", PermissionsRequestUpdate),
    (r"/permissions/{}".format(PERMISSION_VALIDATION), PermissionView),
    (r"/permissions", PermissionsView),
    (r"/permissions/{}/enable-auditing".format(PERMISSION_VALIDATION), PermissionEnableAuditing),
    (r"/permissions/{}/disable-auditing".format(PERMISSION_VALIDATION), PermissionDisableAuditing),
    (r"/permissions/grant/{}".format(NAME_VALIDATION), PermissionsGrant),
    (
        r"/permissions/{}/revoke/(?P<mapping_id>[0-9]+)".format(PERMISSION_VALIDATION),
        PermissionsRevoke
    ),
    (r"/search", Search),
    (r"/users", UsersView),
    (r"/users/public-keys", UsersPublicKey),
    (r"/users/tokens", UsersUserTokens),
    (r"/user/requests", UserRequests),
]

for regex in (r"(?P<user_id>[0-9]+)", USERNAME_VALIDATION):
    HANDLERS.extend([
        (r"/users/{}".format(regex), UserView),
        (r"/users/{}/disable".format(regex), UserDisable),
        (r"/users/{}/enable".format(regex), UserEnable),
        (r"/users/{}/public-key/add".format(regex), PublicKeyAdd),
        (
            r"/users/{}/public-key/(?P<key_id>[0-9]+)/delete".format(regex),
            PublicKeyDelete
        ),
        (r"/users/{}/tokens/add".format(regex), UserTokenAdd),
        (r"/users/{}/tokens/(?P<token_id>[0-9]+)/disable".format(regex), UserTokenDisable),
    ])

for regex in (r"(?P<group_id>[0-9]+)", NAME_VALIDATION):
    HANDLERS.extend([
        (r"/groups/{}".format(regex), GroupView),
        (r"/groups/{}/edit".format(regex), GroupEdit),
        (r"/groups/{}/disable".format(regex), GroupDisable),
        (r"/groups/{}/enable".format(regex), GroupEnable),
        (r"/groups/{}/join".format(regex), GroupJoin),
        (r"/groups/{}/add".format(regex), GroupAdd),
        (r"/groups/{}/remove".format(regex), GroupRemove),
        (r"/groups/{}/leave".format(regex), GroupLeave),
        (r"/groups/{}/requests".format(regex), GroupRequests),
        (r"/groups/{}/requests/(?P<request_id>[0-9]+)".format(regex), GroupRequestUpdate),
        (r"/groups/{}/permission/request".format(regex), GroupPermissionRequest),
        (
            r"/groups/{}/edit/(?P<member_type>user|group)/{}".format(regex, NAME2_VALIDATION),
            GroupEditMember
        ),
    ])

HANDLERS += [
    (r"/help", Help),
    (r"/debug/stats", Stats),
    (r"/debug/profile/(?P<trace_uuid>[\-\w]+)", PerfProfile),

    (r"/.*", NotFound),
]
