```json
{
  "id": "7b4187547825d1a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292386,
  "host_pid": "9e6742732c60:1",
  "hash": "4a7856bd5d7af0f888579a62a214731a52d31d8cc8c7648ef11b458362b0e9fb",
  "cid": "QmV14a7856bd5d7af0f888579a62a214731a52d31d8c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292386,
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
      "evaluated_at": 1760292386
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
  "sig": "17bc0bb68e8b08608ed5c48a5e8fbb35f2a3f49df0cd0d46adcf2f6220722e0f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031078531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 15072988, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285765, 'matching_hash': '2bea5b783a868e31'}}}