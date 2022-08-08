
// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;
pragma experimental ABIEncoderV2;

contract SimpleStorage {
    
    uint256 favNo = 5;

    struct Person {
        string name;
        uint256 id;
    }
    function storeFavNo(uint256 _favNo) public {
        favNo = _favNo;
    }
    function getFavNo() public view returns (uint256) {
        return favNo;
    }
   
   Person[] public persons;
   uint256 count = 0;

   mapping(string=> uint256) public nameToFavNumber;

   function addPerson(string memory _name, uint256 _id) public returns(Person memory)  {
       persons.push(Person(_name, _id));
       return Person(_name, _id);
   }
   function calculate(uint256 _count) public pure {
       1 + _count;
   }

   function addPerson1(string memory _name, uint256 _id) public {
       persons.push(Person(_name, _id));
   }
   function seePersons() public view returns(Person[] memory){
       return persons;
   }
   function addMapping(string memory _name, uint256 _id) public{
       nameToFavNumber[_name] = _id;
   }
}