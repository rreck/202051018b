```json
{
  "id": "599ee02a1966987b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288057,
  "host_pid": "9e6742732c60:1",
  "hash": "0ce5ef85962610ad8b09d0633fa4fcd6f229dc3e5c04bc76605bf8de86f497b2",
  "cid": "QmV10ce5ef85962610ad8b09d0633fa4fcd6f229dc3e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288057,
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
      "evaluated_at": 1760288057
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
  "sig": "b83f97d6e01dbafe1c33903abdc5e3c2c26077f959ef572493832503a2f862bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028777791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285763, 'matching_hash': 'd241f2dd5b1f162a'}}}een': 1760285765, 'matching_hash': '5ddc61c49d89e409'}}}