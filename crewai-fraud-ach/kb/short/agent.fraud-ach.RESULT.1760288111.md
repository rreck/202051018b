```json
{
  "id": "f26e9b5bb36c3187",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288111,
  "host_pid": "9e6742732c60:1",
  "hash": "37370d3830696397f1dde6c976a462298927a82172d34e4a35cd3bf704c90780",
  "cid": "QmV137370d3830696397f1dde6c976a462298927a821",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288111,
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
      "evaluated_at": 1760288111
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
  "sig": "7709f8632d7fd7475425b2e0ff9f140ff9115a85c6543248b1b624de442e55bf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159610548
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 27059245, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285764, 'matching_hash': '505487b98e445d12'}}}