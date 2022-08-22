# oct_appchain_monitor
monitor appchain state

## 1. env requirement
```
python 3.9
```

## 2. clone code
```
git clone https://github.com/0xtronzheng/oct_appchain_monitor.git
```
## install depend
```
cd oct_appchain_monitor
pip install -r requirements.txt
```

## modify rpc_endpoint & my_ss58_addr
```
MY_SS58_ADDR = "" # self ss58 addr 
RPC_ENDPOINT = "wss://gateway.mainnet.octopus.network/fusotao/0efwa9v0crdx4dg3uj8jdmc5y7dj4ir2" # want to monitor appchain's rpc_endpoint
```
## run
```
python main.py
```