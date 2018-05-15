# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:35:24 2018

@author: Suharshith
"""
import smtplib
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems




sendemail(from_addr    = 'suharshith.****@gmail.com', 
          to_addr_list = ['suharshith.****@gmail.com'],
          cc_addr_list = [''], 
          subject      = 'Howdy', 
          message      = 'Howdy from a python function', 
          login        = 'suharshith.****@gmail.com', 
          password     = '********')