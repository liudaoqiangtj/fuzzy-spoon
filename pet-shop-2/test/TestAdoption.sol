pragma solidity ^0.4.20;
import 'truffle/Assert.sol';
import 'truffle/DeployedAddresses.sol';
import '../contracts/Adoption.sol';

contract TestAdoption {
    Adoption adoption = Adoption(DeployedAddresses.Adoption());
    function testUserCanAdoptPet() public {
        uint returnedId = adoption.adopt(8);
        Assert.equal(returnedId,8,"8 be recorede");
    }

    function testGetAdopterAddressByPetid() public {
        address adopter = adoption.adopters(8);
        Assert.equal(adopter,this,"address equal this");
    }

    function testGetAdopterAddressByPetIdInArray() public {
        address[16] memory adopters = adoption.getAdopters();
        Assert.equal(adopters[8], this,"equal");
    }
}