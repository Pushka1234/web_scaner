import scanner


target_url = "https://kuzstu.ru/"
links_to_ignore = []
data_dict = {"username": "admin", "password": "password", "Login": "submit"}

vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
vuln_scanner.session.post(target_url, data=data_dict)

#vuln_scanner.crawler()

vuln_scanner.run_scanner()


