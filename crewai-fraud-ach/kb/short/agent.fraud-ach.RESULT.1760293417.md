```json
{
  "id": "7f8935b8c78a9cfc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293417,
  "host_pid": "9e6742732c60:1",
  "hash": "b748bcdb68b0b2adac5c9e665302fe5551f86ccdfec14243898538fcf712242b",
  "cid": "QmV1b748bcdb68b0b2adac5c9e665302fe5551f86ccd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293417,
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
      "evaluated_at": 1760293417
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
  "sig": "2f837ea334c1bf2c0dcc03ff82303517c99e3bdb78da75385ffcdf193fcdb83c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467383207
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 55387914, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': 'cf3979d2ed99750b'}}}