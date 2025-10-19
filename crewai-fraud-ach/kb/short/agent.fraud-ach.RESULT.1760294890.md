```json
{
  "id": "6911ac29767ab464",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294890,
  "host_pid": "9e6742732c60:1",
  "hash": "af34b8d311c3b866de1deb8c04953cfe657d3f725ad0022c2a3d78bedb8993a7",
  "cid": "QmV1af34b8d311c3b866de1deb8c04953cfe657d3f72",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294890,
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
      "evaluated_at": 1760294890
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
  "sig": "635df689b16bed11a1d6eddc627b5d8ab168c22e467484aee62c0dde9b52b526"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025895266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 69839400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': '9ac81502eabc8fa5'}}}}