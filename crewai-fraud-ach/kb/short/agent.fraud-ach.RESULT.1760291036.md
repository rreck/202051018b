```json
{
  "id": "816341136ba5d995",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291036,
  "host_pid": "9e6742732c60:1",
  "hash": "3c9ea54a47d2cc7a5163d8ccf4950afe325446d58177b652114adb399e763c8d",
  "cid": "QmV13c9ea54a47d2cc7a5163d8ccf4950afe325446d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291036,
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
      "evaluated_at": 1760291036
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
  "sig": "bb4cd2926fee5b140de3c05baa54e0b507822e29696fbd0edf968f1588abc910"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151957108
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 79537260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285765, 'matching_hash': 'c64e753eaec43197'}}}