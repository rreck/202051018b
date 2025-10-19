```json
{
  "id": "65d31a32bd80eaab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287954,
  "host_pid": "9e6742732c60:1",
  "hash": "4bbe33884ef2511e35deb7163de7a545bb6cf81dcd0598a0a7beb77b5d34a8ef",
  "cid": "QmV14bbe33884ef2511e35deb7163de7a545bb6cf81d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287954,
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
      "evaluated_at": 1760287954
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
  "sig": "d645c0167c7da317ba8d8ce483dc8e075b9a3dfe9c8130ad983e3cabc50edeff"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201463734572
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 39000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285763, 'matching_hash': '9877b0a7b07093eb'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}