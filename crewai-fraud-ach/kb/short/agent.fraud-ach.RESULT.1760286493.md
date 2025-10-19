```json
{
  "id": "65748b94354b335a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286493,
  "host_pid": "9e6742732c60:1",
  "hash": "74ec13c90b6cd09a47b0c0d9c92790f64e90db2f6d08ea097dd4a7c0a45e6e0d",
  "cid": "QmV174ec13c90b6cd09a47b0c0d9c92790f64e90db2f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286493,
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
      "evaluated_at": 1760286493
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
  "sig": "4e2d84af7ab102b2150db1af017bede83372d9bd3a42bfdbaa352e5e3357e7f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599696280
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 24530995, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760284979, 'matching_hash': '32fd26aee1bbbffc'}}}