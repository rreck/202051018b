```json
{
  "id": "ed4e110fc2252166",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288896,
  "host_pid": "9e6742732c60:1",
  "hash": "b654bc9b3af6eb00e57db8197bff1e3cf592ec4e2aa330a37643dadcaf9a6384",
  "cid": "QmV1b654bc9b3af6eb00e57db8197bff1e3cf592ec4e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288896,
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
      "evaluated_at": 1760288896
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
  "sig": "5c62a3146a69d76cb73ae8e8b0c659ca0d076e0f86195c197a6e3da01fa4a626"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598542542
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 35786257, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285764, 'matching_hash': '3cc1c7bbce52acf6'}}}