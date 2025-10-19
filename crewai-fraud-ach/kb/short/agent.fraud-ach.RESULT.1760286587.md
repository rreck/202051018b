```json
{
  "id": "11a2980bc224751e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286587,
  "host_pid": "9e6742732c60:1",
  "hash": "d51837e93703e2b4cb099a8bade200ecd2b8de92118480b0b280cf5888175076",
  "cid": "QmV1d51837e93703e2b4cb099a8bade200ecd2b8de92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286587,
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
      "evaluated_at": 1760286587
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
  "sig": "e65075e1474c20402ca9b3cd41b317a9bacaa1b30613ddaf00f54d1306c2cd8e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000021660412
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285764, 'matching_hash': '19be1dcf8b4c513c'}}}