```json
{
  "id": "88e2d997553732fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294772,
  "host_pid": "9e6742732c60:1",
  "hash": "69a8977546951b4392e57996e103f9152e33c1d5c327c4801a94a44caa9e2727",
  "cid": "QmV169a8977546951b4392e57996e103f9152e33c1d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294772,
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
      "evaluated_at": 1760294772
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
  "sig": "fca243268b598e2135d3293b206827a26e687587663500d2380b78b7fdf4c880"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465280061
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 32451512, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '24e243e35a5cb5f6'}}}