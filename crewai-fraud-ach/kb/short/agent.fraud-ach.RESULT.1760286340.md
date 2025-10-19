```json
{
  "id": "9ee0ca8827e96453",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286340,
  "host_pid": "9e6742732c60:1",
  "hash": "64b673beade062d4cb8f3c3cb7e748e97592586a9f49e7820e127d10d41a5bdc",
  "cid": "QmV164b673beade062d4cb8f3c3cb7e748e97592586a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286340,
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
      "evaluated_at": 1760286340
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
  "sig": "a00d1b9f369e38c6276991c34cd3dc3870e9dd9fde649d12df3134a0afc29ed4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000024765233
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285763, 'matching_hash': 'feb1cc4bc40c71bc'}}}