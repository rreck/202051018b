```json
{
  "id": "eb078e4f6b75f7eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286643,
  "host_pid": "9e6742732c60:1",
  "hash": "c98be50be871e6681c5cc2509fb2ed8ba17ddf57d976f7f097a9cd2633b83bad",
  "cid": "QmV1c98be50be871e6681c5cc2509fb2ed8ba17ddf57",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286643,
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
      "evaluated_at": 1760286643
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
  "sig": "5cc1639b23fd988440a7fb90a0be3c7354f0d129cefaf853b55b844585ae11a2"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105153385568
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285763, 'matching_hash': '556aff2bced704f0'}}}