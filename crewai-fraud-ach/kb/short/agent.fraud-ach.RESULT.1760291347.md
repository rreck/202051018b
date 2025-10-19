```json
{
  "id": "ec5078844739484c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291347,
  "host_pid": "9e6742732c60:1",
  "hash": "fd2ba9644954d11332120c903e31a2ca7a68be67e59fffb77ddb34eb6cc4b8b6",
  "cid": "QmV1fd2ba9644954d11332120c903e31a2ca7a68be67",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291347,
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
      "evaluated_at": 1760291347
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
  "sig": "d518b65d17128f351feddf2286383cfcdb74181c5b5b5f6d55a759f0c0f9cc0d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033919598
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 65205257, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285763, 'matching_hash': '1dbf667d29bdf8b7'}}}