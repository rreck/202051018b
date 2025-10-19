```json
{
  "id": "528e96cd9b4f4635",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291326,
  "host_pid": "9e6742732c60:1",
  "hash": "05546dfe26593444629bbb4c3e186ff49bc8783c3902298826da3cb8d4c441cc",
  "cid": "QmV105546dfe26593444629bbb4c3e186ff49bc8783c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291326,
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
      "evaluated_at": 1760291326
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "5a888904b122ad58e01f832ccf6532011552e8c9bf3c06576e51448a757ae853"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 122105156669076
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 172000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': '4057ff9fca3d2276'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}