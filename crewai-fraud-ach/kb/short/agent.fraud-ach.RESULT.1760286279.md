```json
{
  "id": "3b0974aa9651d108",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286279,
  "host_pid": "9e6742732c60:1",
  "hash": "8eb9fcafabde3d8b7eb880f51ce91d1d24c1655935d01eb1b2f346bcab32f754",
  "cid": "QmV18eb9fcafabde3d8b7eb880f51ce91d1d24c16559",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286279,
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
      "evaluated_at": 1760286279
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
  "sig": "004eb9734ae79ae41b49461e1f05730db7ec1b2758fa1d0b50d260aef7a5f4b4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105157031776
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285763, 'matching_hash': '2e79bf0e4633df5f'}}}