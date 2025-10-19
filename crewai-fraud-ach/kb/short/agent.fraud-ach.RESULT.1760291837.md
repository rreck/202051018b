```json
{
  "id": "199584569fc6f9f0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291837,
  "host_pid": "9e6742732c60:1",
  "hash": "e8ff1721a5b76c90ba535135ff345aa2bbab8145420427a4eb49b2c3e12442f6",
  "cid": "QmV1e8ff1721a5b76c90ba535135ff345aa2bbab8145",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291837,
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
      "evaluated_at": 1760291837
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
  "sig": "77288ffa7abd704f748f4e145bbc41e655aaf5f8beaf065d6288f6f54c9ecf8f"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201460873764
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 92000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': '6dda2db9e90937c1'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}