```json
{
  "id": "a00b67bca493820e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293718,
  "host_pid": "9e6742732c60:1",
  "hash": "e1ad4ae3f7e81e9f54b56f5660696d6d00a70ca933b9632379bdbd4ddce6eee4",
  "cid": "QmV1e1ad4ae3f7e81e9f54b56f5660696d6d00a70ca9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293718,
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
      "evaluated_at": 1760293718
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
  "sig": "b93ffdb9ee3daab299c1f91318efd526fb84316d5d82836f8b4ce30ecd194661"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 122105158962917
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 224000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': '11dc2cfd2eb8ef5d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}