frappe.pages['entry-dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Entry Dashboard',
		single_column: true
	});
	console.log(page)
}