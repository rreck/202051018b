```json
{
  "id": "ba86714af8c18f2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292700,
  "host_pid": "9e6742732c60:1",
  "hash": "aa5c32de862d847891a855dc82fdb294515e8ea2622f3d545558ca8c4089e95b",
  "cid": "QmV1aa5c32de862d847891a855dc82fdb294515e8ea2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292700,
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
      "evaluated_at": 1760292700
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
  "sig": "9eb2028a6652ba7b47d50bc680811036057edc5f4818a5cdfc03d8a41ebed2ad"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026281875
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 83172754, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': 'ee0b29e0b2882e41'}}}