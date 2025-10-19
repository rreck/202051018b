```json
{
  "id": "3e40ba0c034cd15f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287130,
  "host_pid": "9e6742732c60:1",
  "hash": "deb3c1830f254200dcb0c6eedb299d67d4a528c1c5c10da8126c5a01e685cf19",
  "cid": "QmV1deb3c1830f254200dcb0c6eedb299d67d4a528c1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287130,
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
      "evaluated_at": 1760287130
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "b50e5ed0dfff5f7afa6f229712b86f9b1de718d4e2868eb20d27a64248785a15"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 122105156669076
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 49000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285763, 'matching_hash': '4057ff9fca3d2276'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}