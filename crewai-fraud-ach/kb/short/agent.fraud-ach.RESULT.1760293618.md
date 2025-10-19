```json
{
  "id": "5de3814282eb2490",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293618,
  "host_pid": "9e6742732c60:1",
  "hash": "0e819936e38585e6471f232643e9329bfe32a7fe6a350dc3ce570e5324003174",
  "cid": "QmV10e819936e38585e6471f232643e9329bfe32a7fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293618,
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
      "evaluated_at": 1760293618
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
  "sig": "089915e0f8ea282998b69731d75328daa2f475f38ae8d960e90726f7cf4dc854"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279947961
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 19129074, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '22db2c62b181c93f'}}}