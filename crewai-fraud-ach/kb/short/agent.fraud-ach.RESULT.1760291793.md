```json
{
  "id": "82cfdacb74312fa7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291793,
  "host_pid": "9e6742732c60:1",
  "hash": "8f33fc74069acf350b8712ce4ed5373913598c7ad8b3aeeb3b89e313f1379a3a",
  "cid": "QmV18f33fc74069acf350b8712ce4ed5373913598c7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291793,
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
      "evaluated_at": 1760291793
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
  "sig": "0318deab984cd81bd38267d848ec700e41136cdca19b7931e651dfb8fe7a5ef2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037692858
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 259, 'threshold': 50, 'total_amount': 33753398, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 258, 'first_seen': 1760284979, 'matching_hash': '7018b288608f6738'}}}