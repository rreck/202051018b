```json
{
  "id": "7814a1103e11b4fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292109,
  "host_pid": "9e6742732c60:1",
  "hash": "1f4b67e05b46ac4d81d7f68aec8a86ecdad2c4749e8e9f7478382f9ff90b3b47",
  "cid": "QmV11f4b67e05b46ac4d81d7f68aec8a86ecdad2c474",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292109,
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
      "evaluated_at": 1760292109
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
  "sig": "c0a745f18fcd4f71457dedf7a0392ddfda56fda901ad47b77f9c56f31af4b59e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156494107
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 94824630, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285764, 'matching_hash': 'c1327b457e76afdd'}}}