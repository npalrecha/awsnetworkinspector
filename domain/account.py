class Account:
    id = ''
    name = ''
    profilename = ''

    instances = []
    vpcs = []
    elasticips = []
    subnets = []

    def __init__(self) :
        self.profilename = ''

    def linksubnetstovpcs(self):
        for vpc in self.vpcs:
            for subnet in self.subnets:
                if subnet.VpcId == vpc.VpcId:
                    vpc.subnets.append(subnet)

    def hydratefromitem(self):
        
        for item in self.vpcs:
            item.hydratefromitem()

        for item in self.instances:
            item.hydratefromitem()

        for item in self.elasticips:
            item.hydratefromitem()

        for item in self.subnets:
            item.hydratefromitem()
            
        self.linksubnetstovpcs()

    def prettyprint(self):
        
        print('Number of Vpcs: {}  '.format(len(self.vpcs)))

        print ('------------ Account Printout  -------------------')
        print ('Account Id ' + str(self.id))

        for vpc in self.vpcs:
            vpc.prettyprint(' ', 5)

        print ('-------------Instances---------------------------- ')
        for instance in self.instances:
            instance.prettyprint()

        print ('-------------Elastic Ips---------------------------- ')
        for eip in self.elasticips:
            eip.prettyprint()
        
        # print ('-------------Subnets---------------------------- ')
        # for subnet in self.subnets:
        #     subnet.prettyprint()