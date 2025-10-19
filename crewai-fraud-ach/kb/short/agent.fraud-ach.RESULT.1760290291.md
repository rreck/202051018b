```json
{
  "id": "a3cd419b7960e747",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290291,
  "host_pid": "9e6742732c60:1",
  "hash": "76756f0d16ed53bb580d7a4eb4a88545e0d1d83b7b5b0d9e2a424dba6d4697a7",
  "cid": "QmV176756f0d16ed53bb580d7a4eb4a88545e0d1d83b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290291,
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
      "evaluated_at": 1760290291
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
  "sig": "241e0c001e29625cbe895a8629ff1a8ffd393803b2db44fdf21168850605e02d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241355402
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 23785298, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285765, 'matching_hash': '58524718dce63a85'}}}