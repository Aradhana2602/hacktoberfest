# Python3 code to perform add,
# multiply and transpose on sparse matrices
class sparse_matrix :

	def __init__(self, r, c):
	
		# Maximum number of elements in matrix
		self.MAX = 100;
		
		# Array representation
		# of sparse matrix
		#[][0] represents row
		#[][1] represents col
		#[][2] represents value
		self.data = [None for _ in range(self.MAX)]
		for i in range(self.MAX):
			self.data[i] = [None for _ in range(3)]

		# dimensions of matrix
		self.row = r;
		self.col = c;

		# total number of elements in matrix
		self.len = 0;
	
	# insert elements into sparse matrix
	def insert(self, r, c, val):
	
		# invalid entry
		if (r > self.row or c > self.col) :
			print("Wrong entry");
		else :

			# insert row value
			self.data[self.len][0] = r;

			# insert col value
			self.data[self.len][1] = c;

			# insert element's value
			self.data[self.len][2] = val;

			# increment number of data in matrix
			self.len += 1;
		
	def add(self, b):

		# if matrices don't have same dimensions
		if (self.row != b.row or self.col != b.col) :
			print("Matrices can't be added");
		else:

			apos = 0;
			bpos = 0;
			result = sparse_matrix(self.row, self.col);

			while (apos < self.len and bpos < b.len):

				# if b's row and col is smaller
				if (self.data[apos][0] > b.data[bpos][0] or (self.data[apos][0] == b.data[bpos][0] and self.data[apos][1] > b.data[bpos][1])):

					# insert smaller value into result
					result.insert(b.data[bpos][0],
								b.data[bpos][1],
								b.data[bpos][2]);
					bpos += 1
				
				# if a's row and col is smaller
				elif (self.data[apos][0] < b.data[bpos][0] or (self.data[apos][0] == b.data[bpos][0] and self.data[apos][1] < b.data[bpos][1])):
					
					# insert smaller value into result
					result.insert(self.data[apos][0], self.data[apos][1], self.data[apos][2]);
					apos += 1;
			
				else:

					# add the values as row and col is same
					addedval = self.data[apos][2] + b.data[bpos][2];

					if (addedval != 0):
						result.insert(self.data[apos][0], self.data[apos][1], addedval);
					# then insert
					apos += 1;
					bpos += 1;
				
			# insert remaining elements
			while (apos < self.len):
				result.insert(self.data[apos][0],self.data[apos][1], self.data[apos][2]);
				apos += 1

			while (bpos < b.len):
				result.insert(b.data[bpos][0], b.data[bpos][1], b.data[bpos][2]);
				bpos += 1

			# print result
			result.print();
		
	def transpose(self):
	
		# new matrix with inversed row X col
		result = sparse_matrix(self.col, self.row);

		# same number of elements
		result.len = self.len;

		# to count number of elements in each column
		count = [None for _ in range(self.col + 1)];

		# initialize all to 0
		for i in range(1, 1 + self.col):
			count[i] = 0;

		for i in range(0, self.len):
			count[self.data[i][1]] += 1

		index = [None for _ in range(self.col + 1)]

		# to count number of elements having col smaller
		# than particular i

		# as there is no col with value < 1
		index[1] = 0;

		# initialize rest of the indices
		for i in range(2, 1 + self.col):
			index[i] = index[i - 1] + count[i - 1];

		for i in range(self.len): 

			# insert a data at rpos and increment its value
			rpos = index[self.data[i][1]]
			index[self.data[i][1]] += 1

			# transpose row=col
			result.data[rpos][0] = self.data[i][1];

			# transpose col=row
			result.data[rpos][1] = self.data[i][0];

			# same value
			result.data[rpos][2] = self.data[i][2];
		
		# the above method ensures
		# sorting of transpose matrix
		# according to row-col value
		return result;
	
	def multiply(self, b):
		if (self.col != b.row):

			# Invalid multiplication
			print("Can't multiply, Invalid dimensions");
			return;
		
		# transpose b to compare row
		# and col values and to add them at the end
		b = b.transpose();

		# result matrix of dimension row X b.col
		# however b has been transposed, hence row X b.row
		result = sparse_matrix(self.row, b.row);

		# iterate over all elements of A
		for apos in range(self.len): 

			# current row of result matrix
			r = self.data[apos][0];

			# iterate over all elements of B
			for bpos in range(b.len): 

				# current column of result matrix
				# data[][0] used as b is transposed
				c = b.data[bpos][0];

				# temporary pointers created to add all
				# multiplied values to obtain current
				# element of result matrix
				tempa = apos;
				tempb = bpos;
				sum = 0;

				# iterate over all elements with
				# same row and col value
				# to calculate result[r]
				while (tempa < self.len and self.data[tempa][0] == r and tempb < b.len and b.data[tempb][0] == c):

					if (self.data[tempa][1] < b.data[tempb][1]):

						# skip a
						tempa += 1

					elif (self.data[tempa][1] > b.data[tempb][1]):

						# skip b
						tempb += 1
					else:

						# same col, so multiply and
						# increment
						sum += self.data[tempa][2] * b.data[tempb][2];
						tempa += 1
						tempb += 1
				
				# insert sum obtained in result[r]
				# if its not equal to 0
				if (sum != 0):
					result.insert(r, c, sum);
				while (bpos < b.len and b.data[bpos][0] == c):

					# jump to next column
					bpos += 1
			
			while (apos < self.len and self.data[apos][0] == r):

				# jump to next row
				apos += 1
		
		result.print();
	
	# printing matrix
	def print(self):
		print("Dimension:", self.row, "x", self.col);
		print("Sparse Matrix: \nRow Column Value");
	
		for i in range(self.len): 
			print(self.data[i][0], self.data[i][1], self.data[i][2]);
		
# create two sparse matrices and insert values
a = sparse_matrix(4, 4);
b = sparse_matrix(4, 4);

a.insert(1, 2, 10);
a.insert(1, 4, 12);
a.insert(3, 3, 5);
a.insert(4, 1, 15);
a.insert(4, 2, 12);
b.insert(1, 3, 8);
b.insert(2, 4, 23);
b.insert(3, 3, 9);
b.insert(4, 1, 20);
b.insert(4, 2, 25);

# Output result
print("Addition: ");
a.add(b);
print("\nMultiplication: ");
a.multiply(b);
print("\nTranspose: ");
atranspose = a.transpose();
atranspose.print();

# This code is contributed by phasing17
