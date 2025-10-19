```json
{
  "id": "439a4bf523680d93",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294646,
  "host_pid": "9e6742732c60:1",
  "hash": "d344f0f66321b61519160a16102cd0c31f60809628b16ce15e7f287ccc95e19c",
  "cid": "QmV1d344f0f66321b61519160a16102cd0c31f608096",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294646,
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
      "evaluated_at": 1760294646
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
  "sig": "21985bf16352889ad4f21abfd43576f6a6490f59ee1460430ffd71bb5a210207"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277559927
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 23750606, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '07b51054ae5371fb'}}}}