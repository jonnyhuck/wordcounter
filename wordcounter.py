import sys, nltk, re, getopt
from nltk.stem import WordNetLemmatizer

###
# NB: Use 'zap gremlins' in text wrangler before running text through this software!
### 

###
# Extract all nouns, lemmatise, count and export to csv report and text file to make 
#  a word cloud in Wordle.
# @author jonnyhuck
### 
def getWordCloud(inputFile, quiet):


	if quiet == False:
		print "starting..."

	#get the data from a file
	file_path = inputFile
	f = open(file_path)
	text = f.read()



	if quiet == False:
		print "parsing text..."

	#split sentences & tokens
	sentences = nltk.tokenize.sent_tokenize(text)
	tokens = [nltk.tokenize.word_tokenize(s) for s in sentences]

	#part of speech tagging (weird recursive loop thing)
	pos_tagged_tokens = [nltk.pos_tag(t) for t in tokens]
	pos_tagged_tokens = [token for sent in pos_tagged_tokens for token in sent]

	#variable setup
	all_entity_chunks = []
	previous_pos = None
	current_entity_chunk = []

	#nouns? adjectives? other?
	tag = 'NN'



	if quiet == False:
		print "extracting nouns..."

	#loop through parts of speech
	for(token,pos) in pos_tagged_tokens:
		#extract nouns
		if pos == previous_pos and pos.startswith(tag):
			current_entity_chunk.append(token)
		elif pos.startswith(tag):
			if current_entity_chunk != []:
				all_entity_chunks.append((' '.join(current_entity_chunk),pos))
		
			current_entity_chunk = [token]
		
		#update previous pos
		previous_pos = pos
	
	
	
	if quiet == False:
		print "lemmatising..."

	# lemmatize words
	lemmatizer = WordNetLemmatizer()
	for i,(word,pos) in enumerate(all_entity_chunks):
	# 	try:
			# update the tuple
		all_entity_chunks[i] = (lemmatizer.lemmatize(word),pos)
	# 	except:	# if an exception is thrown it's probably a dodgy character - just skip
	# 		pass



	if quiet == False:
		print "counting word frequencies..."

	#count word frequency
	wc = {}
	for word in all_entity_chunks:
		#get word from the entity chunk tuple (& remove unwanted chars)
		stripped_word = re.sub(r'[^a-zA-Z0-9#@ ]', '', word[0])
		#lowercase
		stripped_word = stripped_word.lower()
		#if anything is left after removal of unwanted chars...
		if stripped_word != '':
			#create a dictionary entry
			wc.setdefault(stripped_word,0)
			#count it up
			wc[stripped_word]+=1



	if quiet == False:
		print "writing csv..."

	#write word counts into a csv
	try:
		#create a text file
		text_file = open("noun_counts.csv", "w")

		#loop through the resulting counts
		for c in wc: 
			#if >1 write into the file
			if wc[c] > 2:
				#print c + ", " + str(wc[c])
				text_file.write(c + "," + str(wc[c]) + "\n")

		#close the text file
		text_file.close()
	except:
		print "Whoops - can't get in the csv file!"
		sys.exit()



	if quiet == False:
		print "writing word cloud text..."

	#write word cloud text
	try:
		#create a text file
		text_file = open("word_cloud.txt", "w")

		#loop through the resulting counts
		for c in wc: 
			#if >1 write into the file
			if wc[c] > 2:
				#write the word as many times as it appeared
				j=1
				while j <= wc[c]:
					text_file.write(c + " ")
					j = j + 1

		#close the text file
		text_file.close()
	except:
		print "Whoops - can't get in the csv file!"
		sys.exit()
	
	if quiet == False:
		print""
		print "Done!"


##
# Main Function
# @author jonnyhuck
##
def main(argv):
   
    # test for arguments
	try:
		opts, args = getopt.getopt(argv, "hqi:")
	except getopt.GetoptError:
		print 'python wordcloud_generator.py -i path/to/input/file.txt'
		sys.exit()
	
	# flag for whether to run quietly
	quiet = False

	# read in all of the arguments
	for opt, arg in opts:
		if opt == '-h':
			print 'python wordcloud_generator.py -i path/to/input/file.txt'
			sys.exit()
		elif opt == '-i':
			inputFile = arg
		elif opt == '-q':
			quiet = True

	# verify inputs 	
	if inputFile != '':
		
		# create the centroids shapefile
		getWordCloud(inputFile, quiet)
		
	else:
		print 'python wordcloud_generator.py -i path/to/input/file.txt'

##
# Python nonsense...
# @author jonnyhuck
##
if __name__ == "__main__":
    main(sys.argv[1:])