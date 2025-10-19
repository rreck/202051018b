```json
{
  "id": "94dc93d3222f21dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288359,
  "host_pid": "9e6742732c60:1",
  "hash": "a45eba006da311ce7903955770ccb3e338fc9e93856e937072b967e39f71a132",
  "cid": "QmV1a45eba006da311ce7903955770ccb3e338fc9e93",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288359,
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
      "evaluated_at": 1760288359
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
  "sig": "cd73b9e3f4d3ad2a3505d9c31eb26f950998d5ce74640b23b4d03b5452a5c034"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271295485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 34707946, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285763, 'matching_hash': '1c5bb12c0a4cbea7'}}}