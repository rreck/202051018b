```json
{
  "id": "7bee0712e1f35212",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292897,
  "host_pid": "9e6742732c60:1",
  "hash": "140f44303728f5d65e2b8868d2d329d88a89512f0ed5066b7364b32fcc62674b",
  "cid": "QmV1140f44303728f5d65e2b8868d2d329d88a89512f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292897,
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
      "evaluated_at": 1760292897
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
  "sig": "b7dd5c2fcb327811469c3733815012c9051185c0ddd7aba974077ea73f99b298"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271648434
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 48997521, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': '7a167e1c4ddc5d6e'}}}