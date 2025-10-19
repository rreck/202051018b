```json
{
  "id": "6827d7a45434b580",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288670,
  "host_pid": "9e6742732c60:1",
  "hash": "e91782da1e0af37d70eea76e674ba2300c83db7bba8de9450da45c8055058643",
  "cid": "QmV1e91782da1e0af37d70eea76e674ba2300c83db7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288670,
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
      "evaluated_at": 1760288670
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
  "sig": "a5ef7f4b2c8c27b9fecf67626686558eceaaf3bddad4c85e835841b3f1a3c048"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025840854
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 42013100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285765, 'matching_hash': 'de322b9b0535588e'}}}