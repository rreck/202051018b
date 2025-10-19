```json
{
  "id": "88edc20cd056a9ec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292089,
  "host_pid": "9e6742732c60:1",
  "hash": "e7a2cf92da7f705ba09971357ebc0c9f1beeb178a769bd33435f1d5bd8674e21",
  "cid": "QmV1e7a2cf92da7f705ba09971357ebc0c9f1beeb178",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292089,
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
      "evaluated_at": 1760292089
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
  "sig": "1bb54fd127a51965748221356892179d23ed0d2fb73e43e216955edf56d6e9ca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240863608
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 35263050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': '74bcaa5b0fcf4d77'}}}