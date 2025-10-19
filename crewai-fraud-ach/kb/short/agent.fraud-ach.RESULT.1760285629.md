```json
{
  "id": "fdf7ceb6dd549106",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285629,
  "host_pid": "9e6742732c60:1",
  "hash": "ac90f9a1713ceaeccdd82c771ac27a71dd93eeb5c0f7546ce12ef5b487e5a912",
  "cid": "QmV1ac90f9a1713ceaeccdd82c771ac27a71dd93eeb5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285629,
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
      "evaluated_at": 1760285629
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
  "sig": "1dbb03a421169a115217f26377726ba11e0a9aef84e53db427f4aa16881d913c"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 26969216, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}