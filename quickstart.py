# Enda Crossan, 04/11/2022
# Python diagram library demo, quickstart.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

# Set show to True/False to see png output on execution
with Diagram("Quickstart Demo", show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")

