import sys
from substrateinterface import SubstrateInterface

MY_SS58_ADDR = "5FNQXuVvhhLAbWBw56xD1CdrvwUiEFsgj3yCwvnK7zD9PH4o"
RPC_ENDPOINT = "wss://gateway.mainnet.octopus.network/fusotao/0efwa9v0crdx4dg3uj8jdmc5y7dj4ir2"
DIFF_COUNT = 50 #
client = SubstrateInterface(url=RPC_ENDPOINT)

def get_blockchain_info():
    reward_list = []
    try:
        # get current era
        era_rst = client.query("OctopusLpos","ActiveEra")
        current_era = era_rst["index"]

        #get reward info
        current_era = int('{}'.format(current_era))
        node_rst = client.query("OctopusLpos","ErasRewardPoints",params=[current_era])
        og_reward_list = node_rst["individual"]
        
        # convert scale_info to list
        for item in og_reward_list:
            reward_list.append((item[0],item[1]))

        return reward_list
    except Exception as e:
        print("get blockchain info error {}".format(e))
        return []

def get_self_point(reward_list):
    self_point = 0
    for item in reward_list:
        if item[0] == MY_SS58_ADDR:
            self_point = item[1]
            print("my node get reward points-->{}".format(self_point))
            break
    return self_point

def get_max_point(reward_list):
    #get second max reward count
    points_list = []
    for item in reward_list:
        points_list.append(item[1])
    points_list.sort()
    max_point = points_list[len(points_list)-3]  # get three max point
    print("max reward points--->{}".format(max_point))
    return max_point

#send msg to telegram
def send_email():
    pass


def alarm(self_point,max_point):
    #alarm
    str_self_point = '{}'.format(self_point)
    str_max_point = '{}'.format(max_point)
    diff = int(str_max_point) - int(str_self_point)
    if diff > DIFF_COUNT:
        print("My Node is Exception,Please Check")
        send_email()
    else:
        print("My Node is Normal")




if __name__ == "__main__":
    print("start......")
    reward_list = get_blockchain_info()

    if len(reward_list) == 0:
        print("get info error")
        send_email()
        sys.exit(0)
    
    self_point = get_self_point(reward_list)
    max_point = get_max_point(reward_list)
    alarm(self_point, max_point)
    
    print("end.......")


