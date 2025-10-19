```json
{
  "id": "eedd28fe4c1aa767",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288985,
  "host_pid": "9e6742732c60:1",
  "hash": "e981ddb6cb7421b3c3063018bb99c8bfa6d86d3c770cf618ac680e008835214e",
  "cid": "QmV1e981ddb6cb7421b3c3063018bb99c8bfa6d86d3c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288985,
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
      "evaluated_at": 1760288985
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
  "sig": "4ea5f6066b2b4a172677b178e15a092f9707d11573b5c6c411026ec913af3f66"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023603818
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 49392860, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285764, 'matching_hash': '07334b550f79eb68'}}}