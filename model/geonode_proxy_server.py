from enum import Enum
from typing import Optional, List
from datetime import datetime
from dataclasses import dataclass


class AnonymityLevel(Enum):
    ELITE = "elite"
    TRANSPARENT = "transparent"


class Protocol(Enum):
    HTTP = "http"
    SOCKS4 = "socks4"
    SOCKS5 = "socks5"


@dataclass
class Datum:
    id: str
    ip: str
    anonymity_level: AnonymityLevel
    asn: Optional[str]
    city: str
    country: str
    created_at: datetime
    google: bool
    isp: str
    last_checked: int
    latency: float
    org: Optional[str]
    port: int
    protocols: List[Protocol]
    region: None
    response_time: int
    speed: int
    updated_at: datetime
    working_percent: None
    up_time: float
    up_time_success_count: int
    up_time_try_count: int

    def __init__(self, id: str, ip: str, anonymity_level: AnonymityLevel, asn: Optional[str], city: str, country: str,
                 created_at: datetime, google: bool, isp: str, last_checked: int, latency: float, org: Optional[str],
                 port: int, protocols: List[Protocol], region: None, response_time: int, speed: int,
                 updated_at: datetime, working_percent: None, up_time: float, up_time_success_count: int,
                 up_time_try_count: int) -> None:
        self.id = id
        self.ip = ip
        self.anonymity_level = anonymity_level
        self.asn = asn
        self.city = city
        self.country = country
        self.created_at = created_at
        self.google = google
        self.isp = isp
        self.last_checked = last_checked
        self.latency = latency
        self.org = org
        self.port = port
        self.protocols = protocols
        self.region = region
        self.response_time = response_time
        self.speed = speed
        self.updated_at = updated_at
        self.working_percent = working_percent
        self.up_time = up_time
        self.up_time_success_count = up_time_success_count
        self.up_time_try_count = up_time_try_count


@dataclass
class GeonodeProxyServers:
    data: List[Datum]
    total: int
    page: int
    limit: int

    def __init__(self, data: List[Datum], total: int, page: int, limit: int) -> None:
        self.data = data
        self.total = total
        self.page = page
        self.limit = limit
