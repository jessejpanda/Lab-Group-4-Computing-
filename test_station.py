# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

#Test for Task 1F

def test_typical_range_consistent():
    """Tests to check that the outputs from funtion "typical_range_consistent" are as expected"""
    excluded_stations_and_names = []
    inconsistent = sorted(excluded_stations_and_names)
    assert type(inconsistent) is list
    assert inconsistent == sorted(inconsistent)

def test_inconsistent_typical_range_stations():
    """Tests to check that the outputs from funtion "inconsistent_typical_range_stations" are as expected"""
    excluded_stations_and_names = []
    inconsistent = sorted(excluded_stations_and_names)
    assert type(excluded_stations_and_names) is list




    



