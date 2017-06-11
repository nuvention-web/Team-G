#!/usr/bin/python

import MySQLdb as mdb
import sys
import cgi
import cgitb
import os
import re
import smtplib
from pullSMdata import get_insta_followers

print 'Content-type: text/html\n\n'

form = cgi.FieldStorage()

con = None

if os.environ['REQUEST_METHOD'] == 'POST':
    print "Post request received."
    
	# Create SQL entry

    try:
        con = mdb.connect('localhost', 'mhealth', 'mhealth', 'mhealthplay')
        print "Connected."
        print "Time: " + str(form.getvalue("time"))
        req_type = str(form.getvalue("req_type"))
        if req_type == 'adduser':
	        username = str(form.getvalue("username"))
	        check_query = "select count(username) from account_data where username = '" + username + "';"
	        cur = con.cursor()
	        cur.execute(check_query)
	        rows = cur.fetchall()
	        for col in rows:
	        	for val in col:
	        		if val == 0:
	        			break
	        		else:
	        			print "ERROR: User already exists"
	        			exit()

	        password = str(form.getvalue("password"))
	        company = str(form.getvalue("company"))
	        rep_name = str(form.getvalue("rep_name"))
	        email = str(form.getvalue("email"))
	        phone = str(form.getvalue("phone"))
	        active = str(form.getvalue("active"))
	        cardnumber = str(form.getvalue("card_number"))
	        card_cvc = str(form.getvalue("card_cvc"))
	        card_exp_data = str(form.getvalue("card_exp_data"))
	        reoccuring = str(form.getvalue("reoccuring"))
	        amount = str(form.getvalue("amount"))
			# NOTE: the query string puts the mac address and time
			# parameter in single quotes. Do NOT put the mac parameter 
			# in single quotes or the syntax will fail. 
			# TODO: sanitize data inputs to avoid injection

	        queryString = "insert into account_data(username, password, company, rep_name, email, phone, active, cardnumber, cardCVC, cardExpDate, reoccuring, amount) values(" +\
	        "'" + username + "'," + "'" + password + "'," + "'" + company + "'," + "'" + rep_name + "'," + "'" + email + "'," +\
	        "'" + phone + "'," + "'" + active + "'," + "'" + cardnumber + "'," + "'" + card_cvc + "'," + "'" + card_exp_data +\
	        "'," + "'" + reoccuring + "'," + "'" + amount + "'" + ");"
	        
	        cur = con.cursor()
	        print "Executing: " + queryString
	        cur.execute(queryString)
	        print "Executed."

        elif req_type == 'getuser':
	        username = str(form.getvalue("username"))
	        check_query = "select count(*) from account_data where username ='"  + username + "';"
	        user_data = []
	        cur = con.cursor()
	        cur.execute(check_query)
	        rows = cur.fetchall()
	        for row in rows:
	        	for val in row:
	        		if val != 0:
	        			break
	        		else:
	        			print "ERROR: User doesn't exist"
	        			exit()
	        queryString = "select * from account_data where username ='"  + username + "';"
	        cur = con.cursor()
	        cur.execute(queryString)
	        rows = cur.fetchall()
	        for row in rows:
	        	for val in row:
	        		user_data.append(val)

	        print 'Username: ' + str(user_data[0])
	        print 'Password: ' + str(user_data[1])
	        print 'Company: ' + str(user_data[2])
	        print 'Representative name: ' + str(user_data[3])
	        print 'Email: ' + str(user_data[4])
	        print 'Phone: ' + str(user_data[5])
	        print 'Active: ' + str(user_data[6])
	        print 'Card Number: ' + str(user_data[7])
	        print 'Card CVC: ' + str(user_data[8])
	        print 'Card Expiry Date: ' + str(user_data[9])
	        print 'Recurrring: ' + str(user_data[10])
	        print 'Amount: ' + str(user_data[11])

        elif req_type == 'listusers':
	        check_query = "select count(*) from account_data;"
	        all_user_data = []
	        cur = con.cursor()
	        cur.execute(check_query)
	        rows = cur.fetchall()
	        for row in rows:
	        	for val in row:
	        		if val != 0:
	        			break
	        		else:
	        			print "ERROR: No users present"
	        			exit()

	        queryString = "select * from account_data;"
	        cur = con.cursor()
	        cur.execute(queryString)
	        rows = cur.fetchall()
	        for row in rows:
	        	user_data = []
	        	for val in row:
	        		user_data.append(val)
	        	all_user_data.append(user_data)
	        count = 1
	        for user_data in all_user_data:
	        	print "User Number " + str(count)
		        print 'Username: ' + str(user_data[0])
		        print 'Password: ' + str(user_data[1])
		        print 'Company: ' + str(user_data[2])
		        print 'Representative name: ' + str(user_data[3])
		        print 'Email: ' + str(user_data[4])
		        print 'Phone: ' + str(user_data[5])
		        print 'Active: ' + str(user_data[6])
		        print 'Card Number: ' + str(user_data[7])
		        print 'Card CVC: ' + str(user_data[8])
		        print 'Card Expiry Date: ' + str(user_data[9])
		        print 'Recurrring: ' + str(user_data[10])
		        print 'Amount: ' + str(user_data[11])
		        print '----------------------------'
		        count+=1
	        
        elif req_type == 'send_mail':
	        username = str(form.getvalue("username"))
	        check_query = "select count(*) from account_data where username ='"  + username + "';"
	        user_data = []
	        cur = con.cursor()
	        cur.execute(check_query)
	        rows = cur.fetchall()
	        for row in rows:
	        	for val in row:
	        		if val != 0:
	        			break
	        		else:
	        			print "ERROR: User doesn't exist"
	        			exit()

        	queryString = "select company,rep_name,email,amount from account_data where username ='"  + username + "';"
	        cur = con.cursor()
	        cur.execute(queryString)
	        rows = cur.fetchall()
	        for row in rows:
	        	for val in row:
	        		user_data.append(val)

	        company = str(user_data[0])
	        rep_name = str(user_data[1])
	        email = str(user_data[2])
	        amount = str(user_data[3])
	        # follower_count = get_insta_followers('follower.stack')
	        smtpObj = smtplib.SMTP('smtp.gmail.com',587)
	        smtpObj.ehlo()
	        smtpObj.starttls()
	        smtpObj.login('nufollowerstack@gmail.com ', 'asdfghjkl12345')
	        try:
	        	smtpObj.sendmail('nufollowerstack@gmail.com', email,"Subject: Hello from FollowerStack\nDear " + rep_name + ",\n\nGreetings from Followerstack!\n\nThis is a gentle reminder for the payment of your social media account(s) booster for " + company + " in the amount of $" + amount + ".\n\nKindly ignore this mail if you have already paid the amount.\n\nSincerely,\nFollowerStack")
	        except e:
	        	print e
	        smtpObj.quit()
	        print 'Email sent'

        elif req_type == 'delete_user':
        	username = str(form.getvalue("username"))
        	check_query = "select count(*) from account_data where username ='"  + username+"';"
        	all_user_data = []
        	cur = con.cursor()
        	cur.execute(check_query)
        	rows = cur.fetchall()

        	for row in rows:
        		for val in row:
					if val != 0:
						break
					else:
						print "ERROR: No users present"
						exit()

	        queryString = "delete from account_data where username ='"  + username+"';"
	        cur = con.cursor()
	        cur.execute(queryString)
	        print "User deleted successfully!"

        elif req_type == 'delete_sm':
			username = str(form.getvalue("username"))
			sm_platform = str(form.getvalue("sm_platform"))
			check_query = "select count(*) from smad where username ='"  + username+"' and sm_platform='"  + sm_platform +"';"
			all_user_data = []
			cur = con.cursor()
			cur.execute(check_query)
			rows = cur.fetchall()
			for row in rows:
				for val in row:
					if val != 0:
						break
					else:
						print "ERROR: No users present"
						exit()

			queryString = "delete from smad where username ='"  + username+"' and sm_platform='"  + sm_platform +"';"
			cur = con.cursor()
			cur.execute(queryString)
			print "User deleted successfully!"

        elif req_type == 'delete_tp':
			username = str(form.getvalue("username"))
			param_type = str(form.getvalue("param_type"))
			check_query = "select count(*) from target_parameters where username ='"  + username +"' and param_type='"  + param_type +"';"
			all_user_data = []
			cur = con.cursor()
			cur.execute(check_query)
			rows = cur.fetchall()
			for row in rows:
				for val in row:
					if val != 0:
						break
					else:
						print "ERROR: No users present"
						exit()

			queryString = "delete from target_parameters where username ='"  + username+"' and param_type ='"  + param_type +"';"
			cur = con.cursor()
			cur.execute(queryString)
			print "User deleted successfully!"

        elif req_type == 'list_user_tp':
			username = str(form.getvalue("username"))
			check_query = "select count(username) from target_parameters where username = '" + username + "';"
			all_user_data = []
			cur = con.cursor()
			cur.execute(check_query)
			rows = cur.fetchall()
			for row in rows:
				for val in row:
					if val != 0:
						break
					else:
						print "ERROR: No users present"
						exit()

			queryString = "select * from target_parameters where username ='"  + username+"';"
			cur = con.cursor()
			cur.execute(queryString)
			rows = cur.fetchall()
			for row in rows:
				user_data = []
				for val in row:
					user_data.append(val)
				all_user_data.append(user_data)
			count = 1
			for user_data in all_user_data:
				print "User Number " + str(count)
				print 'Username: ' + str(user_data[0])
				print 'Parameter type: ' + str(user_data[1])
				print 'Parameter Description: ' + str(user_data[2])
				print '----------------------------'
				count+=1

        elif req_type == 'list_user_sm':
			username = str(form.getvalue("username"))
			check_query = "select count(username) from smad where username = '" + username + "';"
			all_user_data = []
			cur = con.cursor()
			cur.execute(check_query)
			rows = cur.fetchall()
			for row in rows:
				for val in row:
					if val != 0:
						break
					else:
						print "ERROR: No users present"
						exit()

			queryString = "select * from smad where username ='"  + username +"';"
			cur = con.cursor()
			cur.execute(queryString)
			rows = cur.fetchall()
			for row in rows:
				user_data = []
				for val in row:
					user_data.append(val)
				all_user_data.append(user_data)
			count = 1
			for user_data in all_user_data:
				print "User Number " + str(count)
				print 'Username: ' + str(user_data[0])
				print 'SM Platform: ' + str(user_data[1])
				print 'SM Username: ' + str(user_data[2])
				print 'SM Password: ' + str(user_data[3])
				print '----------------------------'
				count+=1

        elif req_type == 'add_tp':
        	username = str(form.getvalue("username"))
        	param_type = str(form.getvalue("param_type"))
        	param_description = str(form.getvalue("param_desc"))
        	queryString = "insert into target_parameters (username, param_type, param_desc) values('" + username + "'," + "'" + param_type + "'," + "'" + param_description + "');"
        	cur = con.cursor()
        	cur.execute(queryString)
        	print "Record added successfully!"

        elif req_type == 'get_growth':
        	username = str(form.getvalue("username"))
        	sm_platform = str(form.getvalue("sm_platform"))
        	check_query = "select count(username) from smag where username = '" + username + "';"
        	all_user_data = []
        	cur = con.cursor()
        	cur.execute(check_query)
        	rows = cur.fetchall()
        	for row in rows:
        		for val in row:
        			if val != 0:
        				break
        			else:
        				print "ERROR: No users present"
        				exit()
        	queryString = "select username, date, follower_count from smag where username ='" + username + "' and sm_platform='"  + sm_platform +"';"
        	cur = con.cursor()
        	cur.execute(queryString)
        	rows = cur.fetchall()
        	for row in rows:
        		user_data = []
        		for val in row:
        			user_data.append(val)
        		all_user_data.append(user_data)
        	count = 1
        	for user_data in all_user_data:
        		print "User Number " + str(count)
        		print 'Username: ' + str(user_data[0])
        		print 'Date: ' + str(user_data[1])
        		print 'Follower Count: ' + str(user_data[2])
        		print '----------------------------'
        		count+=1

        elif req_type == 'get_payment_log':
        	username = str(form.getvalue("username"))
        	check_query="select count(username) from payment_log where username = '" + username + "';"
        	all_user_data = []
        	cur = con.cursor()
        	cur.execute(check_query)
        	rows = cur.fetchall()
        	for row in rows:
        		for val in row:
        			if val != 0:
        				break
        			else:
        				print "ERROR: No users present"
        				exit()
        	queryString = "select * from payment_log where username ='"  + username +"';"
        	cur = con.cursor()
        	cur.execute(queryString)
        	rows = cur.fetchall()
        	for row in rows:
        		user_data = []
        		for val in row:
        			user_data.append(val)
        		all_user_data.append(user_data)
        	count = 1
        	for user_data in all_user_data:
        		print "User Number " + str(count)
        		print 'Username: ' + str(user_data[0])
        		print 'Date: ' + str(user_data[1])
        		print 'Amount: ' + str(user_data[2])
        		print '----------------------------'
        		count+=1

        elif req_type == 'get_mth_payment':
        	year = str(form.getvalue("yyyy-mm"))
        	queryString = "select * from payment_log where date LIKE '"  + year +"-%';"
        	cur = con.cursor()
        	cur.execute(queryString)
        	rows = cur.fetchall()
        	all_user_data = []
        	for row in rows:
        		user_data = []
        		for val in row:
        			user_data.append(val)
        		all_user_data.append(user_data)
        	count = 1
        	for user_data in all_user_data:
        		print "User Number " + str(count)
        		print 'Username: ' + str(user_data[0])
        		print 'Date: ' + str(user_data[1])
        		print 'Amount: ' + str(user_data[2])
        		count+=1

    except mdb.Error, e:
        print "Error connecting or executing query string." 
        print e
    finally:
        if con:
            con.close()
			    
	
elif os.environ['REQUEST_METHOD'] == 'GET':
#	print "GET received"
	print "<h3 style='background-color:#8e44ad;color:white;height:65px;line-height:60px;padding:10px;font-size:35px'>FollowerStack</h3>"
	try:
		con = mdb.connect('localhost', 'mhealth', 'mhealth', 'mhealthplay')
		cur = con.cursor()
		cur.execute("select * from account_data")
		rows = cur.fetchall()
		
		# Display the data in a table
		print "<h3>account_data -</h3>"
		print "<style type='text/css'>td{padding:5px;border-style:solid;font-size:20px;margin:10px}</style>"
		print "<table border='1'>"
		# print "<tr><th>Device</th><th>Activity</th><th>Timestamp</th><th>Activity Code</th></tr>"
		for row in rows:
			print "<tr>"
			for col in row:
				print "<td>"
				print col
				print "</td>"
			print "</tr>"
		print "</table>"

		cur = con.cursor()
		cur.execute("select * from smad")
		rows = cur.fetchall()
		
		# Display the data in a table
		print "<br /><br /><h3>Social Media Account Data -</h3>"
		print "<style type='text/css'>td{padding:5px;border-style:solid;font-size:20px;margin:10px}</style>"
		print "<table border='1'>"
		# print "<tr><th>Timestamp</th><th>Overeating Label</th></tr>"
		for row in rows:
			print "<tr>"
			for col in row:
				print "<td>"
				print col
				print "</td>"
			print "</tr>"
		print "</table>"

		cur = con.cursor()
		cur.execute("select * from target_parameters")
		rows = cur.fetchall()
		
		# Display the data in a table
		print "<br /><br /><h3>target_parameters -</h3>"
		print "<style type='text/css'>td{padding:5px;border-style:solid;font-size:20px;margin:10px}</style>"
		print "<table border='1'>"
		# print "<tr><th>Timestamp</th><th>Overeating Label</th></tr>"
		for row in rows:
			print "<tr>"
			for col in row:
				print "<td>"
				print col
				print "</td>"
			print "</tr>"
		print "</table>"


		cur = con.cursor()
		cur.execute("select * from smag")
		rows = cur.fetchall()
		
		# Display the data in a table
		print "<br /><br /><h3>Social Media Account Growth -</h3>"
		print "<style type='text/css'>td{padding:5px;border-style:solid;font-size:20px;margin:10px}</style>"
		print "<table border='1'>"
		# print "<tr><th>Timestamp</th><th>Overeating Label</th></tr>"
		for row in rows:
			print "<tr>"
			for col in row:
				print "<td>"
				print col
				print "</td>"
			print "</tr>"
		print "</table>"


		cur = con.cursor()
		cur.execute("select * from payment_log")
		rows = cur.fetchall()
		
		# Display the data in a table
		print "<br /><br /><h3>payment_log -</h3>"
		print "<style type='text/css'>td{padding:5px;border-style:solid;font-size:20px;margin:10px}</style>"
		print "<table border='1'>"
		# print "<tr><th>Timestamp</th><th>Overeating Label</th></tr>"
		for row in rows:
			print "<tr>"
			for col in row:
				print "<td>"
				print col
				print "</td>"
			print "</tr>"
		print "</table>"
	
	except mdb.Error, e:
		print "Error %d = %s<p>" % (e.args[0],e.args[1])
		sys.exit(1)
		
	finally:
		if con:
			con.close()
		
else:
	print "You sent a " + str(os.environ['REQUEST_METHOD']) + \
	    " request. This script only works with POST and GET requests."
