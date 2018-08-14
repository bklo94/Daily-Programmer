CC = g++
CPP_Flags = -fopenmp -lm
rm	= rm -f

.PHONY: all clean remove .FORCE

default:
	$(CC) $(CPP_Flags) -O3 pcswap.cpp -o pcswap
	$(CC) $(CPP_Flags) -O3 pcswapRenaming.cpp -o pcswapRenaming
	$(CC) $(CPP_Flags) -O3 pcswapRenamingOpt.cpp -o pcswapRenamingOpt
	$(CC) $(CPP_Flags) -O3 cswap.cpp -o cswap
	$(CC) $(CPP_Flags) -O3 cswapRenaming.cpp -o cswapRenaming
	$(CC) $(CPP_Flags) -O3 cswapRenamingOpt.cpp -o cswapRenamingOpt

clean: remove
	@echo "Cleanup Complete!"

remove:
	$(rm) cswap cswapRenaming cswapRenamingOpt pcswap pcswapRenaming pcswapRenamingOpt
	$(rm) *.csv
