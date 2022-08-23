import sys, os
from substrateinterface import SubstrateInterface
from sms import send_sms as send_notify

MY_SS58_ADDR = os.getenv("MY_SS58_ADDR")
RPC_ENDPOINT = os.getenv("RPC_ENDPOINT")
APPCHAIN_NAME = RPC_ENDPOINT.split('/')[3]
DIFF_COUNT = 50 #
PHONE_NUMBER = 15159665573

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
        return reward_list

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

def alarm(self_point,max_point):
    #alarm
    str_self_point = '{}'.format(self_point)
    str_max_point = '{}'.format(max_point)
    diff = int(str_max_point) - int(str_self_point)
    if diff > DIFF_COUNT:
        print("My Node is Exception,Please Check")
        msg = "My {} Node is Exception,Please Check\n My point-->{}\n Max Point-->{}".format(APPCHAIN_NAME, self_point, max_point)
        send_notify(PHONE_NUMBER, msg)
    else:
        print("My {} Node is Normal".format(APPCHAIN_NAME))

if __name__ == "__main__":
    print("start......")
    reward_list = get_blockchain_info()

    if len(reward_list) == 0:
        print("get info error")
        msg = "Get {} Blockchain Info Error".format(APPCHAIN_NAME)
        send_notify(PHONE_NUMBER, msg)
        sys.exit(0)
    
    self_point = get_self_point(reward_list)
    max_point = get_max_point(reward_list)
    alarm(self_point, max_point)
    
    print("end.......")


