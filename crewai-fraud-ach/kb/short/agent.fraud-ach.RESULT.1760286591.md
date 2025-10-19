```json
{
  "id": "ff5ed53771a3a2cf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286591,
  "host_pid": "9e6742732c60:1",
  "hash": "7268a2ad8960455950c3aa031dbb9c0ecada4b927d18b5f4dfbb30245e07b858",
  "cid": "QmV17268a2ad8960455950c3aa031dbb9c0ecada4b92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286591,
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
      "evaluated_at": 1760286591
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
  "sig": "8ba2834dbd925f5ab0574896734643b0a094a6ca96adb5c8131a5ae207f49880"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000025341515
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285765, 'matching_hash': '76c6a410184ad94b'}}}