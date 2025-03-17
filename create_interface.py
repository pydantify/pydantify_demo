from rich import print_json

from models.ietf_interface import (
    Model,
    InterfacesContainer,
    InterfaceListEntry,
    EnumerationEnum2,
    EnumerationEnum3,
)

if __name__ == "__main__":
    eth1 = InterfaceListEntry(
        name="eth1",
        type="iana-if-type:ethernetCsmacd",
        admin_status=EnumerationEnum2.up,
        oper_status=EnumerationEnum3.up,
        if_index=1,
    )
    interfaces_config = InterfacesContainer(interface=[eth1])
    model = Model(interfaces=interfaces_config)

    payload = model.model_dump_json(exclude_defaults=True, by_alias=True)
    print_json(payload, indent=2)
