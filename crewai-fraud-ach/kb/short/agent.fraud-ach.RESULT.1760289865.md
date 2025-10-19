```json
{
  "id": "88fa0ca96c7d3d27",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289865,
  "host_pid": "9e6742732c60:1",
  "hash": "da98d206528d2bdc2c50945d5d395ad110cf34fca102c287c56a2f3634cf5eb2",
  "cid": "QmV1da98d206528d2bdc2c50945d5d395ad110cf34fc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289865,
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
      "evaluated_at": 1760289865
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
  "sig": "84b32aae1a2cf6effb24cf56733972a46e611b5be7c1f0f8f40598ca80f714dc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025341279
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 55531575, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285763, 'matching_hash': 'e2ff1695635a899d'}}}