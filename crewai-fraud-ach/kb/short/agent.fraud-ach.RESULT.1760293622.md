```json
{
  "id": "85e48d06d576329b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293622,
  "host_pid": "9e6742732c60:1",
  "hash": "06ea0829f63c087ba91a3cb1389a4a26c6ac13603380866a36fe92aaf418d054",
  "cid": "QmV106ea0829f63c087ba91a3cb1389a4a26c6ac1360",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293622,
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
      "evaluated_at": 1760293622
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
  "sig": "a836f029ca7fcf730eabfbefb4670ff4d897ce476eb174b83bec7ee3e3710d1a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039436848
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 100128438, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '703cb1be49d2cf8f'}}}