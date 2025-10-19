```json
{
  "id": "588bd15f59dc7d02",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292310,
  "host_pid": "9e6742732c60:1",
  "hash": "fc1edb11a213ff463ec119bf16754b026129e595900c77fd1751410383bab3a3",
  "cid": "QmV1fc1edb11a213ff463ec119bf16754b026129e595",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292310,
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
      "evaluated_at": 1760292310
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
  "sig": "1aaee242cc570ddf93b7cd81f825f30c3f342d2fcadeb3fdf102ab229068f0df"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201463734572
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 97500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': '9877b0a7b07093eb'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}