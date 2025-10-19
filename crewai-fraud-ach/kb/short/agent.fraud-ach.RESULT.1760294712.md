```json
{
  "id": "0f32386684f3c35f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294712,
  "host_pid": "9e6742732c60:1",
  "hash": "f4becc83ee00f1c7d12c86b8a4fc9ca516d419504b68107504beb3e2ec474458",
  "cid": "QmV1f4becc83ee00f1c7d12c86b8a4fc9ca516d41950",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294712,
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
      "evaluated_at": 1760294712
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
  "sig": "7b5e3cc24221be596b731f2912012c86cda60feab1fd261d7b68c6fd26bc877a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155063461
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 76556664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285764, 'matching_hash': '55217e698cd3f78f'}}}