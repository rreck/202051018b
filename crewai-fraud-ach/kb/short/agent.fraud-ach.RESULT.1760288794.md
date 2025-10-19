```json
{
  "id": "839f425a189c5583",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288794,
  "host_pid": "9e6742732c60:1",
  "hash": "ef6693d786ab2b8eeaca9b4ac0da2bb1d60cebd52311442963bbc767788b6eba",
  "cid": "QmV1ef6693d786ab2b8eeaca9b4ac0da2bb1d60cebd5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288794,
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
      "evaluated_at": 1760288794
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
  "sig": "81af0749794c0cea996f572d8deb8998319ccd6539de21b37a4b0738812dcc8e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029313979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 49153208, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285765, 'matching_hash': 'ee97e2abac1557d2'}}}