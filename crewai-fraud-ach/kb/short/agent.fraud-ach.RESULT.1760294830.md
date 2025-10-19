```json
{
  "id": "e2b53a34c9b6c090",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294830,
  "host_pid": "9e6742732c60:1",
  "hash": "d0ba1c4c2ce2641d30b6118b65872d9aa682750ce8a74d583d55f9651bf8a851",
  "cid": "QmV1d0ba1c4c2ce2641d30b6118b65872d9aa682750c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294830,
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
      "evaluated_at": 1760294830
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
  "sig": "5004086f13b8e95aff39575caebacbe0d3f248c6227f30fdfd1efe552e9302bf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034789126
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 321, 'threshold': 50, 'total_amount': 68713581, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 320, 'first_seen': 1760284979, 'matching_hash': '5ec025bcbfaa0fd9'}}}