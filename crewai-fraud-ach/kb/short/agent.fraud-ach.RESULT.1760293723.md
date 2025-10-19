```json
{
  "id": "197f3c7ed691bc06",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293723,
  "host_pid": "9e6742732c60:1",
  "hash": "3182ac4bcb66da21b16778de4f6a802829ef4e3301c9c69db3b46e06519c3b61",
  "cid": "QmV13182ac4bcb66da21b16778de4f6a802829ef4e33",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293723,
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
      "evaluated_at": 1760293723
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
  "sig": "8eba9cf89391b462e372e2176bb991c5f698a41d9d6ec56515b5380a05de2f0a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030256978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 300, 'threshold': 50, 'total_amount': 113866200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 299, 'first_seen': 1760284979, 'matching_hash': 'a2caca18f22a9a3d'}}}