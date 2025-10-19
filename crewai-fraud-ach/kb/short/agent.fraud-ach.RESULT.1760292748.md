```json
{
  "id": "9ee8bec348d59de9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292748,
  "host_pid": "9e6742732c60:1",
  "hash": "c34d9fc057704883f724b19d88f8cfa502d213b2459f234e1d4b30cdadf6af53",
  "cid": "QmV1c34d9fc057704883f724b19d88f8cfa502d213b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292748,
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
      "evaluated_at": 1760292748
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
  "sig": "ef598bd2b4a87b403edfd117a221b13d07fb7f7f90ef33128461a733cfe2db61"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026281875
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 83582472, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': 'ee0b29e0b2882e41'}}}