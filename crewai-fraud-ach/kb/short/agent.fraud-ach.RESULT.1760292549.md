```json
{
  "id": "4b4c3ea82d396667",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292549,
  "host_pid": "9e6742732c60:1",
  "hash": "3968ce816024fb64cde7643eb4053d55575e7e1f73e929dd4186d5ff12ec5500",
  "cid": "QmV13968ce816024fb64cde7643eb4053d55575e7e1f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292549,
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
      "evaluated_at": 1760292549
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
  "sig": "841d40c0588e58dcd6a0e1e3bacbf1bd256fb4006de4c070de58d60e60bdd726"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464554990
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 54622600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': 'ab9afd20a22fc7b8'}}}