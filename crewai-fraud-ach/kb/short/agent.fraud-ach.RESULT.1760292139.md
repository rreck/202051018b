```json
{
  "id": "af66c2c1fe1a592e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292139,
  "host_pid": "9e6742732c60:1",
  "hash": "93eb848063b60e6dbc4f85bbbdf3ba0069e30ecb057c3d9773a50d469136e758",
  "cid": "QmV193eb848063b60e6dbc4f85bbbdf3ba0069e30ecb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292139,
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
      "evaluated_at": 1760292139
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
  "sig": "c403bafa643290e9f78ec3933406d885656b6a36b075b7420db350aafc73dbff"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469045536
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 65484159, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': 'd92613c41315e1ec'}}}