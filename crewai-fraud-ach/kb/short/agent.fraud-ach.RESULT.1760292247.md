```json
{
  "id": "841859dcb837fcc7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292247,
  "host_pid": "9e6742732c60:1",
  "hash": "4bc64ad94e8551ccdaa8debb4d581aeff17ed5638a8b9327c4bb855d9c47fe28",
  "cid": "QmV14bc64ad94e8551ccdaa8debb4d581aeff17ed563",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292247,
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
      "evaluated_at": 1760292247
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
  "sig": "ab4d286561d4cfb8b7f8cc532bdf0b51d1ec5f9860607aad8eb9113b89df661c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243187094
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 86540235, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285764, 'matching_hash': '46900333a68fa7ba'}}}