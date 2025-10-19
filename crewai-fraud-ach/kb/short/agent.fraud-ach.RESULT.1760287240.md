```json
{
  "id": "e1e90ee96e930800",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287240,
  "host_pid": "9e6742732c60:1",
  "hash": "3deef65b72727483d647c528d649e2fa2575f83e691ad6f5c76c1d2dea78c2b1",
  "cid": "QmV13deef65b72727483d647c528d649e2fa2575f83e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287240,
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
      "evaluated_at": 1760287240
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
  "sig": "79c1cfe963218ed557955e153fb3a01aea17cec2853526290e1bc6cca9ce15ac"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105152187504
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 53, 'threshold': 50, 'total_amount': 25039532, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285764, 'matching_hash': '4c6bc703d31ba532'}}}