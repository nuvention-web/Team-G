import sys
import requests
url = 'http://murphy.wot.eecs.northwestern.edu/~sme0261/followerstackserv.py'


def main() :

	req_type = sys.argv[1]
	username = sys.argv[2]
	
	# ----------------------------- Account Data -------------------------------

	# Create new user (adduser username password company rep_name email phone active(1/0 T/F) card_number card_cvc card_exp_date reoccuring(1/0 T/F) amount)
	if req_type == 'adduser':
		password = sys.argv[3]
		company = sys.argv[4]
		rep_name = sys.argv[5]
		email = sys.argv[6]
		phone = sys.argv[7]
		active = sys.argv[8]
		card_number = sys.argv[9]
		card_cvc = sys.argv[10]
		card_exp_date = sys.argv[11]
		reoccuring = sys.argv[12]
		amount = sys.argv[13]
		if int(active) == 1:
			active = True
		else:
			active = False
		if int(reoccuring) == 1:
			reoccuring = True
		else:
			reoccuring = False
		
		payload = {'req_type': req_type, 'username': username, 'password': password, 'company': company, 'rep_name': rep_name, 'email': email, 'phone': phone, 'active': active, 'card_number': card_number, 'card_cvc': card_cvc, 'card_exp_date': card_exp_date, 'reoccuring': reoccuring, 'amount': amount}
		r = requests.post(url, data=payload)
		if 'ERROR: User already exists' in r.text:
			print 'That username already exists, please enter another username'
		else:
			print 'New user account created. Username: '+username

	# Search for user (getuser username)
	if req_type == 'getuser':
		payload = {'req_type': req_type, 'username': username}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'No user found'
		else:
			print r.text

	# List users (listusers)
	if req_type == 'listusers':
		payload = {'req_type': req_type}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'No users'
		else:
			print r.text

	# Modify user (modifyuser username email newEmail@gmail.com)
	if req_type == 'modifyuser':
		modify_field = sys.argv[3]
		modify_value = sys.argv[4]

		payload = {'req_type': req_type, 'username': username, 'modify_field': modify_field, 'modify_value': modify_value}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Incorrect username or fieldname. Account details not modified'
		else:
			print modify_field+' successfully modified'

	# Delete user (deleteuser username)
	if req_type == 'deleteuser':

		payload = {'req_type': req_type, 'username': username}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'No such user exists. Account not deleted'
		else:
			print 'Account deleted'



	# -------------------------- Social Media Account Data ---------------------------
	
	# Add/update SM account (updatesm username sm_platform sm_username sm_password)
	if req_type == 'updatesm':
		sm_platform = sys.argv[3]
		sm_username = sys.argv[4]
		sm_password = sys.argv[5]

		payload = {'req_type': req_type, 'username': username, 'sm_platform': sm_platform, 'sm_username': sm_username, 'sm_password': sm_password}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Incorrect username or sm_platform. Social media account not added/updated'
		else:
			print sm_platform+' account updated'

	# List user's SM accounts (listusersm username)
	if req_type == 'listusersm':
		payload = {'req_type': req_type, 'username': username}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'No such user exists, or no social media accounts found for this user'
		else:
			print r.text

	# Delete SM account (deletesm username sm_platform)
	if req_type == 'deletesm':
		sm_platform = sys.argv[3]

		payload = {'req_type': req_type, 'username': username, 'sm_platform': sm_platform}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Incorrect username or sm_platform. Social media account not deleted'
		else:
			print sm_platform+' account deleted'

	# --------------------------------- Target Parameters -------------------------------

	# Add target parameter (addtp username param_type param_description)
	if req_type == 'addtp':
		param_type = sys.argv[3]
		param_description = sys.argv[4]

		payload = {'req_type': req_type, 'username': username, 'param_type': param_type, 'param_description': param_description}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Incorrect username or param_type. Target parameter not added'
		else:
			print 'Target parameter added'

	# List user's target parameters (listusertp username)
	if req_type == 'listusertp':
		payload = {'req_type': req_type, 'username': username}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'No such user exists, or no target parameters found for this user'
		else:
			print r.text

	# Delete target parameter (deletetp username param_type param_description)
	if req_type == 'deletetp':
		param_type = sys.argv[3]
		param_description = sys.argv[4]

		payload = {'req_type': req_type, 'username': username, 'param_type': param_type, 'param_description': param_description}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Incorrect username or param_type. Target parameter not deleted'
		else:
			print 'Target parameter removed'

	# --------------------------- Social Media Account Growth ---------------------------

	# List user's social media account growth (getgrowth username sm_platform)
	if req_type == 'getgrowth':
		sm_platform = sys.argv[3]

		payload = {'req_type': req_type, 'username': username, 'sm_platform': sm_platform}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Incorrect username or sm_platform'
		else:
			print r.text

	# ------------------------------------ Payment Log ---------------------------------

	# List user's payment log (getpaymentlog username)
	if req_type == 'getpaymentlog':

		payload = {'req_type': req_type, 'username': username}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Incorrect username'
		else:
			print r.text

	# Get all payments for a month (getmthpayment mmyy)
	if req_type == 'getmthpayment':
		mmyy = sys.argv[3]

		payload = {'req_type': req_type, 'mmyy': mmyy}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Enter month in MMYY format (Jan 2017 as 0117)'
		else:
			print r.text

if __name__ == '__main__':
    main()