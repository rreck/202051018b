```json
{
  "id": "5f756515cfb9f0be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292236,
  "host_pid": "9e6742732c60:1",
  "hash": "75417ab3b56cccac3101ce67d21c2b3ff49a852003bca6268420bb273bd8e2fc",
  "cid": "QmV175417ab3b56cccac3101ce67d21c2b3ff49a8520",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292236,
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
      "evaluated_at": 1760292236
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
  "sig": "37dc82782d1b4500b549add427986ac8f78d3eecc46c7de334d16e7613fbec2d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270739022
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 55696905, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '068659374d77a711'}}}