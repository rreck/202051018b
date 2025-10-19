```json
{
  "id": "11f80b25d166ac0f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290737,
  "host_pid": "9e6742732c60:1",
  "hash": "a38da761ff300d275910c9c502f51a367d834f8100b16a51869a60af264227c6",
  "cid": "QmV1a38da761ff300d275910c9c502f51a367d834f81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290737,
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
      "evaluated_at": 1760290737
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
  "sig": "43edc2f39726a94dc01e123ea66a9114fefbba42c1ffcf5a2e8c9ea743bad9f6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159610548
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 51510370, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285764, 'matching_hash': '505487b98e445d12'}}}