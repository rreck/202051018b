```json
{
  "id": "2d51eb388a708794",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289803,
  "host_pid": "9e6742732c60:1",
  "hash": "7ae4522a9d4d31adf793ec6d16ec44f53f53b22fa0800a2efe2ed7bd18bce23d",
  "cid": "QmV17ae4522a9d4d31adf793ec6d16ec44f53f53b22f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289803,
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
      "evaluated_at": 1760289803
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
  "sig": "0e3aee9efcc66076798ecece6daf88adc9fab32f503bd8d2c99db63d714512af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025840854
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 55877423, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285765, 'matching_hash': 'de322b9b0535588e'}}}