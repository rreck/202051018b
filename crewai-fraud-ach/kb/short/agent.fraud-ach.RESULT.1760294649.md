```json
{
  "id": "a7d5b49c5257f609",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294649,
  "host_pid": "9e6742732c60:1",
  "hash": "121f47b9dcc01ff3076e9d94da747c8b317b8c295a3c8c6d67d5637d7aef20f4",
  "cid": "QmV1121f47b9dcc01ff3076e9d94da747c8b317b8c29",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294649,
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
      "evaluated_at": 1760294649
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
  "sig": "fb5f80448ec866a3fae0b37846f6cfb95c939dbf286b9177830d7d9578040d7e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150546450
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 112422068, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '173a3d8db8c10352'}}}