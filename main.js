const provider = new WalletConnectProvider({
    infuraId: "113308962c114124ba65dd93a5390a2e", // Required
  });
  
  //  Enable session (triggers QR Code modal)
  await provider.enable();
  
  //  Create Web3 instance
  const web3 = new Web3(provider);
  
  