```json
{
  "id": "60d0f3dfe243b9e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286853,
  "host_pid": "9e6742732c60:1",
  "hash": "1e91cc19923713d20931d32ea6fcd10d0df0b29d5724ab0ab87cc4602b3bae8f",
  "cid": "QmV11e91cc19923713d20931d32ea6fcd10d0df0b29d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286853,
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
      "evaluated_at": 1760286853
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
  "sig": "e204ed68ae2a1bbd3e217ba064f8265171196ad979243d8ccb870c4bb65d9227"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000249254910
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285765, 'matching_hash': '80dc97a16e454830'}}}