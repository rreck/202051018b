```json
{
  "id": "0cc6c0d468762f26",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287070,
  "host_pid": "9e6742732c60:1",
  "hash": "e03a525ffa5dd8ee884ced9016585f79f83ea2388873227da8031dbe123d25eb",
  "cid": "QmV1e03a525ffa5dd8ee884ced9016585f79f83ea238",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287070,
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
      "evaluated_at": 1760287070
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "dfa6089fa2709a0c336628788bccd1637116a49574b9fefdbdbb96703f96b6f2"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026466423
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 22194622, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285764, 'matching_hash': '1fcdc28f16166b10'}}}760284979, 'matching_hash': 'fdbb68f6e232305a'}}}