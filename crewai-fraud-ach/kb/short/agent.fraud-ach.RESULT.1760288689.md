```json
{
  "id": "a2794d5396959bb4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288689,
  "host_pid": "9e6742732c60:1",
  "hash": "d77958ba16b0467bec7ecea755306727e2180bd9f9ad4d50357e03600173e860",
  "cid": "QmV1d77958ba16b0467bec7ecea755306727e2180bd9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288689,
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
      "evaluated_at": 1760288689
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
  "sig": "4f8231fad1491683ffc6be2c024c8b45765a93480da290baa2718636c9dd68e6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273941483
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 31629160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285763, 'matching_hash': '33ec4b85754ad38a'}}}