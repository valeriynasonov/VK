import requests
class VKuser:
  def __init__(self, token, version, id):
    self.token = token
    self.version = version
    self.id = id

  def search_friends(self, user_id):
    list_of_friend = [ ]
    list_general_friends = [ ]
    resp = requests.get("https://api.vk.com/method/friends.get", params = {"user_id": self.id, "count": "10", "fields": "name", "access_token":self.token, "v":"5.126"}).json()
    for element in resp["response"]["items"]:
      name_friend = element["first_name"] + element["last_name"]
      list_of_friend.append(name_friend)
    resp1 = requests.get("https://api.vk.com/method/friends.get", params = {"user_id": self.id, "count": "10", "fields": "name", "access_token":self.token, "v":"5.126"}).json()
    for elements in resp1["response"]["items"]:
      name_friend1 = elements["first_name"] + elements["last_name"]
      list_of_friend.append(name_friend1)
    for position in list_of_friend:
      if list_of_friend.count(position) > 1:
        list_general_friends.append(position)
    return set(list_general_friends)


  def __and__(self, others):
    return list(self.search_friends(self, others.id))

  def __str__(self):
    return "http://vk.com//" + self.id