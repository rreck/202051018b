```json
{
  "id": "58d6b5db4d0c03e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290775,
  "host_pid": "9e6742732c60:1",
  "hash": "85207108d505e3f982c65cdaea049936543b43d58558a5bf0a32334ad38d6daf",
  "cid": "QmV185207108d505e3f982c65cdaea049936543b43d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290775,
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
      "evaluated_at": 1760290775
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
  "sig": "b5159d2e47581be307b2c8f429126ff6dd6054caf8762bd21b90192cb685e6e3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038503048
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 54824949, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285763, 'matching_hash': '8e1259c289f167a8'}}}