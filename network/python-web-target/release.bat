@echo off
echo "上传文件"
scp .\main.py root@10.92.2.71:/data01/test-target-tool
::echo "重启服务"
::ssh root@10.92.2.71 sh /data01/test-target-tool/stop.sh
::ssh root@10.92.2.71 sh /data01/test-target-tool/start.sh
