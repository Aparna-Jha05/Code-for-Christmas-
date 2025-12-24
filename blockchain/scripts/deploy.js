const hre = require("hardhat");

async function main() {
  const TrustAirdrop = await hre.ethers.getContractFactory("TrustAirdrop");
  const contract = await TrustAirdrop.deploy();
  await contract.waitForDeployment();

  console.log("TrustAirdrop deployed to:", await contract.getAddress());
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
