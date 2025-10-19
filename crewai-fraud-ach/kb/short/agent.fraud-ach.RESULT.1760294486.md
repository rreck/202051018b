```json
{
  "id": "1527935b997f6b0e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294486,
  "host_pid": "9e6742732c60:1",
  "hash": "3d965f1005af24b1677c9449cfec4135a4c1b2421c7022e80355598e4ebfa5f6",
  "cid": "QmV13d965f1005af24b1677c9449cfec4135a4c1b242",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294486,
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
      "evaluated_at": 1760294486
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
  "sig": "2e682c4e219db852e44edb69f3249b403bfa41931e8d0c18a227cefb66c58da8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028270724
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 11950000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': 'c4ee7f0f971d402b'}}}}