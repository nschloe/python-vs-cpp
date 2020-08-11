default:
	@echo "make plots?"

plots:
	python3 plot.py dot-product-vectors/ -o dot-product-vectors.svg
	python3 plot.py dot-product-vectors/ -o dot-product-vectors-relative.svg -r
	#
	python3 plot.py matrix-matrix-products/ -o matrix-matrix-products.svg
	python3 plot.py matrix-matrix-products/ -o matrix-matrix-products-relative.svg -r
	#
	python3 plot.py sum -o sum.svg
	python3 plot.py sum -o sum-relative.svg -r
	#
	python3 plot.py sum -o sum-vectors.svg
	python3 plot.py sum -o sum-vectors-relative.svg -r

clean:
	rm -f *.svg
