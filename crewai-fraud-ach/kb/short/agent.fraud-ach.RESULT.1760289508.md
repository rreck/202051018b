```json
{
  "id": "5ebbbdd32f4ff77a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289508,
  "host_pid": "9e6742732c60:1",
  "hash": "c4365b4dd37ce60ecef24c5a64407069d9a9d694aa0e996a614f499125555849",
  "cid": "QmV1c4365b4dd37ce60ecef24c5a64407069d9a9d694",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289508,
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
      "evaluated_at": 1760289508
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
  "sig": "bb2d685b329d36a97cca69adb7ddc018e280da91828192e75dfa2c7634962529"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035025346
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 20103625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': 'a8a877b5861d69af'}}}