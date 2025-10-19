```json
{
  "id": "bc19e9deff4f3639",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290124,
  "host_pid": "9e6742732c60:1",
  "hash": "6db1e5911f303365b48e4d74fefb1ce61345db9562ac8494a97ca5ae9a0285d2",
  "cid": "QmV16db1e5911f303365b48e4d74fefb1ce61345db95",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290124,
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
      "evaluated_at": 1760290124
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
  "sig": "bbdf060b5fe287bc61754ce05b2c50d13f6a83bb1059b09551b43ffb56e1ef6b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034056272
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 19627524, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285763, 'matching_hash': 'aae4e2a94575911d'}}}