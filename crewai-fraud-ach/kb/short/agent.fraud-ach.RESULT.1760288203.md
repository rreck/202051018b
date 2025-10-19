```json
{
  "id": "4b24197c4e501b26",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288203,
  "host_pid": "9e6742732c60:1",
  "hash": "76c9ab719c209698d45341ba9523f9662aeb8109ccb8222cbd86994186e9b263",
  "cid": "QmV176c9ab719c209698d45341ba9523f9662aeb8109",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288203,
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
      "evaluated_at": 1760288203
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
  "sig": "db175cdddb21cec6740ee82f34f465155fb80f6408185372cdc372f4ee5dffcd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461090276
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 22286040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285763, 'matching_hash': '697ecd0ef10c625b'}}}