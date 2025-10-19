```json
{
  "id": "6f6d2215f89f1b9e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290460,
  "host_pid": "9e6742732c60:1",
  "hash": "7536df534d3f37bb820df17efb03adc7cf3563cff557b12d552f952560e1cab3",
  "cid": "QmV17536df534d3f37bb820df17efb03adc7cf3563cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290460,
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
      "evaluated_at": 1760290460
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
  "sig": "7178483e55fb0e0b5d1e8a4ed567306fc91838e3cc4f7cff403412d1a72121f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247162231
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 41695781, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285763, 'matching_hash': '92769f469bceb512'}}}