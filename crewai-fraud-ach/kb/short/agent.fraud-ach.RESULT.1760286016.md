```json
{
  "id": "e5a19b4a13d3f06c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286016,
  "host_pid": "9e6742732c60:1",
  "hash": "308f80a325d4d8ae24b8161b9f707ddfe0a1ab94e14903adbbb19be2d2839760",
  "cid": "QmV1308f80a325d4d8ae24b8161b9f707ddfe0a1ab94",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286016,
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
      "evaluated_at": 1760286016
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
  "sig": "7613cdd250b16a6ca29b152e542edfc6e28ce5e54975d8168bd44857e16298f9"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}