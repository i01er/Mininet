from mininet.topo import Topo
from mininet.net import Mininet

class MyTopo(Topo):
	def __init__(self):
		Topo.__init__(self)

		sl_h1 = self.addHost('sl_h1')
		sl_h2 = self.addHost('sl_h2')
		sl_h3 = self.addHost('sl_h3')
		sl_h4 = self.addHost('sl_h4')
		sl_h5 = self.addHost('sl_h5')

		so1_h1 = self.addHost('so1_h1')
		so1_h2 = self.addHost('so1_h2')
		so1_h3 = self.addHost('so1_h3')

		so2_h1 = self.addHost('so2_h1')

		so3_h1 = self.addHost('so3_h1')

		sw_h1 = self.addHost('sw_h1')

		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
		s3 = self.addSwitch('s3')

		self.addLink(s1, s2, bw=1000, delay='20us', loss=0)
		self.addLink(s1, s3, bw=1000, delay='20us', loss=0)

		self.addLink(sl_h1, s1, bw=10, delay='50ms', loss=5)
		self.addLink(sl_h2, s1, bw=10, delay='50ms', loss=5)
		self.addLink(sl_h3, s1, bw=10, delay='50ms', loss=5)
		self.addLink(sl_h4, s1, bw=10, delay='50ms', loss=5)
		self.addLink(sl_h5, s1, bw=10, delay='50ms', loss=5)

		self.addLink(so1_h1, s2, bw=50, delay='20ms', loss=2)
		self.addLink(so1_h2, s2, bw=50, delay='20ms', loss=2)
		self.addLink(so1_h3, s2, bw=50, delay='20ms', loss=2)

		self.addLink(so2_h1, s2, bw=50, delay='20ms', loss=2)
		
		self.addLink(so3_h1, s2, bw=50, delay='20ms', loss=1)
		
		self.addLink(sw_h1, s3, bw=100, delay='10ms', loss=1)

# if __name__ == '__main__':
# 	topo = MyTopo(3)
# 	net = Mininet(topo = topo, link=TCLink, controller=none)
# 	net.start()
# 	CLI(net)
# 	net.stop()

topos = {'mytopo': (lambda:MyTopo())}