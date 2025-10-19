```json
{
  "id": "a9dcb8b84a9e3987",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292382,
  "host_pid": "9e6742732c60:1",
  "hash": "6464c265e404a9df4572e4eef590058e6fefb2b0c768677c6ae47750e9ef40d5",
  "cid": "QmV16464c265e404a9df4572e4eef590058e6fefb2b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292382,
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
      "evaluated_at": 1760292382
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
  "sig": "d96ef7dc3dc71c4a0ea2604ae10c2b5f3d77bd1ffcf295971231ac422ee2d8c1"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 044000033820068
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 98000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': 'f27958456f681c61'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}