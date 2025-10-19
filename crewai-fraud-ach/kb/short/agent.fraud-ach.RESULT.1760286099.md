```json
{
  "id": "b64ff75a40b99b4a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286099,
  "host_pid": "9e6742732c60:1",
  "hash": "6e0da53712ca9f9fdfe3d1440cc48b320426abf8586ef1a23210a41a3861289e",
  "cid": "QmV16e0da53712ca9f9fdfe3d1440cc48b320426abf8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286099,
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
      "evaluated_at": 1760286099
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
  "sig": "08b48ef3dbc35e0667fbb9a9cb5937490c00ee0e1f804c2a4932aaa83508c6fa"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201468417432
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285764, 'matching_hash': '3485380f8c896007'}}}