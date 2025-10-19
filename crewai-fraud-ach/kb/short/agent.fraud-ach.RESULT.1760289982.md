```json
{
  "id": "a3a958ae75f5d301",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289982,
  "host_pid": "9e6742732c60:1",
  "hash": "85d1532adec9a3cfc8d1b6a39853880889858af47974ba3b001d207cc805e613",
  "cid": "QmV185d1532adec9a3cfc8d1b6a39853880889858af4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289982,
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
      "evaluated_at": 1760289982
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
  "sig": "9b2bdfd8fa2d9767f30e9d5e8c97f3e068d8b0a468843fa247c053df45826ef5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241271300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 31565292, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285763, 'matching_hash': 'c5ade7cea17f41fa'}}}