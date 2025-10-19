```json
{
  "id": "dc46b5591ee3e540",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286033,
  "host_pid": "9e6742732c60:1",
  "hash": "70c2610714daeef6ad223db46141894a7c413a55419ce16a37074b49acdf1850",
  "cid": "QmV170c2610714daeef6ad223db46141894a7c413a55",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286033,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760286033
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "1c5984729b23037033a652cba0bdc56418ad06baed859ea4b2eb3ed8279d3f3c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596082668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 18926072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760284979, 'matching_hash': '3a96bbca6babd2b6'}}}