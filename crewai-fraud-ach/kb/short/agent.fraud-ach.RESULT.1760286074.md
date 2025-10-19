```json
{
  "id": "0e0b34bba0a80111",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286074,
  "host_pid": "9e6742732c60:1",
  "hash": "1716634d8f523aaf566ea9334e80d616fe07e919afad4c2c7adc9aca4491907c",
  "cid": "QmV11716634d8f523aaf566ea9334e80d616fe07e919",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286074,
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
      "evaluated_at": 1760286074
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
  "sig": "90e5a09539342e8d54c9a84ef8752f7fb203dcac6f251aa74247b1ea2566ddf5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100270650471
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285765, 'matching_hash': '471e898b7e147a60'}}}