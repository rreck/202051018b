```json
{
  "id": "acbebebe50eeab78",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286192,
  "host_pid": "9e6742732c60:1",
  "hash": "b066ff3654416d961b9eff04884c07b58f00543ac7fe80ebeaa1d4d2a06c42de",
  "cid": "QmV1b066ff3654416d961b9eff04884c07b58f00543a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286192,
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
      "evaluated_at": 1760286192
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
  "sig": "5a274f894d40d3baa477f576aa61ebb0ce61319789aecdca9fd31efa7067a11a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000027147487
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285765, 'matching_hash': 'f2056111b893f4fa'}}}