```json
{
  "id": "06fa7aeb7c433752",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289460,
  "host_pid": "9e6742732c60:1",
  "hash": "626a3604e55fe5cec1db6cda615557c7f745811d13789b89bf6efdeb5e83c559",
  "cid": "QmV1626a3604e55fe5cec1db6cda615557c7f745811d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289460,
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
      "evaluated_at": 1760289460
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
  "sig": "43da151d192204fbc26387bfaf28d17bafd34dbd48481a006092c2a4554326af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244346820
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285763, 'matching_hash': 'e760cf0efa3150cb'}}}een': 1760285763, 'matching_hash': '86add4fc1587ca1b'}}}