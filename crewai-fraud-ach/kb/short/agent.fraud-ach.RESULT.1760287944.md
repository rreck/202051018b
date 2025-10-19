```json
{
  "id": "d4f6271d5082dcd8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287944,
  "host_pid": "9e6742732c60:1",
  "hash": "b2c96f4943b065cd30d92d07a5183c6dae1bd067f826a58985301939194f2079",
  "cid": "QmV1b2c96f4943b065cd30d92d07a5183c6dae1bd067",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287944,
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
      "evaluated_at": 1760287944
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
  "sig": "d245591d193ff00ad13e5f6ca06b2d005dd9ab8ee22082b3a37c53f0e6ab0ba7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 24505096, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}