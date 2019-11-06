# -*- coding: utf-8 -*-
# Copyright (c) 2018, VHRS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class VerifyAddressCheck1(Document):
	pass

@frappe.whitelist()
def get_check(applicant_id):
	address_check1_id = frappe.get_list("Address Check1", filters={"applicant_id":applicant_id}, fields=("name")) 
	# frappe.errprint(employment_check1_id)
	return address_check1_id


