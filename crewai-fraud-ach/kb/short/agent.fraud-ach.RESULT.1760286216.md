```json
{
  "id": "d4810335119dd399",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286216,
  "host_pid": "9e6742732c60:1",
  "hash": "a7c0a09888ed9fdee496f066e39f202a6292d3e16722f811bf47582769085611",
  "cid": "QmV1a7c0a09888ed9fdee496f066e39f202a6292d3e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286216,
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
      "evaluated_at": 1760286216
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
  "sig": "c276ef7d1bcc56f41617797d81e2021af9a5e1f617b21eef4ad5891645e615dc"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000028860438
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285763, 'matching_hash': '1ce58b471eab5597'}}}