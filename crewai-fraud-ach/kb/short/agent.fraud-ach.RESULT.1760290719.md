```json
{
  "id": "78be38353a4f79b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290719,
  "host_pid": "9e6742732c60:1",
  "hash": "54d0e52b6b19cd98d63533b6a0c86c1170837878045eb196a522dc0b46dac027",
  "cid": "QmV154d0e52b6b19cd98d63533b6a0c86c1170837878",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290719,
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
      "evaluated_at": 1760290719
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
  "sig": "14435e5bda932a3fb291ed236787fe0a71a1b11252d6cdcf7fe02d9c82e84e20"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027607406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 17394187, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285765, 'matching_hash': '504131d6dff02852'}}}