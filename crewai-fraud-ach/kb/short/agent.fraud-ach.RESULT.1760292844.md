```json
{
  "id": "2aac171221ab4d06",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292844,
  "host_pid": "9e6742732c60:1",
  "hash": "d46e77091e1201758590bb9395fd85160d203a56eb8930e4dae3b909f218a315",
  "cid": "QmV1d46e77091e1201758590bb9395fd85160d203a56",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292844,
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
      "evaluated_at": 1760292844
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
  "sig": "cbe477494e0cbc11cf3c5551a52fbe1acf415de49ea8b891c10e28949885ac8b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024300942
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 16629762, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '95903848ba405d51'}}}}