```json
{
  "id": "ef0ce389c11c7d9a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287937,
  "host_pid": "9e6742732c60:1",
  "hash": "469ca69a44b3cb6e4abf3d88b188c5cff82e1166aa55b6d05b3ce4faeef4e5e6",
  "cid": "QmV1469ca69a44b3cb6e4abf3d88b188c5cff82e1166",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287937,
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
      "evaluated_at": 1760287937
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
  "sig": "bd48ecec4ccd376307680c9d1213a4cd467f65f08d4389fa0effb45dcfcb129b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462125361
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 13492017, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285764, 'matching_hash': '410e2c6110d1d339'}}}