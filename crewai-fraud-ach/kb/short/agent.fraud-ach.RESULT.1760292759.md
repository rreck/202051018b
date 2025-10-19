```json
{
  "id": "dbf887422890b8ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292759,
  "host_pid": "9e6742732c60:1",
  "hash": "1c0441390164178664d55c2ecd2f7bb64160ad07861d4b596299379bd4c4ef75",
  "cid": "QmV11c0441390164178664d55c2ecd2f7bb64160ad07",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292759,
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
      "evaluated_at": 1760292759
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
  "sig": "d7391da26d10fdbeed89d6ce846c0a26011702e65d572238323246f0153d003a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026887900
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 65365476, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285765, 'matching_hash': '21e48734f91c19c6'}}}