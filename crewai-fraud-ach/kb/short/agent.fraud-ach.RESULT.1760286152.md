```json
{
  "id": "1622631f61b4d464",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286152,
  "host_pid": "9e6742732c60:1",
  "hash": "555df4b15a978f155cb54f4655313c16884283feafe67096ba0db84b204ae1bf",
  "cid": "QmV1555df4b15a978f155cb54f4655313c16884283fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286152,
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
      "evaluated_at": 1760286152
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
  "sig": "c4fdba93e5453b474330c12b3a8d6702c2d0242f14c65b904cb6ec932dc5ef35"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100271088524
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285763, 'matching_hash': '9bd457f641df29ee'}}}