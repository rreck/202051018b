```json
{
  "id": "e97037f764a23361",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290234,
  "host_pid": "9e6742732c60:1",
  "hash": "f89df649a3f5b8119b2eb7361a521f0cc73cd88544a302fffe90695eb76de4d1",
  "cid": "QmV1f89df649a3f5b8119b2eb7361a521f0cc73cd885",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290234,
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
      "evaluated_at": 1760290234
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
  "sig": "50a396c9ddfae03d6ddf353037f8ba5320446e8649ad221778edde7368fa8f74"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156823921
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 40531125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': '5764ccd6c01b314b'}}}