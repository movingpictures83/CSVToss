import PyPluMA

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

class CSVTossPlugin:
   def input(self, filename):
      self.txtfile = open(filename, 'r')
      self.parameters = dict()
      for line in self.txtfile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()
      if len(PyPluMA.prefix()) != 0:
         self.parameters['csvfile'] = PyPluMA.prefix() + "/" + self.parameters['csvfile']

   def run(self):
         self.newlines = []
         threshold = float(self.parameters['threshold'])
         csvfile = open(self.parameters['csvfile'], 'r')
         self.header = csvfile.readline().strip()

         self.my_mat = []
         for line in csvfile:
           line = line.strip()
           contents = line.split(',')
           self.my_mat.append(contents)

         self.m = len(self.my_mat)
         self.n = len(self.my_mat[0])
         self.to_remove = []
         #print(self.m)
         #print(self.n)
         for j in range(1, self.n):
            count = 0.0
            for i in range(self.m):
                #print("EXECUTE")
                if (is_number(self.my_mat[i][j]) and float(self.my_mat[i][j]) != 0):
                    count = count + 1
                #elif (not is_number(self.my_mat[i][j])):
                #    print("WARNING: NOT A NUMBER: "+self.my_mat[i][j])
                ##else:
                #    print(self.my_mat[i][j])
            if ((count/self.m) < threshold):
                #print("REMOVING: PRESENT IN "+str(count)+" OUT OF "+str(self.m))
                self.to_remove.append(j)
            #print(len(self.to_remove))

   def output(self, filename):
      filestuff2 = open(filename, 'w')
      #filestuff2.write(self.header+"\n")

      headercontents = self.header.strip().split(',')
      first = True
      for j in range(len(headercontents)):
          if (j not in self.to_remove):
            if (not first):
              filestuff2.write(',')
            filestuff2.write(headercontents[j])
            first = False
      filestuff2.write('\n')

      for i in range(len(self.my_mat)):
         first = True
         for j in range(len(self.my_mat[i])):
            if (j not in self.to_remove):
              if (not first):
                filestuff2.write(',')
              filestuff2.write(self.my_mat[i][j])
              first = False
         if (i != len(self.my_mat)-1):
             filestuff2.write('\n')



