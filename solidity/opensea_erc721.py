#
#  Panoramix v4 Oct 2019 
#  Decompiled source of 0x18Df6C571F6fE9283B87f910E41dc5c8b77b7da5
# 
#  Let's make the world open source 
# 
#
#  I failed with these: 
#  - withdrawAll()
#  - tokenURI(uint256 _tokenId)
#  - _fallback()
#  All the rest is below.
#

# 0x18df6c571f6fe9283b87f910e41dc5c8b77b7da5

def storage:
  stor0 is array of struct at storage 0
  stor1 is array of struct at storage 1
  ownerOf is mapping of addr at storage 2
  balanceOf is mapping of uint256 at storage 3
  approved is mapping of addr at storage 4
  stor5 is mapping of uint8 at storage 5
  tokenOfOwnerByIndex is mapping of uint256 at storage 6
  stor7 is mapping of uint256 at storage 7
  tokenByIndex is array of uint256 at storage 8
  stor9 is mapping of uint256 at storage 9
  owner is addr at storage 10
  stor11 is array of uint256 at storage 11
  stor12 is uint256 at storage 12
  price is uint256 at storage 13
  unknown16c61ccc is uint8 at storage 14

def getApproved(uint256 _tokenId): # not payable
  require calldata.size - 4 >=′ 32
  require _tokenId == _tokenId
  if not ownerOf[_tokenId]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: approved query for nonexistent token'
  return approved[_tokenId]

def unknown16c61ccc(): # not payable
  return bool(unknown16c61ccc)

def totalSupply(): # not payable
  return tokenByIndex.length

def tokenOfOwnerByIndex(address _owner, uint256 _index): # not payable
  require calldata.size - 4 >=′ 64
  require _owner == _owner
  require _index == _index
  if not _owner:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
  if _index >= balanceOf[addr(_owner)]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721Enumerable: owner index out of bounds'
  return tokenOfOwnerByIndex[addr(_owner)][_index]

def tokenByIndex(uint256 _index): # not payable
  require calldata.size - 4 >=′ 32
  require _index == _index
  if _index >= tokenByIndex.length:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721Enumerable: global index out of bounds'
  return tokenByIndex[_index]

def ownerOf(uint256 _tokenId): # not payable
  require calldata.size - 4 >=′ 32
  require _tokenId == _tokenId
  if not ownerOf[_tokenId]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
  return ownerOf[_tokenId]

def balanceOf(address _owner): # not payable
  require calldata.size - 4 >=′ 32
  require _owner == _owner
  if not _owner:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
  return balanceOf[addr(_owner)]

def owner(): # not payable
  return owner

def getPrice(): # not payable
  return price

def isApprovedForAll(address _owner, address _operator): # not payable
  require calldata.size - 4 >=′ 64
  require _owner == _owner
  require _operator == _operator
  return bool(stor5[addr(_owner)][addr(_operator)])

#
#  Regular functions
#

def renounceOwnership(): # not payable
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=0)
  owner = 0

def setPrice(uint256 _newPrice): # not payable
  require calldata.size - 4 >=′ 32
  require _newPrice == _newPrice
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  price = _newPrice

def pause(bool _paused): # not payable
  require calldata.size - 4 >=′ 32
  require _paused == _paused
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  unknown16c61ccc = uint8(_paused)

def transferOwnership(address _newOwner): # not payable
  require calldata.size - 4 >=′ 32
  require _newOwner == _newOwner
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  if not _newOwner:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'Ownable: new owner is the zero address'
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner

def setApprovalForAll(address _to, bool _approved): # not payable
  require calldata.size - 4 >=′ 64
  require _to == _to
  require _approved == _approved
  if _to == caller:
      revert with 0, 'ERC721: approve to caller'
  stor5[caller][addr(_to)] = uint8(_approved)
  log ApprovalForAll(
        address owner=_approved,
        address operator=caller,
        bool approved=_to)

def supportsInterface(bytes4 _interfaceId): # not payable
  require calldata.size - 4 >=′ 32
  require _interfaceId == Mask(32, 224, _interfaceId)
  if Mask(32, 224, _interfaceId) == 0x780e9d6300000000000000000000000000000000000000000000000000000000:
      return True
  if Mask(32, 224, _interfaceId) == 0x80ac58cd00000000000000000000000000000000000000000000000000000000:
      return True
  if Mask(32, 224, _interfaceId) == 0x5b5e139f00000000000000000000000000000000000000000000000000000000:
      return True
  return (Mask(32, 224, _interfaceId) == 0x1ffc9a700000000000000000000000000000000000000000000000000000000)

def approve(address _spender, uint256 _value): # not payable
  require calldata.size - 4 >=′ 64
  require _spender == _spender
  require _value == _value
  if not ownerOf[_value]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
  if _spender == ownerOf[_value]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: approval to current owner'
  if ownerOf[_value] != caller:
      if not stor5[stor2[_value]][caller]:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 
                      'ERC721: approve caller is not owner nor approved for all'
  approved[_value] = _spender
  if not ownerOf[_value]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
  log Approval(
        address owner=ownerOf[_value],
        address spender=_spender,
        uint256 value=_value)

def setBaseURI(string _baseURI): # not payable
  require calldata.size - 4 >=′ 32
  require _baseURI <= 18446744073709551615
  require _baseURI + 35 <′ calldata.size
  if _baseURI.length > 18446744073709551615:
      revert with 'NH{q', 65
  if ceil32(_baseURI.length) + 128 > 18446744073709551615 or ceil32(_baseURI.length) + 128 < 96:
      revert with 'NH{q', 65
  require _baseURI + _baseURI.length + 36 <= calldata.size
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  if bool(stor11.length):
      if bool(stor11.length) == stor11.length.field_1 < 32:
          revert with 'NH{q', 34
      if _baseURI.length:
          stor11[].field_0 = Array(len=_baseURI.length, data=_baseURI[all])
      else:
          stor11.length = 0
          idx = 0
          while stor11.length.field_1 + 31 / 32 > idx:
              stor11[idx].field_0 = 0
              idx = idx + 1
              continue 
  else:
      if bool(stor11.length) == stor11.length.field_1 < 32:
          revert with 'NH{q', 34
      if _baseURI.length:
          stor11[].field_0 = Array(len=_baseURI.length, data=_baseURI[all])
      else:
          stor11.length = 0
          idx = 0
          while stor11.length.field_1 + 31 / 32 > idx:
              stor11[idx].field_0 = 0
              idx = idx + 1
              continue 

def unknown438b6300(uint256 _param1): # not payable
  require calldata.size - 4 >=′ 32
  require _param1 == addr(_param1)
  if not addr(_param1):
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
  if balanceOf[addr(_param1)] > 18446744073709551615:
      revert with 'NH{q', 65
  if balanceOf[addr(_param1)]:
      mem[128 len 32 * balanceOf[addr(_param1)]] = call.data[calldata.size len 32 * balanceOf[addr(_param1)]]
  idx = 0
  while idx < balanceOf[addr(_param1)]:
      if not addr(_param1):
          revert with 0, 'ERC721: balance query for the zero address'
      if idx >= balanceOf[addr(_param1)]:
          revert with 0, 'ERC721Enumerable: owner index out of bounds'
      mem[0] = idx
      mem[32] = sha3(addr(_param1), 6)
      if idx >= balanceOf[addr(_param1)]:
          revert with 'NH{q', 50
      mem[(32 * idx) + 128] = tokenOfOwnerByIndex[addr(_param1)][idx]
      if idx == -1:
          revert with 'NH{q', 17
      idx = idx + 1
      continue 
  return Array(len=balanceOf[addr(_param1)], data=mem[128 len 32 * balanceOf[addr(_param1)]])

def name(): # not payable
  if bool(stor0.length):
      if bool(stor0.length) == stor0.length.field_1 < 32:
          revert with 'NH{q', 34
      if bool(stor0.length):
          if bool(stor0.length) == stor0.length.field_1 < 32:
              revert with 'NH{q', 34
          if stor0.length.field_1:
              if 31 < stor0.length.field_1:
                  mem[128] = uint256(stor0.field_0)
                  idx = 128
                  s = 0
                  while stor0.length.field_1 + 96 > idx:
                      mem[idx + 32] = stor0[s].field_256
                      idx = idx + 32
                      s = s + 1
                      continue 
                  return Array(len=2 * Mask(256, -1, stor0.length.field_1), data=mem[128 len ceil32(stor0.length.field_1)])
              mem[128] = 256 * stor0.length.field_8
      else:
          if bool(stor0.length) == stor0.length.field_1 < 32:
              revert with 'NH{q', 34
          if stor0.length.field_1:
              if 31 < stor0.length.field_1:
                  mem[128] = uint256(stor0.field_0)
                  idx = 128
                  s = 0
                  while stor0.length.field_1 + 96 > idx:
                      mem[idx + 32] = stor0[s].field_256
                      idx = idx + 32
                      s = s + 1
                      continue 
                  return Array(len=2 * Mask(256, -1, stor0.length.field_1), data=mem[128 len ceil32(stor0.length.field_1)])
              mem[128] = 256 * stor0.length.field_8
      mem[ceil32(stor0.length.field_1) + 192 len ceil32(stor0.length.field_1)] = mem[128 len ceil32(stor0.length.field_1)]
      if ceil32(stor0.length.field_1) > stor0.length.field_1:
          mem[ceil32(stor0.length.field_1) + stor0.length.field_1 + 192] = 0
      return Array(len=2 * Mask(256, -1, stor0.length.field_1), data=mem[128 len ceil32(stor0.length.field_1)], mem[(2 * ceil32(stor0.length.field_1)) + 192 len 2 * ceil32(stor0.length.field_1)]), 
  if bool(stor0.length) == stor0.length.field_1 < 32:
      revert with 'NH{q', 34
  if bool(stor0.length):
      if bool(stor0.length) == stor0.length.field_1 < 32:
          revert with 'NH{q', 34
      if stor0.length.field_1:
          if 31 < stor0.length.field_1:
              mem[128] = uint256(stor0.field_0)
              idx = 128
              s = 0
              while stor0.length.field_1 + 96 > idx:
                  mem[idx + 32] = stor0[s].field_256
                  idx = idx + 32
                  s = s + 1
                  continue 
              return Array(len=stor0.length % 128, data=mem[128 len ceil32(stor0.length.field_1)])
          mem[128] = 256 * stor0.length.field_8
  else:
      if bool(stor0.length) == stor0.length.field_1 < 32:
          revert with 'NH{q', 34
      if stor0.length.field_1:
          if 31 < stor0.length.field_1:
              mem[128] = uint256(stor0.field_0)
              idx = 128
              s = 0
              while stor0.length.field_1 + 96 > idx:
                  mem[idx + 32] = stor0[s].field_256
                  idx = idx + 32
                  s = s + 1
                  continue 
              return Array(len=stor0.length % 128, data=mem[128 len ceil32(stor0.length.field_1)])
          mem[128] = 256 * stor0.length.field_8
  mem[ceil32(stor0.length.field_1) + 192 len ceil32(stor0.length.field_1)] = mem[128 len ceil32(stor0.length.field_1)]
  if ceil32(stor0.length.field_1) > stor0.length.field_1:
      mem[ceil32(stor0.length.field_1) + stor0.length.field_1 + 192] = 0
  return Array(len=stor0.length % 128, data=mem[128 len ceil32(stor0.length.field_1)], mem[(2 * ceil32(stor0.length.field_1)) + 192 len 2 * ceil32(stor0.length.field_1)]), 

def symbol(): # not payable
  if bool(stor1.length):
      if bool(stor1.length) == stor1.length.field_1 < 32:
          revert with 'NH{q', 34
      if bool(stor1.length):
          if bool(stor1.length) == stor1.length.field_1 < 32:
              revert with 'NH{q', 34
          if stor1.length.field_1:
              if 31 < stor1.length.field_1:
                  mem[128] = uint256(stor1.field_0)
                  idx = 128
                  s = 0
                  while stor1.length.field_1 + 96 > idx:
                      mem[idx + 32] = stor1[s].field_256
                      idx = idx + 32
                      s = s + 1
                      continue 
                  return Array(len=2 * Mask(256, -1, stor1.length.field_1), data=mem[128 len ceil32(stor1.length.field_1)])
              mem[128] = 256 * stor1.length.field_8
      else:
          if bool(stor1.length) == stor1.length.field_1 < 32:
              revert with 'NH{q', 34
          if stor1.length.field_1:
              if 31 < stor1.length.field_1:
                  mem[128] = uint256(stor1.field_0)
                  idx = 128
                  s = 0
                  while stor1.length.field_1 + 96 > idx:
                      mem[idx + 32] = stor1[s].field_256
                      idx = idx + 32
                      s = s + 1
                      continue 
                  return Array(len=2 * Mask(256, -1, stor1.length.field_1), data=mem[128 len ceil32(stor1.length.field_1)])
              mem[128] = 256 * stor1.length.field_8
      mem[ceil32(stor1.length.field_1) + 192 len ceil32(stor1.length.field_1)] = mem[128 len ceil32(stor1.length.field_1)]
      if ceil32(stor1.length.field_1) > stor1.length.field_1:
          mem[ceil32(stor1.length.field_1) + stor1.length.field_1 + 192] = 0
      return Array(len=2 * Mask(256, -1, stor1.length.field_1), data=mem[128 len ceil32(stor1.length.field_1)], mem[(2 * ceil32(stor1.length.field_1)) + 192 len 2 * ceil32(stor1.length.field_1)]), 
  if bool(stor1.length) == stor1.length.field_1 < 32:
      revert with 'NH{q', 34
  if bool(stor1.length):
      if bool(stor1.length) == stor1.length.field_1 < 32:
          revert with 'NH{q', 34
      if stor1.length.field_1:
          if 31 < stor1.length.field_1:
              mem[128] = uint256(stor1.field_0)
              idx = 128
              s = 0
              while stor1.length.field_1 + 96 > idx:
                  mem[idx + 32] = stor1[s].field_256
                  idx = idx + 32
                  s = s + 1
                  continue 
              return Array(len=stor1.length % 128, data=mem[128 len ceil32(stor1.length.field_1)])
          mem[128] = 256 * stor1.length.field_8
  else:
      if bool(stor1.length) == stor1.length.field_1 < 32:
          revert with 'NH{q', 34
      if stor1.length.field_1:
          if 31 < stor1.length.field_1:
              mem[128] = uint256(stor1.field_0)
              idx = 128
              s = 0
              while stor1.length.field_1 + 96 > idx:
                  mem[idx + 32] = stor1[s].field_256
                  idx = idx + 32
                  s = s + 1
                  continue 
              return Array(len=stor1.length % 128, data=mem[128 len ceil32(stor1.length.field_1)])
          mem[128] = 256 * stor1.length.field_8
  mem[ceil32(stor1.length.field_1) + 192 len ceil32(stor1.length.field_1)] = mem[128 len ceil32(stor1.length.field_1)]
  if ceil32(stor1.length.field_1) > stor1.length.field_1:
      mem[ceil32(stor1.length.field_1) + stor1.length.field_1 + 192] = 0
  return Array(len=stor1.length % 128, data=mem[128 len ceil32(stor1.length.field_1)], mem[(2 * ceil32(stor1.length.field_1)) + 192 len 2 * ceil32(stor1.length.field_1)]), 

def mint(uint256 _wad) payable: 
  mem[64] = 96
  require calldata.size - 4 >=′ 32
  require _wad == _wad
  if unknown16c61ccc:
      revert with 0, 'Sale paused'
  if _wad >= 22:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'You can mint a maximum of 25 Animetas'
  if 10102 < stor12:
      revert with 'NH{q', 17
  if tokenByIndex.length > -_wad - 1:
      revert with 'NH{q', 17
  if tokenByIndex.length + _wad >= -stor12 + 10102:
      revert with 0, 'Exceeds maximum Animetas supply'
  if price and _wad > -1 / price:
      revert with 'NH{q', 17
  if call.value < price * _wad:
      revert with 0, 'Ether sent is not correct'
  idx = 0
  while idx < _wad:
      if tokenByIndex.length > -idx - 1:
          revert with 'NH{q', 17
      _97 = mem[64]
      mem[64] = mem[64] + 32
      mem[_97] = 0
      if not caller:
          revert with 0, 'ERC721: mint to the zero address'
      if ownerOf[stor8.length + idx]:
          revert with 0, 'ERC721: token already minted'
      stor9[stor8.length + idx] = tokenByIndex.length
      tokenByIndex.length++
      tokenByIndex[tokenByIndex.length] = tokenByIndex.length + idx
      if caller:
          tokenOfOwnerByIndex[caller][stor3[caller]] = tokenByIndex.length + idx
          stor7[stor8.length + idx] = balanceOf[caller]
          if balanceOf[caller] > -2:
              revert with 'NH{q', 17
          balanceOf[caller]++
          mem[0] = tokenByIndex.length + idx
          mem[32] = 2
          ownerOf[stor8.length + idx] = caller
          log Transfer(
                address from=0,
                address to=caller,
                uint256 value=tokenByIndex.length + idx)
          if ext_code.size(caller) > 0:
              mem[mem[64]] = 0x150b7a0200000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = caller
              mem[mem[64] + 36] = 0
              mem[mem[64] + 68] = tokenByIndex.length + idx
              mem[mem[64] + 100] = 128
              mem[mem[64] + 132] = 0
              s = 0
              while s < 0:
                  mem[mem[64] + s + 164] = mem[_97 + s + 32]
                  s = s + 32
                  continue 
              require ext_code.size(caller)
              call caller.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                   gas gas_remaining wei
                  args caller, 0, tokenByIndex.length + idx, 128, 0
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  if not return_data.size:
                      if not mem[96]:
                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                      revert with memory
                        from 128
                         len mem[96]
                  if not return_data.size:
                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                  revert with ext_call.return_data[0 len return_data.size]
              _191 = mem[64]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              require mem[_191] == Mask(32, 224, mem[_191])
              if Mask(32, 224, mem[_191]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
      else:
          if tokenByIndex.length < 1:
              revert with 'NH{q', 17
          if tokenByIndex.length - 1 >= tokenByIndex.length:
              revert with 'NH{q', 50
          if stor9[stor8.length + idx] >= tokenByIndex.length:
              revert with 'NH{q', 50
          tokenByIndex[stor9[tokenByIndex.length + idx]] = tokenByIndex[tokenByIndex.length]
          stor9[stor8[stor8.length]] = stor9[stor8.length + idx]
          stor9[stor8.length + idx] = 0
          if not tokenByIndex.length:
              revert with 'NH{q', 49
          tokenByIndex[tokenByIndex.length] = 0
          tokenByIndex.length--
          if balanceOf[caller] > -2:
              revert with 'NH{q', 17
          balanceOf[caller]++
          mem[0] = tokenByIndex.length + idx
          mem[32] = 2
          ownerOf[stor8.length + idx] = caller
          log Transfer(
                address from=0,
                address to=caller,
                uint256 value=tokenByIndex.length + idx)
          if ext_code.size(caller) > 0:
              mem[mem[64]] = 0x150b7a0200000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = caller
              mem[mem[64] + 36] = 0
              mem[mem[64] + 68] = tokenByIndex.length + idx
              mem[mem[64] + 100] = 128
              mem[mem[64] + 132] = 0
              s = 0
              while s < 0:
                  mem[mem[64] + s + 164] = mem[_97 + s + 32]
                  s = s + 32
                  continue 
              require ext_code.size(caller)
              call caller.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                   gas gas_remaining wei
                  args caller, 0, tokenByIndex.length + idx, 128, 0
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  if not return_data.size:
                      if not mem[96]:
                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                      revert with memory
                        from 128
                         len mem[96]
                  if not return_data.size:
                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                  revert with ext_call.return_data[0 len return_data.size]
              _192 = mem[64]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              require mem[_192] == Mask(32, 224, mem[_192])
              if Mask(32, 224, mem[_192]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
      if idx == -1:
          revert with 'NH{q', 17
      idx = idx + 1
      continue 

def unknownca800144(uint256 _param1, uint256 _param2) payable: 
  mem[64] = 96
  require not call.value
  require calldata.size - 4 >=′ 64
  require _param1 == addr(_param1)
  require _param2 == _param2
  if owner != caller:
      revert with 0, 'Ownable: caller is not the owner'
  if _param2 > stor12:
      revert with 0, 'Exceeds reserved Animetas supply'
  idx = 0
  while idx < _param2:
      if tokenByIndex.length > -idx - 1:
          revert with 'NH{q', 17
      _93 = mem[64]
      mem[64] = mem[64] + 32
      mem[_93] = 0
      if not addr(_param1):
          revert with 0, 'ERC721: mint to the zero address'
      if ownerOf[stor8.length + idx]:
          revert with 0, 'ERC721: token already minted'
      stor9[stor8.length + idx] = tokenByIndex.length
      tokenByIndex.length++
      tokenByIndex[tokenByIndex.length] = tokenByIndex.length + idx
      if addr(_param1):
          tokenOfOwnerByIndex[addr(_param1)][stor3[addr(_param1)]] = tokenByIndex.length + idx
          stor7[stor8.length + idx] = balanceOf[addr(_param1)]
          if balanceOf[addr(_param1)] > -2:
              revert with 'NH{q', 17
          balanceOf[addr(_param1)]++
          mem[0] = tokenByIndex.length + idx
          mem[32] = 2
          ownerOf[stor8.length + idx] = addr(_param1)
          log Transfer(
                address from=0,
                address to=addr(_param1),
                uint256 value=tokenByIndex.length + idx)
          if ext_code.size(addr(_param1)) > 0:
              mem[mem[64]] = 0x150b7a0200000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = caller
              mem[mem[64] + 36] = 0
              mem[mem[64] + 68] = tokenByIndex.length + idx
              mem[mem[64] + 100] = 128
              mem[mem[64] + 132] = 0
              s = 0
              while s < 0:
                  mem[mem[64] + s + 164] = mem[_93 + s + 32]
                  s = s + 32
                  continue 
              require ext_code.size(addr(_param1))
              call addr(_param1).onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                   gas gas_remaining wei
                  args caller, 0, tokenByIndex.length + idx, 128, 0
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  if not return_data.size:
                      if not mem[96]:
                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                      revert with memory
                        from 128
                         len mem[96]
                  if not return_data.size:
                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                  revert with ext_call.return_data[0 len return_data.size]
              _187 = mem[64]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              require mem[_187] == Mask(32, 224, mem[_187])
              if Mask(32, 224, mem[_187]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
      else:
          if tokenByIndex.length < 1:
              revert with 'NH{q', 17
          if tokenByIndex.length - 1 >= tokenByIndex.length:
              revert with 'NH{q', 50
          if stor9[stor8.length + idx] >= tokenByIndex.length:
              revert with 'NH{q', 50
          tokenByIndex[stor9[tokenByIndex.length + idx]] = tokenByIndex[tokenByIndex.length]
          stor9[stor8[stor8.length]] = stor9[stor8.length + idx]
          stor9[stor8.length + idx] = 0
          if not tokenByIndex.length:
              revert with 'NH{q', 49
          tokenByIndex[tokenByIndex.length] = 0
          tokenByIndex.length--
          if balanceOf[addr(_param1)] > -2:
              revert with 'NH{q', 17
          balanceOf[addr(_param1)]++
          mem[0] = tokenByIndex.length + idx
          mem[32] = 2
          ownerOf[stor8.length + idx] = addr(_param1)
          log Transfer(
                address from=0,
                address to=addr(_param1),
                uint256 value=tokenByIndex.length + idx)
          if ext_code.size(addr(_param1)) > 0:
              mem[mem[64]] = 0x150b7a0200000000000000000000000000000000000000000000000000000000
              mem[mem[64] + 4] = caller
              mem[mem[64] + 36] = 0
              mem[mem[64] + 68] = tokenByIndex.length + idx
              mem[mem[64] + 100] = 128
              mem[mem[64] + 132] = 0
              s = 0
              while s < 0:
                  mem[mem[64] + s + 164] = mem[_93 + s + 32]
                  s = s + 32
                  continue 
              require ext_code.size(addr(_param1))
              call addr(_param1).onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                   gas gas_remaining wei
                  args caller, 0, tokenByIndex.length + idx, 128, 0
              mem[mem[64]] = ext_call.return_data[0]
              if not ext_call.success:
                  if not return_data.size:
                      if not mem[96]:
                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                      revert with memory
                        from 128
                         len mem[96]
                  if not return_data.size:
                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                  revert with ext_call.return_data[0 len return_data.size]
              _188 = mem[64]
              mem[64] = mem[64] + ceil32(return_data.size)
              require return_data.size >=′ 32
              require mem[_188] == Mask(32, 224, mem[_188])
              if Mask(32, 224, mem[_188]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
      if idx == -1:
          revert with 'NH{q', 17
      idx = idx + 1
      continue 
  if stor12 < _param2:
      revert with 'NH{q', 17
  stor12 -= _param2

def transferFrom(address _from, address _to, uint256 _value): # not payable
  require calldata.size - 4 >=′ 96
  require _from == _from
  require _to == _to
  require _value == _value
  if not ownerOf[_value]:
      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: operator query for nonexistent token'
  else:
      if not ownerOf[_value]:
          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
      else:
          if caller == ownerOf[_value]:
              if not ownerOf[_value]:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
              else:
                  if ownerOf[_value] != _from:
                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: transfer of token that is not own'
                  else:
                      if not _to:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: transfer to the zero address'
                      else:
                          if _from:
                              if _from == _to:
                                  if _to:
                                      if _to == _from:
                                          approved[_value] = 0
                                          if not ownerOf[_value]:
                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                          else:
                                              log Approval(
                                                    address owner=ownerOf[_value],
                                                    address spender=0,
                                                    uint256 value=_value)
                                              if balanceOf[addr(_from)] < 1:
                                                  revert with 'NH{q', 17
                                              else:
                                                  balanceOf[addr(_from)]--
                                                  if balanceOf[addr(_to)] > -2:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      balanceOf[addr(_to)]++
                                                      ownerOf[_value] = _to
                                                      log Transfer(
                                                            address from=_from,
                                                            address to=_to,
                                                            uint256 value=_value)
                                                      stop
                                      else:
                                          if not _to:
                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                          else:
                                              tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _value
                                              stor7[_value] = balanceOf[addr(_to)]
                                              approved[_value] = 0
                                              if not ownerOf[_value]:
                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                              else:
                                                  log Approval(
                                                        address owner=ownerOf[_value],
                                                        address spender=0,
                                                        uint256 value=_value)
                                                  if balanceOf[addr(_from)] < 1:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      balanceOf[addr(_from)]--
                                                      if balanceOf[addr(_to)] > -2:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_to)]++
                                                          ownerOf[_value] = _to
                                                          log Transfer(
                                                                address from=_from,
                                                                address to=_to,
                                                                uint256 value=_value)
                                                          stop
                                  else:
                                      if tokenByIndex.length < 1:
                                          revert with 'NH{q', 17
                                      else:
                                          if tokenByIndex.length - 1 >= tokenByIndex.length:
                                              revert with 'NH{q', 50
                                          else:
                                              if stor9[_value] >= tokenByIndex.length:
                                                  revert with 'NH{q', 50
                                              else:
                                                  tokenByIndex[stor9[_value]] = tokenByIndex[tokenByIndex.length]
                                                  stor9[stor8[stor8.length]] = stor9[_value]
                                                  stor9[_value] = 0
                                                  if not tokenByIndex.length:
                                                      revert with 'NH{q', 49
                                                  else:
                                                      tokenByIndex[tokenByIndex.length] = 0
                                                      tokenByIndex.length--
                                                      approved[_value] = 0
                                                      if not ownerOf[_value]:
                                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                      else:
                                                          log Approval(
                                                                address owner=ownerOf[_value],
                                                                address spender=0,
                                                                uint256 value=_value)
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_from)]--
                                                              if balanceOf[addr(_to)] > -2:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_to)]++
                                                                  ownerOf[_value] = _to
                                                                  log Transfer(
                                                                        address from=_from,
                                                                        address to=_to,
                                                                        uint256 value=_value)
                                                                  stop
                              else:
                                  if not _from:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                  else:
                                      if balanceOf[addr(_from)] < 1:
                                          revert with 'NH{q', 17
                                      else:
                                          if stor7[_value] == balanceOf[addr(_from)] - 1:
                                              stor7[_value] = 0
                                              tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                              if _to:
                                                  if _to == _from:
                                                      approved[_value] = 0
                                                      if not ownerOf[_value]:
                                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                      else:
                                                          log Approval(
                                                                address owner=ownerOf[_value],
                                                                address spender=0,
                                                                uint256 value=_value)
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_from)]--
                                                              if balanceOf[addr(_to)] > -2:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_to)]++
                                                                  ownerOf[_value] = _to
                                                                  log Transfer(
                                                                        address from=_from,
                                                                        address to=_to,
                                                                        uint256 value=_value)
                                                                  stop
                                                  else:
                                                      if not _to:
                                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                                      else:
                                                          tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _value
                                                          stor7[_value] = balanceOf[addr(_to)]
                                                          approved[_value] = 0
                                                          if not ownerOf[_value]:
                                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                          else:
                                                              log Approval(
                                                                    address owner=ownerOf[_value],
                                                                    address spender=0,
                                                                    uint256 value=_value)
                                                              if balanceOf[addr(_from)] < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_from)]--
                                                                  if balanceOf[addr(_to)] > -2:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_to)]++
                                                                      ownerOf[_value] = _to
                                                                      log Transfer(
                                                                            address from=_from,
                                                                            address to=_to,
                                                                            uint256 value=_value)
                                                                      stop
                                              else:
                                                  if tokenByIndex.length < 1:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                          revert with 'NH{q', 50
                                                      else:
                                                          if stor9[_value] >= tokenByIndex.length:
                                                              revert with 'NH{q', 50
                                                          else:
                                                              tokenByIndex[stor9[_value]] = tokenByIndex[tokenByIndex.length]
                                                              stor9[stor8[stor8.length]] = stor9[_value]
                                                              stor9[_value] = 0
                                                              if not tokenByIndex.length:
                                                                  revert with 'NH{q', 49
                                                              else:
                                                                  tokenByIndex[tokenByIndex.length] = 0
                                                                  tokenByIndex.length--
                                                                  approved[_value] = 0
                                                                  if not ownerOf[_value]:
                                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_value],
                                                                            address spender=0,
                                                                            uint256 value=_value)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_value] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_value)
                                                                              stop
                                          else:
                                              tokenOfOwnerByIndex[addr(_from)][stor7[_value]] = tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1]
                                              stor7[stor6[addr(_from)][stor3[addr(_from)] - 1]] = stor7[_value]
                                              stor7[_value] = 0
                                              tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                              if _to:
                                                  if _to == _from:
                                                      approved[_value] = 0
                                                      if not ownerOf[_value]:
                                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                      else:
                                                          log Approval(
                                                                address owner=ownerOf[_value],
                                                                address spender=0,
                                                                uint256 value=_value)
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_from)]--
                                                              if balanceOf[addr(_to)] > -2:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_to)]++
                                                                  ownerOf[_value] = _to
                                                                  log Transfer(
                                                                        address from=_from,
                                                                        address to=_to,
                                                                        uint256 value=_value)
                                                                  stop
                                                  else:
                                                      if not _to:
                                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                                      else:
                                                          tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _value
                                                          stor7[_value] = balanceOf[addr(_to)]
                                                          approved[_value] = 0
                                                          if not ownerOf[_value]:
                                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                          else:
                                                              log Approval(
                                                                    address owner=ownerOf[_value],
                                                                    address spender=0,
                                                                    uint256 value=_value)
                                                              if balanceOf[addr(_from)] < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_from)]--
                                                                  if balanceOf[addr(_to)] > -2:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_to)]++
                                                                      ownerOf[_value] = _to
                                                                      log Transfer(
                                                                            address from=_from,
                                                                            address to=_to,
                                                                            uint256 value=_value)
                                                                      stop
                                              else:
                                                  if tokenByIndex.length < 1:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                          revert with 'NH{q', 50
                                                      else:
                                                          if stor9[_value] >= tokenByIndex.length:
                                                              revert with 'NH{q', 50
                                                          else:
                                                              tokenByIndex[stor9[_value]] = tokenByIndex[tokenByIndex.length]
                                                              stor9[stor8[stor8.length]] = stor9[_value]
                                                              stor9[_value] = 0
                                                              if not tokenByIndex.length:
                                                                  revert with 'NH{q', 49
                                                              else:
                                                                  tokenByIndex[tokenByIndex.length] = 0
                                                                  tokenByIndex.length--
                                                                  approved[_value] = 0
                                                                  if not ownerOf[_value]:
                                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_value],
                                                                            address spender=0,
                                                                            uint256 value=_value)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_value] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_value)
                                                                              stop
                          else:
                              stor9[_value] = tokenByIndex.length
                              tokenByIndex.length++
                              tokenByIndex[tokenByIndex.length] = _value
                              if _to:
                                  if _to == _from:
                                      approved[_value] = 0
                                      if not ownerOf[_value]:
                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                      else:
                                          log Approval(
                                                address owner=ownerOf[_value],
                                                address spender=0,
                                                uint256 value=_value)
                                          if balanceOf[addr(_from)] < 1:
                                              revert with 'NH{q', 17
                                          else:
                                              balanceOf[addr(_from)]--
                                              if balanceOf[addr(_to)] > -2:
                                                  revert with 'NH{q', 17
                                              else:
                                                  balanceOf[addr(_to)]++
                                                  ownerOf[_value] = _to
                                                  log Transfer(
                                                        address from=_from,
                                                        address to=_to,
                                                        uint256 value=_value)
                                                  stop
                                  else:
                                      if not _to:
                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                      else:
                                          tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _value
                                          stor7[_value] = balanceOf[addr(_to)]
                                          approved[_value] = 0
                                          if not ownerOf[_value]:
                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                          else:
                                              log Approval(
                                                    address owner=ownerOf[_value],
                                                    address spender=0,
                                                    uint256 value=_value)
                                              if balanceOf[addr(_from)] < 1:
                                                  revert with 'NH{q', 17
                                              else:
                                                  balanceOf[addr(_from)]--
                                                  if balanceOf[addr(_to)] > -2:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      balanceOf[addr(_to)]++
                                                      ownerOf[_value] = _to
                                                      log Transfer(
                                                            address from=_from,
                                                            address to=_to,
                                                            uint256 value=_value)
                                                      stop
                              else:
                                  if tokenByIndex.length < 1:
                                      revert with 'NH{q', 17
                                  else:
                                      if tokenByIndex.length - 1 >= tokenByIndex.length:
                                          revert with 'NH{q', 50
                                      else:
                                          if stor9[_value] >= tokenByIndex.length:
                                              revert with 'NH{q', 50
                                          else:
                                              tokenByIndex[stor9[_value]] = tokenByIndex[tokenByIndex.length]
                                              stor9[stor8[stor8.length]] = stor9[_value]
                                              stor9[_value] = 0
                                              if not tokenByIndex.length:
                                                  revert with 'NH{q', 49
                                              else:
                                                  tokenByIndex[tokenByIndex.length] = 0
                                                  tokenByIndex.length--
                                                  approved[_value] = 0
                                                  if not ownerOf[_value]:
                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                  else:
                                                      log Approval(
                                                            address owner=ownerOf[_value],
                                                            address spender=0,
                                                            uint256 value=_value)
                                                      if balanceOf[addr(_from)] < 1:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_from)]--
                                                          if balanceOf[addr(_to)] > -2:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_to)]++
                                                              ownerOf[_value] = _to
                                                              log Transfer(
                                                                    address from=_from,
                                                                    address to=_to,
                                                                    uint256 value=_value)
                                                              stop
          else:
              if not ownerOf[_value]:
                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: approved query for nonexistent token'
              else:
                  if approved[_value] == caller:
                      if not ownerOf[_value]:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                      else:
                          if ownerOf[_value] != _from:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: transfer of token that is not own'
                          else:
                              if not _to:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: transfer to the zero address'
                              else:
                                  if _from:
                                      if _from == _to:
                                          if _to:
                                              if _to == _from:
                                                  approved[_value] = 0
                                                  if not ownerOf[_value]:
                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                  else:
                                                      log Approval(
                                                            address owner=ownerOf[_value],
                                                            address spender=0,
                                                            uint256 value=_value)
                                                      if balanceOf[addr(_from)] < 1:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_from)]--
                                                          if balanceOf[addr(_to)] > -2:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_to)]++
                                                              ownerOf[_value] = _to
                                                              log Transfer(
                                                                    address from=_from,
                                                                    address to=_to,
                                                                    uint256 value=_value)
                                                              stop
                                              else:
                                                  if not _to:
                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                                  else:
                                                      tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _value
                                                      stor7[_value] = balanceOf[addr(_to)]
                                                      approved[_value] = 0
                                                      if not ownerOf[_value]:
                                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                      else:
                                                          log Approval(
                                                                address owner=ownerOf[_value],
                                                                address spender=0,
                                                                uint256 value=_value)
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_from)]--
                                                              if balanceOf[addr(_to)] > -2:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_to)]++
                                                                  ownerOf[_value] = _to
                                                                  log Transfer(
                                                                        address from=_from,
                                                                        address to=_to,
                                                                        uint256 value=_value)
                                                                  stop
                                          else:
                                              if tokenByIndex.length < 1:
                                                  revert with 'NH{q', 17
                                              else:
                                                  if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                      revert with 'NH{q', 50
                                                  else:
                                                      if stor9[_value] >= tokenByIndex.length:
                                                          revert with 'NH{q', 50
                                                      else:
                                                          tokenByIndex[stor9[_value]] = tokenByIndex[tokenByIndex.length]
                                                          stor9[stor8[stor8.length]] = stor9[_value]
                                                          stor9[_value] = 0
                                                          if not tokenByIndex.length:
                                                              revert with 'NH{q', 49
                                                          else:
                                                              tokenByIndex[tokenByIndex.length] = 0
                                                              tokenByIndex.length--
                                                              approved[_value] = 0
                                                              if not ownerOf[_value]:
                                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                              else:
                                                                  log Approval(
                                                                        address owner=ownerOf[_value],
                                                                        address spender=0,
                                                                        uint256 value=_value)
                                                                  if balanceOf[addr(_from)] < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_from)]--
                                                                      if balanceOf[addr(_to)] > -2:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_to)]++
                                                                          ownerOf[_value] = _to
                                                                          log Transfer(
                                                                                address from=_from,
                                                                                address to=_to,
                                                                                uint256 value=_value)
                                                                          stop
                                      else:
                                          if not _from:
                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                          else:
                                              if balanceOf[addr(_from)] < 1:
                                                  revert with 'NH{q', 17
                                              else:
                                                  if stor7[_value] == balanceOf[addr(_from)] - 1:
                                                      stor7[_value] = 0
                                                      tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                                      if _to:
                                                          if _to == _from:
                                                              approved[_value] = 0
                                                              if not ownerOf[_value]:
                                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                              else:
                                                                  log Approval(
                                                                        address owner=ownerOf[_value],
                                                                        address spender=0,
                                                                        uint256 value=_value)
                                                                  if balanceOf[addr(_from)] < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_from)]--
                                                                      if balanceOf[addr(_to)] > -2:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_to)]++
                                                                          ownerOf[_value] = _to
                                                                          log Transfer(
                                                                                address from=_from,
                                                                                address to=_to,
                                                                                uint256 value=_value)
                                                                          stop
                                                          else:
                                                              if not _to:
                                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                                              else:
                                                                  tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _value
                                                                  stor7[_value] = balanceOf[addr(_to)]
                                                                  approved[_value] = 0
                                                                  if not ownerOf[_value]:
                                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_value],
                                                                            address spender=0,
                                                                            uint256 value=_value)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_value] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_value)
                                                                              stop
                                                      else:
                                                          if tokenByIndex.length < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                  revert with 'NH{q', 50
                                                              else:
                                                                  if stor9[_value] >= tokenByIndex.length:
                                                                      revert with 'NH{q', 50
                                                                  else:
                                                                      tokenByIndex[stor9[_value]] = tokenByIndex[tokenByIndex.length]
                                                                      stor9[stor8[stor8.length]] = stor9[_value]
                                                                      stor9[_value] = 0
                                                                      if not tokenByIndex.length:
                                                                          revert with 'NH{q', 49
                                                                      else:
                                                                          tokenByIndex[tokenByIndex.length] = 0
                                                                          tokenByIndex.length--
                                                                          approved[_value] = 0
                                                                          if not ownerOf[_value]:
                                                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                                          else:
                                                                              log Approval(
                                                                                    address owner=ownerOf[_value],
                                                                                    address spender=0,
                                                                                    uint256 value=_value)
                                                                              if balanceOf[addr(_from)] < 1:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_from)]--
                                                                                  if balanceOf[addr(_to)] > -2:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_to)]++
                                                                                      ownerOf[_value] = _to
                                                                                      log Transfer(
                                                                                            address from=_from,
                                                                                            address to=_to,
                                                                                            uint256 value=_value)
                                                                                      stop
                                                  else:
                                                      tokenOfOwnerByIndex[addr(_from)][stor7[_value]] = tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1]
                                                      stor7[stor6[addr(_from)][stor3[addr(_from)] - 1]] = stor7[_value]
                                                      stor7[_value] = 0
                                                      tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                                      if _to:
                                                          if _to == _from:
                                                              approved[_value] = 0
                                                              if not ownerOf[_value]:
                                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                              else:
                                                                  log Approval(
                                                                        address owner=ownerOf[_value],
                                                                        address spender=0,
                                                                        uint256 value=_value)
                                                                  if balanceOf[addr(_from)] < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_from)]--
                                                                      if balanceOf[addr(_to)] > -2:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_to)]++
                                                                          ownerOf[_value] = _to
                                                                          log Transfer(
                                                                                address from=_from,
                                                                                address to=_to,
                                                                                uint256 value=_value)
                                                                          stop
                                                          else:
                                                              if not _to:
                                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                                              else:
                                                                  tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _value
                                                                  stor7[_value] = balanceOf[addr(_to)]
                                                                  approved[_value] = 0
                                                                  if not ownerOf[_value]:
                                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_value],
                                                                            address spender=0,
                                                                            uint256 value=_value)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_value] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_value)
                                                                              stop
                                                      else:
                                                          if tokenByIndex.length < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                  revert with 'NH{q', 50
                                                              else:
                                                                  if stor9[_value] >= tokenByIndex.length:
                                                                      revert with 'NH{q', 50
                                                                  else:
                                                                      tokenByIndex[stor9[_value]] = tokenByIndex[tokenByIndex.length]
                                                                      stor9[stor8[stor8.length]] = stor9[_value]
                                                                      stor9[_value] = 0
                                                                      if not tokenByIndex.length:
                                                                          revert with 'NH{q', 49
                                                                      else:
                                                                          tokenByIndex[tokenByIndex.length] = 0
                                                                          tokenByIndex.length--
                                                                          approved[_value] = 0
                                                                          if not ownerOf[_value]:
                                                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                                          else:
                                                                              log Approval(
                                                                                    address owner=ownerOf[_value],
                                                                                    address spender=0,
                                                                                    uint256 value=_value)
                                                                              if balanceOf[addr(_from)] < 1:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_from)]--
                                                                                  if balanceOf[addr(_to)] > -2:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_to)]++
                                                                                      ownerOf[_value] = _to
                                                                                      log Transfer(
                                                                                            address from=_from,
                                                                                            address to=_to,
                                                                                            uint256 value=_value)
                                                                                      stop
                                  else:
                                      stor9[_value] = tokenByIndex.length
                                      tokenByIndex.length++
                                      tokenByIndex[tokenByIndex.length] = _value
                                      if _to:
                                          if _to == _from:
                                              approved[_value] = 0
                                              if not ownerOf[_value]:
                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                              else:
                                                  log Approval(
                                                        address owner=ownerOf[_value],
                                                        address spender=0,
                                                        uint256 value=_value)
                                                  if balanceOf[addr(_from)] < 1:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      balanceOf[addr(_from)]--
                                                      if balanceOf[addr(_to)] > -2:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_to)]++
                                                          ownerOf[_value] = _to
                                                          log Transfer(
                                                                address from=_from,
                                                                address to=_to,
                                                                uint256 value=_value)
                                                          stop
                                          else:
                                              if not _to:
                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                              else:
                                                  tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _value
                                                  stor7[_value] = balanceOf[addr(_to)]
                                                  approved[_value] = 0
                                                  if not ownerOf[_value]:
                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                  else:
                                                      log Approval(
                                                            address owner=ownerOf[_value],
                                                            address spender=0,
                                                            uint256 value=_value)
                                                      if balanceOf[addr(_from)] < 1:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_from)]--
                                                          if balanceOf[addr(_to)] > -2:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_to)]++
                                                              ownerOf[_value] = _to
                                                              log Transfer(
                                                                    address from=_from,
                                                                    address to=_to,
                                                                    uint256 value=_value)
                                                              stop
                                      else:
                                          if tokenByIndex.length < 1:
                                              revert with 'NH{q', 17
                                          else:
                                              if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                  revert with 'NH{q', 50
                                              else:
                                                  if stor9[_value] >= tokenByIndex.length:
                                                      revert with 'NH{q', 50
                                                  else:
                                                      tokenByIndex[stor9[_value]] = tokenByIndex[tokenByIndex.length]
                                                      stor9[stor8[stor8.length]] = stor9[_value]
                                                      stor9[_value] = 0
                                                      if not tokenByIndex.length:
                                                          revert with 'NH{q', 49
                                                      else:
                                                          tokenByIndex[tokenByIndex.length] = 0
                                                          tokenByIndex.length--
                                                          approved[_value] = 0
                                                          if not ownerOf[_value]:
                                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                          else:
                                                              log Approval(
                                                                    address owner=ownerOf[_value],
                                                                    address spender=0,
                                                                    uint256 value=_value)
                                                              if balanceOf[addr(_from)] < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_from)]--
                                                                  if balanceOf[addr(_to)] > -2:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_to)]++
                                                                      ownerOf[_value] = _to
                                                                      log Transfer(
                                                                            address from=_from,
                                                                            address to=_to,
                                                                            uint256 value=_value)
                                                                      stop
                  else:
                      if not stor5[stor2[_value]][caller]:
                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: transfer caller is not owner nor approved'
                      else:
                          if not ownerOf[_value]:
                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                          else:
                              if ownerOf[_value] != _from:
                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: transfer of token that is not own'
                              else:
                                  if not _to:
                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: transfer to the zero address'
                                  else:
                                      if _from:
                                          if _from == _to:
                                              if _to:
                                                  if _to == _from:
                                                      approved[_value] = 0
                                                      if not ownerOf[_value]:
                                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                      else:
                                                          log Approval(
                                                                address owner=ownerOf[_value],
                                                                address spender=0,
                                                                uint256 value=_value)
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_from)]--
                                                              if balanceOf[addr(_to)] > -2:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_to)]++
                                                                  ownerOf[_value] = _to
                                                                  log Transfer(
                                                                        address from=_from,
                                                                        address to=_to,
                                                                        uint256 value=_value)
                                                                  stop
                                                  else:
                                                      if not _to:
                                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                                      else:
                                                          tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _value
                                                          stor7[_value] = balanceOf[addr(_to)]
                                                          approved[_value] = 0
                                                          if not ownerOf[_value]:
                                                              revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                          else:
                                                              log Approval(
                                                                    address owner=ownerOf[_value],
                                                                    address spender=0,
                                                                    uint256 value=_value)
                                                              if balanceOf[addr(_from)] < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_from)]--
                                                                  if balanceOf[addr(_to)] > -2:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_to)]++
                                                                      ownerOf[_value] = _to
                                                                      log Transfer(
                                                                            address from=_from,
                                                                            address to=_to,
                                                                            uint256 value=_value)
                                                                      stop
                                              else:
                                                  if tokenByIndex.length < 1:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                          revert with 'NH{q', 50
                                                      else:
                                                          if stor9[_value] >= tokenByIndex.length:
                                                              revert with 'NH{q', 50
                                                          else:
                                                              tokenByIndex[stor9[_value]] = tokenByIndex[tokenByIndex.length]
                                                              stor9[stor8[stor8.length]] = stor9[_value]
                                                              stor9[_value] = 0
                                                              if not tokenByIndex.length:
                                                                  revert with 'NH{q', 49
                                                              else:
                                                                  tokenByIndex[tokenByIndex.length] = 0
                                                                  tokenByIndex.length--
                                                                  approved[_value] = 0
                                                                  if not ownerOf[_value]:
                                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_value],
                                                                            address spender=0,
                                                                            uint256 value=_value)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_value] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_value)
                                                                              stop
                                          else:
                                              if not _from:
                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                              else:
                                                  if balanceOf[addr(_from)] < 1:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      if stor7[_value] == balanceOf[addr(_from)] - 1:
                                                          stor7[_value] = 0
                                                          tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                                          if _to:
                                                              if _to == _from:
                                                                  approved[_value] = 0
                                                                  if not ownerOf[_value]:
                                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_value],
                                                                            address spender=0,
                                                                            uint256 value=_value)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_value] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_value)
                                                                              stop
                                                              else:
                                                                  if not _to:
                                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                                                  else:
                                                                      tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _value
                                                                      stor7[_value] = balanceOf[addr(_to)]
                                                                      approved[_value] = 0
                                                                      if not ownerOf[_value]:
                                                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                                      else:
                                                                          log Approval(
                                                                                address owner=ownerOf[_value],
                                                                                address spender=0,
                                                                                uint256 value=_value)
                                                                          if balanceOf[addr(_from)] < 1:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_from)]--
                                                                              if balanceOf[addr(_to)] > -2:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_to)]++
                                                                                  ownerOf[_value] = _to
                                                                                  log Transfer(
                                                                                        address from=_from,
                                                                                        address to=_to,
                                                                                        uint256 value=_value)
                                                                                  stop
                                                          else:
                                                              if tokenByIndex.length < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                      revert with 'NH{q', 50
                                                                  else:
                                                                      if stor9[_value] >= tokenByIndex.length:
                                                                          revert with 'NH{q', 50
                                                                      else:
                                                                          tokenByIndex[stor9[_value]] = tokenByIndex[tokenByIndex.length]
                                                                          stor9[stor8[stor8.length]] = stor9[_value]
                                                                          stor9[_value] = 0
                                                                          if not tokenByIndex.length:
                                                                              revert with 'NH{q', 49
                                                                          else:
                                                                              tokenByIndex[tokenByIndex.length] = 0
                                                                              tokenByIndex.length--
                                                                              approved[_value] = 0
                                                                              if not ownerOf[_value]:
                                                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                                              else:
                                                                                  log Approval(
                                                                                        address owner=ownerOf[_value],
                                                                                        address spender=0,
                                                                                        uint256 value=_value)
                                                                                  if balanceOf[addr(_from)] < 1:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_from)]--
                                                                                      if balanceOf[addr(_to)] > -2:
                                                                                          revert with 'NH{q', 17
                                                                                      else:
                                                                                          balanceOf[addr(_to)]++
                                                                                          ownerOf[_value] = _to
                                                                                          log Transfer(
                                                                                                address from=_from,
                                                                                                address to=_to,
                                                                                                uint256 value=_value)
                                                                                          stop
                                                      else:
                                                          tokenOfOwnerByIndex[addr(_from)][stor7[_value]] = tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1]
                                                          stor7[stor6[addr(_from)][stor3[addr(_from)] - 1]] = stor7[_value]
                                                          stor7[_value] = 0
                                                          tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                                          if _to:
                                                              if _to == _from:
                                                                  approved[_value] = 0
                                                                  if not ownerOf[_value]:
                                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_value],
                                                                            address spender=0,
                                                                            uint256 value=_value)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_value] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_value)
                                                                              stop
                                                              else:
                                                                  if not _to:
                                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                                                  else:
                                                                      tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _value
                                                                      stor7[_value] = balanceOf[addr(_to)]
                                                                      approved[_value] = 0
                                                                      if not ownerOf[_value]:
                                                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                                      else:
                                                                          log Approval(
                                                                                address owner=ownerOf[_value],
                                                                                address spender=0,
                                                                                uint256 value=_value)
                                                                          if balanceOf[addr(_from)] < 1:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_from)]--
                                                                              if balanceOf[addr(_to)] > -2:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_to)]++
                                                                                  ownerOf[_value] = _to
                                                                                  log Transfer(
                                                                                        address from=_from,
                                                                                        address to=_to,
                                                                                        uint256 value=_value)
                                                                                  stop
                                                          else:
                                                              if tokenByIndex.length < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                      revert with 'NH{q', 50
                                                                  else:
                                                                      if stor9[_value] >= tokenByIndex.length:
                                                                          revert with 'NH{q', 50
                                                                      else:
                                                                          tokenByIndex[stor9[_value]] = tokenByIndex[tokenByIndex.length]
                                                                          stor9[stor8[stor8.length]] = stor9[_value]
                                                                          stor9[_value] = 0
                                                                          if not tokenByIndex.length:
                                                                              revert with 'NH{q', 49
                                                                          else:
                                                                              tokenByIndex[tokenByIndex.length] = 0
                                                                              tokenByIndex.length--
                                                                              approved[_value] = 0
                                                                              if not ownerOf[_value]:
                                                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                                              else:
                                                                                  log Approval(
                                                                                        address owner=ownerOf[_value],
                                                                                        address spender=0,
                                                                                        uint256 value=_value)
                                                                                  if balanceOf[addr(_from)] < 1:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_from)]--
                                                                                      if balanceOf[addr(_to)] > -2:
                                                                                          revert with 'NH{q', 17
                                                                                      else:
                                                                                          balanceOf[addr(_to)]++
                                                                                          ownerOf[_value] = _to
                                                                                          log Transfer(
                                                                                                address from=_from,
                                                                                                address to=_to,
                                                                                                uint256 value=_value)
                                                                                          stop
                                      else:
                                          stor9[_value] = tokenByIndex.length
                                          tokenByIndex.length++
                                          tokenByIndex[tokenByIndex.length] = _value
                                          if _to:
                                              if _to == _from:
                                                  approved[_value] = 0
                                                  if not ownerOf[_value]:
                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                  else:
                                                      log Approval(
                                                            address owner=ownerOf[_value],
                                                            address spender=0,
                                                            uint256 value=_value)
                                                      if balanceOf[addr(_from)] < 1:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_from)]--
                                                          if balanceOf[addr(_to)] > -2:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_to)]++
                                                              ownerOf[_value] = _to
                                                              log Transfer(
                                                                    address from=_from,
                                                                    address to=_to,
                                                                    uint256 value=_value)
                                                              stop
                                              else:
                                                  if not _to:
                                                      revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: balance query for the zero address'
                                                  else:
                                                      tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _value
                                                      stor7[_value] = balanceOf[addr(_to)]
                                                      approved[_value] = 0
                                                      if not ownerOf[_value]:
                                                          revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                      else:
                                                          log Approval(
                                                                address owner=ownerOf[_value],
                                                                address spender=0,
                                                                uint256 value=_value)
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_from)]--
                                                              if balanceOf[addr(_to)] > -2:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_to)]++
                                                                  ownerOf[_value] = _to
                                                                  log Transfer(
                                                                        address from=_from,
                                                                        address to=_to,
                                                                        uint256 value=_value)
                                                                  stop
                                          else:
                                              if tokenByIndex.length < 1:
                                                  revert with 'NH{q', 17
                                              else:
                                                  if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                      revert with 'NH{q', 50
                                                  else:
                                                      if stor9[_value] >= tokenByIndex.length:
                                                          revert with 'NH{q', 50
                                                      else:
                                                          tokenByIndex[stor9[_value]] = tokenByIndex[tokenByIndex.length]
                                                          stor9[stor8[stor8.length]] = stor9[_value]
                                                          stor9[_value] = 0
                                                          if not tokenByIndex.length:
                                                              revert with 'NH{q', 49
                                                          else:
                                                              tokenByIndex[tokenByIndex.length] = 0
                                                              tokenByIndex.length--
                                                              approved[_value] = 0
                                                              if not ownerOf[_value]:
                                                                  revert with 0x8c379a000000000000000000000000000000000000000000000000000000000, 'ERC721: owner query for nonexistent token'
                                                              else:
                                                                  log Approval(
                                                                        address owner=ownerOf[_value],
                                                                        address spender=0,
                                                                        uint256 value=_value)
                                                                  if balanceOf[addr(_from)] < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_from)]--
                                                                      if balanceOf[addr(_to)] > -2:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_to)]++
                                                                          ownerOf[_value] = _to
                                                                          log Transfer(
                                                                                address from=_from,
                                                                                address to=_to,
                                                                                uint256 value=_value)
                                                                          stop

def safeTransferFrom(address _from, address _to, uint256 _tokenId): # not payable
  require calldata.size - 4 >=′ 96
  require _from == _from
  require _to == _to
  require _tokenId == _tokenId
  if not ownerOf[_tokenId]:
      revert with 0, 'ERC721: operator query for nonexistent token'
  else:
      if not ownerOf[_tokenId]:
          revert with 0, 'ERC721: owner query for nonexistent token'
      else:
          if caller == ownerOf[_tokenId]:
              if not ownerOf[_tokenId]:
                  revert with 0, 'ERC721: owner query for nonexistent token'
              else:
                  if ownerOf[_tokenId] != _from:
                      revert with 0, 'ERC721: transfer of token that is not own'
                  else:
                      if not _to:
                          revert with 0, 'ERC721: transfer to the zero address'
                      else:
                          if _from:
                              if _from == _to:
                                  if _to:
                                      if _to == _from:
                                          approved[_tokenId] = 0
                                          if not ownerOf[_tokenId]:
                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                          else:
                                              log Approval(
                                                    address owner=ownerOf[_tokenId],
                                                    address spender=0,
                                                    uint256 value=_tokenId)
                                              if balanceOf[addr(_from)] < 1:
                                                  revert with 'NH{q', 17
                                              else:
                                                  balanceOf[addr(_from)]--
                                                  if balanceOf[addr(_to)] > -2:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      balanceOf[addr(_to)]++
                                                      ownerOf[_tokenId] = _to
                                                      log Transfer(
                                                            address from=_from,
                                                            address to=_to,
                                                            uint256 value=_tokenId)
                                                      if ext_code.size(_to) <= 0:
                                                          stop
                                                      else:
                                                          require ext_code.size(_to)
                                                          call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                               gas gas_remaining wei
                                                              args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                          if not ext_call.success:
                                                              if not return_data.size:
                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                              else:
                                                                  if not return_data.size:
                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                  else:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                          else:
                                                              require return_data.size >=′ 32
                                                              require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                              if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                              else:
                                                                  stop
                                      else:
                                          if not _to:
                                              revert with 0, 'ERC721: balance query for the zero address'
                                          else:
                                              tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                              stor7[_tokenId] = balanceOf[addr(_to)]
                                              approved[_tokenId] = 0
                                              if not ownerOf[_tokenId]:
                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                              else:
                                                  log Approval(
                                                        address owner=ownerOf[_tokenId],
                                                        address spender=0,
                                                        uint256 value=_tokenId)
                                                  if balanceOf[addr(_from)] < 1:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      balanceOf[addr(_from)]--
                                                      if balanceOf[addr(_to)] > -2:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_to)]++
                                                          ownerOf[_tokenId] = _to
                                                          log Transfer(
                                                                address from=_from,
                                                                address to=_to,
                                                                uint256 value=_tokenId)
                                                          if ext_code.size(_to) <= 0:
                                                              stop
                                                          else:
                                                              require ext_code.size(_to)
                                                              call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                   gas gas_remaining wei
                                                                  args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                              if not ext_call.success:
                                                                  if not return_data.size:
                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                  else:
                                                                      if not return_data.size:
                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                      else:
                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                              else:
                                                                  require return_data.size >=′ 32
                                                                  require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                  if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                  else:
                                                                      stop
                                  else:
                                      if tokenByIndex.length < 1:
                                          revert with 'NH{q', 17
                                      else:
                                          if tokenByIndex.length - 1 >= tokenByIndex.length:
                                              revert with 'NH{q', 50
                                          else:
                                              if stor9[_tokenId] >= tokenByIndex.length:
                                                  revert with 'NH{q', 50
                                              else:
                                                  tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                  stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                  stor9[_tokenId] = 0
                                                  if not tokenByIndex.length:
                                                      revert with 'NH{q', 49
                                                  else:
                                                      tokenByIndex[tokenByIndex.length] = 0
                                                      tokenByIndex.length--
                                                      approved[_tokenId] = 0
                                                      if not ownerOf[_tokenId]:
                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                      else:
                                                          log Approval(
                                                                address owner=ownerOf[_tokenId],
                                                                address spender=0,
                                                                uint256 value=_tokenId)
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_from)]--
                                                              if balanceOf[addr(_to)] > -2:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_to)]++
                                                                  ownerOf[_tokenId] = _to
                                                                  log Transfer(
                                                                        address from=_from,
                                                                        address to=_to,
                                                                        uint256 value=_tokenId)
                                                                  if ext_code.size(_to) <= 0:
                                                                      stop
                                                                  else:
                                                                      require ext_code.size(_to)
                                                                      call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                           gas gas_remaining wei
                                                                          args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                      if not ext_call.success:
                                                                          if not return_data.size:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              if not return_data.size:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          require return_data.size >=′ 32
                                                                          require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                          if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              stop
                              else:
                                  if not _from:
                                      revert with 0, 'ERC721: balance query for the zero address'
                                  else:
                                      if balanceOf[addr(_from)] < 1:
                                          revert with 'NH{q', 17
                                      else:
                                          if stor7[_tokenId] == balanceOf[addr(_from)] - 1:
                                              stor7[_tokenId] = 0
                                              tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                              if _to:
                                                  if _to == _from:
                                                      approved[_tokenId] = 0
                                                      if not ownerOf[_tokenId]:
                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                      else:
                                                          log Approval(
                                                                address owner=ownerOf[_tokenId],
                                                                address spender=0,
                                                                uint256 value=_tokenId)
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_from)]--
                                                              if balanceOf[addr(_to)] > -2:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_to)]++
                                                                  ownerOf[_tokenId] = _to
                                                                  log Transfer(
                                                                        address from=_from,
                                                                        address to=_to,
                                                                        uint256 value=_tokenId)
                                                                  if ext_code.size(_to) <= 0:
                                                                      stop
                                                                  else:
                                                                      require ext_code.size(_to)
                                                                      call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                           gas gas_remaining wei
                                                                          args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                      if not ext_call.success:
                                                                          if not return_data.size:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              if not return_data.size:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          require return_data.size >=′ 32
                                                                          require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                          if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              stop
                                                  else:
                                                      if not _to:
                                                          revert with 0, 'ERC721: balance query for the zero address'
                                                      else:
                                                          tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                          stor7[_tokenId] = balanceOf[addr(_to)]
                                                          approved[_tokenId] = 0
                                                          if not ownerOf[_tokenId]:
                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                          else:
                                                              log Approval(
                                                                    address owner=ownerOf[_tokenId],
                                                                    address spender=0,
                                                                    uint256 value=_tokenId)
                                                              if balanceOf[addr(_from)] < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_from)]--
                                                                  if balanceOf[addr(_to)] > -2:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_to)]++
                                                                      ownerOf[_tokenId] = _to
                                                                      log Transfer(
                                                                            address from=_from,
                                                                            address to=_to,
                                                                            uint256 value=_tokenId)
                                                                      if ext_code.size(_to) <= 0:
                                                                          stop
                                                                      else:
                                                                          require ext_code.size(_to)
                                                                          call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                               gas gas_remaining wei
                                                                              args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                          if not ext_call.success:
                                                                              if not return_data.size:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  if not return_data.size:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              require return_data.size >=′ 32
                                                                              require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                              if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  stop
                                              else:
                                                  if tokenByIndex.length < 1:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                          revert with 'NH{q', 50
                                                      else:
                                                          if stor9[_tokenId] >= tokenByIndex.length:
                                                              revert with 'NH{q', 50
                                                          else:
                                                              tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                              stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                              stor9[_tokenId] = 0
                                                              if not tokenByIndex.length:
                                                                  revert with 'NH{q', 49
                                                              else:
                                                                  tokenByIndex[tokenByIndex.length] = 0
                                                                  tokenByIndex.length--
                                                                  approved[_tokenId] = 0
                                                                  if not ownerOf[_tokenId]:
                                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_tokenId],
                                                                            address spender=0,
                                                                            uint256 value=_tokenId)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_tokenId] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_tokenId)
                                                                              if ext_code.size(_to) <= 0:
                                                                                  stop
                                                                              else:
                                                                                  require ext_code.size(_to)
                                                                                  call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                       gas gas_remaining wei
                                                                                      args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                      if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          stop
                                          else:
                                              tokenOfOwnerByIndex[addr(_from)][stor7[_tokenId]] = tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1]
                                              stor7[stor6[addr(_from)][stor3[addr(_from)] - 1]] = stor7[_tokenId]
                                              stor7[_tokenId] = 0
                                              tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                              if _to:
                                                  if _to == _from:
                                                      approved[_tokenId] = 0
                                                      if not ownerOf[_tokenId]:
                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                      else:
                                                          log Approval(
                                                                address owner=ownerOf[_tokenId],
                                                                address spender=0,
                                                                uint256 value=_tokenId)
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_from)]--
                                                              if balanceOf[addr(_to)] > -2:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_to)]++
                                                                  ownerOf[_tokenId] = _to
                                                                  log Transfer(
                                                                        address from=_from,
                                                                        address to=_to,
                                                                        uint256 value=_tokenId)
                                                                  if ext_code.size(_to) <= 0:
                                                                      stop
                                                                  else:
                                                                      require ext_code.size(_to)
                                                                      call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                           gas gas_remaining wei
                                                                          args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                      if not ext_call.success:
                                                                          if not return_data.size:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              if not return_data.size:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          require return_data.size >=′ 32
                                                                          require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                          if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              stop
                                                  else:
                                                      if not _to:
                                                          revert with 0, 'ERC721: balance query for the zero address'
                                                      else:
                                                          tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                          stor7[_tokenId] = balanceOf[addr(_to)]
                                                          approved[_tokenId] = 0
                                                          if not ownerOf[_tokenId]:
                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                          else:
                                                              log Approval(
                                                                    address owner=ownerOf[_tokenId],
                                                                    address spender=0,
                                                                    uint256 value=_tokenId)
                                                              if balanceOf[addr(_from)] < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_from)]--
                                                                  if balanceOf[addr(_to)] > -2:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_to)]++
                                                                      ownerOf[_tokenId] = _to
                                                                      log Transfer(
                                                                            address from=_from,
                                                                            address to=_to,
                                                                            uint256 value=_tokenId)
                                                                      if ext_code.size(_to) <= 0:
                                                                          stop
                                                                      else:
                                                                          require ext_code.size(_to)
                                                                          call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                               gas gas_remaining wei
                                                                              args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                          if not ext_call.success:
                                                                              if not return_data.size:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  if not return_data.size:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              require return_data.size >=′ 32
                                                                              require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                              if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  stop
                                              else:
                                                  if tokenByIndex.length < 1:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                          revert with 'NH{q', 50
                                                      else:
                                                          if stor9[_tokenId] >= tokenByIndex.length:
                                                              revert with 'NH{q', 50
                                                          else:
                                                              tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                              stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                              stor9[_tokenId] = 0
                                                              if not tokenByIndex.length:
                                                                  revert with 'NH{q', 49
                                                              else:
                                                                  tokenByIndex[tokenByIndex.length] = 0
                                                                  tokenByIndex.length--
                                                                  approved[_tokenId] = 0
                                                                  if not ownerOf[_tokenId]:
                                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_tokenId],
                                                                            address spender=0,
                                                                            uint256 value=_tokenId)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_tokenId] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_tokenId)
                                                                              if ext_code.size(_to) <= 0:
                                                                                  stop
                                                                              else:
                                                                                  require ext_code.size(_to)
                                                                                  call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                       gas gas_remaining wei
                                                                                      args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                      if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          stop
                          else:
                              stor9[_tokenId] = tokenByIndex.length
                              tokenByIndex.length++
                              tokenByIndex[tokenByIndex.length] = _tokenId
                              if _to:
                                  if _to == _from:
                                      approved[_tokenId] = 0
                                      if not ownerOf[_tokenId]:
                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                      else:
                                          log Approval(
                                                address owner=ownerOf[_tokenId],
                                                address spender=0,
                                                uint256 value=_tokenId)
                                          if balanceOf[addr(_from)] < 1:
                                              revert with 'NH{q', 17
                                          else:
                                              balanceOf[addr(_from)]--
                                              if balanceOf[addr(_to)] > -2:
                                                  revert with 'NH{q', 17
                                              else:
                                                  balanceOf[addr(_to)]++
                                                  ownerOf[_tokenId] = _to
                                                  log Transfer(
                                                        address from=_from,
                                                        address to=_to,
                                                        uint256 value=_tokenId)
                                                  if ext_code.size(_to) <= 0:
                                                      stop
                                                  else:
                                                      require ext_code.size(_to)
                                                      call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                           gas gas_remaining wei
                                                          args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                      if not ext_call.success:
                                                          if not return_data.size:
                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                          else:
                                                              if not return_data.size:
                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                              else:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                      else:
                                                          require return_data.size >=′ 32
                                                          require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                          if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                          else:
                                                              stop
                                  else:
                                      if not _to:
                                          revert with 0, 'ERC721: balance query for the zero address'
                                      else:
                                          tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                          stor7[_tokenId] = balanceOf[addr(_to)]
                                          approved[_tokenId] = 0
                                          if not ownerOf[_tokenId]:
                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                          else:
                                              log Approval(
                                                    address owner=ownerOf[_tokenId],
                                                    address spender=0,
                                                    uint256 value=_tokenId)
                                              if balanceOf[addr(_from)] < 1:
                                                  revert with 'NH{q', 17
                                              else:
                                                  balanceOf[addr(_from)]--
                                                  if balanceOf[addr(_to)] > -2:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      balanceOf[addr(_to)]++
                                                      ownerOf[_tokenId] = _to
                                                      log Transfer(
                                                            address from=_from,
                                                            address to=_to,
                                                            uint256 value=_tokenId)
                                                      if ext_code.size(_to) <= 0:
                                                          stop
                                                      else:
                                                          require ext_code.size(_to)
                                                          call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                               gas gas_remaining wei
                                                              args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                          if not ext_call.success:
                                                              if not return_data.size:
                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                              else:
                                                                  if not return_data.size:
                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                  else:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                          else:
                                                              require return_data.size >=′ 32
                                                              require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                              if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                              else:
                                                                  stop
                              else:
                                  if tokenByIndex.length < 1:
                                      revert with 'NH{q', 17
                                  else:
                                      if tokenByIndex.length - 1 >= tokenByIndex.length:
                                          revert with 'NH{q', 50
                                      else:
                                          if stor9[_tokenId] >= tokenByIndex.length:
                                              revert with 'NH{q', 50
                                          else:
                                              tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                              stor9[stor8[stor8.length]] = stor9[_tokenId]
                                              stor9[_tokenId] = 0
                                              if not tokenByIndex.length:
                                                  revert with 'NH{q', 49
                                              else:
                                                  tokenByIndex[tokenByIndex.length] = 0
                                                  tokenByIndex.length--
                                                  approved[_tokenId] = 0
                                                  if not ownerOf[_tokenId]:
                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                  else:
                                                      log Approval(
                                                            address owner=ownerOf[_tokenId],
                                                            address spender=0,
                                                            uint256 value=_tokenId)
                                                      if balanceOf[addr(_from)] < 1:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_from)]--
                                                          if balanceOf[addr(_to)] > -2:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_to)]++
                                                              ownerOf[_tokenId] = _to
                                                              log Transfer(
                                                                    address from=_from,
                                                                    address to=_to,
                                                                    uint256 value=_tokenId)
                                                              if ext_code.size(_to) <= 0:
                                                                  stop
                                                              else:
                                                                  require ext_code.size(_to)
                                                                  call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                       gas gas_remaining wei
                                                                      args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                  if not ext_call.success:
                                                                      if not return_data.size:
                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                      else:
                                                                          if not return_data.size:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >=′ 32
                                                                      require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                      if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                      else:
                                                                          stop
          else:
              if not ownerOf[_tokenId]:
                  revert with 0, 'ERC721: approved query for nonexistent token'
              else:
                  if approved[_tokenId] == caller:
                      if not ownerOf[_tokenId]:
                          revert with 0, 'ERC721: owner query for nonexistent token'
                      else:
                          if ownerOf[_tokenId] != _from:
                              revert with 0, 'ERC721: transfer of token that is not own'
                          else:
                              if not _to:
                                  revert with 0, 'ERC721: transfer to the zero address'
                              else:
                                  if _from:
                                      if _from == _to:
                                          if _to:
                                              if _to == _from:
                                                  approved[_tokenId] = 0
                                                  if not ownerOf[_tokenId]:
                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                  else:
                                                      log Approval(
                                                            address owner=ownerOf[_tokenId],
                                                            address spender=0,
                                                            uint256 value=_tokenId)
                                                      if balanceOf[addr(_from)] < 1:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_from)]--
                                                          if balanceOf[addr(_to)] > -2:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_to)]++
                                                              ownerOf[_tokenId] = _to
                                                              log Transfer(
                                                                    address from=_from,
                                                                    address to=_to,
                                                                    uint256 value=_tokenId)
                                                              if ext_code.size(_to) <= 0:
                                                                  stop
                                                              else:
                                                                  require ext_code.size(_to)
                                                                  call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                       gas gas_remaining wei
                                                                      args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                  if not ext_call.success:
                                                                      if not return_data.size:
                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                      else:
                                                                          if not return_data.size:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >=′ 32
                                                                      require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                      if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                      else:
                                                                          stop
                                              else:
                                                  if not _to:
                                                      revert with 0, 'ERC721: balance query for the zero address'
                                                  else:
                                                      tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                      stor7[_tokenId] = balanceOf[addr(_to)]
                                                      approved[_tokenId] = 0
                                                      if not ownerOf[_tokenId]:
                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                      else:
                                                          log Approval(
                                                                address owner=ownerOf[_tokenId],
                                                                address spender=0,
                                                                uint256 value=_tokenId)
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_from)]--
                                                              if balanceOf[addr(_to)] > -2:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_to)]++
                                                                  ownerOf[_tokenId] = _to
                                                                  log Transfer(
                                                                        address from=_from,
                                                                        address to=_to,
                                                                        uint256 value=_tokenId)
                                                                  if ext_code.size(_to) <= 0:
                                                                      stop
                                                                  else:
                                                                      require ext_code.size(_to)
                                                                      call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                           gas gas_remaining wei
                                                                          args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                      if not ext_call.success:
                                                                          if not return_data.size:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              if not return_data.size:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          require return_data.size >=′ 32
                                                                          require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                          if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              stop
                                          else:
                                              if tokenByIndex.length < 1:
                                                  revert with 'NH{q', 17
                                              else:
                                                  if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                      revert with 'NH{q', 50
                                                  else:
                                                      if stor9[_tokenId] >= tokenByIndex.length:
                                                          revert with 'NH{q', 50
                                                      else:
                                                          tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                          stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                          stor9[_tokenId] = 0
                                                          if not tokenByIndex.length:
                                                              revert with 'NH{q', 49
                                                          else:
                                                              tokenByIndex[tokenByIndex.length] = 0
                                                              tokenByIndex.length--
                                                              approved[_tokenId] = 0
                                                              if not ownerOf[_tokenId]:
                                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                                              else:
                                                                  log Approval(
                                                                        address owner=ownerOf[_tokenId],
                                                                        address spender=0,
                                                                        uint256 value=_tokenId)
                                                                  if balanceOf[addr(_from)] < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_from)]--
                                                                      if balanceOf[addr(_to)] > -2:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_to)]++
                                                                          ownerOf[_tokenId] = _to
                                                                          log Transfer(
                                                                                address from=_from,
                                                                                address to=_to,
                                                                                uint256 value=_tokenId)
                                                                          if ext_code.size(_to) <= 0:
                                                                              stop
                                                                          else:
                                                                              require ext_code.size(_to)
                                                                              call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                   gas gas_remaining wei
                                                                                  args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                              if not ext_call.success:
                                                                                  if not return_data.size:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require return_data.size >=′ 32
                                                                                  require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                  if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      stop
                                      else:
                                          if not _from:
                                              revert with 0, 'ERC721: balance query for the zero address'
                                          else:
                                              if balanceOf[addr(_from)] < 1:
                                                  revert with 'NH{q', 17
                                              else:
                                                  if stor7[_tokenId] == balanceOf[addr(_from)] - 1:
                                                      stor7[_tokenId] = 0
                                                      tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                                      if _to:
                                                          if _to == _from:
                                                              approved[_tokenId] = 0
                                                              if not ownerOf[_tokenId]:
                                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                                              else:
                                                                  log Approval(
                                                                        address owner=ownerOf[_tokenId],
                                                                        address spender=0,
                                                                        uint256 value=_tokenId)
                                                                  if balanceOf[addr(_from)] < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_from)]--
                                                                      if balanceOf[addr(_to)] > -2:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_to)]++
                                                                          ownerOf[_tokenId] = _to
                                                                          log Transfer(
                                                                                address from=_from,
                                                                                address to=_to,
                                                                                uint256 value=_tokenId)
                                                                          if ext_code.size(_to) <= 0:
                                                                              stop
                                                                          else:
                                                                              require ext_code.size(_to)
                                                                              call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                   gas gas_remaining wei
                                                                                  args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                              if not ext_call.success:
                                                                                  if not return_data.size:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require return_data.size >=′ 32
                                                                                  require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                  if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      stop
                                                          else:
                                                              if not _to:
                                                                  revert with 0, 'ERC721: balance query for the zero address'
                                                              else:
                                                                  tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                                  stor7[_tokenId] = balanceOf[addr(_to)]
                                                                  approved[_tokenId] = 0
                                                                  if not ownerOf[_tokenId]:
                                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_tokenId],
                                                                            address spender=0,
                                                                            uint256 value=_tokenId)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_tokenId] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_tokenId)
                                                                              if ext_code.size(_to) <= 0:
                                                                                  stop
                                                                              else:
                                                                                  require ext_code.size(_to)
                                                                                  call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                       gas gas_remaining wei
                                                                                      args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                      if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          stop
                                                      else:
                                                          if tokenByIndex.length < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                  revert with 'NH{q', 50
                                                              else:
                                                                  if stor9[_tokenId] >= tokenByIndex.length:
                                                                      revert with 'NH{q', 50
                                                                  else:
                                                                      tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                                      stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                                      stor9[_tokenId] = 0
                                                                      if not tokenByIndex.length:
                                                                          revert with 'NH{q', 49
                                                                      else:
                                                                          tokenByIndex[tokenByIndex.length] = 0
                                                                          tokenByIndex.length--
                                                                          approved[_tokenId] = 0
                                                                          if not ownerOf[_tokenId]:
                                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                                          else:
                                                                              log Approval(
                                                                                    address owner=ownerOf[_tokenId],
                                                                                    address spender=0,
                                                                                    uint256 value=_tokenId)
                                                                              if balanceOf[addr(_from)] < 1:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_from)]--
                                                                                  if balanceOf[addr(_to)] > -2:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_to)]++
                                                                                      ownerOf[_tokenId] = _to
                                                                                      log Transfer(
                                                                                            address from=_from,
                                                                                            address to=_to,
                                                                                            uint256 value=_tokenId)
                                                                                      if ext_code.size(_to) <= 0:
                                                                                          stop
                                                                                      else:
                                                                                          require ext_code.size(_to)
                                                                                          call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                               gas gas_remaining wei
                                                                                              args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                                          if not ext_call.success:
                                                                                              if not return_data.size:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  if not return_data.size:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                          else:
                                                                                              require return_data.size >=′ 32
                                                                                              require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                              if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  stop
                                                  else:
                                                      tokenOfOwnerByIndex[addr(_from)][stor7[_tokenId]] = tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1]
                                                      stor7[stor6[addr(_from)][stor3[addr(_from)] - 1]] = stor7[_tokenId]
                                                      stor7[_tokenId] = 0
                                                      tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                                      if _to:
                                                          if _to == _from:
                                                              approved[_tokenId] = 0
                                                              if not ownerOf[_tokenId]:
                                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                                              else:
                                                                  log Approval(
                                                                        address owner=ownerOf[_tokenId],
                                                                        address spender=0,
                                                                        uint256 value=_tokenId)
                                                                  if balanceOf[addr(_from)] < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_from)]--
                                                                      if balanceOf[addr(_to)] > -2:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_to)]++
                                                                          ownerOf[_tokenId] = _to
                                                                          log Transfer(
                                                                                address from=_from,
                                                                                address to=_to,
                                                                                uint256 value=_tokenId)
                                                                          if ext_code.size(_to) <= 0:
                                                                              stop
                                                                          else:
                                                                              require ext_code.size(_to)
                                                                              call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                   gas gas_remaining wei
                                                                                  args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                              if not ext_call.success:
                                                                                  if not return_data.size:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require return_data.size >=′ 32
                                                                                  require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                  if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      stop
                                                          else:
                                                              if not _to:
                                                                  revert with 0, 'ERC721: balance query for the zero address'
                                                              else:
                                                                  tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                                  stor7[_tokenId] = balanceOf[addr(_to)]
                                                                  approved[_tokenId] = 0
                                                                  if not ownerOf[_tokenId]:
                                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_tokenId],
                                                                            address spender=0,
                                                                            uint256 value=_tokenId)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_tokenId] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_tokenId)
                                                                              if ext_code.size(_to) <= 0:
                                                                                  stop
                                                                              else:
                                                                                  require ext_code.size(_to)
                                                                                  call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                       gas gas_remaining wei
                                                                                      args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                      if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          stop
                                                      else:
                                                          if tokenByIndex.length < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                  revert with 'NH{q', 50
                                                              else:
                                                                  if stor9[_tokenId] >= tokenByIndex.length:
                                                                      revert with 'NH{q', 50
                                                                  else:
                                                                      tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                                      stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                                      stor9[_tokenId] = 0
                                                                      if not tokenByIndex.length:
                                                                          revert with 'NH{q', 49
                                                                      else:
                                                                          tokenByIndex[tokenByIndex.length] = 0
                                                                          tokenByIndex.length--
                                                                          approved[_tokenId] = 0
                                                                          if not ownerOf[_tokenId]:
                                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                                          else:
                                                                              log Approval(
                                                                                    address owner=ownerOf[_tokenId],
                                                                                    address spender=0,
                                                                                    uint256 value=_tokenId)
                                                                              if balanceOf[addr(_from)] < 1:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_from)]--
                                                                                  if balanceOf[addr(_to)] > -2:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_to)]++
                                                                                      ownerOf[_tokenId] = _to
                                                                                      log Transfer(
                                                                                            address from=_from,
                                                                                            address to=_to,
                                                                                            uint256 value=_tokenId)
                                                                                      if ext_code.size(_to) <= 0:
                                                                                          stop
                                                                                      else:
                                                                                          require ext_code.size(_to)
                                                                                          call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                               gas gas_remaining wei
                                                                                              args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                                          if not ext_call.success:
                                                                                              if not return_data.size:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  if not return_data.size:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                          else:
                                                                                              require return_data.size >=′ 32
                                                                                              require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                              if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  stop
                                  else:
                                      stor9[_tokenId] = tokenByIndex.length
                                      tokenByIndex.length++
                                      tokenByIndex[tokenByIndex.length] = _tokenId
                                      if _to:
                                          if _to == _from:
                                              approved[_tokenId] = 0
                                              if not ownerOf[_tokenId]:
                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                              else:
                                                  log Approval(
                                                        address owner=ownerOf[_tokenId],
                                                        address spender=0,
                                                        uint256 value=_tokenId)
                                                  if balanceOf[addr(_from)] < 1:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      balanceOf[addr(_from)]--
                                                      if balanceOf[addr(_to)] > -2:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_to)]++
                                                          ownerOf[_tokenId] = _to
                                                          log Transfer(
                                                                address from=_from,
                                                                address to=_to,
                                                                uint256 value=_tokenId)
                                                          if ext_code.size(_to) <= 0:
                                                              stop
                                                          else:
                                                              require ext_code.size(_to)
                                                              call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                   gas gas_remaining wei
                                                                  args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                              if not ext_call.success:
                                                                  if not return_data.size:
                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                  else:
                                                                      if not return_data.size:
                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                      else:
                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                              else:
                                                                  require return_data.size >=′ 32
                                                                  require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                  if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                  else:
                                                                      stop
                                          else:
                                              if not _to:
                                                  revert with 0, 'ERC721: balance query for the zero address'
                                              else:
                                                  tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                  stor7[_tokenId] = balanceOf[addr(_to)]
                                                  approved[_tokenId] = 0
                                                  if not ownerOf[_tokenId]:
                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                  else:
                                                      log Approval(
                                                            address owner=ownerOf[_tokenId],
                                                            address spender=0,
                                                            uint256 value=_tokenId)
                                                      if balanceOf[addr(_from)] < 1:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_from)]--
                                                          if balanceOf[addr(_to)] > -2:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_to)]++
                                                              ownerOf[_tokenId] = _to
                                                              log Transfer(
                                                                    address from=_from,
                                                                    address to=_to,
                                                                    uint256 value=_tokenId)
                                                              if ext_code.size(_to) <= 0:
                                                                  stop
                                                              else:
                                                                  require ext_code.size(_to)
                                                                  call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                       gas gas_remaining wei
                                                                      args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                  if not ext_call.success:
                                                                      if not return_data.size:
                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                      else:
                                                                          if not return_data.size:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >=′ 32
                                                                      require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                      if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                      else:
                                                                          stop
                                      else:
                                          if tokenByIndex.length < 1:
                                              revert with 'NH{q', 17
                                          else:
                                              if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                  revert with 'NH{q', 50
                                              else:
                                                  if stor9[_tokenId] >= tokenByIndex.length:
                                                      revert with 'NH{q', 50
                                                  else:
                                                      tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                      stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                      stor9[_tokenId] = 0
                                                      if not tokenByIndex.length:
                                                          revert with 'NH{q', 49
                                                      else:
                                                          tokenByIndex[tokenByIndex.length] = 0
                                                          tokenByIndex.length--
                                                          approved[_tokenId] = 0
                                                          if not ownerOf[_tokenId]:
                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                          else:
                                                              log Approval(
                                                                    address owner=ownerOf[_tokenId],
                                                                    address spender=0,
                                                                    uint256 value=_tokenId)
                                                              if balanceOf[addr(_from)] < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_from)]--
                                                                  if balanceOf[addr(_to)] > -2:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_to)]++
                                                                      ownerOf[_tokenId] = _to
                                                                      log Transfer(
                                                                            address from=_from,
                                                                            address to=_to,
                                                                            uint256 value=_tokenId)
                                                                      if ext_code.size(_to) <= 0:
                                                                          stop
                                                                      else:
                                                                          require ext_code.size(_to)
                                                                          call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                               gas gas_remaining wei
                                                                              args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                          if not ext_call.success:
                                                                              if not return_data.size:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  if not return_data.size:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              require return_data.size >=′ 32
                                                                              require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                              if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  stop
                  else:
                      if not stor5[stor2[_tokenId]][caller]:
                          revert with 0, 'ERC721: transfer caller is not owner nor approved'
                      else:
                          if not ownerOf[_tokenId]:
                              revert with 0, 'ERC721: owner query for nonexistent token'
                          else:
                              if ownerOf[_tokenId] != _from:
                                  revert with 0, 'ERC721: transfer of token that is not own'
                              else:
                                  if not _to:
                                      revert with 0, 'ERC721: transfer to the zero address'
                                  else:
                                      if _from:
                                          if _from == _to:
                                              if _to:
                                                  if _to == _from:
                                                      approved[_tokenId] = 0
                                                      if not ownerOf[_tokenId]:
                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                      else:
                                                          log Approval(
                                                                address owner=ownerOf[_tokenId],
                                                                address spender=0,
                                                                uint256 value=_tokenId)
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_from)]--
                                                              if balanceOf[addr(_to)] > -2:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_to)]++
                                                                  ownerOf[_tokenId] = _to
                                                                  log Transfer(
                                                                        address from=_from,
                                                                        address to=_to,
                                                                        uint256 value=_tokenId)
                                                                  if ext_code.size(_to) <= 0:
                                                                      stop
                                                                  else:
                                                                      require ext_code.size(_to)
                                                                      call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                           gas gas_remaining wei
                                                                          args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                      if not ext_call.success:
                                                                          if not return_data.size:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              if not return_data.size:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          require return_data.size >=′ 32
                                                                          require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                          if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              stop
                                                  else:
                                                      if not _to:
                                                          revert with 0, 'ERC721: balance query for the zero address'
                                                      else:
                                                          tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                          stor7[_tokenId] = balanceOf[addr(_to)]
                                                          approved[_tokenId] = 0
                                                          if not ownerOf[_tokenId]:
                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                          else:
                                                              log Approval(
                                                                    address owner=ownerOf[_tokenId],
                                                                    address spender=0,
                                                                    uint256 value=_tokenId)
                                                              if balanceOf[addr(_from)] < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_from)]--
                                                                  if balanceOf[addr(_to)] > -2:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_to)]++
                                                                      ownerOf[_tokenId] = _to
                                                                      log Transfer(
                                                                            address from=_from,
                                                                            address to=_to,
                                                                            uint256 value=_tokenId)
                                                                      if ext_code.size(_to) <= 0:
                                                                          stop
                                                                      else:
                                                                          require ext_code.size(_to)
                                                                          call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                               gas gas_remaining wei
                                                                              args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                          if not ext_call.success:
                                                                              if not return_data.size:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  if not return_data.size:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              require return_data.size >=′ 32
                                                                              require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                              if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  stop
                                              else:
                                                  if tokenByIndex.length < 1:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                          revert with 'NH{q', 50
                                                      else:
                                                          if stor9[_tokenId] >= tokenByIndex.length:
                                                              revert with 'NH{q', 50
                                                          else:
                                                              tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                              stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                              stor9[_tokenId] = 0
                                                              if not tokenByIndex.length:
                                                                  revert with 'NH{q', 49
                                                              else:
                                                                  tokenByIndex[tokenByIndex.length] = 0
                                                                  tokenByIndex.length--
                                                                  approved[_tokenId] = 0
                                                                  if not ownerOf[_tokenId]:
                                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_tokenId],
                                                                            address spender=0,
                                                                            uint256 value=_tokenId)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_tokenId] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_tokenId)
                                                                              if ext_code.size(_to) <= 0:
                                                                                  stop
                                                                              else:
                                                                                  require ext_code.size(_to)
                                                                                  call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                       gas gas_remaining wei
                                                                                      args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                      if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          stop
                                          else:
                                              if not _from:
                                                  revert with 0, 'ERC721: balance query for the zero address'
                                              else:
                                                  if balanceOf[addr(_from)] < 1:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      if stor7[_tokenId] == balanceOf[addr(_from)] - 1:
                                                          stor7[_tokenId] = 0
                                                          tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                                          if _to:
                                                              if _to == _from:
                                                                  approved[_tokenId] = 0
                                                                  if not ownerOf[_tokenId]:
                                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_tokenId],
                                                                            address spender=0,
                                                                            uint256 value=_tokenId)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_tokenId] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_tokenId)
                                                                              if ext_code.size(_to) <= 0:
                                                                                  stop
                                                                              else:
                                                                                  require ext_code.size(_to)
                                                                                  call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                       gas gas_remaining wei
                                                                                      args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                      if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          stop
                                                              else:
                                                                  if not _to:
                                                                      revert with 0, 'ERC721: balance query for the zero address'
                                                                  else:
                                                                      tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                                      stor7[_tokenId] = balanceOf[addr(_to)]
                                                                      approved[_tokenId] = 0
                                                                      if not ownerOf[_tokenId]:
                                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                                      else:
                                                                          log Approval(
                                                                                address owner=ownerOf[_tokenId],
                                                                                address spender=0,
                                                                                uint256 value=_tokenId)
                                                                          if balanceOf[addr(_from)] < 1:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_from)]--
                                                                              if balanceOf[addr(_to)] > -2:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_to)]++
                                                                                  ownerOf[_tokenId] = _to
                                                                                  log Transfer(
                                                                                        address from=_from,
                                                                                        address to=_to,
                                                                                        uint256 value=_tokenId)
                                                                                  if ext_code.size(_to) <= 0:
                                                                                      stop
                                                                                  else:
                                                                                      require ext_code.size(_to)
                                                                                      call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                           gas gas_remaining wei
                                                                                          args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                                      if not ext_call.success:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              if not return_data.size:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                                      else:
                                                                                          require return_data.size >=′ 32
                                                                                          require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                          if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              stop
                                                          else:
                                                              if tokenByIndex.length < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                      revert with 'NH{q', 50
                                                                  else:
                                                                      if stor9[_tokenId] >= tokenByIndex.length:
                                                                          revert with 'NH{q', 50
                                                                      else:
                                                                          tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                                          stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                                          stor9[_tokenId] = 0
                                                                          if not tokenByIndex.length:
                                                                              revert with 'NH{q', 49
                                                                          else:
                                                                              tokenByIndex[tokenByIndex.length] = 0
                                                                              tokenByIndex.length--
                                                                              approved[_tokenId] = 0
                                                                              if not ownerOf[_tokenId]:
                                                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                                                              else:
                                                                                  log Approval(
                                                                                        address owner=ownerOf[_tokenId],
                                                                                        address spender=0,
                                                                                        uint256 value=_tokenId)
                                                                                  if balanceOf[addr(_from)] < 1:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_from)]--
                                                                                      if balanceOf[addr(_to)] > -2:
                                                                                          revert with 'NH{q', 17
                                                                                      else:
                                                                                          balanceOf[addr(_to)]++
                                                                                          ownerOf[_tokenId] = _to
                                                                                          log Transfer(
                                                                                                address from=_from,
                                                                                                address to=_to,
                                                                                                uint256 value=_tokenId)
                                                                                          if ext_code.size(_to) <= 0:
                                                                                              stop
                                                                                          else:
                                                                                              require ext_code.size(_to)
                                                                                              call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                                   gas gas_remaining wei
                                                                                                  args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                                  if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      stop
                                                      else:
                                                          tokenOfOwnerByIndex[addr(_from)][stor7[_tokenId]] = tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1]
                                                          stor7[stor6[addr(_from)][stor3[addr(_from)] - 1]] = stor7[_tokenId]
                                                          stor7[_tokenId] = 0
                                                          tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                                          if _to:
                                                              if _to == _from:
                                                                  approved[_tokenId] = 0
                                                                  if not ownerOf[_tokenId]:
                                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_tokenId],
                                                                            address spender=0,
                                                                            uint256 value=_tokenId)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_tokenId] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_tokenId)
                                                                              if ext_code.size(_to) <= 0:
                                                                                  stop
                                                                              else:
                                                                                  require ext_code.size(_to)
                                                                                  call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                       gas gas_remaining wei
                                                                                      args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                      if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          stop
                                                              else:
                                                                  if not _to:
                                                                      revert with 0, 'ERC721: balance query for the zero address'
                                                                  else:
                                                                      tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                                      stor7[_tokenId] = balanceOf[addr(_to)]
                                                                      approved[_tokenId] = 0
                                                                      if not ownerOf[_tokenId]:
                                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                                      else:
                                                                          log Approval(
                                                                                address owner=ownerOf[_tokenId],
                                                                                address spender=0,
                                                                                uint256 value=_tokenId)
                                                                          if balanceOf[addr(_from)] < 1:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_from)]--
                                                                              if balanceOf[addr(_to)] > -2:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_to)]++
                                                                                  ownerOf[_tokenId] = _to
                                                                                  log Transfer(
                                                                                        address from=_from,
                                                                                        address to=_to,
                                                                                        uint256 value=_tokenId)
                                                                                  if ext_code.size(_to) <= 0:
                                                                                      stop
                                                                                  else:
                                                                                      require ext_code.size(_to)
                                                                                      call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                           gas gas_remaining wei
                                                                                          args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                                      if not ext_call.success:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              if not return_data.size:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                                      else:
                                                                                          require return_data.size >=′ 32
                                                                                          require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                          if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              stop
                                                          else:
                                                              if tokenByIndex.length < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                      revert with 'NH{q', 50
                                                                  else:
                                                                      if stor9[_tokenId] >= tokenByIndex.length:
                                                                          revert with 'NH{q', 50
                                                                      else:
                                                                          tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                                          stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                                          stor9[_tokenId] = 0
                                                                          if not tokenByIndex.length:
                                                                              revert with 'NH{q', 49
                                                                          else:
                                                                              tokenByIndex[tokenByIndex.length] = 0
                                                                              tokenByIndex.length--
                                                                              approved[_tokenId] = 0
                                                                              if not ownerOf[_tokenId]:
                                                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                                                              else:
                                                                                  log Approval(
                                                                                        address owner=ownerOf[_tokenId],
                                                                                        address spender=0,
                                                                                        uint256 value=_tokenId)
                                                                                  if balanceOf[addr(_from)] < 1:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_from)]--
                                                                                      if balanceOf[addr(_to)] > -2:
                                                                                          revert with 'NH{q', 17
                                                                                      else:
                                                                                          balanceOf[addr(_to)]++
                                                                                          ownerOf[_tokenId] = _to
                                                                                          log Transfer(
                                                                                                address from=_from,
                                                                                                address to=_to,
                                                                                                uint256 value=_tokenId)
                                                                                          if ext_code.size(_to) <= 0:
                                                                                              stop
                                                                                          else:
                                                                                              require ext_code.size(_to)
                                                                                              call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                                   gas gas_remaining wei
                                                                                                  args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                                  if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      stop
                                      else:
                                          stor9[_tokenId] = tokenByIndex.length
                                          tokenByIndex.length++
                                          tokenByIndex[tokenByIndex.length] = _tokenId
                                          if _to:
                                              if _to == _from:
                                                  approved[_tokenId] = 0
                                                  if not ownerOf[_tokenId]:
                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                  else:
                                                      log Approval(
                                                            address owner=ownerOf[_tokenId],
                                                            address spender=0,
                                                            uint256 value=_tokenId)
                                                      if balanceOf[addr(_from)] < 1:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_from)]--
                                                          if balanceOf[addr(_to)] > -2:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_to)]++
                                                              ownerOf[_tokenId] = _to
                                                              log Transfer(
                                                                    address from=_from,
                                                                    address to=_to,
                                                                    uint256 value=_tokenId)
                                                              if ext_code.size(_to) <= 0:
                                                                  stop
                                                              else:
                                                                  require ext_code.size(_to)
                                                                  call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                       gas gas_remaining wei
                                                                      args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                  if not ext_call.success:
                                                                      if not return_data.size:
                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                      else:
                                                                          if not return_data.size:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >=′ 32
                                                                      require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                      if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                      else:
                                                                          stop
                                              else:
                                                  if not _to:
                                                      revert with 0, 'ERC721: balance query for the zero address'
                                                  else:
                                                      tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                      stor7[_tokenId] = balanceOf[addr(_to)]
                                                      approved[_tokenId] = 0
                                                      if not ownerOf[_tokenId]:
                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                      else:
                                                          log Approval(
                                                                address owner=ownerOf[_tokenId],
                                                                address spender=0,
                                                                uint256 value=_tokenId)
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_from)]--
                                                              if balanceOf[addr(_to)] > -2:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_to)]++
                                                                  ownerOf[_tokenId] = _to
                                                                  log Transfer(
                                                                        address from=_from,
                                                                        address to=_to,
                                                                        uint256 value=_tokenId)
                                                                  if ext_code.size(_to) <= 0:
                                                                      stop
                                                                  else:
                                                                      require ext_code.size(_to)
                                                                      call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                           gas gas_remaining wei
                                                                          args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                      if not ext_call.success:
                                                                          if not return_data.size:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              if not return_data.size:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          require return_data.size >=′ 32
                                                                          require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                          if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              stop
                                          else:
                                              if tokenByIndex.length < 1:
                                                  revert with 'NH{q', 17
                                              else:
                                                  if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                      revert with 'NH{q', 50
                                                  else:
                                                      if stor9[_tokenId] >= tokenByIndex.length:
                                                          revert with 'NH{q', 50
                                                      else:
                                                          tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                          stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                          stor9[_tokenId] = 0
                                                          if not tokenByIndex.length:
                                                              revert with 'NH{q', 49
                                                          else:
                                                              tokenByIndex[tokenByIndex.length] = 0
                                                              tokenByIndex.length--
                                                              approved[_tokenId] = 0
                                                              if not ownerOf[_tokenId]:
                                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                                              else:
                                                                  log Approval(
                                                                        address owner=ownerOf[_tokenId],
                                                                        address spender=0,
                                                                        uint256 value=_tokenId)
                                                                  if balanceOf[addr(_from)] < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_from)]--
                                                                      if balanceOf[addr(_to)] > -2:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_to)]++
                                                                          ownerOf[_tokenId] = _to
                                                                          log Transfer(
                                                                                address from=_from,
                                                                                address to=_to,
                                                                                uint256 value=_tokenId)
                                                                          if ext_code.size(_to) <= 0:
                                                                              stop
                                                                          else:
                                                                              require ext_code.size(_to)
                                                                              call _to.onERC721Received(address operator, address from, uint256 tokenId, bytes data) with:
                                                                                   gas gas_remaining wei
                                                                                  args 0, uint32(caller), addr(_from), _tokenId, 128, 0
                                                                              if not ext_call.success:
                                                                                  if not return_data.size:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require return_data.size >=′ 32
                                                                                  require ext_call.return_data == Mask(32, 224, ext_call.return_data[0])
                                                                                  if Mask(32, 224, ext_call.return_data[0]) != 0x150b7a0200000000000000000000000000000000000000000000000000000000:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      stop

def safeTransferFrom(address _from, address _to, uint256 _tokenId, bytes _data): # not payable
  require calldata.size - 4 >=′ 128
  require _from == _from
  require _to == _to
  require _tokenId == _tokenId
  require _data <= 18446744073709551615
  require _data + 35 <′ calldata.size
  if _data.length > 18446744073709551615:
      revert with 'NH{q', 65
  else:
      if ceil32(_data.length) + 128 > 18446744073709551615 or ceil32(_data.length) + 128 < 96:
          revert with 'NH{q', 65
      else:
          require _data + _data.length + 36 <= calldata.size
          if not ownerOf[_tokenId]:
              revert with 0, 'ERC721: operator query for nonexistent token'
          else:
              if not ownerOf[_tokenId]:
                  revert with 0, 'ERC721: owner query for nonexistent token'
              else:
                  if caller == ownerOf[_tokenId]:
                      if not ownerOf[_tokenId]:
                          revert with 0, 'ERC721: owner query for nonexistent token'
                      else:
                          if ownerOf[_tokenId] != _from:
                              revert with 0, 'ERC721: transfer of token that is not own'
                          else:
                              if not _to:
                                  revert with 0, 'ERC721: transfer to the zero address'
                              else:
                                  if _from:
                                      if _from == _to:
                                          if _to:
                                              if _to == _from:
                                                  approved[_tokenId] = 0
                                                  if not ownerOf[_tokenId]:
                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                  else:
                                                      log Approval(
                                                            address owner=ownerOf[_tokenId],
                                                            address spender=0,
                                                            uint256 value=_tokenId)
                                                      if balanceOf[addr(_from)] < 1:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_from)]--
                                                          if balanceOf[addr(_to)] > -2:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_to)]++
                                                              ownerOf[_tokenId] = _to
                                                              log Transfer(
                                                                    address from=_from,
                                                                    address to=_to,
                                                                    uint256 value=_tokenId)
                                                              if ext_code.size(_to) <= 0:
                                                                  stop
                                                              else:
                                                                  if ceil32(_data.length) <= _data.length:
                                                                      require ext_code.size(_to)
                                                                      call _to with:
                                                                           gas gas_remaining wei
                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                      if not ext_call.success:
                                                                          if not return_data.size:
                                                                              if not _data.length:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  revert with _data[all]
                                                                          else:
                                                                              if not return_data.size:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          require return_data.size >=′ 32
                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                  else:
                                                                      require ext_code.size(_to)
                                                                      call _to with:
                                                                           gas gas_remaining wei
                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                      if not ext_call.success:
                                                                          if not return_data.size:
                                                                              if not _data.length:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  revert with _data[all]
                                                                          else:
                                                                              if not return_data.size:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          require return_data.size >=′ 32
                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                              else:
                                                  if not _to:
                                                      revert with 0, 'ERC721: balance query for the zero address'
                                                  else:
                                                      tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                      stor7[_tokenId] = balanceOf[addr(_to)]
                                                      approved[_tokenId] = 0
                                                      if not ownerOf[_tokenId]:
                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                      else:
                                                          log Approval(
                                                                address owner=ownerOf[_tokenId],
                                                                address spender=0,
                                                                uint256 value=_tokenId)
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_from)]--
                                                              if balanceOf[addr(_to)] > -2:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_to)]++
                                                                  ownerOf[_tokenId] = _to
                                                                  log Transfer(
                                                                        address from=_from,
                                                                        address to=_to,
                                                                        uint256 value=_tokenId)
                                                                  if ext_code.size(_to) <= 0:
                                                                      stop
                                                                  else:
                                                                      if ceil32(_data.length) <= _data.length:
                                                                          require ext_code.size(_to)
                                                                          call _to with:
                                                                               gas gas_remaining wei
                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                          if not ext_call.success:
                                                                              if not return_data.size:
                                                                                  if not _data.length:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      revert with _data[all]
                                                                              else:
                                                                                  if not return_data.size:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              require return_data.size >=′ 32
                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                      else:
                                                                          require ext_code.size(_to)
                                                                          call _to with:
                                                                               gas gas_remaining wei
                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                          if not ext_call.success:
                                                                              if not return_data.size:
                                                                                  if not _data.length:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      revert with _data[all]
                                                                              else:
                                                                                  if not return_data.size:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              require return_data.size >=′ 32
                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                          else:
                                              if tokenByIndex.length < 1:
                                                  revert with 'NH{q', 17
                                              else:
                                                  if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                      revert with 'NH{q', 50
                                                  else:
                                                      if stor9[_tokenId] >= tokenByIndex.length:
                                                          revert with 'NH{q', 50
                                                      else:
                                                          tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                          stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                          stor9[_tokenId] = 0
                                                          if not tokenByIndex.length:
                                                              revert with 'NH{q', 49
                                                          else:
                                                              tokenByIndex[tokenByIndex.length] = 0
                                                              tokenByIndex.length--
                                                              approved[_tokenId] = 0
                                                              if not ownerOf[_tokenId]:
                                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                                              else:
                                                                  log Approval(
                                                                        address owner=ownerOf[_tokenId],
                                                                        address spender=0,
                                                                        uint256 value=_tokenId)
                                                                  if balanceOf[addr(_from)] < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_from)]--
                                                                      if balanceOf[addr(_to)] > -2:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_to)]++
                                                                          ownerOf[_tokenId] = _to
                                                                          log Transfer(
                                                                                address from=_from,
                                                                                address to=_to,
                                                                                uint256 value=_tokenId)
                                                                          if ext_code.size(_to) <= 0:
                                                                              stop
                                                                          else:
                                                                              if ceil32(_data.length) <= _data.length:
                                                                                  require ext_code.size(_to)
                                                                                  call _to with:
                                                                                       gas gas_remaining wei
                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          if not _data.length:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with _data[all]
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  require ext_code.size(_to)
                                                                                  call _to with:
                                                                                       gas gas_remaining wei
                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          if not _data.length:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with _data[all]
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                      else:
                                          if not _from:
                                              revert with 0, 'ERC721: balance query for the zero address'
                                          else:
                                              if balanceOf[addr(_from)] < 1:
                                                  revert with 'NH{q', 17
                                              else:
                                                  if stor7[_tokenId] == balanceOf[addr(_from)] - 1:
                                                      stor7[_tokenId] = 0
                                                      tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                                      if _to:
                                                          if _to == _from:
                                                              approved[_tokenId] = 0
                                                              if not ownerOf[_tokenId]:
                                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                                              else:
                                                                  log Approval(
                                                                        address owner=ownerOf[_tokenId],
                                                                        address spender=0,
                                                                        uint256 value=_tokenId)
                                                                  if balanceOf[addr(_from)] < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_from)]--
                                                                      if balanceOf[addr(_to)] > -2:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_to)]++
                                                                          ownerOf[_tokenId] = _to
                                                                          log Transfer(
                                                                                address from=_from,
                                                                                address to=_to,
                                                                                uint256 value=_tokenId)
                                                                          if ext_code.size(_to) <= 0:
                                                                              stop
                                                                          else:
                                                                              if ceil32(_data.length) <= _data.length:
                                                                                  require ext_code.size(_to)
                                                                                  call _to with:
                                                                                       gas gas_remaining wei
                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          if not _data.length:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with _data[all]
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  require ext_code.size(_to)
                                                                                  call _to with:
                                                                                       gas gas_remaining wei
                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          if not _data.length:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with _data[all]
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                          else:
                                                              if not _to:
                                                                  revert with 0, 'ERC721: balance query for the zero address'
                                                              else:
                                                                  tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                                  stor7[_tokenId] = balanceOf[addr(_to)]
                                                                  approved[_tokenId] = 0
                                                                  if not ownerOf[_tokenId]:
                                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_tokenId],
                                                                            address spender=0,
                                                                            uint256 value=_tokenId)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_tokenId] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_tokenId)
                                                                              if ext_code.size(_to) <= 0:
                                                                                  stop
                                                                              else:
                                                                                  if ceil32(_data.length) <= _data.length:
                                                                                      require ext_code.size(_to)
                                                                                      call _to with:
                                                                                           gas gas_remaining wei
                                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                      if not ext_call.success:
                                                                                          if not return_data.size:
                                                                                              if not _data.length:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with _data[all]
                                                                                          else:
                                                                                              if not return_data.size:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                                      else:
                                                                                          require return_data.size >=′ 32
                                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      require ext_code.size(_to)
                                                                                      call _to with:
                                                                                           gas gas_remaining wei
                                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                      if not ext_call.success:
                                                                                          if not return_data.size:
                                                                                              if not _data.length:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with _data[all]
                                                                                          else:
                                                                                              if not return_data.size:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                                      else:
                                                                                          require return_data.size >=′ 32
                                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                      else:
                                                          if tokenByIndex.length < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                  revert with 'NH{q', 50
                                                              else:
                                                                  if stor9[_tokenId] >= tokenByIndex.length:
                                                                      revert with 'NH{q', 50
                                                                  else:
                                                                      tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                                      stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                                      stor9[_tokenId] = 0
                                                                      if not tokenByIndex.length:
                                                                          revert with 'NH{q', 49
                                                                      else:
                                                                          tokenByIndex[tokenByIndex.length] = 0
                                                                          tokenByIndex.length--
                                                                          approved[_tokenId] = 0
                                                                          if not ownerOf[_tokenId]:
                                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                                          else:
                                                                              log Approval(
                                                                                    address owner=ownerOf[_tokenId],
                                                                                    address spender=0,
                                                                                    uint256 value=_tokenId)
                                                                              if balanceOf[addr(_from)] < 1:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_from)]--
                                                                                  if balanceOf[addr(_to)] > -2:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_to)]++
                                                                                      ownerOf[_tokenId] = _to
                                                                                      log Transfer(
                                                                                            address from=_from,
                                                                                            address to=_to,
                                                                                            uint256 value=_tokenId)
                                                                                      if ext_code.size(_to) <= 0:
                                                                                          stop
                                                                                      else:
                                                                                          if ceil32(_data.length) <= _data.length:
                                                                                              require ext_code.size(_to)
                                                                                              call _to with:
                                                                                                   gas gas_remaining wei
                                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      if not _data.length:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with _data[all]
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              require ext_code.size(_to)
                                                                                              call _to with:
                                                                                                   gas gas_remaining wei
                                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      if not _data.length:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with _data[all]
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                  else:
                                                      tokenOfOwnerByIndex[addr(_from)][stor7[_tokenId]] = tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1]
                                                      stor7[stor6[addr(_from)][stor3[addr(_from)] - 1]] = stor7[_tokenId]
                                                      stor7[_tokenId] = 0
                                                      tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                                      if _to:
                                                          if _to == _from:
                                                              approved[_tokenId] = 0
                                                              if not ownerOf[_tokenId]:
                                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                                              else:
                                                                  log Approval(
                                                                        address owner=ownerOf[_tokenId],
                                                                        address spender=0,
                                                                        uint256 value=_tokenId)
                                                                  if balanceOf[addr(_from)] < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_from)]--
                                                                      if balanceOf[addr(_to)] > -2:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_to)]++
                                                                          ownerOf[_tokenId] = _to
                                                                          log Transfer(
                                                                                address from=_from,
                                                                                address to=_to,
                                                                                uint256 value=_tokenId)
                                                                          if ext_code.size(_to) <= 0:
                                                                              stop
                                                                          else:
                                                                              if ceil32(_data.length) <= _data.length:
                                                                                  require ext_code.size(_to)
                                                                                  call _to with:
                                                                                       gas gas_remaining wei
                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          if not _data.length:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with _data[all]
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  require ext_code.size(_to)
                                                                                  call _to with:
                                                                                       gas gas_remaining wei
                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          if not _data.length:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with _data[all]
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                          else:
                                                              if not _to:
                                                                  revert with 0, 'ERC721: balance query for the zero address'
                                                              else:
                                                                  tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                                  stor7[_tokenId] = balanceOf[addr(_to)]
                                                                  approved[_tokenId] = 0
                                                                  if not ownerOf[_tokenId]:
                                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_tokenId],
                                                                            address spender=0,
                                                                            uint256 value=_tokenId)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_tokenId] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_tokenId)
                                                                              if ext_code.size(_to) <= 0:
                                                                                  stop
                                                                              else:
                                                                                  if ceil32(_data.length) <= _data.length:
                                                                                      require ext_code.size(_to)
                                                                                      call _to with:
                                                                                           gas gas_remaining wei
                                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                      if not ext_call.success:
                                                                                          if not return_data.size:
                                                                                              if not _data.length:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with _data[all]
                                                                                          else:
                                                                                              if not return_data.size:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                                      else:
                                                                                          require return_data.size >=′ 32
                                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      require ext_code.size(_to)
                                                                                      call _to with:
                                                                                           gas gas_remaining wei
                                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                      if not ext_call.success:
                                                                                          if not return_data.size:
                                                                                              if not _data.length:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with _data[all]
                                                                                          else:
                                                                                              if not return_data.size:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                                      else:
                                                                                          require return_data.size >=′ 32
                                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                      else:
                                                          if tokenByIndex.length < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                  revert with 'NH{q', 50
                                                              else:
                                                                  if stor9[_tokenId] >= tokenByIndex.length:
                                                                      revert with 'NH{q', 50
                                                                  else:
                                                                      tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                                      stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                                      stor9[_tokenId] = 0
                                                                      if not tokenByIndex.length:
                                                                          revert with 'NH{q', 49
                                                                      else:
                                                                          tokenByIndex[tokenByIndex.length] = 0
                                                                          tokenByIndex.length--
                                                                          approved[_tokenId] = 0
                                                                          if not ownerOf[_tokenId]:
                                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                                          else:
                                                                              log Approval(
                                                                                    address owner=ownerOf[_tokenId],
                                                                                    address spender=0,
                                                                                    uint256 value=_tokenId)
                                                                              if balanceOf[addr(_from)] < 1:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_from)]--
                                                                                  if balanceOf[addr(_to)] > -2:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_to)]++
                                                                                      ownerOf[_tokenId] = _to
                                                                                      log Transfer(
                                                                                            address from=_from,
                                                                                            address to=_to,
                                                                                            uint256 value=_tokenId)
                                                                                      if ext_code.size(_to) <= 0:
                                                                                          stop
                                                                                      else:
                                                                                          if ceil32(_data.length) <= _data.length:
                                                                                              require ext_code.size(_to)
                                                                                              call _to with:
                                                                                                   gas gas_remaining wei
                                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      if not _data.length:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with _data[all]
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              require ext_code.size(_to)
                                                                                              call _to with:
                                                                                                   gas gas_remaining wei
                                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      if not _data.length:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with _data[all]
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                  else:
                                      stor9[_tokenId] = tokenByIndex.length
                                      tokenByIndex.length++
                                      tokenByIndex[tokenByIndex.length] = _tokenId
                                      if _to:
                                          if _to == _from:
                                              approved[_tokenId] = 0
                                              if not ownerOf[_tokenId]:
                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                              else:
                                                  log Approval(
                                                        address owner=ownerOf[_tokenId],
                                                        address spender=0,
                                                        uint256 value=_tokenId)
                                                  if balanceOf[addr(_from)] < 1:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      balanceOf[addr(_from)]--
                                                      if balanceOf[addr(_to)] > -2:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_to)]++
                                                          ownerOf[_tokenId] = _to
                                                          log Transfer(
                                                                address from=_from,
                                                                address to=_to,
                                                                uint256 value=_tokenId)
                                                          if ext_code.size(_to) <= 0:
                                                              stop
                                                          else:
                                                              if ceil32(_data.length) <= _data.length:
                                                                  require ext_code.size(_to)
                                                                  call _to with:
                                                                       gas gas_remaining wei
                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                  if not ext_call.success:
                                                                      if not return_data.size:
                                                                          if not _data.length:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              revert with _data[all]
                                                                      else:
                                                                          if not return_data.size:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >=′ 32
                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                              else:
                                                                  require ext_code.size(_to)
                                                                  call _to with:
                                                                       gas gas_remaining wei
                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                  if not ext_call.success:
                                                                      if not return_data.size:
                                                                          if not _data.length:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              revert with _data[all]
                                                                      else:
                                                                          if not return_data.size:
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                  else:
                                                                      require return_data.size >=′ 32
                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                          else:
                                              if not _to:
                                                  revert with 0, 'ERC721: balance query for the zero address'
                                              else:
                                                  tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                  stor7[_tokenId] = balanceOf[addr(_to)]
                                                  approved[_tokenId] = 0
                                                  if not ownerOf[_tokenId]:
                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                  else:
                                                      log Approval(
                                                            address owner=ownerOf[_tokenId],
                                                            address spender=0,
                                                            uint256 value=_tokenId)
                                                      if balanceOf[addr(_from)] < 1:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          balanceOf[addr(_from)]--
                                                          if balanceOf[addr(_to)] > -2:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_to)]++
                                                              ownerOf[_tokenId] = _to
                                                              log Transfer(
                                                                    address from=_from,
                                                                    address to=_to,
                                                                    uint256 value=_tokenId)
                                                              if ext_code.size(_to) <= 0:
                                                                  stop
                                                              else:
                                                                  if ceil32(_data.length) <= _data.length:
                                                                      require ext_code.size(_to)
                                                                      call _to with:
                                                                           gas gas_remaining wei
                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                      if not ext_call.success:
                                                                          if not return_data.size:
                                                                              if not _data.length:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  revert with _data[all]
                                                                          else:
                                                                              if not return_data.size:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          require return_data.size >=′ 32
                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                  else:
                                                                      require ext_code.size(_to)
                                                                      call _to with:
                                                                           gas gas_remaining wei
                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                      if not ext_call.success:
                                                                          if not return_data.size:
                                                                              if not _data.length:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  revert with _data[all]
                                                                          else:
                                                                              if not return_data.size:
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                      else:
                                                                          require return_data.size >=′ 32
                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                      else:
                                          if tokenByIndex.length < 1:
                                              revert with 'NH{q', 17
                                          else:
                                              if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                  revert with 'NH{q', 50
                                              else:
                                                  if stor9[_tokenId] >= tokenByIndex.length:
                                                      revert with 'NH{q', 50
                                                  else:
                                                      tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                      stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                      stor9[_tokenId] = 0
                                                      if not tokenByIndex.length:
                                                          revert with 'NH{q', 49
                                                      else:
                                                          tokenByIndex[tokenByIndex.length] = 0
                                                          tokenByIndex.length--
                                                          approved[_tokenId] = 0
                                                          if not ownerOf[_tokenId]:
                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                          else:
                                                              log Approval(
                                                                    address owner=ownerOf[_tokenId],
                                                                    address spender=0,
                                                                    uint256 value=_tokenId)
                                                              if balanceOf[addr(_from)] < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_from)]--
                                                                  if balanceOf[addr(_to)] > -2:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_to)]++
                                                                      ownerOf[_tokenId] = _to
                                                                      log Transfer(
                                                                            address from=_from,
                                                                            address to=_to,
                                                                            uint256 value=_tokenId)
                                                                      if ext_code.size(_to) <= 0:
                                                                          stop
                                                                      else:
                                                                          if ceil32(_data.length) <= _data.length:
                                                                              require ext_code.size(_to)
                                                                              call _to with:
                                                                                   gas gas_remaining wei
                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                              if not ext_call.success:
                                                                                  if not return_data.size:
                                                                                      if not _data.length:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with _data[all]
                                                                                  else:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require return_data.size >=′ 32
                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              require ext_code.size(_to)
                                                                              call _to with:
                                                                                   gas gas_remaining wei
                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                              if not ext_call.success:
                                                                                  if not return_data.size:
                                                                                      if not _data.length:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with _data[all]
                                                                                  else:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require return_data.size >=′ 32
                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                  else:
                      if not ownerOf[_tokenId]:
                          revert with 0, 'ERC721: approved query for nonexistent token'
                      else:
                          if approved[_tokenId] == caller:
                              if not ownerOf[_tokenId]:
                                  revert with 0, 'ERC721: owner query for nonexistent token'
                              else:
                                  if ownerOf[_tokenId] != _from:
                                      revert with 0, 'ERC721: transfer of token that is not own'
                                  else:
                                      if not _to:
                                          revert with 0, 'ERC721: transfer to the zero address'
                                      else:
                                          if _from:
                                              if _from == _to:
                                                  if _to:
                                                      if _to == _from:
                                                          approved[_tokenId] = 0
                                                          if not ownerOf[_tokenId]:
                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                          else:
                                                              log Approval(
                                                                    address owner=ownerOf[_tokenId],
                                                                    address spender=0,
                                                                    uint256 value=_tokenId)
                                                              if balanceOf[addr(_from)] < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_from)]--
                                                                  if balanceOf[addr(_to)] > -2:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_to)]++
                                                                      ownerOf[_tokenId] = _to
                                                                      log Transfer(
                                                                            address from=_from,
                                                                            address to=_to,
                                                                            uint256 value=_tokenId)
                                                                      if ext_code.size(_to) <= 0:
                                                                          stop
                                                                      else:
                                                                          if ceil32(_data.length) <= _data.length:
                                                                              require ext_code.size(_to)
                                                                              call _to with:
                                                                                   gas gas_remaining wei
                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                              if not ext_call.success:
                                                                                  if not return_data.size:
                                                                                      if not _data.length:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with _data[all]
                                                                                  else:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require return_data.size >=′ 32
                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              require ext_code.size(_to)
                                                                              call _to with:
                                                                                   gas gas_remaining wei
                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                              if not ext_call.success:
                                                                                  if not return_data.size:
                                                                                      if not _data.length:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with _data[all]
                                                                                  else:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require return_data.size >=′ 32
                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                      else:
                                                          if not _to:
                                                              revert with 0, 'ERC721: balance query for the zero address'
                                                          else:
                                                              tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                              stor7[_tokenId] = balanceOf[addr(_to)]
                                                              approved[_tokenId] = 0
                                                              if not ownerOf[_tokenId]:
                                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                                              else:
                                                                  log Approval(
                                                                        address owner=ownerOf[_tokenId],
                                                                        address spender=0,
                                                                        uint256 value=_tokenId)
                                                                  if balanceOf[addr(_from)] < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_from)]--
                                                                      if balanceOf[addr(_to)] > -2:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_to)]++
                                                                          ownerOf[_tokenId] = _to
                                                                          log Transfer(
                                                                                address from=_from,
                                                                                address to=_to,
                                                                                uint256 value=_tokenId)
                                                                          if ext_code.size(_to) <= 0:
                                                                              stop
                                                                          else:
                                                                              if ceil32(_data.length) <= _data.length:
                                                                                  require ext_code.size(_to)
                                                                                  call _to with:
                                                                                       gas gas_remaining wei
                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          if not _data.length:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with _data[all]
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  require ext_code.size(_to)
                                                                                  call _to with:
                                                                                       gas gas_remaining wei
                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          if not _data.length:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with _data[all]
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                  else:
                                                      if tokenByIndex.length < 1:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                              revert with 'NH{q', 50
                                                          else:
                                                              if stor9[_tokenId] >= tokenByIndex.length:
                                                                  revert with 'NH{q', 50
                                                              else:
                                                                  tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                                  stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                                  stor9[_tokenId] = 0
                                                                  if not tokenByIndex.length:
                                                                      revert with 'NH{q', 49
                                                                  else:
                                                                      tokenByIndex[tokenByIndex.length] = 0
                                                                      tokenByIndex.length--
                                                                      approved[_tokenId] = 0
                                                                      if not ownerOf[_tokenId]:
                                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                                      else:
                                                                          log Approval(
                                                                                address owner=ownerOf[_tokenId],
                                                                                address spender=0,
                                                                                uint256 value=_tokenId)
                                                                          if balanceOf[addr(_from)] < 1:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_from)]--
                                                                              if balanceOf[addr(_to)] > -2:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_to)]++
                                                                                  ownerOf[_tokenId] = _to
                                                                                  log Transfer(
                                                                                        address from=_from,
                                                                                        address to=_to,
                                                                                        uint256 value=_tokenId)
                                                                                  if ext_code.size(_to) <= 0:
                                                                                      stop
                                                                                  else:
                                                                                      if ceil32(_data.length) <= _data.length:
                                                                                          require ext_code.size(_to)
                                                                                          call _to with:
                                                                                               gas gas_remaining wei
                                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                          if not ext_call.success:
                                                                                              if not return_data.size:
                                                                                                  if not _data.length:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with _data[all]
                                                                                              else:
                                                                                                  if not return_data.size:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                          else:
                                                                                              require return_data.size >=′ 32
                                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          require ext_code.size(_to)
                                                                                          call _to with:
                                                                                               gas gas_remaining wei
                                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                          if not ext_call.success:
                                                                                              if not return_data.size:
                                                                                                  if not _data.length:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with _data[all]
                                                                                              else:
                                                                                                  if not return_data.size:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                          else:
                                                                                              require return_data.size >=′ 32
                                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                              else:
                                                  if not _from:
                                                      revert with 0, 'ERC721: balance query for the zero address'
                                                  else:
                                                      if balanceOf[addr(_from)] < 1:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          if stor7[_tokenId] == balanceOf[addr(_from)] - 1:
                                                              stor7[_tokenId] = 0
                                                              tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                                              if _to:
                                                                  if _to == _from:
                                                                      approved[_tokenId] = 0
                                                                      if not ownerOf[_tokenId]:
                                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                                      else:
                                                                          log Approval(
                                                                                address owner=ownerOf[_tokenId],
                                                                                address spender=0,
                                                                                uint256 value=_tokenId)
                                                                          if balanceOf[addr(_from)] < 1:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_from)]--
                                                                              if balanceOf[addr(_to)] > -2:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_to)]++
                                                                                  ownerOf[_tokenId] = _to
                                                                                  log Transfer(
                                                                                        address from=_from,
                                                                                        address to=_to,
                                                                                        uint256 value=_tokenId)
                                                                                  if ext_code.size(_to) <= 0:
                                                                                      stop
                                                                                  else:
                                                                                      if ceil32(_data.length) <= _data.length:
                                                                                          require ext_code.size(_to)
                                                                                          call _to with:
                                                                                               gas gas_remaining wei
                                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                          if not ext_call.success:
                                                                                              if not return_data.size:
                                                                                                  if not _data.length:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with _data[all]
                                                                                              else:
                                                                                                  if not return_data.size:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                          else:
                                                                                              require return_data.size >=′ 32
                                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          require ext_code.size(_to)
                                                                                          call _to with:
                                                                                               gas gas_remaining wei
                                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                          if not ext_call.success:
                                                                                              if not return_data.size:
                                                                                                  if not _data.length:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with _data[all]
                                                                                              else:
                                                                                                  if not return_data.size:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                          else:
                                                                                              require return_data.size >=′ 32
                                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                  else:
                                                                      if not _to:
                                                                          revert with 0, 'ERC721: balance query for the zero address'
                                                                      else:
                                                                          tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                                          stor7[_tokenId] = balanceOf[addr(_to)]
                                                                          approved[_tokenId] = 0
                                                                          if not ownerOf[_tokenId]:
                                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                                          else:
                                                                              log Approval(
                                                                                    address owner=ownerOf[_tokenId],
                                                                                    address spender=0,
                                                                                    uint256 value=_tokenId)
                                                                              if balanceOf[addr(_from)] < 1:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_from)]--
                                                                                  if balanceOf[addr(_to)] > -2:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_to)]++
                                                                                      ownerOf[_tokenId] = _to
                                                                                      log Transfer(
                                                                                            address from=_from,
                                                                                            address to=_to,
                                                                                            uint256 value=_tokenId)
                                                                                      if ext_code.size(_to) <= 0:
                                                                                          stop
                                                                                      else:
                                                                                          if ceil32(_data.length) <= _data.length:
                                                                                              require ext_code.size(_to)
                                                                                              call _to with:
                                                                                                   gas gas_remaining wei
                                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      if not _data.length:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with _data[all]
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              require ext_code.size(_to)
                                                                                              call _to with:
                                                                                                   gas gas_remaining wei
                                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      if not _data.length:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with _data[all]
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                              else:
                                                                  if tokenByIndex.length < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                          revert with 'NH{q', 50
                                                                      else:
                                                                          if stor9[_tokenId] >= tokenByIndex.length:
                                                                              revert with 'NH{q', 50
                                                                          else:
                                                                              tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                                              stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                                              stor9[_tokenId] = 0
                                                                              if not tokenByIndex.length:
                                                                                  revert with 'NH{q', 49
                                                                              else:
                                                                                  tokenByIndex[tokenByIndex.length] = 0
                                                                                  tokenByIndex.length--
                                                                                  approved[_tokenId] = 0
                                                                                  if not ownerOf[_tokenId]:
                                                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                                                  else:
                                                                                      log Approval(
                                                                                            address owner=ownerOf[_tokenId],
                                                                                            address spender=0,
                                                                                            uint256 value=_tokenId)
                                                                                      if balanceOf[addr(_from)] < 1:
                                                                                          revert with 'NH{q', 17
                                                                                      else:
                                                                                          balanceOf[addr(_from)]--
                                                                                          if balanceOf[addr(_to)] > -2:
                                                                                              revert with 'NH{q', 17
                                                                                          else:
                                                                                              balanceOf[addr(_to)]++
                                                                                              ownerOf[_tokenId] = _to
                                                                                              log Transfer(
                                                                                                    address from=_from,
                                                                                                    address to=_to,
                                                                                                    uint256 value=_tokenId)
                                                                                              if ext_code.size(_to) <= 0:
                                                                                                  stop
                                                                                              else:
                                                                                                  if ceil32(_data.length) <= _data.length:
                                                                                                      require ext_code.size(_to)
                                                                                                      call _to with:
                                                                                                           gas gas_remaining wei
                                                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                                      if not ext_call.success:
                                                                                                          if not return_data.size:
                                                                                                              if not _data.length:
                                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                              else:
                                                                                                                  revert with _data[all]
                                                                                                          else:
                                                                                                              if not return_data.size:
                                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                              else:
                                                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                                                      else:
                                                                                                          require return_data.size >=′ 32
                                                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      require ext_code.size(_to)
                                                                                                      call _to with:
                                                                                                           gas gas_remaining wei
                                                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                                      if not ext_call.success:
                                                                                                          if not return_data.size:
                                                                                                              if not _data.length:
                                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                              else:
                                                                                                                  revert with _data[all]
                                                                                                          else:
                                                                                                              if not return_data.size:
                                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                              else:
                                                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                                                      else:
                                                                                                          require return_data.size >=′ 32
                                                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                          else:
                                                              tokenOfOwnerByIndex[addr(_from)][stor7[_tokenId]] = tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1]
                                                              stor7[stor6[addr(_from)][stor3[addr(_from)] - 1]] = stor7[_tokenId]
                                                              stor7[_tokenId] = 0
                                                              tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                                              if _to:
                                                                  if _to == _from:
                                                                      approved[_tokenId] = 0
                                                                      if not ownerOf[_tokenId]:
                                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                                      else:
                                                                          log Approval(
                                                                                address owner=ownerOf[_tokenId],
                                                                                address spender=0,
                                                                                uint256 value=_tokenId)
                                                                          if balanceOf[addr(_from)] < 1:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_from)]--
                                                                              if balanceOf[addr(_to)] > -2:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_to)]++
                                                                                  ownerOf[_tokenId] = _to
                                                                                  log Transfer(
                                                                                        address from=_from,
                                                                                        address to=_to,
                                                                                        uint256 value=_tokenId)
                                                                                  if ext_code.size(_to) <= 0:
                                                                                      stop
                                                                                  else:
                                                                                      if ceil32(_data.length) <= _data.length:
                                                                                          require ext_code.size(_to)
                                                                                          call _to with:
                                                                                               gas gas_remaining wei
                                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                          if not ext_call.success:
                                                                                              if not return_data.size:
                                                                                                  if not _data.length:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with _data[all]
                                                                                              else:
                                                                                                  if not return_data.size:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                          else:
                                                                                              require return_data.size >=′ 32
                                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          require ext_code.size(_to)
                                                                                          call _to with:
                                                                                               gas gas_remaining wei
                                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                          if not ext_call.success:
                                                                                              if not return_data.size:
                                                                                                  if not _data.length:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with _data[all]
                                                                                              else:
                                                                                                  if not return_data.size:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                          else:
                                                                                              require return_data.size >=′ 32
                                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                  else:
                                                                      if not _to:
                                                                          revert with 0, 'ERC721: balance query for the zero address'
                                                                      else:
                                                                          tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                                          stor7[_tokenId] = balanceOf[addr(_to)]
                                                                          approved[_tokenId] = 0
                                                                          if not ownerOf[_tokenId]:
                                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                                          else:
                                                                              log Approval(
                                                                                    address owner=ownerOf[_tokenId],
                                                                                    address spender=0,
                                                                                    uint256 value=_tokenId)
                                                                              if balanceOf[addr(_from)] < 1:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_from)]--
                                                                                  if balanceOf[addr(_to)] > -2:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_to)]++
                                                                                      ownerOf[_tokenId] = _to
                                                                                      log Transfer(
                                                                                            address from=_from,
                                                                                            address to=_to,
                                                                                            uint256 value=_tokenId)
                                                                                      if ext_code.size(_to) <= 0:
                                                                                          stop
                                                                                      else:
                                                                                          if ceil32(_data.length) <= _data.length:
                                                                                              require ext_code.size(_to)
                                                                                              call _to with:
                                                                                                   gas gas_remaining wei
                                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      if not _data.length:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with _data[all]
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              require ext_code.size(_to)
                                                                                              call _to with:
                                                                                                   gas gas_remaining wei
                                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      if not _data.length:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with _data[all]
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                              else:
                                                                  if tokenByIndex.length < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                          revert with 'NH{q', 50
                                                                      else:
                                                                          if stor9[_tokenId] >= tokenByIndex.length:
                                                                              revert with 'NH{q', 50
                                                                          else:
                                                                              tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                                              stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                                              stor9[_tokenId] = 0
                                                                              if not tokenByIndex.length:
                                                                                  revert with 'NH{q', 49
                                                                              else:
                                                                                  tokenByIndex[tokenByIndex.length] = 0
                                                                                  tokenByIndex.length--
                                                                                  approved[_tokenId] = 0
                                                                                  if not ownerOf[_tokenId]:
                                                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                                                  else:
                                                                                      log Approval(
                                                                                            address owner=ownerOf[_tokenId],
                                                                                            address spender=0,
                                                                                            uint256 value=_tokenId)
                                                                                      if balanceOf[addr(_from)] < 1:
                                                                                          revert with 'NH{q', 17
                                                                                      else:
                                                                                          balanceOf[addr(_from)]--
                                                                                          if balanceOf[addr(_to)] > -2:
                                                                                              revert with 'NH{q', 17
                                                                                          else:
                                                                                              balanceOf[addr(_to)]++
                                                                                              ownerOf[_tokenId] = _to
                                                                                              log Transfer(
                                                                                                    address from=_from,
                                                                                                    address to=_to,
                                                                                                    uint256 value=_tokenId)
                                                                                              if ext_code.size(_to) <= 0:
                                                                                                  stop
                                                                                              else:
                                                                                                  if ceil32(_data.length) <= _data.length:
                                                                                                      require ext_code.size(_to)
                                                                                                      call _to with:
                                                                                                           gas gas_remaining wei
                                                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                                      if not ext_call.success:
                                                                                                          if not return_data.size:
                                                                                                              if not _data.length:
                                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                              else:
                                                                                                                  revert with _data[all]
                                                                                                          else:
                                                                                                              if not return_data.size:
                                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                              else:
                                                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                                                      else:
                                                                                                          require return_data.size >=′ 32
                                                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      require ext_code.size(_to)
                                                                                                      call _to with:
                                                                                                           gas gas_remaining wei
                                                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                                      if not ext_call.success:
                                                                                                          if not return_data.size:
                                                                                                              if not _data.length:
                                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                              else:
                                                                                                                  revert with _data[all]
                                                                                                          else:
                                                                                                              if not return_data.size:
                                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                              else:
                                                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                                                      else:
                                                                                                          require return_data.size >=′ 32
                                                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                          else:
                                              stor9[_tokenId] = tokenByIndex.length
                                              tokenByIndex.length++
                                              tokenByIndex[tokenByIndex.length] = _tokenId
                                              if _to:
                                                  if _to == _from:
                                                      approved[_tokenId] = 0
                                                      if not ownerOf[_tokenId]:
                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                      else:
                                                          log Approval(
                                                                address owner=ownerOf[_tokenId],
                                                                address spender=0,
                                                                uint256 value=_tokenId)
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              balanceOf[addr(_from)]--
                                                              if balanceOf[addr(_to)] > -2:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_to)]++
                                                                  ownerOf[_tokenId] = _to
                                                                  log Transfer(
                                                                        address from=_from,
                                                                        address to=_to,
                                                                        uint256 value=_tokenId)
                                                                  if ext_code.size(_to) <= 0:
                                                                      stop
                                                                  else:
                                                                      if ceil32(_data.length) <= _data.length:
                                                                          require ext_code.size(_to)
                                                                          call _to with:
                                                                               gas gas_remaining wei
                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                          if not ext_call.success:
                                                                              if not return_data.size:
                                                                                  if not _data.length:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      revert with _data[all]
                                                                              else:
                                                                                  if not return_data.size:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              require return_data.size >=′ 32
                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                      else:
                                                                          require ext_code.size(_to)
                                                                          call _to with:
                                                                               gas gas_remaining wei
                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                          if not ext_call.success:
                                                                              if not return_data.size:
                                                                                  if not _data.length:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      revert with _data[all]
                                                                              else:
                                                                                  if not return_data.size:
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                          else:
                                                                              require return_data.size >=′ 32
                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                  else:
                                                      if not _to:
                                                          revert with 0, 'ERC721: balance query for the zero address'
                                                      else:
                                                          tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                          stor7[_tokenId] = balanceOf[addr(_to)]
                                                          approved[_tokenId] = 0
                                                          if not ownerOf[_tokenId]:
                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                          else:
                                                              log Approval(
                                                                    address owner=ownerOf[_tokenId],
                                                                    address spender=0,
                                                                    uint256 value=_tokenId)
                                                              if balanceOf[addr(_from)] < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_from)]--
                                                                  if balanceOf[addr(_to)] > -2:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_to)]++
                                                                      ownerOf[_tokenId] = _to
                                                                      log Transfer(
                                                                            address from=_from,
                                                                            address to=_to,
                                                                            uint256 value=_tokenId)
                                                                      if ext_code.size(_to) <= 0:
                                                                          stop
                                                                      else:
                                                                          if ceil32(_data.length) <= _data.length:
                                                                              require ext_code.size(_to)
                                                                              call _to with:
                                                                                   gas gas_remaining wei
                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                              if not ext_call.success:
                                                                                  if not return_data.size:
                                                                                      if not _data.length:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with _data[all]
                                                                                  else:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require return_data.size >=′ 32
                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              require ext_code.size(_to)
                                                                              call _to with:
                                                                                   gas gas_remaining wei
                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                              if not ext_call.success:
                                                                                  if not return_data.size:
                                                                                      if not _data.length:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with _data[all]
                                                                                  else:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require return_data.size >=′ 32
                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                              else:
                                                  if tokenByIndex.length < 1:
                                                      revert with 'NH{q', 17
                                                  else:
                                                      if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                          revert with 'NH{q', 50
                                                      else:
                                                          if stor9[_tokenId] >= tokenByIndex.length:
                                                              revert with 'NH{q', 50
                                                          else:
                                                              tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                              stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                              stor9[_tokenId] = 0
                                                              if not tokenByIndex.length:
                                                                  revert with 'NH{q', 49
                                                              else:
                                                                  tokenByIndex[tokenByIndex.length] = 0
                                                                  tokenByIndex.length--
                                                                  approved[_tokenId] = 0
                                                                  if not ownerOf[_tokenId]:
                                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_tokenId],
                                                                            address spender=0,
                                                                            uint256 value=_tokenId)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_tokenId] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_tokenId)
                                                                              if ext_code.size(_to) <= 0:
                                                                                  stop
                                                                              else:
                                                                                  if ceil32(_data.length) <= _data.length:
                                                                                      require ext_code.size(_to)
                                                                                      call _to with:
                                                                                           gas gas_remaining wei
                                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                      if not ext_call.success:
                                                                                          if not return_data.size:
                                                                                              if not _data.length:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with _data[all]
                                                                                          else:
                                                                                              if not return_data.size:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                                      else:
                                                                                          require return_data.size >=′ 32
                                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      require ext_code.size(_to)
                                                                                      call _to with:
                                                                                           gas gas_remaining wei
                                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                      if not ext_call.success:
                                                                                          if not return_data.size:
                                                                                              if not _data.length:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with _data[all]
                                                                                          else:
                                                                                              if not return_data.size:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                                      else:
                                                                                          require return_data.size >=′ 32
                                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                          else:
                              if not stor5[stor2[_tokenId]][caller]:
                                  revert with 0, 'ERC721: transfer caller is not owner nor approved'
                              else:
                                  if not ownerOf[_tokenId]:
                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                  else:
                                      if ownerOf[_tokenId] != _from:
                                          revert with 0, 'ERC721: transfer of token that is not own'
                                      else:
                                          if not _to:
                                              revert with 0, 'ERC721: transfer to the zero address'
                                          else:
                                              if _from:
                                                  if _from == _to:
                                                      if _to:
                                                          if _to == _from:
                                                              approved[_tokenId] = 0
                                                              if not ownerOf[_tokenId]:
                                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                                              else:
                                                                  log Approval(
                                                                        address owner=ownerOf[_tokenId],
                                                                        address spender=0,
                                                                        uint256 value=_tokenId)
                                                                  if balanceOf[addr(_from)] < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_from)]--
                                                                      if balanceOf[addr(_to)] > -2:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_to)]++
                                                                          ownerOf[_tokenId] = _to
                                                                          log Transfer(
                                                                                address from=_from,
                                                                                address to=_to,
                                                                                uint256 value=_tokenId)
                                                                          if ext_code.size(_to) <= 0:
                                                                              stop
                                                                          else:
                                                                              if ceil32(_data.length) <= _data.length:
                                                                                  require ext_code.size(_to)
                                                                                  call _to with:
                                                                                       gas gas_remaining wei
                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          if not _data.length:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with _data[all]
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  require ext_code.size(_to)
                                                                                  call _to with:
                                                                                       gas gas_remaining wei
                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          if not _data.length:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with _data[all]
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                          else:
                                                              if not _to:
                                                                  revert with 0, 'ERC721: balance query for the zero address'
                                                              else:
                                                                  tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                                  stor7[_tokenId] = balanceOf[addr(_to)]
                                                                  approved[_tokenId] = 0
                                                                  if not ownerOf[_tokenId]:
                                                                      revert with 0, 'ERC721: owner query for nonexistent token'
                                                                  else:
                                                                      log Approval(
                                                                            address owner=ownerOf[_tokenId],
                                                                            address spender=0,
                                                                            uint256 value=_tokenId)
                                                                      if balanceOf[addr(_from)] < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_from)]--
                                                                          if balanceOf[addr(_to)] > -2:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_to)]++
                                                                              ownerOf[_tokenId] = _to
                                                                              log Transfer(
                                                                                    address from=_from,
                                                                                    address to=_to,
                                                                                    uint256 value=_tokenId)
                                                                              if ext_code.size(_to) <= 0:
                                                                                  stop
                                                                              else:
                                                                                  if ceil32(_data.length) <= _data.length:
                                                                                      require ext_code.size(_to)
                                                                                      call _to with:
                                                                                           gas gas_remaining wei
                                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                      if not ext_call.success:
                                                                                          if not return_data.size:
                                                                                              if not _data.length:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with _data[all]
                                                                                          else:
                                                                                              if not return_data.size:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                                      else:
                                                                                          require return_data.size >=′ 32
                                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                  else:
                                                                                      require ext_code.size(_to)
                                                                                      call _to with:
                                                                                           gas gas_remaining wei
                                                                                          args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                      if not ext_call.success:
                                                                                          if not return_data.size:
                                                                                              if not _data.length:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with _data[all]
                                                                                          else:
                                                                                              if not return_data.size:
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                                                      else:
                                                                                          require return_data.size >=′ 32
                                                                                          require not 0, ext_call.return_data[4 len 28]
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                      else:
                                                          if tokenByIndex.length < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                  revert with 'NH{q', 50
                                                              else:
                                                                  if stor9[_tokenId] >= tokenByIndex.length:
                                                                      revert with 'NH{q', 50
                                                                  else:
                                                                      tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                                      stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                                      stor9[_tokenId] = 0
                                                                      if not tokenByIndex.length:
                                                                          revert with 'NH{q', 49
                                                                      else:
                                                                          tokenByIndex[tokenByIndex.length] = 0
                                                                          tokenByIndex.length--
                                                                          approved[_tokenId] = 0
                                                                          if not ownerOf[_tokenId]:
                                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                                          else:
                                                                              log Approval(
                                                                                    address owner=ownerOf[_tokenId],
                                                                                    address spender=0,
                                                                                    uint256 value=_tokenId)
                                                                              if balanceOf[addr(_from)] < 1:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_from)]--
                                                                                  if balanceOf[addr(_to)] > -2:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_to)]++
                                                                                      ownerOf[_tokenId] = _to
                                                                                      log Transfer(
                                                                                            address from=_from,
                                                                                            address to=_to,
                                                                                            uint256 value=_tokenId)
                                                                                      if ext_code.size(_to) <= 0:
                                                                                          stop
                                                                                      else:
                                                                                          if ceil32(_data.length) <= _data.length:
                                                                                              require ext_code.size(_to)
                                                                                              call _to with:
                                                                                                   gas gas_remaining wei
                                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      if not _data.length:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with _data[all]
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              require ext_code.size(_to)
                                                                                              call _to with:
                                                                                                   gas gas_remaining wei
                                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      if not _data.length:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with _data[all]
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                  else:
                                                      if not _from:
                                                          revert with 0, 'ERC721: balance query for the zero address'
                                                      else:
                                                          if balanceOf[addr(_from)] < 1:
                                                              revert with 'NH{q', 17
                                                          else:
                                                              if stor7[_tokenId] == balanceOf[addr(_from)] - 1:
                                                                  stor7[_tokenId] = 0
                                                                  tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                                                  if _to:
                                                                      if _to == _from:
                                                                          approved[_tokenId] = 0
                                                                          if not ownerOf[_tokenId]:
                                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                                          else:
                                                                              log Approval(
                                                                                    address owner=ownerOf[_tokenId],
                                                                                    address spender=0,
                                                                                    uint256 value=_tokenId)
                                                                              if balanceOf[addr(_from)] < 1:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_from)]--
                                                                                  if balanceOf[addr(_to)] > -2:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_to)]++
                                                                                      ownerOf[_tokenId] = _to
                                                                                      log Transfer(
                                                                                            address from=_from,
                                                                                            address to=_to,
                                                                                            uint256 value=_tokenId)
                                                                                      if ext_code.size(_to) <= 0:
                                                                                          stop
                                                                                      else:
                                                                                          if ceil32(_data.length) <= _data.length:
                                                                                              require ext_code.size(_to)
                                                                                              call _to with:
                                                                                                   gas gas_remaining wei
                                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      if not _data.length:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with _data[all]
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              require ext_code.size(_to)
                                                                                              call _to with:
                                                                                                   gas gas_remaining wei
                                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      if not _data.length:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with _data[all]
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                      else:
                                                                          if not _to:
                                                                              revert with 0, 'ERC721: balance query for the zero address'
                                                                          else:
                                                                              tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                                              stor7[_tokenId] = balanceOf[addr(_to)]
                                                                              approved[_tokenId] = 0
                                                                              if not ownerOf[_tokenId]:
                                                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                                                              else:
                                                                                  log Approval(
                                                                                        address owner=ownerOf[_tokenId],
                                                                                        address spender=0,
                                                                                        uint256 value=_tokenId)
                                                                                  if balanceOf[addr(_from)] < 1:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_from)]--
                                                                                      if balanceOf[addr(_to)] > -2:
                                                                                          revert with 'NH{q', 17
                                                                                      else:
                                                                                          balanceOf[addr(_to)]++
                                                                                          ownerOf[_tokenId] = _to
                                                                                          log Transfer(
                                                                                                address from=_from,
                                                                                                address to=_to,
                                                                                                uint256 value=_tokenId)
                                                                                          if ext_code.size(_to) <= 0:
                                                                                              stop
                                                                                          else:
                                                                                              if ceil32(_data.length) <= _data.length:
                                                                                                  require ext_code.size(_to)
                                                                                                  call _to with:
                                                                                                       gas gas_remaining wei
                                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                                  if not ext_call.success:
                                                                                                      if not return_data.size:
                                                                                                          if not _data.length:
                                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                          else:
                                                                                                              revert with _data[all]
                                                                                                      else:
                                                                                                          if not return_data.size:
                                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                          else:
                                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                                  else:
                                                                                                      require return_data.size >=′ 32
                                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  require ext_code.size(_to)
                                                                                                  call _to with:
                                                                                                       gas gas_remaining wei
                                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                                  if not ext_call.success:
                                                                                                      if not return_data.size:
                                                                                                          if not _data.length:
                                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                          else:
                                                                                                              revert with _data[all]
                                                                                                      else:
                                                                                                          if not return_data.size:
                                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                          else:
                                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                                  else:
                                                                                                      require return_data.size >=′ 32
                                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                  else:
                                                                      if tokenByIndex.length < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                              revert with 'NH{q', 50
                                                                          else:
                                                                              if stor9[_tokenId] >= tokenByIndex.length:
                                                                                  revert with 'NH{q', 50
                                                                              else:
                                                                                  tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                                                  stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                                                  stor9[_tokenId] = 0
                                                                                  if not tokenByIndex.length:
                                                                                      revert with 'NH{q', 49
                                                                                  else:
                                                                                      tokenByIndex[tokenByIndex.length] = 0
                                                                                      tokenByIndex.length--
                                                                                      approved[_tokenId] = 0
                                                                                      if not ownerOf[_tokenId]:
                                                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                                                      else:
                                                                                          log Approval(
                                                                                                address owner=ownerOf[_tokenId],
                                                                                                address spender=0,
                                                                                                uint256 value=_tokenId)
                                                                                          if balanceOf[addr(_from)] < 1:
                                                                                              revert with 'NH{q', 17
                                                                                          else:
                                                                                              balanceOf[addr(_from)]--
                                                                                              if balanceOf[addr(_to)] > -2:
                                                                                                  revert with 'NH{q', 17
                                                                                              else:
                                                                                                  balanceOf[addr(_to)]++
                                                                                                  ownerOf[_tokenId] = _to
                                                                                                  log Transfer(
                                                                                                        address from=_from,
                                                                                                        address to=_to,
                                                                                                        uint256 value=_tokenId)
                                                                                                  if ext_code.size(_to) <= 0:
                                                                                                      stop
                                                                                                  else:
                                                                                                      if ceil32(_data.length) <= _data.length:
                                                                                                          require ext_code.size(_to)
                                                                                                          call _to with:
                                                                                                               gas gas_remaining wei
                                                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                                          if not ext_call.success:
                                                                                                              if not return_data.size:
                                                                                                                  if not _data.length:
                                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                                  else:
                                                                                                                      revert with _data[all]
                                                                                                              else:
                                                                                                                  if not return_data.size:
                                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                                  else:
                                                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                                          else:
                                                                                                              require return_data.size >=′ 32
                                                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          require ext_code.size(_to)
                                                                                                          call _to with:
                                                                                                               gas gas_remaining wei
                                                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                                          if not ext_call.success:
                                                                                                              if not return_data.size:
                                                                                                                  if not _data.length:
                                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                                  else:
                                                                                                                      revert with _data[all]
                                                                                                              else:
                                                                                                                  if not return_data.size:
                                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                                  else:
                                                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                                          else:
                                                                                                              require return_data.size >=′ 32
                                                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                              else:
                                                                  tokenOfOwnerByIndex[addr(_from)][stor7[_tokenId]] = tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1]
                                                                  stor7[stor6[addr(_from)][stor3[addr(_from)] - 1]] = stor7[_tokenId]
                                                                  stor7[_tokenId] = 0
                                                                  tokenOfOwnerByIndex[addr(_from)][stor3[addr(_from)] - 1] = 0
                                                                  if _to:
                                                                      if _to == _from:
                                                                          approved[_tokenId] = 0
                                                                          if not ownerOf[_tokenId]:
                                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                                          else:
                                                                              log Approval(
                                                                                    address owner=ownerOf[_tokenId],
                                                                                    address spender=0,
                                                                                    uint256 value=_tokenId)
                                                                              if balanceOf[addr(_from)] < 1:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_from)]--
                                                                                  if balanceOf[addr(_to)] > -2:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_to)]++
                                                                                      ownerOf[_tokenId] = _to
                                                                                      log Transfer(
                                                                                            address from=_from,
                                                                                            address to=_to,
                                                                                            uint256 value=_tokenId)
                                                                                      if ext_code.size(_to) <= 0:
                                                                                          stop
                                                                                      else:
                                                                                          if ceil32(_data.length) <= _data.length:
                                                                                              require ext_code.size(_to)
                                                                                              call _to with:
                                                                                                   gas gas_remaining wei
                                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      if not _data.length:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with _data[all]
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              require ext_code.size(_to)
                                                                                              call _to with:
                                                                                                   gas gas_remaining wei
                                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                              if not ext_call.success:
                                                                                                  if not return_data.size:
                                                                                                      if not _data.length:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with _data[all]
                                                                                                  else:
                                                                                                      if not return_data.size:
                                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                                              else:
                                                                                                  require return_data.size >=′ 32
                                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                      else:
                                                                          if not _to:
                                                                              revert with 0, 'ERC721: balance query for the zero address'
                                                                          else:
                                                                              tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                                              stor7[_tokenId] = balanceOf[addr(_to)]
                                                                              approved[_tokenId] = 0
                                                                              if not ownerOf[_tokenId]:
                                                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                                                              else:
                                                                                  log Approval(
                                                                                        address owner=ownerOf[_tokenId],
                                                                                        address spender=0,
                                                                                        uint256 value=_tokenId)
                                                                                  if balanceOf[addr(_from)] < 1:
                                                                                      revert with 'NH{q', 17
                                                                                  else:
                                                                                      balanceOf[addr(_from)]--
                                                                                      if balanceOf[addr(_to)] > -2:
                                                                                          revert with 'NH{q', 17
                                                                                      else:
                                                                                          balanceOf[addr(_to)]++
                                                                                          ownerOf[_tokenId] = _to
                                                                                          log Transfer(
                                                                                                address from=_from,
                                                                                                address to=_to,
                                                                                                uint256 value=_tokenId)
                                                                                          if ext_code.size(_to) <= 0:
                                                                                              stop
                                                                                          else:
                                                                                              if ceil32(_data.length) <= _data.length:
                                                                                                  require ext_code.size(_to)
                                                                                                  call _to with:
                                                                                                       gas gas_remaining wei
                                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                                  if not ext_call.success:
                                                                                                      if not return_data.size:
                                                                                                          if not _data.length:
                                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                          else:
                                                                                                              revert with _data[all]
                                                                                                      else:
                                                                                                          if not return_data.size:
                                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                          else:
                                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                                  else:
                                                                                                      require return_data.size >=′ 32
                                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                              else:
                                                                                                  require ext_code.size(_to)
                                                                                                  call _to with:
                                                                                                       gas gas_remaining wei
                                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                                  if not ext_call.success:
                                                                                                      if not return_data.size:
                                                                                                          if not _data.length:
                                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                          else:
                                                                                                              revert with _data[all]
                                                                                                      else:
                                                                                                          if not return_data.size:
                                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                          else:
                                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                                  else:
                                                                                                      require return_data.size >=′ 32
                                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                  else:
                                                                      if tokenByIndex.length < 1:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                                              revert with 'NH{q', 50
                                                                          else:
                                                                              if stor9[_tokenId] >= tokenByIndex.length:
                                                                                  revert with 'NH{q', 50
                                                                              else:
                                                                                  tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                                                  stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                                                  stor9[_tokenId] = 0
                                                                                  if not tokenByIndex.length:
                                                                                      revert with 'NH{q', 49
                                                                                  else:
                                                                                      tokenByIndex[tokenByIndex.length] = 0
                                                                                      tokenByIndex.length--
                                                                                      approved[_tokenId] = 0
                                                                                      if not ownerOf[_tokenId]:
                                                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                                                      else:
                                                                                          log Approval(
                                                                                                address owner=ownerOf[_tokenId],
                                                                                                address spender=0,
                                                                                                uint256 value=_tokenId)
                                                                                          if balanceOf[addr(_from)] < 1:
                                                                                              revert with 'NH{q', 17
                                                                                          else:
                                                                                              balanceOf[addr(_from)]--
                                                                                              if balanceOf[addr(_to)] > -2:
                                                                                                  revert with 'NH{q', 17
                                                                                              else:
                                                                                                  balanceOf[addr(_to)]++
                                                                                                  ownerOf[_tokenId] = _to
                                                                                                  log Transfer(
                                                                                                        address from=_from,
                                                                                                        address to=_to,
                                                                                                        uint256 value=_tokenId)
                                                                                                  if ext_code.size(_to) <= 0:
                                                                                                      stop
                                                                                                  else:
                                                                                                      if ceil32(_data.length) <= _data.length:
                                                                                                          require ext_code.size(_to)
                                                                                                          call _to with:
                                                                                                               gas gas_remaining wei
                                                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                                          if not ext_call.success:
                                                                                                              if not return_data.size:
                                                                                                                  if not _data.length:
                                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                                  else:
                                                                                                                      revert with _data[all]
                                                                                                              else:
                                                                                                                  if not return_data.size:
                                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                                  else:
                                                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                                          else:
                                                                                                              require return_data.size >=′ 32
                                                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                      else:
                                                                                                          require ext_code.size(_to)
                                                                                                          call _to with:
                                                                                                               gas gas_remaining wei
                                                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                                          if not ext_call.success:
                                                                                                              if not return_data.size:
                                                                                                                  if not _data.length:
                                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                                  else:
                                                                                                                      revert with _data[all]
                                                                                                              else:
                                                                                                                  if not return_data.size:
                                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                                  else:
                                                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                                          else:
                                                                                                              require return_data.size >=′ 32
                                                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                              else:
                                                  stor9[_tokenId] = tokenByIndex.length
                                                  tokenByIndex.length++
                                                  tokenByIndex[tokenByIndex.length] = _tokenId
                                                  if _to:
                                                      if _to == _from:
                                                          approved[_tokenId] = 0
                                                          if not ownerOf[_tokenId]:
                                                              revert with 0, 'ERC721: owner query for nonexistent token'
                                                          else:
                                                              log Approval(
                                                                    address owner=ownerOf[_tokenId],
                                                                    address spender=0,
                                                                    uint256 value=_tokenId)
                                                              if balanceOf[addr(_from)] < 1:
                                                                  revert with 'NH{q', 17
                                                              else:
                                                                  balanceOf[addr(_from)]--
                                                                  if balanceOf[addr(_to)] > -2:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_to)]++
                                                                      ownerOf[_tokenId] = _to
                                                                      log Transfer(
                                                                            address from=_from,
                                                                            address to=_to,
                                                                            uint256 value=_tokenId)
                                                                      if ext_code.size(_to) <= 0:
                                                                          stop
                                                                      else:
                                                                          if ceil32(_data.length) <= _data.length:
                                                                              require ext_code.size(_to)
                                                                              call _to with:
                                                                                   gas gas_remaining wei
                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                              if not ext_call.success:
                                                                                  if not return_data.size:
                                                                                      if not _data.length:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with _data[all]
                                                                                  else:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require return_data.size >=′ 32
                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                          else:
                                                                              require ext_code.size(_to)
                                                                              call _to with:
                                                                                   gas gas_remaining wei
                                                                                  args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                              if not ext_call.success:
                                                                                  if not return_data.size:
                                                                                      if not _data.length:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with _data[all]
                                                                                  else:
                                                                                      if not return_data.size:
                                                                                          revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                              else:
                                                                                  require return_data.size >=′ 32
                                                                                  require not 0, ext_call.return_data[4 len 28]
                                                                                  revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                      else:
                                                          if not _to:
                                                              revert with 0, 'ERC721: balance query for the zero address'
                                                          else:
                                                              tokenOfOwnerByIndex[addr(_to)][stor3[addr(_to)]] = _tokenId
                                                              stor7[_tokenId] = balanceOf[addr(_to)]
                                                              approved[_tokenId] = 0
                                                              if not ownerOf[_tokenId]:
                                                                  revert with 0, 'ERC721: owner query for nonexistent token'
                                                              else:
                                                                  log Approval(
                                                                        address owner=ownerOf[_tokenId],
                                                                        address spender=0,
                                                                        uint256 value=_tokenId)
                                                                  if balanceOf[addr(_from)] < 1:
                                                                      revert with 'NH{q', 17
                                                                  else:
                                                                      balanceOf[addr(_from)]--
                                                                      if balanceOf[addr(_to)] > -2:
                                                                          revert with 'NH{q', 17
                                                                      else:
                                                                          balanceOf[addr(_to)]++
                                                                          ownerOf[_tokenId] = _to
                                                                          log Transfer(
                                                                                address from=_from,
                                                                                address to=_to,
                                                                                uint256 value=_tokenId)
                                                                          if ext_code.size(_to) <= 0:
                                                                              stop
                                                                          else:
                                                                              if ceil32(_data.length) <= _data.length:
                                                                                  require ext_code.size(_to)
                                                                                  call _to with:
                                                                                       gas gas_remaining wei
                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          if not _data.length:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with _data[all]
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                              else:
                                                                                  require ext_code.size(_to)
                                                                                  call _to with:
                                                                                       gas gas_remaining wei
                                                                                      args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                  if not ext_call.success:
                                                                                      if not return_data.size:
                                                                                          if not _data.length:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with _data[all]
                                                                                      else:
                                                                                          if not return_data.size:
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                          else:
                                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                                  else:
                                                                                      require return_data.size >=′ 32
                                                                                      require not 0, ext_call.return_data[4 len 28]
                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                  else:
                                                      if tokenByIndex.length < 1:
                                                          revert with 'NH{q', 17
                                                      else:
                                                          if tokenByIndex.length - 1 >= tokenByIndex.length:
                                                              revert with 'NH{q', 50
                                                          else:
                                                              if stor9[_tokenId] >= tokenByIndex.length:
                                                                  revert with 'NH{q', 50
                                                              else:
                                                                  tokenByIndex[stor9[_tokenId]] = tokenByIndex[tokenByIndex.length]
                                                                  stor9[stor8[stor8.length]] = stor9[_tokenId]
                                                                  stor9[_tokenId] = 0
                                                                  if not tokenByIndex.length:
                                                                      revert with 'NH{q', 49
                                                                  else:
                                                                      tokenByIndex[tokenByIndex.length] = 0
                                                                      tokenByIndex.length--
                                                                      approved[_tokenId] = 0
                                                                      if not ownerOf[_tokenId]:
                                                                          revert with 0, 'ERC721: owner query for nonexistent token'
                                                                      else:
                                                                          log Approval(
                                                                                address owner=ownerOf[_tokenId],
                                                                                address spender=0,
                                                                                uint256 value=_tokenId)
                                                                          if balanceOf[addr(_from)] < 1:
                                                                              revert with 'NH{q', 17
                                                                          else:
                                                                              balanceOf[addr(_from)]--
                                                                              if balanceOf[addr(_to)] > -2:
                                                                                  revert with 'NH{q', 17
                                                                              else:
                                                                                  balanceOf[addr(_to)]++
                                                                                  ownerOf[_tokenId] = _to
                                                                                  log Transfer(
                                                                                        address from=_from,
                                                                                        address to=_to,
                                                                                        uint256 value=_tokenId)
                                                                                  if ext_code.size(_to) <= 0:
                                                                                      stop
                                                                                  else:
                                                                                      if ceil32(_data.length) <= _data.length:
                                                                                          require ext_code.size(_to)
                                                                                          call _to with:
                                                                                               gas gas_remaining wei
                                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                          if not ext_call.success:
                                                                                              if not return_data.size:
                                                                                                  if not _data.length:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with _data[all]
                                                                                              else:
                                                                                                  if not return_data.size:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                          else:
                                                                                              require return_data.size >=′ 32
                                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                      else:
                                                                                          require ext_code.size(_to)
                                                                                          call _to with:
                                                                                               gas gas_remaining wei
                                                                                              args caller, addr(_from), _tokenId, Array(len=_data.length, data=_data[all])
                                                                                          if not ext_call.success:
                                                                                              if not return_data.size:
                                                                                                  if not _data.length:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with _data[all]
                                                                                              else:
                                                                                                  if not return_data.size:
                                                                                                      revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'
                                                                                                  else:
                                                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                                          else:
                                                                                              require return_data.size >=′ 32
                                                                                              require not 0, ext_call.return_data[4 len 28]
                                                                                              revert with 0, 'ERC721: transfer to non ERC721Receiver implementer'

