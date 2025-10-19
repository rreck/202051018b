```json
{
  "id": "844dff187ccbb1db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292330,
  "host_pid": "9e6742732c60:1",
  "hash": "dc2f1f7b52a943f9383d5566e837fcfe1202022c761e4212287d093b43d99920",
  "cid": "QmV1dc2f1f7b52a943f9383d5566e837fcfe1202022c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292330,
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
      "evaluated_at": 1760292331
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
  "sig": "82d0c42caba9e93a535af89cc20b4418732d306ee8c8b3859576e20fa9a0ba84"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272560065
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 271, 'threshold': 50, 'total_amount': 30968254, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 270, 'first_seen': 1760284979, 'matching_hash': 'aab4f056297a675d'}}}