```json
{
  "id": "db78e0d005169d02",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293321,
  "host_pid": "9e6742732c60:1",
  "hash": "584c5a9b02220bcab119d4d98773f4ae31d6061cc0df1b731a1179edf65a3890",
  "cid": "QmV1584c5a9b02220bcab119d4d98773f4ae31d6061c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293321,
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
      "evaluated_at": 1760293321
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
  "sig": "2233c20cc4d45e2b5a8254d70250b40061e3a8e3c3c93a669c8d9c98c9d764b5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274546383
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 57149280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '76da04c5629ac502'}}}