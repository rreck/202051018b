```json
{
  "id": "3fc2f34c631c06b0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288522,
  "host_pid": "9e6742732c60:1",
  "hash": "f15db8cc7857386e22f26bbb200a00e3e26bb24567c26081f19dcd9b1c6c82b2",
  "cid": "QmV1f15db8cc7857386e22f26bbb200a00e3e26bb245",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288522,
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
      "evaluated_at": 1760288522
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
  "sig": "5fd5c506f09a35649b8e0a92af9714e3798c3abdfcc5eacc108caa136a201d11"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023531334
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285763, 'matching_hash': '62f48a4bdb5932df'}}}een': 1760285763, 'matching_hash': '8e1259c289f167a8'}}}