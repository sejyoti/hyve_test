# hyve_test
A simple command line program that does the required I/O and implements the described algorithms.

Description of the Decoding Algorithm


The decoding algorithm is an implementation of a (non-injective) function that
takes a sequence Cs back to its decoded form s.
Starting with an empty result bytestring, read the encoded pair sequence (with
length n) from the left (i = 0) to the right. For each pair read, if pi = 0, append
qi to the output stream. Otherwise, pi > 0. Read the last pi characters appended
to the result string and take the first (from the left) qi characters.
For example, the following sequence:
(0, 61), (1, 1), (0, 62), (3, 2), (3, 3) (2)
would result in the bytestring ✻✶ ✻✶ ✻✷ ✻✶ ✻✶ ✻✷ ✻✶ ✻✶ (represented here in
hexadecimal) through the sequence [✻✶], [✻✶ ✻✶], [✻✶ ✻✶ ✻✷], [✻✶ ✻✶ ✻✷ ✻✶ ✻✶] ((3, 2) means go back three characters, in this case to the first position, and take
the first two characters afterwards), and finally [✻✶ ✻✶ ✻✷ ✻✶ ✻✶ ✻✷ ✻✶ ✻✶].
The hexadecimal values ✻✶ and ✻✷ become the characters ❛ and ❜ when interpreted as text. So the final output, when converted from bytes to text, is the string
❛❛❜❛❛❜❛❛. However for the purposes of this assignment the conversion from bytes
to text is out of scope and irrelevant, we will effectively be dealing with binary
data only.
