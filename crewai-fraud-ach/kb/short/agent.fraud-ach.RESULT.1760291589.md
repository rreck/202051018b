```json
{
  "id": "b1e09f39c89c4d15",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291589,
  "host_pid": "9e6742732c60:1",
  "hash": "4cd4042f880a5373cde8016a7e34ffea5ae2c304e0f961c310ddc063771247a1",
  "cid": "QmV14cd4042f880a5373cde8016a7e34ffea5ae2c304",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291589,
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
      "evaluated_at": 1760291589
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
  "sig": "eb2bb6f7db0736545d723861dad24a6d63c83cdbbb077ddccde1c3ed2cc6bd1e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150171825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 33458482, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285765, 'matching_hash': 'da3473f59eec3040'}}}