```json
{
  "id": "0a481c8cf554acbe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294681,
  "host_pid": "9e6742732c60:1",
  "hash": "aaa2d5e6306f4dfbc72145bab2027ec8f239b4191e73aa1cb3e66fba65c69ab3",
  "cid": "QmV1aaa2d5e6306f4dfbc72145bab2027ec8f239b419",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294681,
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
      "evaluated_at": 1760294681
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
  "sig": "b46066fa51864addfcc00cda80470f28bbf384b3bd6d25db3a004b2c1017addd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035430994
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 102801600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285765, 'matching_hash': '24f97a880bb92d0e'}}}