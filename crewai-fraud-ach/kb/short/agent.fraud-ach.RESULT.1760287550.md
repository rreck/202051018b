```json
{
  "id": "477ed86419a53a39",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287550,
  "host_pid": "9e6742732c60:1",
  "hash": "43d8d9713bec33bc7b033e3741fa5035a2309306d365c2b60d9de583f70724b4",
  "cid": "QmV143d8d9713bec33bc7b033e3741fa5035a2309306",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287550,
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
      "evaluated_at": 1760287550
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
  "sig": "37b61e928a61182453add2a3e8f81e88d4eff94aa2ca82dc7bd24055b8512a3b"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 111000024460145
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 16230848, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285763, 'matching_hash': '6128e7e8f1f7694a'}}}}}}