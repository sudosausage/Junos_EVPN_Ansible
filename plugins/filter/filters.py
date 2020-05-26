class FilterModule:

# Static Method is used for Ansible
# This filter takes no paramaters and takes the Filter bgp_as_from_rt
    @staticmethod
    def filters():
        return {
            'bgp_as_from_rt': FilterModule.bgp_as_from_rt
        }

# We create a loop to loop over RTs and then split them in half at the :
# We will then only store the first half of the RD before the :
    @staticmethod
    def bgp_as_from_rt(rt_list):
        bgp_as_list = []
        for my_rt in rt_list:
            rt_halves = my_rt.split(':')
            bgp_as_list.append(int(rt_halves[0]))
        return: bgp_as_list
