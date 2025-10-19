```json
{
  "id": "9a27deedc77b5f55",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294411,
  "host_pid": "9e6742732c60:1",
  "hash": "7cf7ad585de9464ab2593715fb34b2c474ff1c24d9c745ab868478bcb202963f",
  "cid": "QmV17cf7ad585de9464ab2593715fb34b2c474ff1c24",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294411,
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
      "evaluated_at": 1760294411
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
  "sig": "16ad0b38bb5f4f0c4573d2eecf367052caec87575a22cec290b18163c1fbe6ce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032712851
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 19712712, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285765, 'matching_hash': 'f72222764ca627d0'}}}