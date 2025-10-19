```json
{
  "id": "cff9edcce662f723",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288333,
  "host_pid": "9e6742732c60:1",
  "hash": "645758a426ba6d085c337da6a9a6a01eae9c6c2574a775b720615acad5e350c1",
  "cid": "QmV1645758a426ba6d085c337da6a9a6a01eae9c6c25",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288333,
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
      "evaluated_at": 1760288333
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
  "sig": "86c7111551b492fd26d09d486d72aea30d398610a2c92bb90ec0572ebb4f501b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156085799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 21265740, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285763, 'matching_hash': 'a879e580def76590'}}}