// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract AntiTheft {

    struct EventData {
        uint id;
        string imageHash;
        uint timestamp;
    }

    EventData[] public events;

    function addEvent(
        string memory _hash
    ) public {

        events.push(
            EventData(
                events.length,
                _hash,
                block.timestamp
            )
        );
    }

    function getEvent(
        uint index
    )
        public
        view
        returns(
            uint,
            string memory,
            uint
        )
    {

        EventData memory e =
        events[index];

        return(
            e.id,
            e.imageHash,
            e.timestamp
        );
    }

    function getTotalEvents()
        public
        view
        returns(uint)
    {
        return events.length;
    }
}