```json
{
  "id": "9e0e02b8eb3ebd13",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288889,
  "host_pid": "9e6742732c60:1",
  "hash": "924085587ae6dffae26c5aef8be770e383910f05997e848f8ac87db9ad4013e0",
  "cid": "QmV1924085587ae6dffae26c5aef8be770e383910f05",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288889,
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
      "evaluated_at": 1760288889
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
  "sig": "5b5793e6ec935f48aea942352a1b964e1f74a92cc44fd9cbf73ee166d168ebc8"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201467886368
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 53500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285763, 'matching_hash': 'b8e6d176a4768585'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}