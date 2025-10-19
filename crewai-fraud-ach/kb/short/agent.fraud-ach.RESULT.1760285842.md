```json
{
  "id": "216c7ef3321cc8bc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285842,
  "host_pid": "9e6742732c60:1",
  "hash": "b3a0e79d378314e3c47b2417118ddb6339ee89915785887bab5f6c2adef3ae39",
  "cid": "QmV1b3a0e79d378314e3c47b2417118ddb6339ee8991",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285842,
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
      "evaluated_at": 1760285842
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
  "sig": "5fe050e583a9ec79f938156cb7eaefacd69138c9a2d588bd1e22bd7ae6586b9a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000027294403
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 4, 'first_seen': 1760285763, 'matching_hash': '8d40dd17cbab8bca'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '472304300', 'validation_error': 'Invalid routing number checksum'}}}