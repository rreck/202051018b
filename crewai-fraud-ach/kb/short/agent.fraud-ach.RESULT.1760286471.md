```json
{
  "id": "e93ae1591b3d4bdc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286471,
  "host_pid": "9e6742732c60:1",
  "hash": "82fbf2a92e7a9ee4ffe586c37a2f3a1235afd6fb393f137dc356994dc19d018e",
  "cid": "QmV182fbf2a92e7a9ee4ffe586c37a2f3a1235afd6fb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286471,
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
      "evaluated_at": 1760286471
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
  "sig": "1193212ac9969f32d7ae92ac74bac7aa723bb691b5080e7c9b4d61dd790ad335"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100279221197
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11609520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285765, 'matching_hash': '706f719d80b46657'}}}