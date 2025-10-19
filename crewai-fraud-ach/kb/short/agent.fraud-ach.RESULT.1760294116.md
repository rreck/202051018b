```json
{
  "id": "c5f8c33755d564f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294116,
  "host_pid": "9e6742732c60:1",
  "hash": "b8478e77a342cac0aa930673fcf3f304fec87ca3280cc44d686e200b13a5691d",
  "cid": "QmV1b8478e77a342cac0aa930673fcf3f304fec87ca3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294116,
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
      "evaluated_at": 1760294116
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
  "sig": "e65ff9329de9638741e7ec55544f375e42109a13e118c97d5761f112cb8a04ec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029133644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 112871248, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': 'fa9b9676ccddb30b'}}}