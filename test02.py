from pyrfc import Connection, ABAPApplicationError, ABAPRuntimeError, LogonError, CommunicationError

import json

user_info = {
    'userid': '',
    'username': '',
    'zbm': '',
    'ztel': '',
    'zmail': '',
    'auth_bukrs': []
}


def user_login(username, pwd):
    try:
        user_in = {
            'USERID': username,
            'PASSWORD': pwd
        }

        conn = Connection(ashost='192.168.95.20',
                          sysnr='00',
                          client='310',
                          user='qlos-abap01',
                          passwd='lsm2009lsm')

        result = conn.call("YREP_USER", USER_IN=user_in)
        # print(result)
        return result

    except CommunicationError:
        return "Could not connect to server"
    except LogonError:
        return "Could not log in Wrong credentials"
    except(ABAPApplicationError, ABAPRuntimeError):
        return "An error occurred"


if __name__ == '__main__':
    ret = user_login('shaoming.lu', '123')
    rfc_msg = ret['EX_MSG'] if 'EX_MSG' in ret else ''
    rfc_msgtyp = ret['EX_MSGTYP'] if 'EX_MSGTYP' in ret else ''
    rfc_user_out = ret['USER_OUT'] if 'USER_OUT' in ret else {}
    rfc_tab_a_bukrs = ret['TAB_A_BUKRS'] if 'TAB_A_BUKRS' in ret else []
    rfc_tab_cata = ret['TAB_CATA'] if 'TAB_CATA' in ret else []
    rfc_tab_appl = ret['TAB_APPL'] if 'TAB_APPL' in ret else []

    print(rfc_msg)
    print(rfc_msgtyp)
    print(rfc_user_out)
    print(rfc_tab_a_bukrs)
    print(rfc_tab_cata)
    print(rfc_tab_appl)

    # json_tab = json.dumps(rfc_tab_a_bukrs)
    # print(json_tab)
    #
    # user_info['userid'] = rfc_user_out['USERID']
    # user_info['username'] = rfc_user_out['USERNAME']
    # user_info['zbm'] = rfc_user_out['ZBM']
    # user_info['zfunc'] = rfc_user_out['ZFUNC']
    # user_info['ztel'] = rfc_user_out['ZTEL']
    # user_info['zmail'] = rfc_user_out['ZMAIL']
    # user_info['auth_bukrs'] = rfc_tab_a_bukrs
    # print(user_info)
    # print(json.dumps(user_info))
