```json
{
  "id": "dba839f93c258a8e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291852,
  "host_pid": "9e6742732c60:1",
  "hash": "c0189bb903de8a8a5bd18e78d0623c29ee24eca41075d49a6a22b2160beabeff",
  "cid": "QmV1c0189bb903de8a8a5bd18e78d0623c29ee24eca4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291852,
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
      "evaluated_at": 1760291852
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
  "sig": "dbd41a74c0a4cb8dc8ab1d5937896061e4373a9b4cb0f250021a55087c7a1a2d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 58557632, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}