import uuid

#OBJECTID
#PARKID2
#SHAPE_Length
#SHAPE_Area
#NAME
#CLASS
#NPU1
#DISTRICT
#ADDRESS
#GIS_AC
#FILE_AC
#PARCEL_ID
#PARKID
#PARKID2_1
#FORMERNAME
#NEIGHBOR
#ZIP
#CDP
#X_TRLPAV
#X_TRLNPAV
#COUNTY
#ACQ_NOTES
#PAVILIONS
#PLAYGROUND
#PIC_SHEL
#PLAYGR_SF
#UPARR
#FUND_SRC
#LWCF
#GAZEBO
#PICNICTABL
#PARKGRILL1
#RESTROOMS
#PV_PRKSPAC
#BALLFIELDS
#SOCCER
#TENNIS
#TRL_TYPE
#TRL_NUM
#TRL_LEN
#TEN_PRAC
#BBALL
#VOLLEYBALL
#POOL
#POOLSIZE
#GYM
#PV_SQ_FT
#GZBOSQFT
#PARKDRINK
#PARKBENCH
#PSPACES
#RECCEN
#ADOPTED
#SURV_TYPE
#SURV_DATE
#SURV_AC
#FEATURE
#COVBB
#DOGPARK
#TRACK
#NAT
#GOLF
#OPFIELD
#AREA_FIN
#FACIL_YN
#ACQUIRED
#POOLENGTH
#BELTLIN
#PLSIZYDS
#SPLASHYDS
#NOTES
#RECCTRCLS
#RECCTRNM
#RECCTRFT2
#SPECFAC
#COMCTRNAM
#COMCTRCLS
#SPFACFT2
#OWNER
#COMCTRFT2
#XDLIST
#GIS_ISTHER
#GIS_WPIN
#GLOBALID

PARK_MAP = {
    'OBJECTID': ('object_id', int),
    'PARKID': ('park_id', str),
    'NAME': ('name', str),
    'CLASS': ('park_class', str),
    'NPU1': ('npu1', str),
    'DISTRICT': ('district', int),
    'ADDRESS': ('address', str),
    'PARCEL_ID': ('parcel_id', str),
    'FORMERNAME': ('former_name', str),
    'NEIGHBOR': ('neighborhood', str),
    'ZIP': ('zipcode', str),
    'COUNTY': ('county', str),
    'GLOBALID': ('global_id', uuid.UUID),
    'Lat': ('latitude', float),
    'long': ('longitude', float),
}
