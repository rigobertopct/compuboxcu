import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery

from .mutations import Mutation as Mutations
from .queries import Query as Queries

class AuthMutation(graphene.ObjectType):
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    update_account = mutations.UpdateAccount.Field()

    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class Query(UserQuery, Queries, graphene.ObjectType):
    pass


class Mutation(AuthMutation, Mutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)