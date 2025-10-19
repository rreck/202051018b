```json
{
  "id": "512c9bdf4fe824e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293625,
  "host_pid": "9e6742732c60:1",
  "hash": "6b641a7e182cd8ce2811d267f4b25c4a35386885345eb52c3205f8083bf12c67",
  "cid": "QmV16b641a7e182cd8ce2811d267f4b25c4a35386885",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293625,
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
      "evaluated_at": 1760293625
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
  "sig": "a6aab62c941c3cd0d623f5268799c9851aa3c4a2c00112096ea8f4a30ee2cd05"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244838202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 298, 'threshold': 50, 'total_amount': 71546820, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 297, 'first_seen': 1760284979, 'matching_hash': 'f90729670e1d4f48'}}}