```json
{
  "id": "b280edb7e90758e8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288442,
  "host_pid": "9e6742732c60:1",
  "hash": "33a44724cdbf3d0fbdf3665a12aa3383dc3d8b9339083aba45786d9c12db5775",
  "cid": "QmV133a44724cdbf3d0fbdf3665a12aa3383dc3d8b93",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288442,
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
      "evaluated_at": 1760288442
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
  "sig": "26f14b0913b584d7efe5c35289da5edfded5058a2af333f56a1c2a410f5df808"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000022377083
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 46500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285765, 'matching_hash': 'fc2d68d27512b7d3'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}