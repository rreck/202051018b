```json
{
  "id": "db8e9cd5b10636d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293840,
  "host_pid": "9e6742732c60:1",
  "hash": "ec7e138575474566e13dc4c4a810d69c2cd3ea6973f3613bdcfb5e7c4f2c442f",
  "cid": "QmV1ec7e138575474566e13dc4c4a810d69c2cd3ea69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293840,
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
      "evaluated_at": 1760293840
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
  "sig": "32207bc875beb0e34add348ebc41266be2a296c2d735ccaee33ddc4cfde3cc03"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241355402
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 36818338, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285765, 'matching_hash': '58524718dce63a85'}}}