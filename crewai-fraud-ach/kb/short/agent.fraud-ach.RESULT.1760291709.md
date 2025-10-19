```json
{
  "id": "a85a09979e20d92c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291709,
  "host_pid": "9e6742732c60:1",
  "hash": "a42734e2095dcc2dd59f788c8be25a3e2d01cb8ee68da7e345476b592aee9040",
  "cid": "QmV1a42734e2095dcc2dd59f788c8be25a3e2d01cb8e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291709,
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
      "evaluated_at": 1760291709
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
  "sig": "1c3bea0f90765a820dd5cf372b4d8171f4b8fd5abee7fdba95c4a3de38f1c133"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595235556
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 31596446, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285765, 'matching_hash': 'e45b9dbcffb11ba0'}}}