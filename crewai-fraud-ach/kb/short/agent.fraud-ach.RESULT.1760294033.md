```json
{
  "id": "702e30ec0d9c9688",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294033,
  "host_pid": "9e6742732c60:1",
  "hash": "f801d4b9c7a9c84e05709ee09a13fac961b0cfd17ecc56f686824c08b80ea949",
  "cid": "QmV1f801d4b9c7a9c84e05709ee09a13fac961b0cfd1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294033,
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
      "evaluated_at": 1760294033
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
  "sig": "e9231d3fc9284316cb8d3ffc4269af634562abb602b46e187ca231173647d25d"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 021000028490637
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 115000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285765, 'matching_hash': '1f028817acc0361c'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}