```json
{
  "id": "7b654aa5c0a9395e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290154,
  "host_pid": "9e6742732c60:1",
  "hash": "01f644d89c85e4d086b040c19699536ec9192e15f6f077fdd1c568b20984b5c5",
  "cid": "QmV101f644d89c85e4d086b040c19699536ec9192e15",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290154,
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
      "evaluated_at": 1760290154
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
  "sig": "bce72823d1f5c5248eeb07801fb96082b1bc97824afbc8a02ba780c95937f34a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039250274
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 16232645, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': 'd24fc6d094fa29d9'}}}