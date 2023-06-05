
class MovingAverage:

    def __init__(self, size):
        self.size = size
        self.vals = []
        self.counter = 0
        self.prefix_sum = []

    def next(self, val:int) ->float:

        self.vals.append(val)

        if self.counter==0:
            self.prefix_sum.append(val)
        else:
            self.prefix_sum.append(self.prefix_sum[-1]+val)

        # get counter

        if self.counter < self.size:
            output = self.prefix_sum[self.counter]/(self.counter+1)
            self.counter += 1
            return output


        output = (self.prefix_sum[self.counter]-self.prefix_sum[self.counter-self.size])/self.size
        self.counter += 1
        return output


test1 = MovingAverage(1)


print(test1.next(4))
print(test1.next(0))