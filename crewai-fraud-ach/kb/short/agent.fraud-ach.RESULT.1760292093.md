```json
{
  "id": "cc4ab30932b2e2ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292093,
  "host_pid": "9e6742732c60:1",
  "hash": "35db3214968916bee7201bbb86492882f6d94a8306f5142d3ab26355328e76f8",
  "cid": "QmV135db3214968916bee7201bbb86492882f6d94a83",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292093,
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
      "evaluated_at": 1760292093
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
  "sig": "46b03ce7e2eb97179db990f98d35f4b5dd5325953ce78130d057302bf9986987"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272276410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 33896380, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285764, 'matching_hash': '97f823784b1b19f6'}}}