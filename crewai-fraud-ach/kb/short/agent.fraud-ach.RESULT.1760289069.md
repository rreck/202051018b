```json
{
  "id": "1fd5de71a6a9f1a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289069,
  "host_pid": "9e6742732c60:1",
  "hash": "aeee244e05fb306305654451bc8c762675e0622d60e43a26c92101a43fa5c42b",
  "cid": "QmV1aeee244e05fb306305654451bc8c762675e0622d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289069,
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
      "evaluated_at": 1760289069
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
  "sig": "8db157e7166479f63b9861fd50a1c543a0f714f66b74b89636fb5bea55c19152"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033965137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 15980160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285765, 'matching_hash': 'a94abbf708458614'}}}