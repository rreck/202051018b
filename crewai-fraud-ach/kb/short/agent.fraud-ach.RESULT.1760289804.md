```json
{
  "id": "58b89a8a53ea19c9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289804,
  "host_pid": "9e6742732c60:1",
  "hash": "edde4a7b824ebbc103ab52aca1ff77209acc8ef31423531af92eea03ce9a2a86",
  "cid": "QmV1edde4a7b824ebbc103ab52aca1ff77209acc8ef3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289804,
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
      "evaluated_at": 1760289804
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
  "sig": "3d9eeb0e47d16f2c3f9cc0997adac6005fa730aa96849657a074258b3ab65e9c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152240558
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 55455281, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285765, 'matching_hash': '0371944fd59dbf43'}}}