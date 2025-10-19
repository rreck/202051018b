```json
{
  "id": "f9c4b3cdf18d53c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293871,
  "host_pid": "9e6742732c60:1",
  "hash": "b744493ab52c61134a1487456617fbaf35f08c43e5a8dec73ee5eb1f04fdb339",
  "cid": "QmV1b744493ab52c61134a1487456617fbaf35f08c43",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293871,
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
      "evaluated_at": 1760293871
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
  "sig": "c766976a32b212881be243235a7d88336461c31e2fbf53962db622a36a614d1c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244430877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 22700000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': 'c92664da58a26885'}}}