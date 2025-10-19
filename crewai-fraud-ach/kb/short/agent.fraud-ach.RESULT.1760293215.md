```json
{
  "id": "3745bd8612e5bff4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293215,
  "host_pid": "9e6742732c60:1",
  "hash": "adb5bacd5649c8bd2d7836bd737a187345584011fbf8c9e766f397b5264dd777",
  "cid": "QmV1adb5bacd5649c8bd2d7836bd737a187345584011",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293215,
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
      "evaluated_at": 1760293215
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
  "sig": "afc421c2929dd122eefc4f6f335888f5319a37e61b5e77fcdc698ba4ba4f81d1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270759086
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 76761800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': 'eb79951538526d2c'}}}}