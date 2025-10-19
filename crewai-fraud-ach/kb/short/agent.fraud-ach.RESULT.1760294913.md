```json
{
  "id": "1607084728326f66",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294913,
  "host_pid": "9e6742732c60:1",
  "hash": "0efbfbe1c123c1c7afd71f7957db776aedba0d352d6b2ff39bd8f6c11f0cc33c",
  "cid": "QmV10efbfbe1c123c1c7afd71f7957db776aedba0d35",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294913,
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
      "evaluated_at": 1760294913
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
  "sig": "7f1ee927e153404385d01334618a126b4f5c037604525075a7f7119db72e8491"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593711895
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 96398172, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760285763, 'matching_hash': '1e7ea83d54912238'}}}