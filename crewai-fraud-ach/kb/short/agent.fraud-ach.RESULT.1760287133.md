```json
{
  "id": "7d28c6c5998dd8b7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287133,
  "host_pid": "9e6742732c60:1",
  "hash": "cfce09b13a37dd66371910de6d393b23e2a539f26dc218f8f295563d4f613578",
  "cid": "QmV1cfce09b13a37dd66371910de6d393b23e2a539f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287133,
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
      "evaluated_at": 1760287133
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "c9fd7b9bcd47ccc31d6ac1e341980f91bae6048635e6ad32b06183057429093f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000020807792
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10228799, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285764, 'matching_hash': '8390351bce6e669b'}}}