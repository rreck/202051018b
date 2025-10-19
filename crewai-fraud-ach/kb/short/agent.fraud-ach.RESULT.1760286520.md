```json
{
  "id": "e6d4908128203776",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286520,
  "host_pid": "9e6742732c60:1",
  "hash": "26b75692b491173745222283c5c47b5fd9442c6c4eff2e999aa88cebd90003d2",
  "cid": "QmV126b75692b491173745222283c5c47b5fd9442c6c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286520,
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
      "evaluated_at": 1760286520
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "d1f5af6c9650cad46de38d4c986d1975d890e36694741511a96eeb4b9b584a7f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100278849424
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285763, 'matching_hash': '586e1ac2088494e1'}}}, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285763, 'matching_hash': '00b0e4c8ffd2abdb'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}routing number checksum'}}}