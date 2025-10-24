from protonvpn_nm_lib.api import protonvpn
from protonvpn_nm_lib.core.environment import ExecutionEnvironment
from protonvpn_nm_lib.enums import ConnectionTypeEnum
from protonvpn_nm_lib.core.utilities import Utilities
from protonvpn_nm_lib.enums import (ProtocolEnum)

class ProtonPyBasic:
    def __init__(self, errors_enabled=False):
        self._env = ExecutionEnvironment()
        self._utils = Utilities
        self.protonvpn = protonvpn
        self.errors_enabled = errors_enabled
        self.current_server = None
        self.session = None
        self.countries = None
    def login(self, username=None, password=None, override=False):
        if self.protonvpn.check_session_exists() and not override:
            print('System logged in already, if you wish to use a different acc make override True and use username and password vars or dotenv with PROTON_PASSWORD and PROTON_USERNAME.')
            return 1
       
        if ((username is None) and not (password is None)) or (not (username is None) and (password is None)):
            raise Exception("Must include password and username.")
        self.protonvpn.login(username, password)

    def start_session(self):
        self.session = self.protonvpn.get_session()
        self.countries = self.protonvpn.get_country().get_dict_with_country_servername(
            self.session.servers, self.session.vpn_tier
        )
    def logout(self):
        self.protonvpn.logout()
    def connect(self, servername=None, connection_type=ConnectionTypeEnum.FREE, protocol=ProtocolEnum.TCP):
        connection_type=ConnectionTypeEnum.SERVERNAME
        self.protonvpn.setup_connection(
            connection_type=connection_type,
            connection_type_extra_arg=servername,
            protocol=protocol
            )
        return self.protonvpn.connect()
    def reconnect(self):
        self.protonvpn.setup_reconnect()
    def _setup(self, servername):
        connection_type=ConnectionTypeEnum.FREE
        protocol=ProtocolEnum.TCP

        self.protonvpn.setup_connection(
            connection_type=connection_type,
            connection_type_extra_arg=servername,
            protocol=protocol
            )
    def disconnect(self):
        self.protonvpn.disconnect()

