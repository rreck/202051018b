```json
{
  "id": "e7567abae7f95c4f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291833,
  "host_pid": "9e6742732c60:1",
  "hash": "518c91e3b69792ff35cad31de23f6c1ac2776a2ed258421d0feee38d26db13d1",
  "cid": "QmV1518c91e3b69792ff35cad31de23f6c1ac2776a2e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291833,
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
      "evaluated_at": 1760291833
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
  "sig": "6507164b98d8514e671bb5e3f1c7caa0df762d58103524e6a2f60d688c4a80d9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023944450
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 13997800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': '3c29e184ba733f5e'}}}