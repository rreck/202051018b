```json
{
  "id": "3969fd91b7eb5808",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288498,
  "host_pid": "9e6742732c60:1",
  "hash": "4e5ca1c31522324c7bb2744a0c4240689b3a5f74f9dd913cf52a7e7ea6a67960",
  "cid": "QmV14e5ca1c31522324c7bb2744a0c4240689b3a5f74",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288498,
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
      "evaluated_at": 1760288498
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
  "sig": "8b60014884b4dcca39e3b40de25f7ddd4754245c3cca5a77748b5143a5917664"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039486184
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 70490133, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760284979, 'matching_hash': '923cee7332714d41'}}}