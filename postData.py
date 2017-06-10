import sys
import requests
url = 'http://murphy.wot.eecs.northwestern.edu/~sme0261/followerstackserv.py'


def main() :

	print 'Request Types:'
	print ' - adduser (create a new user)'
	print ' - getuser (search for user)'
	print ' - listusers (list all users)'
	print ' - modifyuser (modify user account data)'
	print ' - deleteuser (delete a user)\n'
	print ' - updatesm (update or add a social media account)'
	print ' - listusersm (list a user\'s social media accounts)'
	print ' - deletesm (delete a social media account)\n'
	print ' - addtp (add a user\'s target parameter)'
	print ' - listusertp (list a user\'s target parameters)'
	print ' - deletetp (delete a target parameter)\n'
	print ' - getgrowth (list the follower count for user\'s social media account)'
	print ' - getpaymentlog (list user\'s past payments)'
	print ' - getmthpayment (list all payments for a month)'
	print ' - send_mail (send email reminder to user)'
	req_type = input('Enter request type: ')
	
	# ----------------------------- Account Data -------------------------------

	# Create new user
	if req_type == 'adduser':
		username = input('Username: ')
		password = input('Password: ')
		company = input('Company: ')
		rep_name = input('Representative\'s name: ')
		email = input('Email: ')
		phone = input('Phone: ')
		active = input('Account active? (Y/N): ')
		card_number = input('Card number: ')
		card_cvc = input('Card CVC: ')
		card_exp_date = input('Card expirary date: ')
		reoccuring = input('Reoccuring payments? (Y/N) : ')
		amount = input('Monthly amount: USD ')
		if active == 'Y' or active == 'y':
			active = True
		else:
			active = False
		if reoccuring == 'N' or reoccuring == 'n':
			reoccuring = True
		else:
			reoccuring = False
		
		payload = {'req_type': req_type, 'username': username, 'password': password, 'company': company, 'rep_name': rep_name, 'email': email, 'phone': phone, 'active': active, 'card_number': card_number, 'card_cvc': card_cvc, 'card_exp_date': card_exp_date, 'reoccuring': reoccuring, 'amount': amount}
		r = requests.post(url, data=payload)
		if 'ERROR: User already exists' in r.text:
			while 'ERROR: User already exists' in r.text:
				username = input('That username already exists, please enter another username: ')
				payload = {'req_type': req_type, 'username': username, 'password': password, 'company': company, 'rep_name': rep_name, 'email': email, 'phone': phone, 'active': active, 'card_number': card_number, 'card_cvc': card_cvc, 'card_exp_date': card_exp_date, 'reoccuring': reoccuring, 'amount': amount}
				r = requests.post(url, data=payload)
		else:
			print 'New user account created. Username: '+username

	# Search for user
	elif req_type == 'getuser':
		username = input('Username: ')
		payload = {'req_type': req_type, 'username': username}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'No user found'
		else:
			print r.text.split("\n",4)[4]

	# List users
	if req_type == 'listusers':
		payload = {'req_type': req_type}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'No users'
		else:
			print r.text.split("\n",4)[4]

	# Modify user
	if req_type == 'modifyuser':
		username = input('Username: ')
		print 'User\'s account data fields'
		print ' 1) password'
		print ' 2) company'
		print ' 3) representative\'s name'
		print ' 4) email'
		print ' 5) phone'
		print ' 6) account active'
		print ' 7) card number'
		print ' 8) card CVC'
		print ' 9) card expirary date'
		print '10) reoccuring payments'
		print '11) monthly amount'

		modify_field = input('Which field (1-11): ')
		while modify_field < 1 or modify_field > 11:
			modify_field = input('Which field (1-11): ')
		if int(modify_field) == 1:
			modify_field = 'password'
		elif int(modify_field) == 2:
			modify_field = 'company'
		elif int(modify_field) == 3:
			modify_field = 'rep_name'
		elif int(modify_field) == 4:
			modify_field = 'email'
		elif int(modify_field) == 5:
			modify_field = 'phone'
		elif int(modify_field) == 6:
			modify_field = 'active'
			print 'Account active options: Y/N'
		elif int(modify_field) == 7:
			modify_field = 'card_number'
		elif int(modify_field) == 8:
			modify_field = 'card_cvc'
		elif int(modify_field) == 9:
			modify_field = 'card_exp_date'
		elif int(modify_field) == 10:
			modify_field = 'reoccuring'
			print 'Reoccuring payments options: Y/N'
		elif int(modify_field) == 11:
			modify_field = 'amount'

		modify_value = input('New field value: ')

		payload = {'req_type': req_type, 'username': username, 'modify_field': modify_field, 'modify_value': modify_value}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Incorrect username. Account details not modified'
		else:
			print modify_field+' successfully modified'

	# Delete user
	if req_type == 'deleteuser':
		username = input('Username: ')

		payload = {'req_type': req_type, 'username': username}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'No such user exists. Account not deleted'
		else:
			print 'Account deleted'



	# -------------------------- Social Media Account Data ---------------------------
	
	# Add/update SM account
	if req_type == 'updatesm':
		username = input('Username: ')
		sm_platform = input('Social media platform (Instagram, Twitter, or Facebook): ')
		sm_username = input('Social media account username: ')
		sm_password = input('Social media account password: ')

		payload = {'req_type': req_type, 'username': username, 'sm_platform': sm_platform, 'sm_username': sm_username, 'sm_password': sm_password}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Incorrect username or sm_platform. Social media account not added/updated'
		else:
			print sm_platform+' account updated'

	# List user's SM accounts
	if req_type == 'listusersm':
		username = input('Username: ')

		payload = {'req_type': req_type, 'username': username}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'No such user exists, or no social media accounts found for this user'
		else:
			print r.text.split("\n",4)[4]

	# Delete SM account
	if req_type == 'deletesm':
		username = input('Username: ')
		sm_platform = input('Social media platform (Instagram, Twitter, or Facebook): ')

		payload = {'req_type': req_type, 'username': username, 'sm_platform': sm_platform}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Incorrect username or sm_platform. Social media account not deleted'
		else:
			print sm_platform+' account deleted'

	# --------------------------------- Target Parameters -------------------------------

	# Add target parameter
	if req_type == 'addtp':
		username = input('Username: ')
		param_type = input('Target parameter type: ')
		param_description = input('Target parameter description: ')

		payload = {'req_type': req_type, 'username': username, 'param_type': param_type, 'param_description': param_description}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Incorrect username or param_type. Target parameter not added'
		else:
			print 'Target parameter added'

	# List user's target parameters
	if req_type == 'listusertp':
		username = input('Username: ')

		payload = {'req_type': req_type, 'username': username}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'No such user exists, or no target parameters found for this user'
		else:
			print r.text.split("\n",4)[4]

	# Delete target parameter
	if req_type == 'deletetp':
		username = input('Username: ')
		param_type = input('Target parameter type: ')
		param_description = input('Target parameter description: ')

		payload = {'req_type': req_type, 'username': username, 'param_type': param_type, 'param_description': param_description}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Incorrect username or param_type. Target parameter not deleted'
		else:
			print 'Target parameter removed'

	# --------------------------- Social Media Account Growth ---------------------------

	# List user's social media account growth
	if req_type == 'getgrowth':
		username = input('Username: ')
		sm_platform = input('Social media platform (Instagram, Twitter, or Facebook): ')

		payload = {'req_type': req_type, 'username': username, 'sm_platform': sm_platform}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Incorrect username or sm_platform'
		else:
			print r.text.split("\n",4)[4]

	# ------------------------------------ Payment Log ---------------------------------

	# List user's payment log
	if req_type == 'getpaymentlog':
		username = input('Username: ')

		payload = {'req_type': req_type, 'username': username}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Incorrect username'
		else:
			print r.text.split("\n",4)[4]

	# Get all payments for a month
	if req_type == 'getmthpayment':
		mmyy = input('Month (MMYY): ')

		payload = {'req_type': req_type, 'mmyy': mmyy}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'Enter month in MMYY format (Jan 2017 as 0117)'
		else:
			print r.text.split("\n",4)[4]


	# ------------------------------------- Others --------------------------------------

	# Send email reminder to client
	if req_type == 'send_mail':
		username = input('Username: ')
		
		payload = {'req_type': req_type, 'username': username}
		r = requests.post(url, data=payload)
		if 'ERROR' in r.text:
			print 'No such user exists'
		else:
			print 'Email sent to user '+username


if __name__ == '__main__':
    main()