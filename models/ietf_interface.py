from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated


class IsRouterLeaf(BaseModel):
    """
    Indicates that the neighbor node acts as a router.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class IsRouterLeaf2(BaseModel):
    """
    Indicates that the neighbor node acts as a router.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class StatisticsContainer(BaseModel):
    """
    A collection of interface-related statistics objects.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    discontinuity_time: Annotated[
        str,
        Field(
            alias='ietf-interfaces:discontinuity-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ]
    """
    The time on the most recent occasion at which any one or
    more of this interface's counters suffered a
    discontinuity.  If no such discontinuities have occurred
    since the last re-initialization of the local management
    subsystem, then this node contains the time the local
    management subsystem re-initialized itself.
    """
    in_octets: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:in-octets', ge=0, le=18446744073709551615),
    ] = None
    """
    The total number of octets received on the interface,
    including framing characters.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    in_unicast_pkts: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:in-unicast-pkts', ge=0, le=18446744073709551615),
    ] = None
    """
    The number of packets, delivered by this sub-layer to a
    higher (sub-)layer, that were not addressed to a
    multicast or broadcast address at this sub-layer.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    in_broadcast_pkts: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:in-broadcast-pkts', ge=0, le=18446744073709551615),
    ] = None
    """
    The number of packets, delivered by this sub-layer to a
    higher (sub-)layer, that were addressed to a broadcast
    address at this sub-layer.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    in_multicast_pkts: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:in-multicast-pkts', ge=0, le=18446744073709551615),
    ] = None
    """
    The number of packets, delivered by this sub-layer to a
    higher (sub-)layer, that were addressed to a multicast
    address at this sub-layer.  For a MAC-layer protocol,
    this includes both Group and Functional addresses.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    in_discards: Annotated[
        Optional[int], Field(alias='ietf-interfaces:in-discards', ge=0, le=4294967295)
    ] = None
    """
    The number of inbound packets that were chosen to be
    discarded even though no errors had been detected to
    prevent their being deliverable to a higher-layer
    protocol.  One possible reason for discarding such a
    packet could be to free up buffer space.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    in_errors: Annotated[
        Optional[int], Field(alias='ietf-interfaces:in-errors', ge=0, le=4294967295)
    ] = None
    """
    For packet-oriented interfaces, the number of inbound
    packets that contained errors preventing them from being
    deliverable to a higher-layer protocol.  For character-
    oriented or fixed-length interfaces, the number of
    inbound transmission units that contained errors
    preventing them from being deliverable to a higher-layer
    protocol.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    in_unknown_protos: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:in-unknown-protos', ge=0, le=4294967295),
    ] = None
    """
    For packet-oriented interfaces, the number of packets
    received via the interface that were discarded because
    of an unknown or unsupported protocol.  For
    character-oriented or fixed-length interfaces that
    support protocol multiplexing, the number of
    transmission units received via the interface that were
    discarded because of an unknown or unsupported protocol.
    For any interface that does not support protocol
    multiplexing, this counter is not present.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    out_octets: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:out-octets', ge=0, le=18446744073709551615),
    ] = None
    """
    The total number of octets transmitted out of the
    interface, including framing characters.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    out_unicast_pkts: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:out-unicast-pkts', ge=0, le=18446744073709551615),
    ] = None
    """
    The total number of packets that higher-level protocols
    requested be transmitted and that were not addressed
    to a multicast or broadcast address at this sub-layer,
    including those that were discarded or not sent.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    out_broadcast_pkts: Annotated[
        Optional[int],
        Field(
            alias='ietf-interfaces:out-broadcast-pkts', ge=0, le=18446744073709551615
        ),
    ] = None
    """
    The total number of packets that higher-level protocols
    requested be transmitted and that were addressed to a
    broadcast address at this sub-layer, including those
    that were discarded or not sent.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    out_multicast_pkts: Annotated[
        Optional[int],
        Field(
            alias='ietf-interfaces:out-multicast-pkts', ge=0, le=18446744073709551615
        ),
    ] = None
    """
    The total number of packets that higher-level protocols
    requested be transmitted and that were addressed to a
    multicast address at this sub-layer, including those
    that were discarded or not sent.  For a MAC-layer
    protocol, this includes both Group and Functional
    addresses.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    out_discards: Annotated[
        Optional[int], Field(alias='ietf-interfaces:out-discards', ge=0, le=4294967295)
    ] = None
    """
    The number of outbound packets that were chosen to be
    discarded even though no errors had been detected to
    prevent their being transmitted.  One possible reason
    for discarding such a packet could be to free up buffer
    space.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    out_errors: Annotated[
        Optional[int], Field(alias='ietf-interfaces:out-errors', ge=0, le=4294967295)
    ] = None
    """
    For packet-oriented interfaces, the number of outbound
    packets that could not be transmitted because of errors.
    For character-oriented or fixed-length interfaces, the
    number of outbound transmission units that could not be
    transmitted because of errors.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """


class StatisticsContainer2(BaseModel):
    """
    A collection of interface-related statistics objects.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    discontinuity_time: Annotated[
        str,
        Field(
            alias='ietf-interfaces:discontinuity-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ]
    """
    The time on the most recent occasion at which any one or
    more of this interface's counters suffered a
    discontinuity.  If no such discontinuities have occurred
    since the last re-initialization of the local management
    subsystem, then this node contains the time the local
    management subsystem re-initialized itself.
    """
    in_octets: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:in-octets', ge=0, le=18446744073709551615),
    ] = None
    """
    The total number of octets received on the interface,
    including framing characters.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    in_unicast_pkts: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:in-unicast-pkts', ge=0, le=18446744073709551615),
    ] = None
    """
    The number of packets, delivered by this sub-layer to a
    higher (sub-)layer, that were not addressed to a
    multicast or broadcast address at this sub-layer.
    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    in_broadcast_pkts: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:in-broadcast-pkts', ge=0, le=18446744073709551615),
    ] = None
    """
    The number of packets, delivered by this sub-layer to a
    higher (sub-)layer, that were addressed to a broadcast
    address at this sub-layer.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    in_multicast_pkts: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:in-multicast-pkts', ge=0, le=18446744073709551615),
    ] = None
    """
    The number of packets, delivered by this sub-layer to a
    higher (sub-)layer, that were addressed to a multicast
    address at this sub-layer.  For a MAC-layer protocol,
    this includes both Group and Functional addresses.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    in_discards: Annotated[
        Optional[int], Field(alias='ietf-interfaces:in-discards', ge=0, le=4294967295)
    ] = None
    """
    The number of inbound packets that were chosen to be
    discarded even though no errors had been detected to
    prevent their being deliverable to a higher-layer
    protocol.  One possible reason for discarding such a
    packet could be to free up buffer space.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    in_errors: Annotated[
        Optional[int], Field(alias='ietf-interfaces:in-errors', ge=0, le=4294967295)
    ] = None
    """
    For packet-oriented interfaces, the number of inbound
    packets that contained errors preventing them from being
    deliverable to a higher-layer protocol.  For character-
    oriented or fixed-length interfaces, the number of
    inbound transmission units that contained errors
    preventing them from being deliverable to a higher-layer
    protocol.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    in_unknown_protos: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:in-unknown-protos', ge=0, le=4294967295),
    ] = None
    """
    For packet-oriented interfaces, the number of packets
    received via the interface that were discarded because
    of an unknown or unsupported protocol.  For
    character-oriented or fixed-length interfaces that
    support protocol multiplexing, the number of
    transmission units received via the interface that were
    discarded because of an unknown or unsupported protocol.
    For any interface that does not support protocol
    multiplexing, this counter is not present.
    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    out_octets: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:out-octets', ge=0, le=18446744073709551615),
    ] = None
    """
    The total number of octets transmitted out of the
    interface, including framing characters.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    out_unicast_pkts: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:out-unicast-pkts', ge=0, le=18446744073709551615),
    ] = None
    """
    The total number of packets that higher-level protocols
    requested be transmitted and that were not addressed
    to a multicast or broadcast address at this sub-layer,
    including those that were discarded or not sent.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    out_broadcast_pkts: Annotated[
        Optional[int],
        Field(
            alias='ietf-interfaces:out-broadcast-pkts', ge=0, le=18446744073709551615
        ),
    ] = None
    """
    The total number of packets that higher-level protocols
    requested be transmitted and that were addressed to a
    broadcast address at this sub-layer, including those
    that were discarded or not sent.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    out_multicast_pkts: Annotated[
        Optional[int],
        Field(
            alias='ietf-interfaces:out-multicast-pkts', ge=0, le=18446744073709551615
        ),
    ] = None
    """
    The total number of packets that higher-level protocols
    requested be transmitted and that were addressed to a
    multicast address at this sub-layer, including those
    that were discarded or not sent.  For a MAC-layer
    protocol, this includes both Group and Functional
    addresses.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    out_discards: Annotated[
        Optional[int], Field(alias='ietf-interfaces:out-discards', ge=0, le=4294967295)
    ] = None
    """
    The number of outbound packets that were chosen to be
    discarded even though no errors had been detected to
    prevent their being transmitted.  One possible reason
    for discarding such a packet could be to free up buffer
    space.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """
    out_errors: Annotated[
        Optional[int], Field(alias='ietf-interfaces:out-errors', ge=0, le=4294967295)
    ] = None
    """
    For packet-oriented interfaces, the number of outbound
    packets that could not be transmitted because of errors.
    For character-oriented or fixed-length interfaces, the
    number of outbound transmission units that could not be
    transmitted because of errors.

    Discontinuities in the value of this counter can occur
    at re-initialization of the management system and at
    other times as indicated by the value of
    'discontinuity-time'.
    """


class EnumerationEnum(Enum):
    enabled = 'enabled'
    disabled = 'disabled'


class EnumerationEnum10(Enum):
    preferred = 'preferred'
    deprecated = 'deprecated'
    invalid = 'invalid'
    inaccessible = 'inaccessible'
    unknown = 'unknown'
    tentative = 'tentative'
    duplicate = 'duplicate'
    optimistic = 'optimistic'


class EnumerationEnum11(Enum):
    incomplete = 'incomplete'
    reachable = 'reachable'
    stale = 'stale'
    delay = 'delay'
    probe = 'probe'


class EnumerationEnum2(Enum):
    up = 'up'
    down = 'down'
    testing = 'testing'


class EnumerationEnum3(Enum):
    up = 'up'
    down = 'down'
    testing = 'testing'
    unknown = 'unknown'
    dormant = 'dormant'
    not_present = 'not-present'
    lower_layer_down = 'lower-layer-down'


class EnumerationEnum4(Enum):
    other = 'other'
    static = 'static'
    dhcp = 'dhcp'
    link_layer = 'link-layer'
    random = 'random'


class EnumerationEnum5(Enum):
    other = 'other'
    static = 'static'
    dynamic = 'dynamic'


class EnumerationEnum6(Enum):
    preferred = 'preferred'
    deprecated = 'deprecated'
    invalid = 'invalid'
    inaccessible = 'inaccessible'
    unknown = 'unknown'
    tentative = 'tentative'
    duplicate = 'duplicate'
    optimistic = 'optimistic'


class EnumerationEnum7(Enum):
    incomplete = 'incomplete'
    reachable = 'reachable'
    stale = 'stale'
    delay = 'delay'
    probe = 'probe'


class EnumerationEnum8(Enum):
    up = 'up'
    down = 'down'
    testing = 'testing'


class EnumerationEnum9(Enum):
    up = 'up'
    down = 'down'
    testing = 'testing'
    unknown = 'unknown'
    dormant = 'dormant'
    not_present = 'not-present'
    lower_layer_down = 'lower-layer-down'


class AutoconfContainer(BaseModel):
    """
    Parameters to control the autoconfiguration of IPv6
    addresses, as described in RFC 4862.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    create_global_addresses: Annotated[
        Optional[bool], Field(alias='ietf-ip:create-global-addresses')
    ] = True
    """
    If enabled, the host creates global addresses as
    described in RFC 4862.
    """
    create_temporary_addresses: Annotated[
        Optional[bool], Field(alias='ietf-ip:create-temporary-addresses')
    ] = False
    """
    If enabled, the host creates temporary addresses as
    described in RFC 4941.
    """
    temporary_valid_lifetime: Annotated[
        Optional[int],
        Field(alias='ietf-ip:temporary-valid-lifetime', ge=0, le=4294967295),
    ] = 604800
    """
    The time period during which the temporary address
    is valid.
    """
    temporary_preferred_lifetime: Annotated[
        Optional[int],
        Field(alias='ietf-ip:temporary-preferred-lifetime', ge=0, le=4294967295),
    ] = 86400
    """
    The time period during which the temporary address is
    preferred.
    """


class NetmaskCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    netmask: Annotated[
        Optional[str],
        Field(
            alias='ietf-ip:netmask',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = None
    """
    The subnet specified as a netmask.
    """


class NetmaskCase2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    netmask: Annotated[
        Optional[str],
        Field(
            alias='ietf-ip:netmask',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = None
    """
    The subnet specified as a netmask.
    """


class PrefixLengthCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    prefix_length: Annotated[
        Optional[int], Field(alias='ietf-ip:prefix-length', ge=0, le=32)
    ] = None
    """
    The length of the subnet prefix.
    """


class PrefixLengthCase2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    prefix_length: Annotated[
        Optional[int], Field(alias='ietf-ip:prefix-length', ge=0, le=32)
    ] = None
    """
    The length of the subnet prefix.
    """


class NeighborListEntry(BaseModel):
    """
    A list of mappings from IPv4 addresses to
    link-layer addresses.

    Entries in this list in the intended configuration are
    used as static entries in the ARP Cache.

    In the operational state, this list represents the ARP
    Cache.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ip: Annotated[
        str,
        Field(
            alias='ietf-ip:ip',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\d\\w]+)?$).*$',
        ),
    ]
    """
    The IPv4 address of the neighbor node.
    """
    link_layer_address: Annotated[
        str,
        Field(
            alias='ietf-ip:link-layer-address',
            pattern='^(?=^([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?$).*$',
        ),
    ]
    """
    The link-layer address of the neighbor node.
    """
    origin: Annotated[Optional[EnumerationEnum5], Field(alias='ietf-ip:origin')] = None
    """
    The origin of this neighbor entry.
    """


class NeighborListEntry2(BaseModel):
    """
    A list of mappings from IPv6 addresses to
    link-layer addresses.

    Entries in this list in the intended configuration are
    used as static entries in the Neighbor Cache.

    In the operational state, this list represents the
    Neighbor Cache.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ip: Annotated[
        str,
        Field(
            alias='ietf-ip:ip',
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\d\\w]+)?$)(?=^(([^:]+:){6}(([^:]+:[^:]+)|(.*\\..*)))|((([^:]+:)*[^:]+)?::(([^:]+:)*[^:]+)?)(%.+)?$).*$',
        ),
    ]
    """
    The IPv6 address of the neighbor node.
    """
    link_layer_address: Annotated[
        str,
        Field(
            alias='ietf-ip:link-layer-address',
            pattern='^(?=^([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?$).*$',
        ),
    ]
    """
    The link-layer address of the neighbor node.

    In the operational state, if the neighbor's 'state' leaf
    is 'incomplete', this leaf is not instantiated.
    """
    origin: Annotated[Optional[EnumerationEnum5], Field(alias='ietf-ip:origin')] = None
    """
    The origin of this neighbor entry.
    """
    is_router: Annotated[Optional[IsRouterLeaf], Field(alias='ietf-ip:is-router')] = (
        None
    )
    state: Annotated[Optional[EnumerationEnum7], Field(alias='ietf-ip:state')] = None
    """
    The Neighbor Unreachability Detection state of this
    entry.
    """


class NeighborListEntry3(BaseModel):
    """
    A list of mappings from IPv4 addresses to
    link-layer addresses.

    This list represents the ARP Cache.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ip: Annotated[
        str,
        Field(
            alias='ietf-ip:ip',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\d\\w]+)?$).*$',
        ),
    ]
    """
    The IPv4 address of the neighbor node.
    """
    link_layer_address: Annotated[
        Optional[str],
        Field(
            alias='ietf-ip:link-layer-address',
            pattern='^(?=^([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?$).*$',
        ),
    ] = None
    """
    The link-layer address of the neighbor node.
    """
    origin: Annotated[Optional[EnumerationEnum5], Field(alias='ietf-ip:origin')] = None
    """
    The origin of this neighbor entry.
    """


class NeighborListEntry4(BaseModel):
    """
    A list of mappings from IPv6 addresses to
    link-layer addresses.

    This list represents the Neighbor Cache.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ip: Annotated[
        str,
        Field(
            alias='ietf-ip:ip',
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\d\\w]+)?$)(?=^(([^:]+:){6}(([^:]+:[^:]+)|(.*\\..*)))|((([^:]+:)*[^:]+)?::(([^:]+:)*[^:]+)?)(%.+)?$).*$',
        ),
    ]
    """
    The IPv6 address of the neighbor node.
    """
    link_layer_address: Annotated[
        Optional[str],
        Field(
            alias='ietf-ip:link-layer-address',
            pattern='^(?=^([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?$).*$',
        ),
    ] = None
    """
    The link-layer address of the neighbor node.
    """
    origin: Annotated[Optional[EnumerationEnum5], Field(alias='ietf-ip:origin')] = None
    """
    The origin of this neighbor entry.
    """
    is_router: Annotated[Optional[IsRouterLeaf2], Field(alias='ietf-ip:is-router')] = (
        None
    )
    state: Annotated[Optional[EnumerationEnum11], Field(alias='ietf-ip:state')] = None
    """
    The Neighbor Unreachability Detection state of this
    entry.
    """


class AddressListEntry(BaseModel):
    """
    The list of IPv4 addresses on the interface.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ip: Annotated[
        str,
        Field(
            alias='ietf-ip:ip',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\d\\w]+)?$).*$',
        ),
    ]
    """
    The IPv4 address on the interface.
    """
    subnet: Annotated[
        Union[PrefixLengthCase, NetmaskCase], Field(alias='ietf-ip:subnet')
    ]
    origin: Annotated[Optional[EnumerationEnum4], Field(alias='ietf-ip:origin')] = None
    """
    The origin of this address.
    """


class AddressListEntry2(BaseModel):
    """
    The list of IPv6 addresses on the interface.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ip: Annotated[
        str,
        Field(
            alias='ietf-ip:ip',
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\d\\w]+)?$)(?=^(([^:]+:){6}(([^:]+:[^:]+)|(.*\\..*)))|((([^:]+:)*[^:]+)?::(([^:]+:)*[^:]+)?)(%.+)?$).*$',
        ),
    ]
    """
    The IPv6 address on the interface.
    """
    prefix_length: Annotated[int, Field(alias='ietf-ip:prefix-length', ge=0, le=128)]
    """
    The length of the subnet prefix.
    """
    origin: Annotated[Optional[EnumerationEnum4], Field(alias='ietf-ip:origin')] = None
    """
    The origin of this address.
    """
    status: Annotated[Optional[EnumerationEnum6], Field(alias='ietf-ip:status')] = None
    """
    The status of an address.  Most of the states correspond
    to states from the IPv6 Stateless Address
    Autoconfiguration protocol.
    """


class AddressListEntry3(BaseModel):
    """
    The list of IPv4 addresses on the interface.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ip: Annotated[
        str,
        Field(
            alias='ietf-ip:ip',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\d\\w]+)?$).*$',
        ),
    ]
    """
    The IPv4 address on the interface.
    """
    subnet: Annotated[
        Optional[Union[PrefixLengthCase2, NetmaskCase2]], Field(alias='ietf-ip:subnet')
    ] = None
    origin: Annotated[Optional[EnumerationEnum4], Field(alias='ietf-ip:origin')] = None
    """
    The origin of this address.
    """


class AddressListEntry4(BaseModel):
    """
    The list of IPv6 addresses on the interface.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ip: Annotated[
        str,
        Field(
            alias='ietf-ip:ip',
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\d\\w]+)?$)(?=^(([^:]+:){6}(([^:]+:[^:]+)|(.*\\..*)))|((([^:]+:)*[^:]+)?::(([^:]+:)*[^:]+)?)(%.+)?$).*$',
        ),
    ]
    """
    The IPv6 address on the interface.
    """
    prefix_length: Annotated[int, Field(alias='ietf-ip:prefix-length', ge=0, le=128)]
    """
    The length of the subnet prefix.
    """
    origin: Annotated[Optional[EnumerationEnum4], Field(alias='ietf-ip:origin')] = None
    """
    The origin of this address.
    """
    status: Annotated[Optional[EnumerationEnum10], Field(alias='ietf-ip:status')] = None
    """
    The status of an address.  Most of the states correspond
    to states from the IPv6 Stateless Address
    Autoconfiguration protocol.
    """


class Ipv4Container(BaseModel):
    """
    Parameters for the IPv4 address family.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    enabled: Annotated[Optional[bool], Field(alias='ietf-ip:enabled')] = True
    """
    Controls whether IPv4 is enabled or disabled on this
    interface.  When IPv4 is enabled, this interface is
    connected to an IPv4 stack, and the interface can send
    and receive IPv4 packets.
    """
    forwarding: Annotated[Optional[bool], Field(alias='ietf-ip:forwarding')] = False
    """
    Controls IPv4 packet forwarding of datagrams received by,
    but not addressed to, this interface.  IPv4 routers
    forward datagrams.  IPv4 hosts do not (except those
    source-routed via the host).
    """
    mtu: Annotated[Optional[int], Field(alias='ietf-ip:mtu', ge=68, le=65535)] = None
    """
    The size, in octets, of the largest IPv4 packet that the
    interface will send and receive.

    The server may restrict the allowed values for this leaf,
    depending on the interface's type.

    If this leaf is not configured, the operationally used MTU
    depends on the interface's type.
    """
    address: Annotated[
        Optional[List[AddressListEntry]], Field(alias='ietf-ip:address')
    ] = None
    neighbor: Annotated[
        Optional[List[NeighborListEntry]], Field(alias='ietf-ip:neighbor')
    ] = None


class Ipv4Container2(BaseModel):
    """
    Interface-specific parameters for the IPv4 address family.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    forwarding: Annotated[Optional[bool], Field(alias='ietf-ip:forwarding')] = None
    """
    Indicates whether IPv4 packet forwarding is enabled or
    disabled on this interface.
    """
    mtu: Annotated[Optional[int], Field(alias='ietf-ip:mtu', ge=68, le=65535)] = None
    """
    The size, in octets, of the largest IPv4 packet that the
    interface will send and receive.
    """
    address: Annotated[
        Optional[List[AddressListEntry3]], Field(alias='ietf-ip:address')
    ] = None
    neighbor: Annotated[
        Optional[List[NeighborListEntry3]], Field(alias='ietf-ip:neighbor')
    ] = None


class Ipv6Container(BaseModel):
    """
    Parameters for the IPv6 address family.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    enabled: Annotated[Optional[bool], Field(alias='ietf-ip:enabled')] = True
    """
    Controls whether IPv6 is enabled or disabled on this
    interface.  When IPv6 is enabled, this interface is
    connected to an IPv6 stack, and the interface can send
    and receive IPv6 packets.
    """
    forwarding: Annotated[Optional[bool], Field(alias='ietf-ip:forwarding')] = False
    """
    Controls IPv6 packet forwarding of datagrams received by,
    but not addressed to, this interface.  IPv6 routers
    forward datagrams.  IPv6 hosts do not (except those
    source-routed via the host).
    """
    mtu: Annotated[
        Optional[int], Field(alias='ietf-ip:mtu', ge=1280, le=4294967295)
    ] = None
    """
    The size, in octets, of the largest IPv6 packet that the
    interface will send and receive.

    The server may restrict the allowed values for this leaf,
    depending on the interface's type.

    If this leaf is not configured, the operationally used MTU
    depends on the interface's type.
    """
    address: Annotated[
        Optional[List[AddressListEntry2]], Field(alias='ietf-ip:address')
    ] = None
    neighbor: Annotated[
        Optional[List[NeighborListEntry2]], Field(alias='ietf-ip:neighbor')
    ] = None
    dup_addr_detect_transmits: Annotated[
        Optional[int],
        Field(alias='ietf-ip:dup-addr-detect-transmits', ge=0, le=4294967295),
    ] = 1
    """
    The number of consecutive Neighbor Solicitation messages
    sent while performing Duplicate Address Detection on a
    tentative address.  A value of zero indicates that
    Duplicate Address Detection is not performed on
    tentative addresses.  A value of one indicates a single
    transmission with no follow-up retransmissions.
    """
    autoconf: Annotated[
        Optional[AutoconfContainer], Field(alias='ietf-ip:autoconf')
    ] = None


class Ipv6Container2(BaseModel):
    """
    Parameters for the IPv6 address family.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    forwarding: Annotated[Optional[bool], Field(alias='ietf-ip:forwarding')] = False
    """
    Indicates whether IPv6 packet forwarding is enabled or
    disabled on this interface.
    """
    mtu: Annotated[
        Optional[int], Field(alias='ietf-ip:mtu', ge=1280, le=4294967295)
    ] = None
    """
    The size, in octets, of the largest IPv6 packet that the
    interface will send and receive.
    """
    address: Annotated[
        Optional[List[AddressListEntry4]], Field(alias='ietf-ip:address')
    ] = None
    neighbor: Annotated[
        Optional[List[NeighborListEntry4]], Field(alias='ietf-ip:neighbor')
    ] = None


class InterfaceListEntry(BaseModel):
    """
    The list of interfaces on the device.

    The status of an interface is available in this list in the
    operational state.  If the configuration of a
    system-controlled interface cannot be used by the system
    (e.g., the interface hardware present does not match the
    interface type), then the configuration is not applied to
    the system-controlled interface shown in the operational
    state.  If the configuration of a user-controlled interface
    cannot be used by the system, the configured interface is
    not instantiated in the operational state.

    System-controlled interfaces created by the system are
    always present in this list in the operational state,
    whether or not they are configured.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[str, Field(alias='ietf-interfaces:name')]
    """
    The name of the interface.

    A device MAY restrict the allowed values for this leaf,
    possibly depending on the type of the interface.
    For system-controlled interfaces, this leaf is the
    device-specific name of the interface.

    If a client tries to create configuration for a
    system-controlled interface that is not present in the
    operational state, the server MAY reject the request if
    the implementation does not support pre-provisioning of
    interfaces or if the name refers to an interface that can
    never exist in the system.  A Network Configuration
    Protocol (NETCONF) server MUST reply with an rpc-error
    with the error-tag 'invalid-value' in this case.

    If the device supports pre-provisioning of interface
    configuration, the 'pre-provisioning' feature is
    advertised.

    If the device allows arbitrarily named user-controlled
    interfaces, the 'arbitrary-names' feature is advertised.

    When a configured user-controlled interface is created by
    the system, it is instantiated with the same name in the
    operational state.

    A server implementation MAY map this leaf to the ifName
    MIB object.  Such an implementation needs to use some
    mechanism to handle the differences in size and characters
    allowed between this leaf and ifName.  The definition of
    such a mechanism is outside the scope of this document.
    """
    description: Annotated[
        Optional[str], Field(alias='ietf-interfaces:description')
    ] = None
    """
    A textual description of the interface.

    A server implementation MAY map this leaf to the ifAlias
    MIB object.  Such an implementation needs to use some
    mechanism to handle the differences in size and characters
    allowed between this leaf and ifAlias.  The definition of
    such a mechanism is outside the scope of this document.

    Since ifAlias is defined to be stored in non-volatile
    storage, the MIB implementation MUST map ifAlias to the
    value of 'description' in the persistently stored
    configuration.
    """
    type: Annotated[str, Field(alias='ietf-interfaces:type')]
    """
    The type of the interface.

    When an interface entry is created, a server MAY
    initialize the type leaf with a valid value, e.g., if it
    is possible to derive the type from the name of the
    interface.

    If a client tries to set the type of an interface to a
    value that can never be used by the system, e.g., if the
    type is not supported or if the type does not match the
    name of the interface, the server MUST reject the request.
    A NETCONF server MUST reply with an rpc-error with the
    error-tag 'invalid-value' in this case.
    """
    enabled: Annotated[Optional[bool], Field(alias='ietf-interfaces:enabled')] = True
    """
    This leaf contains the configured, desired state of the
    interface.

    Systems that implement the IF-MIB use the value of this
    leaf in the intended configuration to set
    IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry
    has been initialized, as described in RFC 2863.

    Changes in this leaf in the intended configuration are
    reflected in ifAdminStatus.
    """
    link_up_down_trap_enable: Annotated[
        Optional[EnumerationEnum],
        Field(alias='ietf-interfaces:link-up-down-trap-enable'),
    ] = None
    """
    Controls whether linkUp/linkDown SNMP notifications
    should be generated for this interface.

    If this node is not configured, the value 'enabled' is
    operationally used by the server for interfaces that do
    not operate on top of any other interface (i.e., there are
    no 'lower-layer-if' entries), and 'disabled' otherwise.
    """
    admin_status: Annotated[
        EnumerationEnum2, Field(alias='ietf-interfaces:admin-status')
    ]
    """
    The desired state of the interface.

    This leaf has the same read semantics as ifAdminStatus.
    """
    oper_status: Annotated[EnumerationEnum3, Field(alias='ietf-interfaces:oper-status')]
    """
    The current operational state of the interface.

    This leaf has the same semantics as ifOperStatus.
    """
    last_change: Annotated[
        Optional[str],
        Field(
            alias='ietf-interfaces:last-change',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time the interface entered its current operational
    state.  If the current state was entered prior to the
    last re-initialization of the local network management
    subsystem, then this node is not present.
    """
    if_index: Annotated[
        int, Field(alias='ietf-interfaces:if-index', ge=1, le=2147483647)
    ]
    """
    The ifIndex value for the ifEntry represented by this
    interface.
    """
    phys_address: Annotated[
        Optional[str],
        Field(
            alias='ietf-interfaces:phys-address',
            pattern='^(?=^([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?$).*$',
        ),
    ] = None
    """
    The interface's address at its protocol sub-layer.  For
    example, for an 802.x interface, this object normally
    contains a Media Access Control (MAC) address.  The
    interface's media-specific modules must define the bit
    and byte ordering and the format of the value of this
    object.  For interfaces that do not have such an address
    (e.g., a serial line), this node is not present.
    """
    higher_layer_if: Annotated[
        Optional[List[str]], Field(alias='ietf-interfaces:higher-layer-if')
    ] = []
    """
    A list of references to interfaces layered on top of this
    interface.
    """
    lower_layer_if: Annotated[
        Optional[List[str]], Field(alias='ietf-interfaces:lower-layer-if')
    ] = []
    """
    A list of references to interfaces layered underneath this
    interface.
    """
    speed: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:speed', ge=0, le=18446744073709551615),
    ] = None
    """
    An estimate of the interface's current bandwidth in bits
    per second.  For interfaces that do not vary in
    bandwidth or for those where no accurate estimation can
    be made, this node should contain the nominal bandwidth.
    For interfaces that have no concept of bandwidth, this
    node is not present.
    """
    statistics: Annotated[
        Optional[StatisticsContainer], Field(alias='ietf-interfaces:statistics')
    ] = None
    ipv4: Annotated[Optional[Ipv4Container], Field(alias='ietf-ip:ipv4')] = None
    ipv6: Annotated[Optional[Ipv6Container], Field(alias='ietf-ip:ipv6')] = None


class InterfaceListEntry2(BaseModel):
    """
    The list of interfaces on the device.

    System-controlled interfaces created by the system are
    always present in this list, whether or not they are
    configured.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[str, Field(alias='ietf-interfaces:name')]
    """
    The name of the interface.

    A server implementation MAY map this leaf to the ifName
    MIB object.  Such an implementation needs to use some
    mechanism to handle the differences in size and characters
    allowed between this leaf and ifName.  The definition of
    such a mechanism is outside the scope of this document.
    """
    type: Annotated[str, Field(alias='ietf-interfaces:type')]
    """
    The type of the interface.
    """
    admin_status: Annotated[
        EnumerationEnum8, Field(alias='ietf-interfaces:admin-status')
    ]
    """
    The desired state of the interface.

    This leaf has the same read semantics as ifAdminStatus.
    """
    oper_status: Annotated[EnumerationEnum9, Field(alias='ietf-interfaces:oper-status')]
    """
    The current operational state of the interface.

    This leaf has the same semantics as ifOperStatus.
    """
    last_change: Annotated[
        Optional[str],
        Field(
            alias='ietf-interfaces:last-change',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
        ),
    ] = None
    """
    The time the interface entered its current operational
    state.  If the current state was entered prior to the
    last re-initialization of the local network management
    subsystem, then this node is not present.
    """
    if_index: Annotated[
        int, Field(alias='ietf-interfaces:if-index', ge=1, le=2147483647)
    ]
    """
    The ifIndex value for the ifEntry represented by this
    interface.
    """
    phys_address: Annotated[
        Optional[str],
        Field(
            alias='ietf-interfaces:phys-address',
            pattern='^(?=^([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?$).*$',
        ),
    ] = None
    """
    The interface's address at its protocol sub-layer.  For
    example, for an 802.x interface, this object normally
    contains a Media Access Control (MAC) address.  The
    interface's media-specific modules must define the bit
    and byte ordering and the format of the value of this
    object.  For interfaces that do not have such an address
    (e.g., a serial line), this node is not present.
    """
    higher_layer_if: Annotated[
        Optional[List[str]], Field(alias='ietf-interfaces:higher-layer-if')
    ] = []
    """
    A list of references to interfaces layered on top of this
    interface.
    """
    lower_layer_if: Annotated[
        Optional[List[str]], Field(alias='ietf-interfaces:lower-layer-if')
    ] = []
    """
    A list of references to interfaces layered underneath this
    interface.
    """
    speed: Annotated[
        Optional[int],
        Field(alias='ietf-interfaces:speed', ge=0, le=18446744073709551615),
    ] = None
    """
    An estimate of the interface's current bandwidth in bits
    per second.  For interfaces that do not vary in
    bandwidth or for those where no accurate estimation can

    be made, this node should contain the nominal bandwidth.
    For interfaces that have no concept of bandwidth, this
    node is not present.
    """
    statistics: Annotated[
        Optional[StatisticsContainer2], Field(alias='ietf-interfaces:statistics')
    ] = None
    ipv4: Annotated[Optional[Ipv4Container2], Field(alias='ietf-ip:ipv4')] = None
    ipv6: Annotated[Optional[Ipv6Container2], Field(alias='ietf-ip:ipv6')] = None


class InterfacesStateContainer(BaseModel):
    """
    Data nodes for the operational state of interfaces.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interface: Annotated[
        Optional[List[InterfaceListEntry2]], Field(alias='ietf-interfaces:interface')
    ] = None


class InterfacesContainer(BaseModel):
    """
    Interface parameters.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interface: Annotated[
        Optional[List[InterfaceListEntry]], Field(alias='ietf-interfaces:interface')
    ] = None


class Model(BaseModel):
    """
    Initialize an instance of this class and serialize it to JSON; this results in a RESTCONF payload.

    ## Tips
    Initialization:
    - all values have to be set via keyword arguments
    - if a class contains only a `root` field, it can be initialized as follows:
        - `member=MyNode(root=<value>)`
        - `member=<value>`

    Serialziation:
    - `exclude_defaults=True` omits fields set to their default value (recommended)
    - `by_alias=True` ensures qualified names are used (necessary)
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interfaces: Annotated[
        Optional[InterfacesContainer], Field(alias='ietf-interfaces:interfaces')
    ] = None
    interfaces_state: Annotated[
        Optional[InterfacesStateContainer],
        Field(alias='ietf-interfaces:interfaces-state'),
    ] = None


if __name__ == "__main__":
    model = Model(
        # <Initialize model here>
    )

    restconf_payload = model.model_dump_json(
        exclude_defaults=True, by_alias=True, indent=2
    )

    print(f"Generated output: {restconf_payload}")

    # Send config to network device:
    # from pydantify.utility import restconf_patch_request
    # restconf_patch_request(url='...', user_pw_auth=('usr', 'pw'), data=restconf_payload)