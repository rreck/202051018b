```json
{
  "id": "1c51342fa6530928",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287931,
  "host_pid": "9e6742732c60:1",
  "hash": "cbfcb67663a28ccd4356b6e4f6210711d2f2eff30bd3477194338773d48bd859",
  "cid": "QmV1cbfcb67663a28ccd4356b6e4f6210711d2f2eff3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287931,
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
      "evaluated_at": 1760287931
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
  "sig": "987c35b774a975c72e123825215f9451a11125705a85bd77c526cfbeba057021"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031758687
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 31090444, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285763, 'matching_hash': '8a33e153fff23185'}}}