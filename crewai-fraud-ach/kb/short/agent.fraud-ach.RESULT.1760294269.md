```json
{
  "id": "2128853ea010fa9a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294269,
  "host_pid": "9e6742732c60:1",
  "hash": "325f1bc678c07a7699b4e4c1b32e7ffb45dccaba174a0e74a55844eb8972cf48",
  "cid": "QmV1325f1bc678c07a7699b4e4c1b32e7ffb45dccaba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294269,
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
      "evaluated_at": 1760294269
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
  "sig": "ea819872f5d132ad5b46bcd323279ce6c97440d4ee04d04a9bbfa2a4c2f8273d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038823890
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 49101135, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '81df70e06ca09887'}}}}