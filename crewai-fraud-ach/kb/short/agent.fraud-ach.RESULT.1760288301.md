```json
{
  "id": "4afaa1def342ace0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288301,
  "host_pid": "9e6742732c60:1",
  "hash": "1026ef350559ece636074a38ddf9ff5b60fab3c99542d044b1ce0ad222be9ba6",
  "cid": "QmV11026ef350559ece636074a38ddf9ff5b60fab3c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288301,
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
      "evaluated_at": 1760288301
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
  "sig": "0b71977f683a4a5c0b6fc0b9f330b4a51a61344a47ea151c6e0d4e4658922893"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242647259
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 23412696, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285763, 'matching_hash': '186ae6e653ee56a6'}}}