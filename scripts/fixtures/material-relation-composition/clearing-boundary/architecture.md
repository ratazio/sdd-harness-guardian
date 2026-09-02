# Ledger admission boundary

The unregulated order service may prepare an instruction, but it cannot write
the regulated ledger. The clearing gateway is the sole boundary receiver. It
accepts an instruction only with an immutable order reference and a treasury
approval; otherwise it returns `refuse` to the order service. The treasury lead
owns the approval and the gateway receipt is the reconciliation proof.
