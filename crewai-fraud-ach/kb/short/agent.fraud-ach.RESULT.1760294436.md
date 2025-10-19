```json
{
  "id": "0816f8c38cbd282c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294436,
  "host_pid": "9e6742732c60:1",
  "hash": "cb7725c922a05269626ff8bdf5757e924e8f623b8cc532ebd3249db97acddb6f",
  "cid": "QmV1cb7725c922a05269626ff8bdf5757e924e8f623b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294436,
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
      "evaluated_at": 1760294436
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
  "sig": "da494f22fe414fc84a25b9872518fe9e0f55e2dc5b38aacf55548a2edd19e255"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 121000245827798
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 119000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': '00b0e4c8ffd2abdb'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}