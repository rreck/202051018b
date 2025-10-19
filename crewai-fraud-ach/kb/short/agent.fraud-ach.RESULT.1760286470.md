```json
{
  "id": "83aef7f4431e153a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286470,
  "host_pid": "9e6742732c60:1",
  "hash": "82054d8d5055e44fc778ef932850eb94a8366869b24410ae961d46a27333be9c",
  "cid": "QmV182054d8d5055e44fc778ef932850eb94a8366869",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286470,
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
      "evaluated_at": 1760286470
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
  "sig": "f46a88ba6237afc11798c6296d2b295f17380d3e78d4d0e24d5b78ba10cafda3"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 026009591978167
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 26000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285765, 'matching_hash': '6b05f8817543e1fe'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}