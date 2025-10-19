```json
{
  "id": "e087adb19550888b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293044,
  "host_pid": "9e6742732c60:1",
  "hash": "dbf631526294be6ded6ed54f516ead2c32fda3d2e14d703d32e1843020b94b2a",
  "cid": "QmV1dbf631526294be6ded6ed54f516ead2c32fda3d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293044,
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
      "evaluated_at": 1760293044
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
  "sig": "c40418b6023ece799378001511fca5725f3dca1a893711747fa1edf22d4c7390"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278198984
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 41918310, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285764, 'matching_hash': '4a1385d186e328a3'}}}