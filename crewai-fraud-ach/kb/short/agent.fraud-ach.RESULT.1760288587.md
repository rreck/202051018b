```json
{
  "id": "4a81e8ba95986019",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288587,
  "host_pid": "9e6742732c60:1",
  "hash": "02d0fe952e0787b733de21f706885993ae177c9b8d1f3a35597496ae2553cc9e",
  "cid": "QmV102d0fe952e0787b733de21f706885993ae177c9b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288587,
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
      "evaluated_at": 1760288587
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
  "sig": "45f0b42c3f08d31d3d1af6af6104fedddfe1bc3af35d6e56c72efcfdf1e45db4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038495907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 26656196, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285763, 'matching_hash': '3a0df0e30691ba23'}}}