```json
{
  "id": "8c891b84725e0715",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292858,
  "host_pid": "9e6742732c60:1",
  "hash": "aa678a8140d52302e720e5e85af30c50de340a5bc6fba80f59afa3f0363930d5",
  "cid": "QmV1aa678a8140d52302e720e5e85af30c50de340a5b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292858,
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
      "evaluated_at": 1760292858
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
  "sig": "5fb4d8416c36ed6fca1e387194c92336ea805d49ed1b462ff7d60cc08c5b3561"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 021000023602502
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 206000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285765, 'matching_hash': 'eacad8d3d1630a37'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}