```json
{
  "id": "7911f166df9e4c4a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286965,
  "host_pid": "9e6742732c60:1",
  "hash": "270612e261be5360cf27d653647db0f47ff320deb334a6927d67b806f67a1f92",
  "cid": "QmV1270612e261be5360cf27d653647db0f47ff320de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286965,
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
      "evaluated_at": 1760286965
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
  "sig": "c6a6736c8dc81eb519538f2434b386dd5a5ac731b3f9f5c4a099080e78964cc6"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000023386962
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285765, 'matching_hash': '663df3e5258a7a87'}}}