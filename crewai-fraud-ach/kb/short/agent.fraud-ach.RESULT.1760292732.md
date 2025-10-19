```json
{
  "id": "5e76ceecd605e3c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292732,
  "host_pid": "9e6742732c60:1",
  "hash": "071d69938a79e6dfa9643a5eecfd6c1f98edb6203555514bdb3fb9b203c094d0",
  "cid": "QmV1071d69938a79e6dfa9643a5eecfd6c1f98edb620",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292732,
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
      "evaluated_at": 1760292732
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
  "sig": "0189fb7ee645a83c33479e0a317711bea20ec01a5ecf6114d6b39fd5f03512ef"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466146132
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 80953524, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': '20fb82cc575104fa'}}}